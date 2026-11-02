#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 clock_t start=clock();ifstream f(argv[1],ios::binary);uint32_t n,m2;f.read((char*)&n,4);f.read((char*)&m2,4);
 assert(n==186033&&m2==2021634);vector<uint32_t>off(n+1),adj(m2);f.read((char*)off.data(),4*(n+1));f.read((char*)adj.data(),4*m2);
 vector<int>pins={72425,85923,89934,95946,103392,107088,113094,120546,127006};
 vector<int>d(n,-1),q(n);int h=0,t=0;for(int p:pins){assert(off[p+1]-off[p]<11);d[p]=0;q[t++]=p;}
 while(h<t){int x=q[h++];if(d[x]==5)continue;for(uint32_t k=off[x];k<off[x+1];k++){int y=adj[k];if(d[y]<0){d[y]=d[x]+1;q[t++]=y;}}}
 vector<int>missing;for(uint32_t x=0;x<n;x++)if(d[x]<0)missing.push_back(x);
 ofstream out(argv[2]);out<<"{\"source_n\":"<<n<<",\"source_m\":"<<m2/2<<",\"radius\":5,\"mandatory_pin_count\":9,\"covered_count\":"<<n-missing.size()<<",\"missing_count\":"<<missing.size()<<",\"missing\":[";
 for(size_t i=0;i<missing.size();i++){if(i)out<<',';out<<missing[i];}
 out<<"],\"proposed_reverse_mask_bytes\":"<<uint64_t(24676)*((missing.size()+63)/64)*8<<",\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"mandatory missing "<<missing.size()<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}
