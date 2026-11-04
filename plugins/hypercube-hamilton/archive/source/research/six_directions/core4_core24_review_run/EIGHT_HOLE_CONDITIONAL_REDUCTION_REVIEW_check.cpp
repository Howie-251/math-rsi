#include <array>
#include <cstdint>
#include <iostream>
using U = uint64_t;
int bits(U x) { return __builtin_popcountll(x); }
bool row(int a,int b) {
    return (b==a+1 && a<=2) || (b==a && a>=1) || (b==a+2 && a<=2);
}
// Independent set-bit subset enumeration. Does not call or include the producer.
int main() {
    U even=0,odd=0;
    std::array<U,64> neighbours{};
    for(int x=0;x<64;++x) {
        ((bits(x)&1)?odd:even) |= U(1)<<x;
        for(int i=0;i<6;++i) neighbours[x] |= U(1)<<(x^(1<<i));
    }
    bool ok=true;
    std::cout << "[";
    for(int target : {7,31}) {
        std::array<U,6> face{};
        for(int i=0;i<6;++i) for(int x=0;x<64;++x)
            if(((x^target)&(1<<i))==0) face[i] |= U(1)<<x;
        long long total=0,failures=0,exception_only=0,exception_cuts=0;
        std::array<long long,7> good_counts{};
        std::array<std::array<long long,5>,4> rows{};
        U z1s=even & ~U(1) & ~neighbours[target];
        while(z1s) {
            int z1=__builtin_ctzll(z1s);z1s &= z1s-1;
            U z2s=z1s;
            while(z2s) {
                int z2=__builtin_ctzll(z2s);z2s &= z2s-1;
                U z3s=z2s;
                while(z3s) {
                    int z3=__builtin_ctzll(z3s);z3s &= z3s-1;
                    U z=(U(1)<<z1)|(U(1)<<z2)|(U(1)<<z3);
                    std::array<int,6> a{};
                    for(int i=0;i<6;++i) a[i]=bits(z&face[i]);
                    U w1s=odd & ~(neighbours[z1]|neighbours[z2]|neighbours[z3]) & ~(U(1)<<target);
                    while(w1s) {
                        int w1=__builtin_ctzll(w1s);w1s &= w1s-1;
                        U w2s=w1s;
                        while(w2s) {
                            int w2=__builtin_ctzll(w2s);w2s &= w2s-1;
                            U w3s=w2s;
                            while(w3s) {
                                int w3=__builtin_ctzll(w3s);w3s &= w3s-1;
                                U w=(U(1)<<target)|(U(1)<<w1)|(U(1)<<w2)|(U(1)<<w3);
                                int good=0,ordinary=0;
                                for(int i=0;i<6;++i) {
                                    int b=bits(w&face[i]);
                                    ++rows[a[i]][b];
                                    if(!row(a[i],b)) continue;
                                    ++good;
                                    bool exception=a[i]==0 && b==2 && (target&(1<<i)) &&
                                        ((w&face[i])==((U(1)<<target)|(U(1)<<(1<<i))));
                                    exception_cuts+=exception;
                                    ordinary+=!exception;
                                }
                                ++total;++good_counts[good];
                                failures+=good==0;
                                exception_only+=good>0 && ordinary==0;
                            }
                        }
                    }
                }
            }
        }
        ok &= failures==0;
        if(target==31)std::cout<<",";
        std::cout<<"{\"target\":"<<target<<",\"total\":"<<total<<",\"bad\":"<<failures
            <<",\"exception_only_geometries\":"<<exception_only<<",\"exception_cuts\":"<<exception_cuts
            <<",\"number_of_good_cuts_histogram\":[";
        for(int i=0;i<=6;++i)std::cout<<(i?",":"")<<good_counts[i];
        std::cout<<"],\"cut_row_histogram\":[";
        for(int a=0;a<=3;++a){if(a)std::cout<<",";std::cout<<"[";
            for(int b=0;b<=4;++b)std::cout<<(b?",":"")<<rows[a][b];std::cout<<"]";}
        std::cout<<"]}";
    }
    std::cout<<"]\n";
    return ok?0:1;
}
