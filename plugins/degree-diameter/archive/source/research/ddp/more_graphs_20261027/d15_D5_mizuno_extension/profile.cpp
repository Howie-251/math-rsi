#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
void ints(ostream&f,const vector<int>&v){f<<'[';for(size_t i=0;i<v.size();i++){if(i)f<<',';f<<v[i];}f<<']';}
int main(int argc,char**argv){
 assert(argc==3);clock_t start=clock();rlimit limit{4,5};setrlimit(RLIMIT_CPU,&limit);
 const int N=100132,W=(N+63)/64;string dir=argv[2];vector<vector<int>>g(N);ifstream in(argv[1]);string line;long long m=0,declared=-1;
 while(getline(in,line)){auto p=line.find_first_not_of(" \t\r");if(p==string::npos)continue;
  if(line[p]=='#'){istringstream s(line.substr(p+1));long long n0,m0;if(s>>n0>>m0){assert(n0==N);declared=m0;}continue;}
  istringstream s(line);int u,v;s>>u>>v;assert(s);if(m==0&&u==N&&v>N){declared=v;continue;}
  assert(0<=u&&u<N&&0<=v&&v<N&&u!=v);g[u].push_back(v);g[v].push_back(u);m++;}
 assert(declared<0||declared==m);vector<int>free,degree;map<int,int>hist;long long slots=0;
 ofstream deg(dir+"/degree15.u8.bin",ios::binary);
 for(int v=0;v<N;v++){int d=g[v].size();assert(d<=15);hist[d]++;slots+=15-d;degree.push_back(d);unsigned char b=d;deg.write((char*)&b,1);if(d<15)free.push_back(v);}deg.close();
 {ofstream f(dir+"/free_ports.json");f<<"{\"source_n\":"<<N<<",\"source_m\":"<<m<<",\"delta\":15,\"ports\":";ints(f,free);f<<",\"degrees\":[";
  for(size_t i=0;i<free.size();i++){if(i)f<<',';f<<degree[free[i]];}f<<"],\"free_slots\":[";
  for(size_t i=0;i<free.size();i++){if(i)f<<',';f<<15-degree[free[i]];}f<<"]}\n";}
 vector<int>sample=free;if(sample.size()>20)sample.resize(20);vector<vector<int>>layers;vector<int>sizes;long long sum=0;
 ofstream masks(dir+"/first20_R4.u64le.bin",ios::binary);vector<int>d(N),q(N);
 // The established exact depth4 BFS kernel; no all-source distances.
 for(int root:sample){fill(d.begin(),d.end(),-1);int h=0,t=0;d[root]=0;q[t++]=root;
  while(h<t){int u=q[h++];if(d[u]==4)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q[t++]=v;}}
  vector<int>counts(5);vector<U>bits(W);for(int v=0;v<N;v++)if(d[v]>=0){counts[d[v]]++;bits[v/64]|=U(1)<<(v%64);}
  layers.push_back(counts);sizes.push_back(t);sum+=t;masks.write((char*)bits.data(),W*8);}
 masks.close();bool enough=sample.size()==20;bool larger=enough&&sum*15*94186LL>227600LL*20*N;
 // Complementary exact full-neighborhood transfer, reusing the same source adjacency.
 clock_t starstart=clock();vector<int>satN(N),prototypes;
 for(int u=0;u<N;u++)if(degree[u]==15)for(int v:g[u])satN[v]++;
 for(int v=0;v<N;v++)if(degree[v]>0&&satN[v]==0)prototypes.push_back(v);
 int starecc=-1;
 if(!prototypes.empty()){
  int prototype=prototypes.front();vector<int>pins=g[prototype];ofstream out(dir+"/star_graph_d15_D5_n100133.edges");
  out<<N+1<<' '<<m+pins.size()<<'\n';long long copied=0;for(int u=0;u<N;u++)for(int v:g[u])if(u<v){out<<u<<' '<<v<<'\n';copied++;}
  assert(copied==m);for(int v:pins)out<<N<<' '<<v<<'\n';out.close();
  g.push_back({});for(int v:pins){assert(g[v].size()<15);g[N].push_back(v);g[v].push_back(N);}for(auto&row:g)assert(row.size()<=15);
  vector<int>sd(N+1,-1),sq(N+1);int h=0,t=0;sd[N]=0;sq[t++]=N;
  while(h<t){int u=sq[h++];for(int v:g[u])if(sd[v]<0){sd[v]=sd[u]+1;sq[t++]=v;}}
  assert(t==N+1);starecc=*max_element(sd.begin(),sd.end());assert(starecc<=5);
 }
 {ofstream f(dir+"/SPARE_STAR_RESULT.json");f<<"{\"status\":\""<<(prototypes.empty()?"EXACT_FULL_SPARE_STAR_SCOPE_EMPTY":"COMPLETE100133_SPARE_STAR_EXTENSION")<<"\",\"source_n\":"<<N<<",\"source_m\":"<<m<<",\"prototypes_checked\":"<<N<<",\"passing_prototypes\":";ints(f,prototypes);
  f<<",\"actual_new_n\":";if(prototypes.empty())f<<"null";else f<<N+1;
  f<<",\"new_root_eccentricity\":";if(starecc<0)f<<"null";else f<<starecc;
  f<<",\"new_root_BFS\":"<<(!prototypes.empty()?1:0)<<",\"source_allBFS\":0,\"extra_CPU_seconds\":"<<double(clock()-starstart)/CLOCKS_PER_SEC<<"}\n";}
 ofstream f(dir+"/PROFILE.json");f<<setprecision(15)<<"{\"status\":\"LITERAL_SOURCE_AND_FIRST20_R4_COMPLETE\",\"source_n\":"<<N<<",\"source_m\":"<<m<<",\"maximum_degree\":"<<hist.rbegin()->first<<",\"degree_histogram\":{";
 bool sep=false;for(auto[k,v]:hist){if(sep)f<<',';sep=true;f<<'"'<<k<<"\":"<<v;}f<<"},\"free_vertices\":"<<free.size()<<",\"free_slots\":"<<slots<<",\"first20_free_vertices\":";ints(f,sample);
 f<<",\"first20_degrees\":[";for(size_t i=0;i<sample.size();i++){if(i)f<<',';f<<degree[sample[i]];}f<<"],\"R4_layer_sizes\":[";
 for(size_t i=0;i<layers.size();i++){if(i)f<<',';ints(f,layers[i]);}f<<"],\"R4_sizes\":";ints(f,sizes);f<<",\"R4_balls_computed\":"<<sample.size()<<",\"sum_R4_sizes\":"<<sum;
 f<<",\"mean_R4_size\":"<<(sample.empty()?0.:double(sum)/sample.size())<<",\"mean_R4_fraction\":"<<(sample.empty()?0.:double(sum)/sample.size()/N)<<",\"comparison_D14_rare15_mean_fraction\":"<<227600./15/94186;
 f<<",\"sphere_prediction_supported\":"<<(larger?"true":"false")<<",\"sample_has20_roots\":"<<(enough?"true":"false")<<",\"mask_words_per_row\":"<<W<<",\"all_source_BFS\":0,\"graphs_generated\":"<<(!prototypes.empty()?1:0)<<",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"PROFILE literal "<<N<<'/'<<m<<" free="<<free.size()<<" meanR4fraction="<<(sample.empty()?0.:double(sum)/sample.size()/N)<<" prediction="<<larger<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
