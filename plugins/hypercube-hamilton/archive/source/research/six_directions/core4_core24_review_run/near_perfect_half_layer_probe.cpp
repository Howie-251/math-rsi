// Exhaust a 7! near-perfect B(Q5) family; NOT a Q6 proof.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using Mate=std::array<int,16>;
void gen(unsigned mask,Mate &p,std::vector<Mate>&out){
    if(!mask){out.push_back(p);return;}
    int a=__builtin_ctz(mask);
    for(int j=0;j<4;j++){
        int b=a^(1<<j);
        if(mask&(1u<<b)){p[a]=b;p[b]=a;gen(mask&~(1u<<a)&~(1u<<b),p,out);p[a]=p[b]=-1;}
    }
}
int main(int argc,char**argv){
    if(argc!=2)return 2;
    Mate p;p.fill(-1);std::vector<Mate>full,punctured;
    gen(65535,p,full);gen(65535^3,p,punctured);
    std::array<int,7>ev={3,5,6,9,10,12,15},permutation=ev;
    std::ofstream out(argv[1]);out<<"perm,n0,n1,N0,N1\n";
    unsigned cases=0,failures=0;uint64_t checked=0;
    do {
        int m[32];std::fill(m,m+32,-1);
        for(int q=0;q<16;q++)if(__builtin_popcount((unsigned)q)%2 && q!=1){m[2*q]=2*q+1;m[2*q+1]=2*q;}
        m[1]=3;m[3]=1;
        for(int j=0;j<7;j++){m[2*ev[j]]=2*permutation[j]+1;m[2*permutation[j]+1]=2*ev[j];}
        int found0=-1,found1=-1;
        for(unsigned i=0;i<full.size()&&found0<0;i++)for(unsigned j=0;j<punctured.size();j++){
            checked++;int x=0;uint32_t seen=1u;int visits=1;
            while(true){
                int next=(x&1)?2*punctured[j][x>>1]+1:2*full[i][x>>1];
                if(next<0 || next>=32 || (seen&(1u<<next)))break;
                seen|=1u<<next;visits++;x=next;
                if(x==2)break;
                next=m[x];
                if(next<0 || (seen&(1u<<next)))break;
                seen|=1u<<next;visits++;x=next;
            }
            if(x==2&&visits==30){found0=(int)i;found1=(int)j;break;}
        }
        for(int q:permutation)out<<char('A'+q);out<<','<<found0<<','<<found1;
        if(found0>=0){
            out<<',';for(int q:full[found0])out<<char('A'+q);
            out<<',';for(int q:punctured[found1])out<<(q<0?'-':char('A'+q));
        }
        out<<'\n';cases++;
        if(found0<0){failures++;std::cout<<"UNSAT_CANDIDATE permutation ";for(int q:permutation)std::cout<<q<<' ';std::cout<<'\n';break;}
    }while(std::next_permutation(permutation.begin(),permutation.end()));
    std::cout<<"full="<<full.size()<<" punctured="<<punctured.size()<<" cases="<<cases<<" failed="<<failures<<" pairs_checked="<<checked<<'\n';
}
