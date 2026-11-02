#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
struct Edge {int u,v,half,symbol;};
struct Arc {int to,symbol,sign;};
struct Expr {uint32_t token;unsigned odd=0;array<unsigned char,256> dot{};};
struct Counts {long long b0=0,p0=0,b1=0,p1=0,b2=0,p2=0;};
clock_t started;
bool expired=false,hit=false;
double cpu(){return double(clock()-started)/CLOCKS_PER_SEC;}
int parity(unsigned x){return __builtin_parity(x);}
uint32_t advance_token(uint32_t x,Arc a){
  if(a.symbol==-1)return x;
  if(a.symbol==-2)return x^(1u<<24);
  unsigned shift=3*a.symbol,val=(x>>shift)&7u;
  return (x&~(7u<<shift))|(((val+a.sign)&7u)<<shift);
}
void paths(const array<vector<Arc>,8>&adj,int at,int d,uint32_t x,array<vector<uint32_t>,8>&out){
  out[at].push_back(x);if(d==3)return;
  for(auto a:adj[at])paths(adj,a.to,d+1,advance_token(x,a),out);
}
void counts_json(ostream&o,const Counts&c){
  o<<"{\"parity_domain\":"<<c.b0<<",\"parity_pass\":"<<c.p0
   <<",\"mod4_domain\":"<<c.b1<<",\"mod4_pass\":"<<c.p1
   <<",\"mod8_domain\":"<<c.b2<<",\"mod8_pass\":"<<c.p2<<'}';
}
void save_hit(const vector<Edge>&edges,const vector<int>&values,int case_id){
  array<uint64_t,64> G{};
  for(int u=0;u<64;++u)for(int b:{1,2,4})G[u]|=1ull<<(u^b);
  for(auto e:edges){
    int d=e.half?4:values[e.symbol];
    for(int a=0;a<8;++a){int u=8*a+e.u,v=8*((a+d)%8)+e.v;assert(u!=v);G[u]|=1ull<<v;G[v]|=1ull<<u;}
  }
  for(int u=0;u<64;++u){assert(__builtin_popcountll(G[u])==5);assert(!(G[u]&(1ull<<u)));}
  for(int r=0;r<64;++r){
    uint64_t seen=1ull<<r;
    for(int d=0;d<3;++d){uint64_t next=seen,scan=seen;while(scan){int u=__builtin_ctzll(scan);scan&=scan-1;next|=G[u];}seen=next;}
    assert(seen==~0ull);
  }
  ofstream out("K64.edges");out<<"64 160\n";
  for(int u=0;u<64;++u)for(int v=u+1;v<64;++v)if(G[u]&(1ull<<v))out<<u<<' '<<v<<'\n';
  ofstream params("HIT_PARAMS.json");params<<"{\"case\":"<<case_id<<",\"encoding\":\"8*a+label\",\"edges\":[";
  for(size_t i=0;i<edges.size();++i){if(i)params<<',';auto e=edges[i];params<<'['<<e.u<<','<<e.v<<','<<(e.half?4:values[e.symbol])<<']';}
  params<<"],\"producer_roots_checked\":64,\"degree\":5,\"D_at_most\":3}\n";
}
Counts test_case(const vector<Edge>&edges,int symbols,int case_id){
  array<vector<Arc>,8> adj;
  vector<int> loops;
  for(auto e:edges){
    if(e.half)adj[e.u].push_back({e.u,-2,0});
    else {adj[e.u].push_back({e.v,e.symbol,1});adj[e.v].push_back({e.u,e.symbol,-1});if(e.u==e.v)loops.push_back(e.symbol);}
  }
  for(int l=0;l<8;++l){assert(adj[l].size()==2);for(int b:{1,2,4})adj[l].push_back({l^b,-1,0});}
  vector<vector<uint32_t>> raw;
  for(int r=0;r<8;++r){
    array<vector<uint32_t>,8> out;paths(adj,r,0,0,out);
    for(int t=r;t<8;++t){auto&x=out[t];sort(x.begin(),x.end());x.erase(unique(x.begin(),x.end()),x.end());assert(x.size()>=8);raw.push_back(x);}
  }
  sort(raw.begin(),raw.end(),[](const auto&a,const auto&b){return a.size()<b.size();});
  map<uint32_t,int> ids;vector<Expr> exprs;vector<vector<int>> conditions;
  unsigned assignments=1u<<symbols;
  for(const auto&xs:raw){
    vector<int> condition;
    for(auto token:xs){
      auto it=ids.find(token);
      if(it==ids.end()){
        int id=exprs.size();ids[token]=id;Expr e;e.token=token;e.dot[0]=(token&(1u<<24))?4:0;
        for(int j=0;j<symbols;++j)if((token>>(3*j))&1u)e.odd|=1u<<j;
        for(unsigned bits=1;bits<assignments;++bits){int j=__builtin_ctz(bits);e.dot[bits]=(e.dot[bits&(bits-1)]+((token>>(3*j))&7u))&7u;}
        exprs.push_back(e);condition.push_back(id);
      }else condition.push_back(it->second);
    }
    conditions.push_back(condition);
  }
  Counts counts;
  vector<unsigned char> base(exprs.size());vector<int> values(symbols);
  for(unsigned b0=1;b0<assignments;++b0){
    ++counts.b0;bool ok=true;
    for(const auto&c:conditions){int ones=0;for(int i:c)ones+=parity(exprs[i].odd&b0);if(ones<4||int(c.size())-ones<4){ok=false;break;}}
    if(!ok)continue;
    ++counts.p0;
    unsigned firstodd=b0&-b0;
    for(unsigned b1=0;b1<assignments;++b1){
      if(cpu()>120){expired=true;return counts;}
      if(b1&firstodd)continue;
      bool domain=true;
      // Actual low residue of a self-loop must lie in {1,2,3}.
      for(int j:loops)if(((b0>>j)&1u)==0&&((b1>>j)&1u)==0){domain=false;break;}
      if(!domain)continue;
      ++counts.b1;ok=true;
      for(const auto&c:conditions){
        int n[4]={};for(int i:c)++n[(exprs[i].dot[b0]+2*parity(exprs[i].odd&b1))&3];
        if(*min_element(n,n+4)<2){ok=false;break;}
      }
      if(!ok)continue;
      ++counts.p1;
      for(size_t i=0;i<exprs.size();++i)base[i]=(exprs[i].dot[b0]+2*exprs[i].dot[b1])&7;
      for(unsigned b2=0;b2<assignments;++b2){
        if(b2&firstodd)continue;
        domain=true;
        for(int j:loops)if(b2&(1u<<j)){domain=false;break;}
        if(!domain)continue;
        for(int j=0;j<symbols;++j)values[j]=((b0>>j)&1u)+2*((b1>>j)&1u)+4*((b2>>j)&1u);
        for(size_t i=0;i<edges.size();++i){auto e=edges[i];if(e.half)continue;
          if(e.u!=e.v&&(e.u^e.v)==1&&values[e.symbol]==0)domain=false;
          if(e.u!=e.v&&((e.u^e.v)==2||(e.u^e.v)==4)&&values[e.symbol]==0)domain=false;
          for(size_t j=0;j<i;++j){auto f=edges[j];if(!f.half&&f.u==e.u&&f.v==e.v&&values[f.symbol]==values[e.symbol])domain=false;}
        }
        if(!domain)continue;
        ++counts.b2;ok=true;
        for(const auto&c:conditions){unsigned seen=0;for(int i:c)seen|=1u<<(base[i]^(4*parity(exprs[i].odd&b2)));if(seen!=255u){ok=false;break;}}
        if(!ok)continue;
        ++counts.p2;save_hit(edges,values,case_id);hit=true;return counts;
      }
    }
  }
  return counts;
}
int main(){
  started=clock();ifstream input("canonical_quotients.txt");int total;input>>total;assert(total==110);
  ofstream records("VOLTAGE_CASES.jsonl");Counts all;int completed=0,labelled=0;
  for(int id=0;id<total;++id){
    int n,multiplicity;input>>n>>multiplicity;vector<Edge>edges;int symbols=0;
    for(int j=0;j<n;++j){int u,v,h;input>>u>>v>>h;edges.push_back({u,v,h,h?-2:symbols++});}
    assert(symbols<=8);
    Counts c=test_case(edges,symbols,id);
    records<<"{\"case\":"<<id<<",\"labelled_quotients\":"<<multiplicity<<",\"symbols\":"<<symbols<<",\"complete\":"<<(!expired&&!hit?"true":"false")<<",\"counts\":";
    counts_json(records,c);records<<"}\n";records.flush();
    all.b0+=c.b0;all.p0+=c.p0;all.b1+=c.b1;all.p1+=c.p1;all.b2+=c.b2;all.p2+=c.p2;
    if(expired||hit)break;
    ++completed;labelled+=multiplicity;
  }
  ofstream result("VOLTAGE_RESULT.json");
  result<<"{\"status\":\""<<(hit?"AUXILIARY_HIT_NEEDS_INDEPENDENT_CHECK":expired?"PARTIAL_UNKNOWN":"COMPLETE_CYCLIC_FAMILY_NO_HIT")
        <<"\",\"canonical_total\":"<<total<<",\"completed\":"<<completed<<",\"completed_labelled_quotients\":"<<labelled
        <<",\"counts\":";counts_json(result,all);
  result<<",\"CPU_seconds\":"<<cpu()<<",\"solver_calls\":0,\"auxiliary_positive_graphs\":"<<(hit?1:0)<<",\"main1088_graphs\":0}\n";
  cout<<"completed="<<completed<<'/'<<total<<" hit="<<hit<<" expired="<<expired<<" CPU="<<cpu()<<"\n";
}
