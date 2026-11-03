#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
string ints(const vector<int>&a){ostringstream o;o<<"[";for(size_t i=0;i<a.size();i++){if(i)o<<",";o<<a[i];}o<<"]";return o.str();}
struct DSU{vector<int>p,sz;DSU(int n):p(n),sz(n,1){iota(p.begin(),p.end(),0);}int find(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}void join(int x,int y){x=find(x);y=find(y);if(x==y)return;if(sz[x]<sz[y])swap(x,y);p[y]=x;sz[x]+=sz[y];}};
int main(int argc,char**argv){
 assert(argc==2);double budget=stod(argv[1]);clock_t start=clock();ifstream input("inputs.txt");int count;input>>count;
 int sourceComplete=0,totalComp=0,totalR3=0,eligible=0;bool hit=false,budgetStop=false;
 ofstream profiles("SOURCE_PROFILES.jsonl");
 auto checkpoint=[&](){ofstream f("WORKER_RESULT.json");f<<"{\"status\":\""<<(hit?"HIT":budgetStop?"UNKNOWN_CPU_BUDGET":sourceComplete==count?"COMPLETE_NO_HIT":"RUNNING")<<"\",\"sources_planned\":"<<count<<",\"sources_complete\":"<<sourceComplete<<",\"components_examined\":"<<totalComp<<",\"internal_R3_roots\":"<<totalR3<<",\"eligible_components\":"<<eligible<<",\"worker_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"source_D5_BFS\":0,\"R4_calls\":0,\"solver_calls\":0}\n";};
 for(int si=0;si<count;si++){
  if(double(clock()-start)/CLOCKS_PER_SEC>=budget){budgetStop=true;checkpoint();return 0;}
  int delta,n;long long m;string format,path;input>>delta>>n>>m>>format>>path;
  vector<vector<int>>g(n);
  if(format=="csr"){
   ifstream f(path,ios::binary);uint32_t nn,arcs;f.read((char*)&nn,4);f.read((char*)&arcs,4);assert(nn==uint32_t(n)&&arcs==uint32_t(2*m));
   vector<uint32_t>off(n+1),neighbors(arcs);f.read((char*)off.data(),4*(n+1));f.read((char*)neighbors.data(),4*arcs);assert(off[0]==0&&off[n]==arcs);
   for(int v=0;v<n;v++)g[v]=vector<int>(neighbors.begin()+off[v],neighbors.begin()+off[v+1]);
  }else{
   ifstream f(path);string header;getline(f,header);if(header.size()&&header[0]=='#')header=header.substr(1);istringstream hs(header);int nn;long long mm;hs>>nn>>mm;assert(nn==n&&mm==m);
   for(long long i=0;i<m;i++){int u,v;f>>u>>v;assert(0<=u&&u<n&&0<=v&&v<n&&u!=v);g[u].push_back(v);g[v].push_back(u);}
  }
  vector<int>deg(n);int sat=0;for(int v=0;v<n;v++){deg[v]=g[v].size();assert(deg[v]<=delta&&deg[v]>0);sat+=deg[v]==delta;}
  DSU ds(n);for(int v=0;v<n;v++)if(deg[v]==delta)for(int w:g[v])if(w>v&&deg[w]==delta)ds.join(v,w);
  vector<vector<int>>groups(n);for(int v=0;v<n;v++)if(deg[v]==delta)groups[ds.find(v)].push_back(v);
  vector<vector<int>>components;for(auto&c:groups)if(!c.empty())components.push_back(move(c));sort(components.begin(),components.end(),[](const auto&a,const auto&b){return a.front()<b.front();});
  int moore=1+delta+delta*(delta-1)+delta*(delta-1)*(delta-1);
  int capFail=0,exitFail=0,sizeFail=0,reachFail=0,passedNecessary=0,rootsThis=0,examined=0;map<int,int>hist;
  vector<int>load(n),local(n,-1);ofstream detail("COMPONENTS_D"+to_string(delta)+".jsonl");
  for(auto&C:components){
   if(double(clock()-start)/CLOCKS_PER_SEC>=budget){budgetStop=true;checkpoint();return 0;}
   totalComp++;examined++;hist[C.size()]++;vector<int>touched;int minOutside=delta,zeroExit=0;long long internalArcs=0,boundaryArcs=0;
   for(int c:C){int out=0;for(int x:g[c])if(deg[x]<delta){if(!load[x])touched.push_back(x);load[x]++;out++;boundaryArcs++;}else{assert(ds.find(x)==ds.find(c));internalArcs++;}minOutside=min(minOutside,out);zeroExit+=out==0;}
   int violations=0,firstViolation=-1,maxload=0;for(int x:touched){maxload=max(maxload,load[x]);if(load[x]>delta-deg[x]){violations++;if(firstViolation<0||x<firstViolation)firstViolation=x;}}
   bool badCap=violations>0,badExit=zeroExit>0,badSize=int(C.size())>moore;
   capFail+=badCap;exitFail+=badExit;sizeFail+=badSize;
   bool good=false;int badp=-1,badq=-1,diam=0;vector<int>ecc;
   if(!badCap&&!badExit&&!badSize){
    passedNecessary++;int k=C.size();for(int i=0;i<k;i++)local[C[i]]=i;
    vector<vector<int>>cg(k);for(int i=0;i<k;i++)for(int x:g[C[i]])if(local[x]>=0)cg[i].push_back(local[x]);
    vector<int>d(k),q(k);good=true;
    for(int r=0;r<k;r++){
     if(double(clock()-start)/CLOCKS_PER_SEC>=budget){budgetStop=true;checkpoint();return 0;}
     fill(d.begin(),d.end(),-1);int head=0,tail=1;q[0]=r;d[r]=0;int radius=0;
     while(head<tail){int u=q[head++];if(d[u]==3)continue;for(int v:cg[u])if(d[v]<0){d[v]=d[u]+1;radius=max(radius,d[v]);q[tail++]=v;}}
     rootsThis++;totalR3++;ecc.push_back(radius);
     if(tail<k){good=false;badp=C[r];for(int z=0;z<k;z++)if(d[z]<0){badq=C[z];break;}break;}
     diam=max(diam,radius);
    }
    for(int c:C)local[c]=-1;if(!good)reachFail++;
   }
   ostringstream rec;rec<<"{\"component_index\":"<<examined-1<<",\"Delta\":"<<delta<<",\"source_n\":"<<n<<",\"component_size\":"<<C.size()<<",\"vertices\":"<<ints(C)<<",\"internal_edges\":"<<internalArcs/2<<",\"boundary_spokes\":"<<boundaryArcs<<",\"boundary_vertices\":"<<touched.size()<<",\"max_boundary_load\":"<<maxload<<",\"capacity_violating_boundary_vertices\":"<<violations<<",\"first_capacity_violation\":";
   if(firstViolation<0)rec<<"null";else rec<<"{\"vertex\":"<<firstViolation<<",\"load\":"<<load[firstViolation]<<",\"degree\":"<<deg[firstViolation]<<",\"deficit\":"<<delta-deg[firstViolation]<<"}";
   rec<<",\"vertices_without_outside_exit\":"<<zeroExit<<",\"minimum_outside_degree\":"<<minOutside<<",\"Moore_D3_bound\":"<<moore<<",\"size_bound_pass\":"<<(badSize?"false":"true")<<",\"necessary_gates_pass\":"<<(!badCap&&!badExit&&!badSize?"true":"false")<<",\"internal_R3_roots_checked\":"<<ecc.size()<<",\"first_internal_pair_distance_gt3\":";
   if(badp<0)rec<<"null";else rec<<"["<<badp<<","<<badq<<"]";
   rec<<",\"eligible_copy\":"<<(good?"true":"false")<<"}";detail<<rec.str()<<"\n";detail.flush();
   if(good){
    hit=true;eligible++;int k=C.size();for(int i=0;i<k;i++)local[C[i]]=n+i;
    long long added=internalArcs/2+boundaryArcs;string name="HIT_D"+to_string(delta)+"_n"+to_string(n+k)+".edges";ofstream graph(name);graph<<n+k<<" "<<m+added<<"\n";long long written=0;
    for(int u=0;u<n;u++)for(int v:g[u])if(u<v){graph<<u<<" "<<v<<"\n";written++;}
    for(int c:C)for(int x:g[c])if(deg[x]<delta){graph<<x<<" "<<local[c]<<"\n";written++;}else if(c<x){graph<<local[c]<<" "<<local[x]<<"\n";written++;}
    assert(written==m+added);ofstream h("HIT.json");h<<"{\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"Delta\":"<<delta<<",\"source_file\":\""<<path<<"\",\"new_n\":"<<n+k<<",\"new_m\":"<<m+added<<",\"component\":"<<ints(C)<<",\"new_labels_start\":"<<n<<",\"internal_diameter\":"<<diam<<",\"internal_allroot_eccentricities\":"<<ints(ecc)<<",\"old_edges_retained\":true,\"new_degrees\":"<<delta<<",\"graph\":\""<<name<<"\",\"boundary_loads\":[";
    sort(touched.begin(),touched.end());for(size_t i=0;i<touched.size();i++){int x=touched[i];if(i)h<<",";h<<"{\"vertex\":"<<x<<",\"load\":"<<load[x]<<",\"old_degree\":"<<deg[x]<<"}";}h<<"],\"D_le5_by_component_copy_lemma\":true,\"source_D5_BFS\":0,\"R4_calls\":0}";checkpoint();cout<<"HIT "<<name<<"\n";return 0;
   }
   for(int x:touched)load[x]=0;
  }
  sourceComplete++;
  ostringstream p;p<<"{\"Delta\":"<<delta<<",\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"saturated_vertices\":"<<sat<<",\"total_components\":"<<components.size()<<",\"components_examined\":"<<examined<<",\"capacity_fail_components\":"<<capFail<<",\"exit_fail_components\":"<<exitFail<<",\"Moore_size_fail_components\":"<<sizeFail<<",\"necessary_gate_pass_components\":"<<passedNecessary<<",\"internal_R3_fail_components\":"<<reachFail<<",\"internal_R3_roots\":"<<rootsThis<<",\"eligible_components\":0,\"component_size_histogram\":{";
  bool first=true;for(auto[s,c]:hist){if(!first)p<<",";first=false;p<<"\""<<s<<"\":"<<c;}p<<"}}";profiles<<p.str()<<"\n";profiles.flush();checkpoint();cout<<p.str()<<"\n"<<flush;
 }
 checkpoint();return 0;
}
