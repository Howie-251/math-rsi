// Independent raw edge-list parser and complete BFS for an explicit root range.
// All-roots mode is optional; default wrapper uses a mathematically complete
// cover of the pairs not already supplied by its source/core theorem.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <ctime>
using namespace std;
int main(int argc,char**argv){try{
 if(argc!=6)throw runtime_error("usage: check_roots graph delta diameter first_root past_last_root");
 ifstream f(argv[1]);int n,m;if(!(f>>n>>m))throw runtime_error("header");
 int cap=stoi(argv[2]),D=stoi(argv[3]),lo=stoi(argv[4]),hi=stoi(argv[5]);if(hi<0)hi=n;if(lo<0||hi>n||lo>=hi)throw runtime_error("root range");
 vector<vector<int>>adj(n);int a,b,count=0;while(f>>a>>b){if(a<0||b>=n||a>=b)throw runtime_error("edge");adj[a].push_back(b);adj[b].push_back(a);++count;}
 if(count!=m)throw runtime_error("edge count");int maxdeg=0;for(auto&r:adj){sort(r.begin(),r.end());if(adjacent_find(r.begin(),r.end())!=r.end())throw runtime_error("duplicate");maxdeg=max(maxdeg,int(r.size()));}if(maxdeg>cap)throw runtime_error("degree");
 vector<int>d(n),q(n);int roots=0,maxecc=0;double start=double(clock())/CLOCKS_PER_SEC;
 for(int root=lo;root<hi;++root){fill(d.begin(),d.end(),-1);int h=0,t=1;q[0]=root;d[root]=0;while(h<t){int u=q[h++];for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;q[t++]=v;}}
  int ecc=*max_element(d.begin(),d.end());if(t!=n||ecc>D){cout<<"{\"status\":\"FAIL\",\"root\":"<<root<<",\"visited\":"<<t<<",\"eccentricity\":"<<ecc<<"}\n";return 1;}maxecc=max(maxecc,ecc);++roots;
 }
 cout<<"{\"status\":\"PASS_SPECIFIED_ROOTS\",\"n\":"<<n<<",\"m\":"<<m<<",\"maximum_degree\":"<<maxdeg<<",\"first_root\":"<<lo<<",\"past_last_root\":"<<hi<<",\"complete_BFS_roots\":"<<roots<<",\"maximum_checked_eccentricity\":"<<maxecc<<",\"CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";return 0;
}catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
