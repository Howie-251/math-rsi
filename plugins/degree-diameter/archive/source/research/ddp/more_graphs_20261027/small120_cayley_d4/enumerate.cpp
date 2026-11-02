#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
struct Group{string name;int n,id,z;vector<int>inv,par,quo;vector<vector<int>>mul;long long cases=0;array<long long,3>kind{};long long hit=0,all_even=0,all_odd=0,mixed=0,qfull=0,qfull_notfull=0,qfull_z_absent=0,qfull_z_present=0;};
int main(int argc,char**argv){assert(argc==3);clock_t start=clock();rlimit limit{2,3};setrlimit(RLIMIT_CPU,&limit);ifstream in(argv[1]);ofstream out(argv[2]);int gn;in>>gn;vector<Group>groups(gn);for(auto&g:groups){in>>g.name>>g.n>>g.id>>g.z;g.inv.resize(g.n);g.par.resize(g.n);g.quo.resize(g.n);for(auto&v:g.inv)in>>v;for(auto&v:g.par)in>>v;for(auto&v:g.quo)in>>v;g.mul.resize(g.n,vector<int>(g.n));for(auto&row:g.mul)for(auto&v:row)in>>v;}
 bool running=true,found=false,timeout=false;string hitgroup;array<int,4>hitset{};long long total=0;
 for(auto&g:groups){if(!running)break;vector<int>I,R;for(int x=0;x<g.n;x++)if(x!=g.id){if(g.inv[x]==x)I.push_back(x);else if(x<g.inv[x])R.push_back(x);}int seen[120]={},stamp=0,q[120];
 auto test=[&](array<int,4>s,int kind){if((total&1023)==0&&double(clock()-start)/CLOCKS_PER_SEC>2.7){timeout=true;running=false;return;}g.cases++;g.kind[kind]++;total++;stamp++;int head=0,tail=1;q[0]=g.id;seen[g.id]=stamp;for(int d=0;d<4;d++){int bound=tail;while(head<bound){int u=q[head++];for(int a:s){int v=g.mul[u][a];if(seen[v]!=stamp){seen[v]=stamp;q[tail++]=v;}}}}
  if(g.name=="S5"){int odd=0;for(int a:s)odd+=g.par[a];if(odd==0)g.all_even++;else if(odd==4)g.all_odd++;else g.mixed++;}
  if(g.z>=0){uint64_t classes=0;for(int j=0;j<tail;j++)classes|=uint64_t(1)<<g.quo[q[j]];if(__builtin_popcountll(classes)==60){g.qfull++;if(tail<120)g.qfull_notfull++;if(seen[g.z]!=stamp)g.qfull_z_absent++;else g.qfull_z_present++;}}
  if(tail==120){g.hit++;running=false;found=true;hitgroup=g.name;hitset=s;cout<<"HIT "<<g.name;for(int a:s)cout<<' '<<a;cout<<endl;}
 };
 for(int a=0;a<(int)I.size()&&running;a++)for(int b=a+1;b<(int)I.size()&&running;b++)for(int c=b+1;c<(int)I.size()&&running;c++)for(int d=c+1;d<(int)I.size()&&running;d++)test({I[a],I[b],I[c],I[d]},0);
 for(int a=0;a<(int)I.size()&&running;a++)for(int b=a+1;b<(int)I.size()&&running;b++)for(int r:R){if(!running)break;test({I[a],I[b],r,g.inv[r]},1);}
 for(int a=0;a<(int)R.size()&&running;a++)for(int b=a+1;b<(int)R.size()&&running;b++)test({R[a],g.inv[R[a]],R[b],g.inv[R[b]]},2);
 cout<<"GROUP "<<g.name<<" cases="<<g.cases<<" full="<<g.hit<<" quotientfull="<<g.qfull<<endl;
 }
 out<<"{\"status\":\""<<(found?"FIRST_FULL_HIT":timeout?"PARTIAL_CPU_LIMIT":"COMPLETE_TWO_GROUP_SCOPE")<<"\",\"cases\":"<<total<<",\"groups\":[";
 for(size_t i=0;i<groups.size();i++){if(i)out<<',';auto&g=groups[i];out<<"{\"group\":\""<<g.name<<"\",\"cases\":"<<g.cases<<",\"four_involution_sets\":"<<g.kind[0]<<",\"two_involutions_onepair_sets\":"<<g.kind[1]<<",\"two_pair_sets\":"<<g.kind[2]<<",\"full120_hits\":"<<g.hit<<",\"S5_all_even_sets\":"<<g.all_even<<",\"S5_all_odd_sets\":"<<g.all_odd<<",\"S5_mixed_parity_sets\":"<<g.mixed<<",\"central_quotient60_full_sets\":"<<g.qfull<<",\"quotient60_full_but120_notfull\":"<<g.qfull_notfull<<",\"quotient60full_central_minusI_missing\":"<<g.qfull_z_absent<<",\"quotient60full_central_minusI_reached\":"<<g.qfull_z_present<<"}";}
 out<<"],\"first_full_hit\":";if(!found)out<<"null";else{out<<"{\"group\":\""<<hitgroup<<"\",\"generator_ids\":[";for(int i=0;i<4;i++){if(i)out<<',';out<<hitset[i];}out<<"]}";}out<<",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"DONE cases="<<total<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}
