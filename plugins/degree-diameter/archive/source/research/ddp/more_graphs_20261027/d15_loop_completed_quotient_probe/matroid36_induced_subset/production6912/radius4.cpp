#include <algorithm>
#include <array>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 clock_t begin=clock();ifstream f(argv[1]);int n,m;f>>n>>m;
 vector<vector<int>> a(n);int u,v;while(f>>u>>v){a[u].push_back(v);a[v].push_back(u);}
 vector<int> seen(n,-1),q(n);int full=0;
 for(int root=0;root<n;root++){
  int head=0,tail=1;q[0]=root;seen[root]=root;
  array<int,5> shells{};shells[0]=1;
  for(int d=1;d<=4;d++){
   int lim=tail;
   while(head<lim){int x=q[head++];for(int y:a[x])if(seen[y]!=root){seen[y]=root;q[tail++]=y;shells[d]++;}}
  }
  if(tail<n){
   int miss=0;while(seen[miss]==root)miss++;
   cout<<"{\"status\":\"FIRST_R4_FAILURE\",\"actual_n\":"<<n<<",\"actual_m\":"<<m<<",\"completed_roots\":"<<root+1<<",\"full_R4_roots_before_failure\":"<<full<<",\"first_failure_root\":"<<root<<",\"first_missing_vertex\":"<<miss<<",\"root_R4_count\":"<<tail<<",\"root_R4_missing\":"<<n-tail<<",\"root_shells\":[";
   for(int d=0;d<=4;d++)cout<<(d?",":"")<<shells[d];
   cout<<"],\"global_D\":null,\"cpu_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";return 0;
  }full++;
 }
 cout<<"{\"status\":\"ALL_ROOTS_R4_PASS\",\"actual_n\":"<<n<<",\"actual_m\":"<<m<<",\"completed_roots\":"<<n<<",\"global_D_upper_bound\":4,\"cpu_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";
}
