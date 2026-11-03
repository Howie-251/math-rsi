#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
using U=uint64_t;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
template<class T> void arr(ostream&o,const vector<T>&a){o<<'[';for(size_t i=0;i<a.size();i++){if(i)o<<',';o<<a[i];}o<<']';}
int main(int argc,char**argv){
 assert(argc==6);double start=cpu();string source=argv[1],r4file=argv[2],freefile=argv[3],out=argv[4];double budget=stod(argv[5]);
 rlimit lim{(rlim_t)ceil(budget),(rlim_t)ceil(budget+1)};setrlimit(RLIMIT_CPU,&lim);
 const int N=94186,W=1472,K=3685,SW=(K+63)/64;
 vector<int>free;{ifstream f(freefile);int v;while(f>>v)free.push_back(v);}assert(free.size()==K);
 vector<vector<int>>g(N);long long m=0;{ifstream f(source);string line;while(getline(f,line)){auto p=line.find_first_not_of(" \t\r");if(p==string::npos||line[p]=='#')continue;istringstream s(line);int a,b;s>>a>>b;assert(s&&a>=0&&a<N&&b>=0&&b<N&&a!=b);g[a].push_back(b);g[b].push_back(a);m++;}}
 assert(m==657452);vector<int>actual,spare(K),degreehist(15);for(int v=0;v<N;v++){int d=g[v].size();assert(d>=12&&d<=14);degreehist[d]++;if(d<14)actual.push_back(v);}assert(actual==free&&degreehist[12]==15&&degreehist[13]==3670);
 for(int j=0;j<K;j++)spare[j]=14-g[free[j]].size();
 {ofstream f(out+"/FREE_SPARES.txt");for(int j=0;j<K;j++)f<<free[j]<<' '<<spare[j]<<'\n';}
 vector<U>r3(size_t(K)*W,0);vector<unsigned short>providers(N);vector<int>seen(N,0),depth(N),queue(N),sizes(K);double bfsstart=cpu();
 for(int j=0;j<K;j++){
  if(cpu()-start>budget-.2){ofstream f(out+"/NATIVE_RESULT.json");f<<"{\"status\":\"PARTIAL_R3_BUDGET\",\"completed_R3_roots\":"<<j<<",\"native_CPU_seconds\":"<<cpu()-start<<"}\n";return 0;}
  int stamp=j+1,head=0,tail=0;queue[tail++]=free[j];seen[free[j]]=stamp;depth[free[j]]=0;
  while(head<tail){int u=queue[head++];if(depth[u]==3)continue;for(int v:g[u])if(seen[v]!=stamp){seen[v]=stamp;depth[v]=depth[u]+1;queue[tail++]=v;}}
  U*row=&r3[size_t(j)*W];for(int k=0;k<tail;k++){int v=queue[k];row[v/64]|=U(1)<<(v%64);providers[v]++;}sizes[j]=tail;
 }
 double bfscpu=cpu()-bfsstart;
 {ofstream f(out+"/allfree_R3.u64le.bin",ios::binary);f.write((char*)r3.data(),r3.size()*8);}
 {ofstream f(out+"/target_R3_provider_counts.u16le.bin",ios::binary);f.write((char*)providers.data(),N*2);}
 vector<int>T0;map<int,int>hist;for(int t=0;t<N;t++){hist[providers[t]]++;if(!providers[t])T0.push_back(t);}
 vector<U>r4(size_t(K)*W);{ifstream f(r4file,ios::binary);assert(f);f.seekg(0,ios::end);assert(f.tellg()==streamoff(r4.size()*8));f.seekg(0);assert(f.read((char*)r4.data(),r4.size()*8));}
 vector<U>supportbits(size_t(T0.size())*SW);vector<int>supportcount(T0.size()),mass(T0.size());
 map<pair<int,int>,vector<int>>opposed;int bad=-1;vector<int>badsupport;
 for(size_t i=0;i<T0.size();i++){
  int t=T0[i];vector<int>support;
  for(int j=0;j<K;j++)if(r4[size_t(j)*W+t/64]>>(t%64)&1){support.push_back(j);supportbits[i*SW+j/64]|=U(1)<<(j%64);mass[i]+=min(2,spare[j]);}
  supportcount[i]=support.size();if(mass[i]<2&&bad<0){bad=t;badsupport=support;}
  if(support.size()==2&&spare[support[0]]==1&&spare[support[1]]==1){int a=support[0],b=support[1];opposed[{a,b}].push_back(t);}
 }
 {ofstream f(out+"/T0_R4_support.u64le.bin",ios::binary);f.write((char*)supportbits.data(),supportbits.size()*8);}
 vector<vector<pair<int,int>>>opp(K);for(auto&[ab,ts]:opposed){opp[ab.first].push_back({ab.second,ts[0]});opp[ab.second].push_back({ab.first,ts[0]});}
 vector<int>color(K,-1),parent(K,-1),odd;int components=0;
 for(int root=0;root<K&&odd.empty();root++)if(!opp[root].empty()&&color[root]<0){components++;vector<int>q{root};color[root]=0;for(size_t h=0;h<q.size()&&odd.empty();h++){int u=q[h];for(auto[v,t]:opp[u]){if(color[v]<0){color[v]=color[u]^1;parent[v]=u;q.push_back(v);}else if(color[v]==color[u]){vector<int>a,b;map<int,int>pos;for(int z=u;z>=0;z=parent[z]){pos[z]=a.size();a.push_back(z);}int z=v;while(!pos.count(z)){b.push_back(z);z=parent[z];}a.resize(pos[z]+1);reverse(b.begin(),b.end());odd=a;odd.insert(odd.end(),b.begin(),b.end());odd.push_back(u);break;}}}}
 {ofstream f(out+"/T0.json");arr(f,T0);f<<'\n';}
 {ofstream f(out+"/T0_SUPPORTS.json");f<<"{\"support_words_per_target\":"<<SW<<",\"free_order\":\"FREE_ORDER.txt\",\"support_bits\":\"T0_R4_support.u64le.bin\",\"rows\":[";for(size_t i=0;i<T0.size();i++){if(i)f<<',';f<<"{\"target\":"<<T0[i]<<",\"R4_support_count\":"<<supportcount[i]<<",\"effective_capacity\":"<<mass[i]<<'}';}f<<"]}\n";}
 {ofstream f(out+"/OPPOSITION_GRAPH.json");f<<"{\"components\":"<<components<<",\"edges\":[";bool first=true;for(auto&[ab,ts]:opposed){if(!first)f<<',';first=false;f<<"{\"pins\":["<<free[ab.first]<<','<<free[ab.second]<<"],\"targets\":";arr(f,ts);f<<'}';}f<<"],\"odd_cycle_pins\":[";for(size_t i=0;i<odd.size();i++){if(i)f<<',';f<<free[odd[i]];}f<<"]}\n";}
 if(bad>=0){ofstream f(out+"/CAPACITY_WITNESS.json");f<<"{\"target\":"<<bad<<",\"pins\":[";for(size_t i=0;i<badsupport.size();i++){if(i)f<<',';f<<free[badsupport[i]];}f<<"]}\n";}
 {ofstream f(out+"/R3_META.json");f<<"{\"source_n\":"<<N<<",\"source_m\":"<<m<<",\"free_count\":"<<K<<",\"words_per_row\":"<<W<<",\"free_order\":\"FREE_ORDER.txt\",\"radius\":3,\"complete\":true,\"source_edge_reads\":1,\"R3_runs\":"<<K<<",\"R4_runs\":0,\"degree_histogram\":{\"12\":"<<degreehist[12]<<",\"13\":"<<degreehist[13]<<",\"14\":"<<degreehist[14]<<"},\"provider_count_histogram\":{";bool first=true;for(auto[a,b]:hist){if(!first)f<<',';first=false;f<<'\"'<<a<<"\":"<<b;}f<<"}}\n";}
 string status=bad>=0?"STRICT_K2_CAPACITY_REJECTION":!odd.empty()?"STRICT_K2_ODD_CYCLE_REJECTION":"NECESSARY_ROUTE_GATE_NO_REJECTION";
 {ofstream f(out+"/NATIVE_RESULT.json");f<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"source_n\":"<<N<<",\"source_m\":"<<m<<",\"completed_R3_roots\":"<<K<<",\"zero_R3_provider_targets\":"<<T0.size()<<",\"minimum_R3_provider_count\":"<<hist.begin()->first<<",\"maximum_R3_provider_count\":"<<hist.rbegin()->first<<",\"minimum_T0_R4_support\":"<<(supportcount.empty()?-1:*min_element(supportcount.begin(),supportcount.end()))<<",\"minimum_T0_effective_capacity\":"<<(mass.empty()?-1:*min_element(mass.begin(),mass.end()))<<",\"opposition_edges\":"<<opposed.size()<<",\"odd_cycle_found\":"<<(!odd.empty()?"true":"false")<<",\"R3_CPU_seconds\":"<<bfscpu<<",\"native_CPU_seconds\":"<<cpu()-start<<",\"source_edge_reads\":1,\"old_R4_cache_reads\":1,\"new_R4_runs\":0,\"source_D5_BFS\":0,\"solver_calls\":0}\n";}
 cout<<status<<" T0="<<T0.size()<<" R3CPU="<<bfscpu<<" totalCPU="<<cpu()-start<<'\n';
}
