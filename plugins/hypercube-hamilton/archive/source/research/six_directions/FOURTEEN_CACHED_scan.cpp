#include <bits/stdc++.h>
using namespace std;using U=uint64_t;using B=uint32_t;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
struct Key{B m,j,o;bool operator==(const Key&b)const{return m==b.m&&j==b.j&&o==b.o;}};
struct Hash{size_t operator()(const Key&k)const{return U(k.m)*0x9e3779b185ebca87ULL^(U(k.j)<<17)^U(k.o)*0xc2b2ae3d27d4eb4fULL;}};
struct Value{int family,id;};struct Witness{int d,family,id;U S;B M,J,O;};
B trans(B a,int t){B b=0;while(a){int x=__builtin_ctz(a);a&=a-1;b|=B(1)<<(x^t);}return b;}
int sid(int m,int j,int o){return(m<<16)|(j<<8)|o;}
void put(unsigned char*p,U x,int n){for(int j=0;j<n;++j)p[j]=(x>>(8*j))&255;}
int main(){try{
 unordered_map<Key,Value,Hash>lookup;unordered_set<int>shapes;ifstream reg("FOURTEEN_CACHED_registry.txt");Key k;Value val;while(reg>>k.m>>k.j>>k.o>>val.family>>val.id){need(lookup.emplace(k,val).second,"duplicate registry");shapes.insert(sid(__builtin_popcount(k.m),__builtin_popcount(k.j),__builtin_popcount(k.o)));}need(!lookup.empty(),"registry empty");int project[6][64];for(int d=0;d<6;++d)for(int x=0;x<64;++x)project[d][x]=(x&((1<<d)-1))|((x>>(d+1))<<d);
 ofstream report("FOURTEEN_CACHED_result.json");report<<"{\"status\":\"PRODUCER_CANDIDATE_GEOMETRY_HITS_ONLY_LOCAL_GATES_PENDING\",\"reports\":[";bool comma=false;U total=0,covered=0,totalhits=0,tries=0;map<int,U>hist;auto start=chrono::steady_clock::now();
 for(int v:{1,7,31})for(int free=0;free<2;++free){string tag="h14_v"+to_string(v)+"_"+(free?"free":"covered");ifstream in("FOURTEEN_REUSE_remaining_"+tag+".bin",ios::binary);need(bool(in),"source");ofstream wit("FOURTEEN_CACHED_all_hits_"+tag+".bin",ios::binary),rem("FOURTEEN_CACHED_remaining_"+tag+".bin",ios::binary);unsigned char rec[13];uint32_t index=0,hits=0;
  while(in.read((char*)rec,13)){U H=1;for(int i=0;i<13;++i)H|=U(1)<<rec[i];map<int,Witness>seen;
   for(int d=0;d<6;++d){vector<int>za,zb,wa,wb;for(int i=0;i<6;++i)(((rec[i]>>d&1)==(v>>d&1))?za:zb).push_back(rec[i]);for(int i=6;i<13;++i)(((rec[i]>>d&1)==(v>>d&1))?wa:wb).push_back(rec[i]);int s=int(za.size())+1-int(wa.size());bool even=s>=0;vector<int>pool,minor,major;if(even){if(wa.empty())continue;pool=za;minor=zb;major=wb;}else{s=-s;for(int x:wa)if(x!=(1<<d)&&(!free||x!=v))pool.push_back(x);minor=wb;major=zb;}if(s<=0||s>int(pool.size())||!shapes.count(sid(minor.size(),major.size()+s,s)))continue;B M=0,base=0;for(int x:minor)M|=B(1)<<project[d][x];for(int x:major)base|=B(1)<<project[d][x];
    for(unsigned subset=0;subset<(1U<<pool.size());++subset)if(__builtin_popcount(subset)==s){U S=0;B O=0;for(unsigned j=0;j<pool.size();++j)if(subset>>j&1){int x=pool[j],y=x^(1<<d);need(!(H>>y&1),"mirror hole/root");S|=U(1)<<x;O|=B(1)<<project[d][y];}B J=base|O;int a=__builtin_ctz(M?M:O);auto it=lookup.find({trans(M,a),trans(J,a),trans(O,a)});++tries;if(it==lookup.end())continue;auto h=it->second;int code=(h.family==30?0:1000)+h.id;seen.emplace(code,Witness{d,h.family,h.id,S,M,J,O});}
   }
   if(seen.empty())rem.write((char*)rec,13);else{++hits;for(auto [code,w]:seen){unsigned char b[28]{};put(b,index,4);b[4]=w.family;b[5]=w.d;put(b+6,w.id,2);put(b+8,w.S,8);put(b+16,w.M,4);put(b+20,w.J,4);put(b+24,w.O,4);wit.write((char*)b,28);++hist[code];++totalhits;}}
   ++index;
  }
  need(in.eof()&&!in.gcount(),"source alignment");total+=index;covered+=hits;if(comma)report<<",";comma=true;report<<"{\"v\":"<<v<<",\"free_target\":"<<(free?"true":"false")<<",\"input\":"<<index<<",\"candidate_covered\":"<<hits<<",\"remaining\":"<<index-hits<<"}";cout<<tag<<" input="<<index<<" candidate="<<hits<<" remaining="<<index-hits<<endl;
 }
 need(total==48211,"source count");double seconds=chrono::duration<double>(chrono::steady_clock::now()-start).count();report<<"],\"input\":"<<total<<",\"candidate_covered\":"<<covered<<",\"remaining\":"<<total-covered<<",\"record_candidate_orbit_hits\":"<<totalhits<<",\"legal_projections_checked\":"<<tries<<",\"seconds\":"<<seconds<<",\"candidate_hit_histogram\":{";bool first=true;for(auto [key,n]:hist){if(!first)report<<",";first=false;report<<"\""<<key<<"\":"<<n;}report<<"},\"local_inputs_accepted\":false,\"independent_application_acceptance\":false,\"full_fourteen_hole_proved\":false,\"full_P6_proved\":false}\n";
}catch(const exception&e){cerr<<e.what()<<endl;return 1;}return 0;}
