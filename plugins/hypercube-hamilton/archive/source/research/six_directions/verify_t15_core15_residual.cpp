// Pure witness verifier. Independently enumerates port combinations, A matchings and all crossing bijections.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <cstdint>
using namespace std;
struct BCase{vector<int>ports;vector<pair<int,int>>edges;};vector<BCase>cases;array<int,16>mate;vector<int>ports;int c;ifstream cert;uint64_t checked=0;
void verify(){vector<pair<int,int>>a;for(int v=0;v<16;v++)if(mate[v]>v)a.emplace_back(2*v+1,2*mate[v]+1);
 for(auto&bc:cases){auto bp=bc.ports;do{auto req=a;for(auto[u,v]:bc.edges)req.emplace_back(2*u,2*v);for(int j=0;j<c;j++)req.emplace_back(2*ports[j]+1,2*bp[j]);assert(req.size()==13);unsigned char bytes[56];cert.read((char*)bytes,56);assert(cert.gcount()==56);bool required[32][32]{};for(int j=0;j<13;j++){auto[u,v]=req[j];assert(bytes[2*j]==u&&bytes[2*j+1]==v);required[u][v]=required[v][u]=true;}
 uint32_t seen=0;int found=0;for(int j=0;j<30;j++){unsigned u=bytes[26+j],v=bytes[26+(j+1)%30];assert(u<32&&v<32);assert(!(seen>>u&1));seen|=1u<<u;if(required[u][v])found++;else assert(__builtin_popcount(u^v)==1);}assert(seen==(0xffffffffu^2u^4u));assert(found==13);checked++;
 }while(next_permutation(bp.begin(),bp.end()));}}
void pairup(vector<int>vs){if(vs.empty()){verify();return;}int a=vs.front();for(int j=1;j<(int)vs.size();j++){int b=vs[j];vector<int>rest;for(int k=1;k<(int)vs.size();k++)if(k!=j)rest.push_back(vs[k]);mate[a]=b;mate[b]=a;pairup(rest);mate[a]=mate[b]=-1;}}
void select(vector<int>&base,int start){if(ports.size()==size_t(c)){vector<int>vs;for(int v:base)if(find(ports.begin(),ports.end(),v)==ports.end())vs.push_back(v);assert(vs.size()==size_t(13-c));pairup(vs);return;}for(int j=start;j<int(base.size());j++){ports.push_back(base[j]);select(base,j+1);ports.pop_back();}}
int main(int argc,char**argv){assert(argc==4);c=stoi(argv[1]);assert(c==1||c==3);ifstream in(argv[2]);int first;while(in>>first){BCase b;b.ports.push_back(first);for(int j=1;j<c;j++){int v;in>>v;b.ports.push_back(v);}for(int j=0;j<(13-c)/2;j++){int a,z;in>>a>>z;b.edges.emplace_back(a,z);}cases.push_back(b);}assert(cases.size()==size_t(c==1?12:1));cert.open(argv[3],ios::binary);assert(cert);mate.fill(-1);vector<int>base;for(int v=1;v<16;v++)if(v!=10&&v!=15)base.push_back(v);assert(base.size()==13);select(base,0);assert(checked==1621620);char extra;assert(!cert.get(extra));cout<<"{\"status\":\"PASS\",\"c\":"<<c<<",\"records\":"<<checked<<",\"required_edges\":13,\"cycle_vertices\":30,\"record_bytes\":56,\"total_bytes\":"<<checked*56<<"}\n";}
