// Pure positive certificate checker: independently enumerates every residual input.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;
struct BC{int port;vector<pair<int,int>>edges;};vector<BC> cases;array<int,16>mate;int port;ifstream cert;uint64_t count=0;
void verify(){vector<pair<int,int>>a;for(int v=0;v<16;v++)if(mate[v]>v)a.emplace_back(2*v+1,2*mate[v]+1);
 for(auto&b:cases){auto req=a;for(auto[u,v]:b.edges)req.emplace_back(2*u,2*v);req.emplace_back(2*port+1,2*b.port);assert(req.size()==13);unsigned char bytes[56];cert.read((char*)bytes,56);assert(cert.gcount()==56);bool required[32][32]{};for(int j=0;j<13;j++){auto[u,v]=req[j];assert(bytes[2*j]==u&&bytes[2*j+1]==v);required[u][v]=required[v][u]=true;}
 uint32_t seen=0;int found=0;for(int j=0;j<30;j++){unsigned u=bytes[26+j],v=bytes[26+(j+1)%30];assert(u<32&&v<32);assert(!(seen>>u&1));seen|=1u<<u;if(required[u][v])found++;else assert(__builtin_popcount(u^v)==1);}assert(seen==(0xffffffffu^(1u<<7)^(1u<<2)));assert(found==13);count++;}}
void enumerate(vector<int>vs){if(vs.empty()){verify();return;}int a=vs.front();for(int j=1;j<(int)vs.size();j++){int b=vs[j];vector<int>rest;for(int k=1;k<(int)vs.size();k++)if(k!=j)rest.push_back(vs[k]);mate[a]=b;mate[b]=a;enumerate(rest);mate[a]=mate[b]=-1;}}
int main(int argc,char**argv){assert(argc==3);ifstream in(argv[1]);int bport;while(in>>bport){BC b;b.port=bport;for(int j=0;j<6;j++){int a,z;in>>a>>z;b.edges.emplace_back(a,z);}cases.push_back(b);}assert(cases.size()==3);cert.open(argv[2],ios::binary);assert(cert);mate.fill(-1);for(port=0;port<16;port++)if(port!=3&&port!=6&&port!=12){vector<int>vs;for(int v=0;v<16;v++)if(v!=3&&v!=6&&v!=12&&v!=port)vs.push_back(v);assert(vs.size()==12);enumerate(vs);}assert(count==405405);char extra;assert(!cert.get(extra));cout<<"{\"status\":\"PASS\",\"records\":"<<count<<",\"required_edges\":13,\"cycle_vertices\":30,\"record_bytes\":56,\"total_bytes\":"<<count*56<<"}\n";}
