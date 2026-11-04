#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using U=uint64_t;
int dim,N,terminal,partner_[64],route_[64]; U adj_[64];
uint64_t nodes,cap; bool cutoff;
bool dfs(int x,int previous,U left,int depth){
    if(++nodes>cap){cutoff=true;return false;}
    if(!left)return x==terminal;
    if(x==terminal)return false;
    U active=left|(U(1)<<x);
    for(U t=left;t;t&=t-1){int z=__builtin_ctzll(t);
        if(__builtin_popcountll(adj_[z]&active)<(z==terminal?1:2))return false;
    }
    if((depth&3)==0){
        U seen=U(1)<<x,front=seen;
        while(front){U next=0;for(U t=front;t;t&=t-1)next|=adj_[__builtin_ctzll(t)];front=next&active&~seen;seen|=front;}
        if(seen!=active)return false;
    }
    U choices=adj_[x]&left;
    if(partner_[x]>=0&&partner_[x]!=previous)choices&=U(1)<<partner_[x];
    std::vector<std::pair<int,int>> order;
    for(U t=choices;t;t&=t-1){int y=__builtin_ctzll(t);
        if(y==terminal && __builtin_popcountll(left)!=1)continue;
        if(partner_[y]>=0&&partner_[y]!=x&&!(left&(U(1)<<partner_[y])))continue;
        order.push_back({__builtin_popcountll(adj_[y]&left),y});
    }
    std::sort(order.begin(),order.end());
    for(auto item:order){int y=item.second;route_[depth]=y;
        if(dfs(y,x,left&~(U(1)<<y),depth+1))return true;
        if(cutoff)return false;
    }
    return false;
}
int main(){
    while(std::cin>>dim>>terminal>>cap){
        if(dim<2||dim>6)return 2;N=1<<dim;
        for(int i=0;i<N;i++)std::cin>>partner_[i];
        for(int i=0;i<N;i++){adj_[i]=0;for(int j=0;j<dim;j++)adj_[i]|=U(1)<<(i^(1<<j));}
        nodes=0;cutoff=false;route_[0]=0;
        U all=N==64?~U(0):(U(1)<<N)-1;
        bool found=dfs(0,-1,all&~U(1),1);
        std::cout<<(found?"FOUND":cutoff?"UNKNOWN":"EXHAUSTED")<<' '<<nodes;
        if(found)for(int i=0;i<N;i++)std::cout<<' '<<route_[i];
        std::cout<<'\n'<<std::flush;
    }
}
