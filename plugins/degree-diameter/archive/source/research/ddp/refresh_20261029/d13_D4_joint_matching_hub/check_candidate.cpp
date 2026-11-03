#include <algorithm>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
  assert(argc==4);clock_t start=clock();double limit=stod(argv[3]);constexpr int n=6805,w=6804;
  vector<vector<int>>adj(n);ifstream source(argv[1]);string s;
  while(getline(source,s)){if(s.empty()||s[0]=='#')continue;istringstream row(s);int u,v;row>>u>>v;adj[u].push_back(v);adj[v].push_back(u);}
  ifstream selected(argv[2]);int u,v,k=0;vector<int>endpoints;
  while(selected>>u>>v){assert(u!=v);auto a=find(adj[u].begin(),adj[u].end(),v),b=find(adj[v].begin(),adj[v].end(),u);assert(a!=adj[u].end()&&b!=adj[v].end());adj[u].erase(a);adj[v].erase(b);adj[u].push_back(w);adj[v].push_back(w);adj[w].push_back(u);adj[w].push_back(v);endpoints.push_back(u);endpoints.push_back(v);++k;}
  assert(k>=1&&k<=6);sort(endpoints.begin(),endpoints.end());assert(unique(endpoints.begin(),endpoints.end())==endpoints.end());for(int x=0;x<w;++x)assert(adj[x].size()==13);assert(adj[w].size()==2*k);
  vector<int>d(n),queue(n),roots={w};for(int r=0;r<w;++r)roots.push_back(r);int checked=0;
  for(int root:roots){if(double(clock()-start)/CLOCKS_PER_SEC>limit){cout<<"{\"status\":\"BUDGET_PARTIAL\",\"roots_checked\":"<<checked<<",\"next_root\":"<<root<<"}\n";return 0;}fill(d.begin(),d.end(),-1);int head=0,tail=0;d[root]=0;queue[tail++]=root;while(head<tail){int x=queue[head++];if(d[x]==4)continue;for(int y:adj[x])if(d[y]<0){d[y]=d[x]+1;queue[tail++]=y;}}++checked;if(tail<n){int target=find(d.begin(),d.end(),-1)-d.begin();cout<<"{\"status\":\"FAIL\",\"root\":"<<root<<",\"target\":"<<target<<",\"roots_checked\":"<<checked<<",\"unreached\":"<<n-tail<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";return 0;}}
  ofstream edges("HIT6805.edges");long long m=0;for(auto&a:adj)m+=a.size();edges<<n<<' '<<m/2<<'\n';for(int x=0;x<n;++x)for(int y:adj[x])if(x<y)edges<<x<<' '<<y<<'\n';cout<<"{\"status\":\"HIT_D_AT_MOST_4\",\"roots_checked\":"<<checked<<",\"n\":6805,\"m\":"<<m/2<<",\"hub_degree\":"<<2*k<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
}
