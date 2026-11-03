#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
struct Arc { int to, symbol, sign; };
struct Edge { int u,v,symbol; bool half; };
struct Graph {
  array<vector<Arc>,8> adj;
  vector<Edge> edges;
  int symbols=0;
};
long long tested=0,passed=0;
array<array<long long,8>,8> rejects{};
ofstream survivors("SURVIVING_QUOTIENTS.jsonl"), witnesses("REJECTION_SAMPLES.jsonl");
int samples=0;
uint32_t step(uint32_t token, const Arc &a) {
  if(a.symbol==-1) return token;
  if(a.symbol==-2) return token ^ (1u<<24);
  int shift=3*a.symbol;
  uint32_t val=(token>>shift)&7u;
  return (token & ~(7u<<shift)) | (((val+a.sign)&7u)<<shift);
}
void paths(const Graph &g,int at,int depth,uint32_t token,array<vector<uint32_t>,8> &out) {
  out[at].push_back(token);
  if(depth==3) return;
  for(auto a:g.adj[at]) paths(g,a.to,depth+1,step(token,a),out);
}
void edge_json(ostream &out,const Graph &g) {
  out<<'[';
  for(size_t i=0;i<g.edges.size();++i) {
    if(i) out<<',';
    auto e=g.edges[i];out<<'['<<e.u<<','<<e.v<<','<<e.symbol<<','<<(e.half?1:0)<<']';
  }
  out<<']';
}
void inspect(const Graph &extra) {
  ++tested;
  Graph g=extra;
  for(int l=0;l<8;++l) {
    assert(g.adj[l].size()==2);
    for(int b:{1,2,4}) g.adj[l].push_back({l^b,-1,0});
  }
  int minimum=1000;
  for(int r=0;r<8;++r) {
    array<vector<uint32_t>,8> out;
    paths(g,r,0,0,out);
    for(int t=0;t<8;++t) {
      auto &x=out[t];sort(x.begin(),x.end());x.erase(unique(x.begin(),x.end()),x.end());
      minimum=min(minimum,int(x.size()));
      if(x.size()<8) {
        ++rejects[r][t];
        if(samples<12) {
          witnesses<<"{\"quotient\":";edge_json(witnesses,extra);
          witnesses<<",\"root\":"<<r<<",\"target\":"<<t<<",\"formal_count\":"<<x.size()<<",\"tokens\":[";
          for(size_t i=0;i<x.size();++i) {if(i) witnesses<<',';witnesses<<x[i];}
          witnesses<<"]}\n";++samples;
        }
        return;
      }
    }
  }
  ++passed;survivors<<"{\"quotient\":";edge_json(survivors,extra);
  survivors<<",\"voltage_symbols\":"<<extra.symbols<<",\"minimum_formal_count\":"<<minimum<<"}\n";
}
void ordinary(Graph &g,int u,int v) {
  int symbol=g.symbols++;assert(symbol<8);
  if(u>v) swap(u,v);
  g.edges.push_back({u,v,symbol,false});
  g.adj[u].push_back({v,symbol,1});g.adj[v].push_back({u,symbol,-1});
}
void half(Graph &g,int u) {
  g.edges.push_back({u,u,-2,true});g.adj[u].push_back({u,-2,0});
}
void enumerate(int mask,const Graph &g) {
  if(!mask) {inspect(g);return;}
  int root=__builtin_ctz(unsigned(mask)),rest=mask^(1<<root);
  for(int sub=rest;;sub=(sub-1)&rest) {
    int component=sub|(1<<root),remaining=mask^component;
    vector<int> v;
    for(int l=0;l<8;++l) if(sub&(1<<l)) v.push_back(l);
    if(v.empty()) {
      Graph h=g;ordinary(h,root,root);enumerate(remaining,h);
    } else if(v.size()==1) {
      Graph h=g;ordinary(h,root,v[0]);ordinary(h,root,v[0]);enumerate(remaining,h);
    } else {
      do {
        if(v.front()>v.back()) continue;
        Graph h=g;ordinary(h,root,v[0]);
        for(size_t i=1;i<v.size();++i) ordinary(h,v[i-1],v[i]);
        ordinary(h,v.back(),root);enumerate(remaining,h);
      } while(next_permutation(v.begin(),v.end()));
    }
    if(component!=(1<<root)) {
      v.clear();for(int l=0;l<8;++l) if(component&(1<<l))v.push_back(l);
      do {
        if(v.front()>v.back()) continue;
        Graph h=g;half(h,v.front());half(h,v.back());
        for(size_t i=1;i<v.size();++i)ordinary(h,v[i-1],v[i]);
        enumerate(remaining,h);
      } while(next_permutation(v.begin(),v.end()));
    }
    if(!sub) break;
  }
}
int main() {
  clock_t start=clock();enumerate(255,Graph{});
  assert(tested==213798);
  ofstream result("RESULT.json");
  result<<"{\"status\":\"COMPLETE_FORMAL_ROUTE_CAPACITY_GATE\",\"quotients\":"<<tested
        <<",\"passed\":"<<passed<<",\"rejected\":"<<tested-passed
        <<",\"graph_candidates_generated\":0,\"main1088_graphs\":0,\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC
        <<",\"first_rejection_counts\":[";
  for(int r=0;r<8;++r) {if(r)result<<',';result<<'[';for(int t=0;t<8;++t){if(t)result<<',';result<<rejects[r][t];}result<<']';}
  result<<"]}\n";cout<<"quotients="<<tested<<" passed="<<passed<<" rejected="<<tested-passed<<"\n";
}
