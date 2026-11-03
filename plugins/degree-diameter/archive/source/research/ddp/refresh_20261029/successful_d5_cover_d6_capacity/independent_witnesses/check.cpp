#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
using Walk=vector<int>;
using Buckets=array<vector<vector<Walk>>,4>;
void prefixes(const vector<vector<int>>&G,int u,int previous,Walk &path,Buckets &b){
  int len=path.size()-1;b[len][u].push_back(path);
  if(len==3)return;
  for(int v:G[u])if(v!=previous){path.push_back(v);prefixes(G,v,u,path,b);path.pop_back();}
}
void paths_json(ostream&out,const vector<Walk>&walks){
  out<<'[';
  for(size_t i=0;i<walks.size();++i){if(i)out<<',';out<<'[';for(size_t j=0;j<walks[i].size();++j){if(j)out<<',';out<<walks[i][j];}out<<']';}
  out<<']';
}
int main(int argc,char**argv){
  assert(argc==2);clock_t start=clock();ifstream input(argv[1]);
  ofstream output("WITNESSES.jsonl");int source_count=0,case_count=0;bool match=true;
  string file;int n;long long m;
  while(input>>file>>n>>m){
    ++source_count;ifstream graph(file);vector<vector<int>>G(n);string line;long long rows=0;
    while(getline(graph,line)){
      if(line.empty()||line[0]=='#')continue;
      istringstream row(line);int u,v;assert(bool(row>>u>>v));
      if(u==n&&v==m)continue;
      assert(u>=0&&u<n&&v>=0&&v<n&&u!=v);G[u].push_back(v);G[v].push_back(u);++rows;
    }
    assert(rows==m);
    for(auto &row:G){sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end());}
    for(int ci=0;ci<2;++ci){
      int u,v,radius,expected;input>>u>>v>>radius>>expected;assert(radius==5||radius==6);
      Buckets left,right;for(int d=0;d<4;++d){left[d].resize(n);right[d].resize(n);}
      Walk path={u};prefixes(G,u,-1,path,left);path={v};prefixes(G,v,-1,path,right);
      vector<Walk> walks;array<int,7> counts{};
      for(int len=0;len<=radius;++len){
        int a=len/2,b=len-a;
        for(int mid=0;mid<n;++mid)for(const auto&p:left[a][mid])for(const auto&q:right[b][mid]){
          if(a&&b&&p[p.size()-2]==q[q.size()-2])continue;
          Walk joined=p;
          for(int i=int(q.size())-2;i>=0;--i)joined.push_back(q[i]);
          assert(joined.front()==u&&joined.back()==v&&int(joined.size())==len+1);
          for(int i=1;i<len;++i)assert(joined[i-1]!=joined[i+1]);
          walks.push_back(joined);++counts[len];
        }
      }
      sort(walks.begin(),walks.end());assert(adjacent_find(walks.begin(),walks.end())==walks.end());
      bool ok=int(walks.size())==expected;match&=ok;++case_count;
      output<<"{\"source\":\""<<file<<"\",\"n\":"<<n<<",\"u\":"<<u<<",\"v\":"<<v<<",\"radius\":"<<radius
            <<",\"actual_count\":"<<walks.size()<<",\"expected\":"<<expected<<",\"match\":"<<(ok?"true":"false")<<",\"counts_by_exact_length\":[";
      for(int d=0;d<7;++d){if(d)output<<',';output<<counts[d];}
      output<<"],\"walks\":";paths_json(output,walks);output<<"}\n";
    }
  }
  assert(source_count==3&&case_count==6);output.close();
  ofstream result("RESULT.json");
  result<<"{\"status\":\""<<(match?"ALL_SIX_WITNESSES_MATCH":"COUNT_MISMATCH")<<"\",\"source_reads\":3,\"witness_pairs\":6,\"graph_BFS\":0,\"DP_repeats\":0,\"cover_graphs\":0,\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
  cout<<"matched="<<match<<" pairs="<<case_count<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
  assert(match);
}
