#include <bits/stdc++.h>
using namespace std;
const int N=42342,CORE=41356,TAIL=42177;
vector<vector<int>> g(N);
vector<int> bfs(int bound,const vector<int>&seeds,int radius){
 vector<int>d(bound,-1),q(bound);int h=0,t=0;
 for(int s:seeds)if(s<bound&&d[s]<0){d[s]=0;q[t++]=s;}
 while(h<t){int u=q[h++];if(d[u]==radius)continue;for(int v:g[u])if(v<bound&&d[v]<0){d[v]=d[u]+1;q[t++]=v;}}
 return d;
}
void ints(ostream&f,const vector<int>&a){f<<'[';for(size_t i=0;i<a.size();i++){if(i)f<<',';f<<a[i];}f<<']';}
int main(int argc,char**argv){
 assert(argc==3);string input=argv[1],outdir=argv[2];clock_t started=clock();
 ifstream in(input);string line;int rows=0;
 while(getline(in,line)){
  if(line.empty()||line[0]=='#')continue;istringstream s(line);int u,v;s>>u;assert(u==rows&&u<N);while(s>>v){assert(0<=v&&v<N&&v!=u);g[u].push_back(v);}rows++;
 }assert(rows==N);
 vector<vector<int>> oldpins(N-TAIL);for(int i=TAIL;i<N;i++)for(int v:g[i])if(v<TAIL)oldpins[i-TAIL].push_back(v);
 ofstream f(outdir+"/RESULT.json");f<<"{\"static_core\":"<<TAIL<<",\"proven_core\":"<<CORE<<",\"tail_vertices\":165,\"static_rows\":[";
 int staticfails=0,pairfails=0,firststatic=-1,firststatictarget=-1;vector<int>firstpair;
 for(int k=0;k<N-TAIL;k++){
  auto d=bfs(TAIL,oldpins[k],4);int missing=0;vector<int>sample;
  for(int v=0;v<TAIL;v++)if(d[v]<0){missing++;if(sample.size()<8)sample.push_back(v);}
  if(missing){staticfails++;if(firststatic<0){firststatic=TAIL+k;firststatictarget=sample[0];}}
  if(k)f<<',';f<<"{\"vertex\":"<<TAIL+k<<",\"old_pins\":";ints(f,oldpins[k]);f<<",\"core_R4_missing\":"<<missing<<",\"missing_sample\":";ints(f,sample);f<<'}';
  for(int j=k+1;j<N-TAIL;j++){
   bool okay=false;for(int v:oldpins[j])if(d[v]>=0&&d[v]<=3){okay=true;break;}
   if(!okay){pairfails++;if(firstpair.empty())firstpair={TAIL+k,TAIL+j};}
  }
 }
 f<<"],\"static_cover_failed_vertices\":"<<staticfails<<",\"static_pair_distance_le3_failed_pairs\":"<<pairfails<<",\"first_static_failed_vertex\":"<<firststatic<<",\"first_static_failed_target\":"<<firststatictarget<<",\"first_static_failed_set_pair\":";ints(f,firstpair);
 f<<",\"sequential_rows\":[";int allfails=0,tailfails=0,firstseq=-1,firstseqtarget=-1;
 for(int i=CORE;i<N;i++){
  vector<int>pins;for(int v:g[i])if(v<i)pins.push_back(v);
  auto d=bfs(i,pins,4);int missing=0;vector<int>sample;
  for(int v=0;v<i;v++)if(d[v]<0){missing++;if(sample.size()<8)sample.push_back(v);}
  if(missing){allfails++;if(i>=TAIL)tailfails++;if(firstseq<0){firstseq=i;firstseqtarget=sample[0];}}
  if(i>CORE)f<<',';f<<"{\"vertex\":"<<i<<",\"earlier_pins\":";ints(f,pins);f<<",\"earlier_R4_missing\":"<<missing<<",\"missing_sample\":";ints(f,sample);f<<'}';
 }
 f<<"],\"sequential986_failed_vertices\":"<<allfails<<",\"sequential_tail165_failed_vertices\":"<<tailfails<<",\"first_sequential_failed_vertex\":"<<firstseq<<",\"first_sequential_failed_target\":"<<firstseqtarget;
 int witness=firstseq>=0?firstseq:firststatic,target=firstseq>=0?firstseqtarget:firststatictarget;
 if(witness>=0){
  vector<int>d(N,-1),parent(N,-1);queue<int>q;d[witness]=0;q.push(witness);
  while(!q.empty()&&d[target]<0){int u=q.front();q.pop();if(d[u]>=5)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;parent[v]=u;q.push(v);}}
  vector<int>path;if(d[target]>=0){for(int v=target;v!=-1;v=parent[v])path.push_back(v);reverse(path.begin(),path.end());}
  f<<",\"final_graph_witness\":{\"source\":"<<witness<<",\"target\":"<<target<<",\"distance_found_le5\":"<<d[target]<<",\"path\":";ints(f,path);f<<'}';
 }
 f<<",\"static_radius4_checks\":165,\"sequential_radius4_checks\":986,\"full_all_source_BFS_repeated\":false,\"new_graphs_generated\":0,\"parameter_optimization\":false,\"CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<"}\n";
 cout<<"static_failed="<<staticfails<<" static_pair_failed="<<pairfails<<" sequential_failed="<<allfails<<" tail_sequential_failed="<<tailfails<<" CPU="<<double(clock()-started)/CLOCKS_PER_SEC<<'\n';
}
