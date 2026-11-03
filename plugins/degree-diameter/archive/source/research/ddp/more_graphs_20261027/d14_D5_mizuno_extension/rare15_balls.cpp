#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
void ints(ostream&f,const vector<int>&v){f<<'[';for(size_t j=0;j<v.size();j++){if(j)f<<',';f<<v[j];}f<<']';}
int main(int argc,char**argv){
 assert(argc==3);clock_t start=clock();rlimit limit{8,9};setrlimit(RLIMIT_CPU,&limit);
 const int n=94186,W=(n+63)/64;vector<vector<int>>g(n);ifstream in(argv[1]);string line;
 long long m=0;while(getline(in,line)){size_t p=line.find_first_not_of(" \t\r");if(p==string::npos||line[p]=='#')continue;
  istringstream s(line);int u,v;s>>u>>v;assert(s&&0<=u&&u<n&&0<=v&&v<n&&u!=v);
  g[u].push_back(v);g[v].push_back(u);m++;}
 vector<int>low;for(int v=0;v<n;v++){assert(g[v].size()<=14);if(g[v].size()==12)low.push_back(v);}assert(low.size()==15&&m==657452);
 vector<vector<int>>layers;ofstream binary(string(argv[2])+"/rare15_R4.u64le.bin",ios::binary);
 vector<int>d(n),q(n);
 // Exact depth4 BFS kernel reused from h9_d12_eightpin_extensions/cover.cpp.
 for(int p:low){fill(d.begin(),d.end(),-1);int h=0,t=0;d[p]=0;q[t++]=p;
  while(h<t){int u=q[h++];if(d[u]==4)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q[t++]=v;}}
  vector<U>bits(W);vector<int>counts(5);for(int v=0;v<n;v++)if(d[v]>=0){bits[v/64]|=U(1)<<(v%64);counts[d[v]]++;}
  binary.write((char*)bits.data(),W*8);layers.push_back(counts);}
 binary.close();ofstream f(string(argv[2])+"/RARE15_BALLS.json");
 f<<"{\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"degree12_vertices\":";ints(f,low);
 f<<",\"root_R4_layer_sizes\":[";for(int i=0;i<15;i++){if(i)f<<',';ints(f,layers[i]);}
 f<<"],\"R4_balls_computed\":15,\"mask_words_per_row\":"<<W<<",\"source_allBFS\":0,\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"15 cached R4 balls; CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
