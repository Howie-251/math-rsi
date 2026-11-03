#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
struct Bits{U a=0,b=0;};
Bits operator|(Bits x,Bits y){return{x.a|y.a,x.b|y.b};}bool full(Bits x){return x.a==~U(0)&&x.b==255;}Bits bit(int u){return u<64?Bits{U(1)<<u,0}:Bits{0,U(1)<<(u-64)};}
vector<int> members(Bits x){vector<int>v;while(x.a){int j=__builtin_ctzll(x.a);v.push_back(j);x.a&=x.a-1;}while(x.b){int j=__builtin_ctzll(x.b);v.push_back(j+64);x.b&=x.b-1;}return v;}
void ints(ostream&f,const vector<int>&v){f<<'[';for(int i=0;i<(int)v.size();i++){if(i)f<<',';f<<v[i];}f<<']';}
int main(int argc,char**argv){clock_t st=clock();auto cpu=[&](){return double(clock()-st)/CLOCKS_PER_SEC;};rlimit lim{24,24};setrlimit(RLIMIT_CPU,&lim);string dir=argv[1];ifstream in(dir+"/source.edges");int n,m;in>>n>>m;assert(n==72&&m==180);vector<array<int,2>>edges(m);vector<vector<int>>adj(n);for(auto&e:edges){in>>e[0]>>e[1];adj[e[0]].push_back(e[1]);adj[e[1]].push_back(e[0]);}for(auto&v:adj)assert(v.size()==5);
 auto r2=[&](int s,int e){Bits b=bit(s);for(int v:adj[s]){if(e>=0&&((edges[e][0]==s&&edges[e][1]==v)||(edges[e][1]==s&&edges[e][0]==v)))continue;b=b|bit(v);for(int w:adj[v]){if(e>=0&&((edges[e][0]==v&&edges[e][1]==w)||(edges[e][1]==v&&edges[e][0]==w)))continue;b=b|bit(w);}}return b;};
 vector<Bits>original(n),pairOrig(m);vector<vector<Bits>>erased(m,vector<Bits>(n));for(int s=0;s<n;s++)original[s]=r2(s,-1);for(int e=0;e<m;e++){pairOrig[e]=original[edges[e][0]]|original[edges[e][1]];for(int s=0;s<n;s++)erased[e][s]=r2(s,e);}
 long long operations=0,necessary=0,exact=0;vector<long long>necv(n),exactv(n),nece(m),exacte(m);int completed=0;bool limited=false,profileStop=false;vector<int>firstM,firstS;int firstOmit=-1;ofstream bin(dir+"/root_cover_candidates.u16.bin",ios::binary);
 for(int orphan=0;orphan<m;orphan++){
  if(cpu()>20){limited=true;break;}int u=edges[orphan][0],v=edges[orphan][1];vector<int>other;vector<Bits>pc(m);
  for(int e=0;e<m;e++)if(e!=orphan&&edges[e][0]!=u&&edges[e][1]!=u&&edges[e][0]!=v&&edges[e][1]!=v){other.push_back(e);pc[e]=erased[orphan][edges[e][0]]|erased[orphan][edges[e][1]];}
  for(int a=0;a<(int)other.size();a++)for(int b=a+1;b<(int)other.size();b++){
   int f=other[a],g=other[b];if(edges[f][0]==edges[g][0]||edges[f][0]==edges[g][1]||edges[f][1]==edges[g][0]||edges[f][1]==edges[g][1])continue;
   Bits orig=pairOrig[f]|pairOrig[g],del=pc[f]|pc[g];
   for(int orientation=0;orientation<2;orientation++){
    int seed=orientation?v:u,omitted=orientation?u:v;operations++;if(!full(orig|original[seed]))continue;necessary++;necv[omitted]++;nece[orphan]++;
    if(!full(del|erased[orphan][seed]))continue;exact++;exactv[omitted]++;exacte[orphan]++;
    array<uint16_t,4>record{(uint16_t)orphan,(uint16_t)f,(uint16_t)g,(uint16_t)omitted};sort(record.begin(),record.begin()+3);bin.write((char*)record.data(),8);
    if(firstM.empty()){firstM={record[0],record[1],record[2]};firstOmit=omitted;for(int e:firstM)for(int t:edges[e])if(t!=omitted)firstS.push_back(t);sort(firstS.begin(),firstS.end());assert(firstS.size()==5&&unique(firstS.begin(),firstS.end())==firstS.end());}
   }
  }
  completed++;
  if(completed==10){double projected=cpu()*180/10.;ofstream p(dir+"/profile10orphanedges.json");p<<"{\"orphanedges_completed\":10,\"root_operations\":"<<operations<<",\"original_R2_cover_cases\":"<<necessary<<",\"exact_rootcover_cases\":"<<exact<<",\"CPU_seconds\":"<<cpu()<<",\"projected_total_nativeCPU\":"<<projected<<"}\n";p.close();cerr<<"PROFILE10 operations="<<operations<<" necessary="<<necessary<<" exact="<<exact<<" projected="<<projected<<'\n';if(projected>20){profileStop=true;break;}}
 }
 bin.close();bool complete=completed==180;if(complete)assert(operations%6==0);
 if(!firstM.empty()){ofstream f(dir+"/first_rootcover.json");f<<"{\"deleted_edge_ids\":";ints(f,firstM);f<<",\"deleted_edges\":[";for(int i=0;i<3;i++){if(i)f<<',';auto e=edges[firstM[i]];f<<'['<<e[0]<<','<<e[1]<<']';}f<<"],\"omitted_oldvertex\":"<<firstOmit<<",\"newroot\":72,\"newroot_neighbors\":";ints(f,firstS);f<<",\"new_n\":73,\"new_m\":182,\"exact_newroot_R3_all72old\":true,\"oldold_distance_condition\":\"UNTESTED\",\"fullgraph_D3_claimed\":false}\n";}
 ofstream out(dir+"/RESULT.json");out<<"{\"status\":\""<<(complete?"COMPLETE_ROOT_COVER_ENUMERATION":profileStop?"PARTIAL_PROFILE_OVER_BUDGET":"PARTIAL_CPU_WINDOW")<<"\",\"complete\":"<<(complete?"true":"false")<<",\"source_n\":72,\"source_m\":180,\"target_n\":73,\"target_m\":182,\"target_Delta\":5,\"target_D\":3,\"orphanedges_completed\":"<<completed<<",\"root_operations_examined\":"<<operations<<",\"matching_triples\":"<<(complete?to_string(operations/6):"null")<<",\"necessary_original_R2_cover\":"<<necessary<<",\"exact_after_three_deletions_rootcover\":"<<exact<<",\"necessary_lost_by_orphanedge\":"<<necessary-exact<<",\"positive_records\":"<<exact<<",\"positive_binary\":\"root_cover_candidates.u16.bin\",\"binary_layout\":\"record=(3sortededgeIDs,omittedvertex),4nativeuint16,8bytes\",\"candidategraph_BFS\":0,\"source_D3_BFS\":0,\"oldold_pairs_checked\":false,\"newgraphs_generated\":0,\"CPU_seconds\":"<<setprecision(12)<<cpu()<<",\"necessary_by_omittedvertex\":[";for(int i=0;i<72;i++){if(i)out<<',';out<<necv[i];}out<<"],\"exact_by_omittedvertex\":[";for(int i=0;i<72;i++){if(i)out<<',';out<<exactv[i];}out<<"],\"orphanedge_counts\":[";for(int i=0;i<180;i++){if(i)out<<',';out<<"{\"edge_id\":"<<i<<",\"necessary\":"<<nece[i]<<",\"exact\":"<<exacte[i]<<'}';}out<<"],\"extra_variants\":0}\n";out.close();cerr<<"FINAL complete="<<complete<<" operations="<<operations<<" necessary="<<necessary<<" exact="<<exact<<" cpu="<<cpu()<<'\n';
}
