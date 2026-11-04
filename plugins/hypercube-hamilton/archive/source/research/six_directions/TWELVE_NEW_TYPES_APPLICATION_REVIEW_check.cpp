#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <iterator>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
vector<unsigned char> read(const string&f){ifstream in(f,ios::binary);need(bool(in),"missing "+f);return {(istreambuf_iterator<char>(in)),{}};}
struct Key{uint32_t m,j,u;bool operator==(const Key&b)const{return m==b.m&&j==b.j&&u==b.u;}};
struct Hash{size_t operator()(const Key&k)const{return uint64_t(k.m)*0x9e3779b185ebca87ULL^(uint64_t(k.j)<<19)^uint64_t(k.u)*0xc2b2ae3d27d4eb4fULL;}};
struct Value{int id,type,selected;};using Lookup=unordered_map<Key,Value,Hash>;
int project(int x,int d){return (x&((1<<d)-1))|((x>>(d+1))<<d);}
uint32_t translate(uint32_t a,int t){uint32_t b=0;while(a){int x=__builtin_ctz(a);a&=a-1;b|=uint32_t(1)<<(x^t);}return b;}
uint64_t get(const unsigned char*p,int n){uint64_t ans=0;for(int i=0;i<n;++i)ans|=uint64_t(p[i])<<(8*i);return ans;}
uint64_t rid(int v,uint32_t i){return (uint64_t(v)<<32)|i;}
struct Witness{int v,id,d;uint32_t index;uint64_t S;Key masks;};
using Witnesses=unordered_map<uint64_t,vector<Witness>>;
Witnesses loadw(const string&file,bool single){auto b=read(file);need(b.size()%28==0,"witness alignment");Witnesses out;
 for(size_t off=0;off<b.size();off+=28){auto*p=&b[off];Witness w;w.v=p[0];w.index=get(p+1,4);w.id=get(p+5,2);w.d=p[7];w.S=get(p+8,8);w.masks={uint32_t(get(p+16,4)),uint32_t(get(p+20,4)),uint32_t(get(p+24,4))};need((w.v==1||w.v==7||w.v==31)&&w.d<6&&w.id<380,"witness header");
 auto&vec=out[rid(w.v,w.index)];if(single)need(vec.empty(),"multiple selected witnesses");vec.push_back(w);
 }return out;}
struct Geometry{array<int,5>Z;array<int,6>W;uint64_t H;};
struct Hit{bool ok=false;Value val{};Key masks{};};
Hit eval(const Geometry&g,int v,int d,uint64_t S,const Lookup&lookup){vector<int>za,zb,wa,wb;
 for(int x:g.Z)(((x>>d)&1)==((v>>d)&1)?za:zb).push_back(x);
 for(int x:g.W)(((x>>d)&1)==((v>>d)&1)?wa:wb).push_back(x);
 int s=int(za.size())+1-int(wa.size());bool even=s>=3;if(!even){if(s>-3)return {};s=-s;}
 if(s>5||(even&&wa.empty()))return {};
 vector<int>pool=even?za:wa;uint64_t legal=0;for(int x:pool)if(even||x!=(1<<d))legal|=uint64_t(1)<<x;
 if(__builtin_popcountll(S)!=s||(S&~legal))return {};
 Key actual{};for(int x:even?zb:wb)actual.m|=uint32_t(1)<<project(x,d);for(int x:even?wb:zb)actual.j|=uint32_t(1)<<project(x,d);
 for(int x=0;x<64;++x)if((S>>x)&1){int y=x^(1<<d);need(!((g.H>>y)&1),"mirror is an original hole/root");actual.u|=uint32_t(1)<<project(y,d);}
 actual.j|=actual.u;int nm=__builtin_popcount(actual.m),nj=__builtin_popcount(actual.j),nu=__builtin_popcount(actual.u),type=-1;
 if(nm==2&&nj==8&&nu==3)type=0;if(nm==1&&nj==9&&nu==4)type=1;if(nm==0&&nj==8&&nu==4)type=2;if(nm==0&&nj==10&&nu==5)type=3;if(type<0)return {};
 need(!(actual.m&actual.j)&&nu==s,"actual masks");uint32_t anchor=actual.m?actual.m:actual.u;int t=__builtin_ctz(anchor);
 Key norm{translate(actual.m,t),translate(actual.j,t),translate(actual.u,t)};auto it=lookup.find(norm);if(it==lookup.end())return {};
 need(it->second.type==type,"type mismatch");Hit h;h.ok=true;h.val=it->second;h.masks=actual;return h;
}
int main(){try{
 ifstream in("TWELVE_NEW_TYPES_APPLICATION_REVIEW_lookup.txt");need(bool(in),"lookup");Lookup lookup;Key key;Value val;while(in>>key.m>>key.j>>key.u>>val.id>>val.type>>val.selected)need(lookup.emplace(key,val).second,"lookup duplicate");need(lookup.size()==59860,"lookup size");
 auto selected=loadw("TWELVE_NEW_TYPES_selected_witnesses.bin",true),allhits=loadw("TWELVE_NEW_TYPES_positive_hits.bin",false);
 long long total=0,covered=0,hitcount=0,allreplayed=0,selectedreplayed=0,sourceprojections=0;array<long long,380> histogram{};array<long long,4>chosenTypes{},shapeProjections{};cout<<"{\"reports\":[";int group=0;
 for(int v:{1,7,31}){auto raw=read("HIGHER_Q5_FULL_T37_FORCED_union_remaining_h12_v"+to_string(v)+"_covered.bin");need(raw.size()%11==0,"source alignment");vector<unsigned char>residual;long long ncovered=0;unordered_set<string>unique;
  for(size_t off=0;off<raw.size();off+=11){Geometry g;g.H=1;need(unique.insert(string((char*)&raw[off],11)).second,"duplicate original geometry");
   for(int j=0;j<11;++j){int x=raw[off+j];need(x<64&&x!=0&&!((g.H>>x)&1),"hole domain");need(__builtin_popcount(unsigned(x))%2==(j<5?0:1),"hole parity");g.H|=uint64_t(1)<<x;if(j<5)g.Z[j]=x;else g.W[j-5]=x;}
   need(is_sorted(g.Z.begin(),g.Z.end())&&is_sorted(g.W.begin(),g.W.end()),"hole order");need(!((g.H>>v)&1),"target is not covered");for(int z:g.Z)for(int w:g.W)need(__builtin_popcount(unsigned(z^w))!=1,"nonroot independence");
   uint64_t record=rid(v,off/11);auto chosen=selected.find(record);if(chosen!=selected.end()){auto&w=chosen->second[0];auto h=eval(g,v,w.d,w.S,lookup);need(h.ok&&h.val.selected&&h.val.id==w.id&&h.masks==w.masks,"selected witness failed");++selectedreplayed;++chosenTypes[h.val.type];}
   array<bool,380>expected{},actual{};auto hits=allhits.find(record);if(hits!=allhits.end())for(auto&w:hits->second){need(!expected[w.id],"duplicate record/orbit hit");expected[w.id]=true;auto h=eval(g,v,w.d,w.S,lookup);need(h.ok&&h.val.id==w.id&&h.masks==w.masks,"all-hit witness failed");++allreplayed;}
   bool any=false,anySelected=false;
   for(int d=0;d<6;++d){vector<int>za,wa;for(int x:g.Z)if(((x>>d)&1)==((v>>d)&1))za.push_back(x);for(int x:g.W)if(((x>>d)&1)==((v>>d)&1))wa.push_back(x);
    int s=int(za.size())+1-int(wa.size());bool even=s>=3;if(!even){if(s>-3)continue;s=-s;}if(s>5||(even&&wa.empty()))continue;vector<int>pool;if(even)pool=za;else for(int x:wa)if(x!=(1<<d))pool.push_back(x);
    int nm=even?5-za.size():6-wa.size(),nj=(even?6-wa.size():5-za.size())+s,type=-1;if(nm==2&&nj==8&&s==3)type=0;if(nm==1&&nj==9&&s==4)type=1;if(nm==0&&nj==8&&s==4)type=2;if(nm==0&&nj==10&&s==5)type=3;if(type<0)continue;
    for(unsigned subset=0;subset<(1U<<pool.size());++subset)if(__builtin_popcount(subset)==s){uint64_t S=0;for(unsigned i=0;i<pool.size();++i)if((subset>>i)&1)S|=uint64_t(1)<<pool[i];++sourceprojections;++shapeProjections[type];auto h=eval(g,v,d,S,lookup);if(h.ok){actual[h.val.id]=true;any=true;anySelected|=h.val.selected;}}
   }
   need(actual==expected,"complete per-record orbit-hit set differs");need(any==anySelected,"111/232 geometric predicate unions differ");need(anySelected==(chosen!=selected.end()),"selected coverage set differs");
   for(int i=0;i<380;++i)if(actual[i]){++histogram[i];++hitcount;}
   if(anySelected)++ncovered;else residual.insert(residual.end(),raw.begin()+off,raw.begin()+off+11);
  }
  need(residual==read("TWELVE_NEW_TYPES_positive_remaining_v"+to_string(v)+".bin"),"remaining byte sequence differs");long long count=raw.size()/11;total+=count;covered+=ncovered;
  if(group++)cout<<",";cout<<"{\"v\":"<<v<<",\"input\":"<<count<<",\"covered\":"<<ncovered<<",\"remaining\":"<<residual.size()/11<<"}";cerr<<"verified v"<<v<<" input "<<count<<" covered "<<ncovered<<" remaining "<<residual.size()/11<<"\n";
 }
 need(selectedreplayed==177838&&allreplayed==541463,"unconsumed witness records");need(total==215243&&covered==177838&&hitcount==541463,"totals");
 cout<<"],\"input\":"<<total<<",\"covered\":"<<covered<<",\"remaining\":"<<total-covered<<",\"all_source_projections_checked\":"<<sourceprojections<<",\"selected_witnesses_checked\":"<<selectedreplayed<<",\"all_hit_witnesses_checked\":"<<allreplayed<<",\"positive_record_orbit_sets_reconstructed\":"<<hitcount<<",\"selected_111_and_listed_232_predicate_unions_equal\":true,\"all_three_residual_files_byte_equal\":true,\"chosen_witness_type_histogram\":[";for(int i=0;i<4;++i){if(i)cout<<",";cout<<chosenTypes[i];}cout<<"],\"source_projection_type_histogram\":[";for(int i=0;i<4;++i){if(i)cout<<",";cout<<shapeProjections[i];}cout<<"],\"orbit_hit_histogram\":{";bool first=true;for(int i=0;i<380;++i)if(histogram[i]){if(!first)cout<<",";first=false;cout<<"\""<<i<<"\":"<<histogram[i];}cout<<"},\"pass\":true}\n";
}catch(const exception&e){cerr<<"CHECK FAILED "<<e.what()<<"\n";return 1;}return 0;}
