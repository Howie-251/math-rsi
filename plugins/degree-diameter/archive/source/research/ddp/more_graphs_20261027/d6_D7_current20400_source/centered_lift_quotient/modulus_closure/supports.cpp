#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
struct Port{int to,a,b,c,rev;};Port port[48][6];
__uint128_t sums[1200];long long words;
void visit(int v,int a,int b,int c,int forbidden,int depth){
 sums[25*v+a+5*b]|=__uint128_t(1)<<(c+56);words++;
 if(depth==7)return;
 for(int k=0;k<6;k++)if(k!=forbidden){auto&p=port[v][k];visit(p.to,(a+p.a)%5,(b+p.b)%5,c+p.c,p.rev,depth+1);}
}
int main(int argc,char**argv){
 assert(argc==3);clock_t start=clock();rlimit lim{3,3};setrlimit(RLIMIT_CPU,&lim);ifstream in(argv[1]);string out=argv[2];int n,k;in>>n>>k;assert(n==48&&k==6);
 for(auto&row:port)for(auto&p:row)in>>p.to>>p.a>>p.b>>p.c>>p.rev;
 for(int v=0;v<48;v++)for(int s=0;s<6;s++){auto&p=port[v][s];auto&r=port[p.to][p.rev];assert(r.to==v&&r.rev==s&&(p.a+r.a)%5==0&&(p.b+r.b)%5==0&&p.c+r.c==0);}
 ofstream binary(out+"/endpoint_scalar_masks.u128le.bin",ios::binary);
 int K=999,wr=-1,wq=-1;vector<int>witness;long long total=0;
 for(int root=0;root<48;root++){
  fill(begin(sums),end(sums),0);words=0;visit(root,0,0,0,-1,0);assert(words==117187);total+=words;
  for(int q=0;q<1200;q++){
   vector<int>values;for(int s=-56;s<=56;s++)if((sums[q]>>(s+56))&1)values.push_back(s);
   if((int)values.size()<K){K=values.size();wr=root;wq=q;witness=values;}
   char bytes[16];for(int j=0;j<16;j++)bytes[j]=(sums[q]>>(8*j))&255;binary.write(bytes,16);
  }
 }
 ofstream f(out+"/SUPPORTS.json");f<<"{\"status\":\"COMPLETE_INTEGER_ENDPOINT_SUPPORTS\",\"K\":"<<K<<",\"slots\":57600,\"total_NB_words\":"<<total<<",\"scalar_range\":[-56,56],\"binary\":\"endpoint_scalar_masks.u128le.bin\",\"binary_layout\":\"57600 littleendian128bit masks, rootmajor, q=25base+a+5b; bit(c+56) indicates c\",\"cap_witness\":{\"root_base\":"<<wr<<",\"target_base\":"<<wq/25<<",\"a\":"<<wq%5<<",\"b\":"<<wq%25/5<<",\"integer_scalar_sums\":[";
 for(size_t i=0;i<witness.size();i++){if(i)f<<',';f<<witness[i];}f<<"]},\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"graph_generation\":false,\"BFS\":0}\n";
 cout<<"K="<<K<<" caproot="<<wr<<" capq="<<wq<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
