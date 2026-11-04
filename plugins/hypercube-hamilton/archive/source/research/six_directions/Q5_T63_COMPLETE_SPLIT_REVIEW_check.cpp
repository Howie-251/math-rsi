#include <bits/stdc++.h>
using namespace std;
using U=unsigned char;
void require(bool b,string s){if(!b)throw runtime_error(s);}
vector<U> read(string p){ifstream f(p,ios::binary);require(bool(f),"read "+p);return vector<U>((istreambuf_iterator<char>(f)),{});}
int ix[16][16]; vector<pair<int,int>> edges;
int pc(uint32_t n){return __builtin_popcount(n);}
struct Table {vector<string> keys;vector<uint32_t> masks;map<int,int> hist;long long cycles=0;};
// Independent exhaustive recursion builds the domain as a set; no producer order premise.
void matching(unsigned left,string &m,string tail,unordered_set<string>& expected){
 if(!left){expected.insert(m+tail);return;}
 int x=__builtin_ctz(left);unsigned rest=left^(1u<<x);
 for(int y=0;y<16;y++)if(rest>>y&1){m[x]=y;m[y]=x;matching(rest^(1u<<y),m,tail,expected);m[x]=m[y]=char(255);}
}
Table check(string stem,bool n){
 unordered_set<string> expected;string m(16,char(255));vector<int> even;
 for(int x=0;x<16;x++)if(pc(x)%2==0)even.push_back(x);
 for(int b:{3,15}){
  if(n)matching(65535u^(1u<<0)^(1u<<b),m,string({char(0),char(255)}),expected);
  else for(int c:even)for(int d:even)if(c!=0&&c!=b&&d>c&&d!=b)matching(65535u^(1u<<0)^(1u<<b)^(1u<<c)^(1u<<d),m,string({char(0),char(b)}),expected);
 }
 require(expected.size()==(n?270270:311850),"independent domain count");
 auto in=read(stem+"_inputs.bin"), masks=read(stem+"_unions.bin"), cert=read(stem+"_certificates.bin");
 require(in.size()==18*expected.size()&&masks.size()==4*expected.size(),"table sizes");
 Table out;size_t pos=0;
 for(size_t i=0;i<in.size();i+=18){
  string key((char*)&in[i],18);require(expected.erase(key)==1,"input equality/uniqueness");out.keys.push_back(key);
  require(pos+19<=cert.size(),"certificate header boundary");require(equal(in.begin()+i,in.begin()+i+18,cert.begin()+pos),"certificate bound input");pos+=18;
  int count=cert[pos++],len=n?15:14;require(count>0,"nonempty witnesses");uint32_t mask=0;
  for(int k=0;k<count;k++){
   require(pos+len<=cert.size(),"cycle boundary");array<int,16> where;where.fill(-1);
   for(int j=0;j<len;j++){int v=cert[pos+j];require(v<16&&where[v]==-1,"cycle unique vertex");where[v]=j;}
   for(int x=0;x<16;x++){
    bool omitted=x==in[i+16]||x==in[i+17];require((where[x]<0)==omitted,"exact retained set");
    int y=in[i+x];if(y!=255){require(y<16&&y!=x&&in[i+y]==x,"matching");require(where[x]>=0&&where[y]>=0,"required endpoint");int delta=abs(where[x]-where[y]);require(delta==1||delta==len-1,"required edge");}
   }
   for(int j=0;j<len;j++){int a=cert[pos+j],b=cert[pos+(j+1)%len];if(in[i+a]!=b){require(pc(a^b)==1,"new edge short");mask|=1u<<ix[a][b];}}
   pos+=len;out.cycles++;
  }
  uint32_t claimed=0;for(int j=0;j<4;j++)claimed|=uint32_t(masks[i/18*4+j])<<(8*j);
  require(mask==claimed,"positive union exact equality");out.masks.push_back(mask);out.hist[pc(mask)]++;
 }
 require(pos==cert.size()&&expected.empty(),"complete domains/EOF");return out;
}
int main(){try{
 memset(ix,-1,sizeof ix);for(int a=0;a<16;a++)for(int b=a+1;b<16;b++)if(pc(a^b)==1){ix[a][b]=ix[b][a]=edges.size();edges.push_back({a,b});}
 Table n=check("Q5_T63_n14_exact",true),t=check("Q5_T63_t44_rich_all",false);
 require(n.hist.begin()->first>=15,"N14 lower bound");
 vector<U> low;unordered_map<string,uint32_t> actual;long long nlow=0,maps=0;
 for(int i=0;i<(int)t.keys.size();i++)if(pc(t.masks[i])<18){
  nlow++;auto key=t.keys[i];low.insert(low.end(),key.begin(),key.end());for(int j=0;j<4;j++)low.push_back(t.masks[i]>>(8*j));
  array<int,4> p{0,1,2,3};do{for(int shift=0;shift<16;shift++)if(pc(shift)%2){
   array<int,16> f{};for(int x=0;x<16;x++){f[x]=shift;for(int bit=0;bit<4;bit++)if(x>>bit&1)f[x]^=1<<p[bit];}
   string out(18,char(255));for(int x=0;x<16;x++)if(U(key[x])!=255)out[f[x]]=f[U(key[x])];
   out[16]=min(f[U(key[16])],f[U(key[17])]);out[17]=max(f[U(key[16])],f[U(key[17])]);
   uint32_t mask=0;for(int e=0;e<32;e++)if(t.masks[i]>>e&1)mask|=1u<<ix[f[edges[e].first]][f[edges[e].second]];
   auto it=actual.emplace(out,mask);require(it.second||it.first->second==mask,"duplicate transported mask agreement");maps++;
  }}while(next_permutation(p.begin(),p.end()));
 }
 require(low==read("Q5_T63_t44_rich_low_inputs.bin"),"low subset exact bytes");require(nlow==6978&&maps==6978*192LL&&actual.size()==163152,"low transform coverage");
 array<vector<int>,33> bysize;for(int i=0;i<(int)n.keys.size();i++)bysize[pc(n.masks[i])].push_back(i);
 unordered_set<string> pairs;long long comparisons=0;
 for(auto &[k,m]:actual)for(int w=0;w<=32-pc(m);w++)for(int i:bysize[w]){comparisons++;if(!(m&n.masks[i]))require(pairs.insert(n.keys[i].substr(0,16)+k).second,"pair unique");}
 auto frozen=read("Q5_T63_disjoint_pairs.bin");require(frozen.size()==pairs.size()*34,"pair cardinality");auto remaining=pairs;
 for(size_t i=0;i<frozen.size();i+=34)require(remaining.erase(string((char*)&frozen[i],34))==1,"frozen pair equality");require(remaining.empty()&&pairs.size()==1320,"all exception pairs");
 auto global=read("Q5_T63_exception_positive_cycles.bin");require(global.size()==1320*63,"global size");map<int,int> bridges;
 for(size_t i=0;i<global.size();i+=63){string key((char*)&global[i],34);require(pairs.erase(key)==1,"global exact pair cover");
  array<int,32> where;where.fill(-1);for(int j=0;j<29;j++){int x=global[i+34+j];require(x<32&&where[x]<0,"global vertex uniqueness");where[x]=j;}
  for(int x=0;x<32;x++){bool omitted=x==0||x==(16+U(key[32]))||x==(16+U(key[33]));require((where[x]<0)==omitted,"global exact omissions");int y=U(key[x]);if(y!=255){y+=(x>=16?16:0);require(where[x]>=0&&where[y]>=0,"global required endpoints");int delta=abs(where[x]-where[y]);require(delta==1||delta==28,"global required edges");}}
  int cross=0;for(int j=0;j<29;j++){int a=global[i+34+j],b=global[i+34+(j+1)%29];bool required=(a/16==b/16&&U(key[a])==b%16);if(!required)require(pc(a^b)==1,"global short new edge");cross+=(a/16!=b/16);}bridges[cross]++;
 }
 require(pairs.empty()&&bridges[4]==1308&&bridges[6]==12,"all positive bridge totals");
 ofstream o("Q5_T63_COMPLETE_SPLIT_REVIEW_check.json");o<<"{\"status\":\"PASS\",\"N14_inputs\":"<<n.keys.size()<<",\"T44_inputs\":"<<t.keys.size()<<",\"N14_cycles_replayed\":"<<n.cycles<<",\"T44_cycles_replayed\":"<<t.cycles<<",\"low_T44\":"<<nlow<<",\"transform_descriptions\":"<<maps<<",\"actual_low_states\":"<<actual.size()<<",\"width_filtered_comparisons\":"<<comparisons<<",\"exact_exception_pairs\":1320,\"positive_29cycles\":1320,\"four_bridges\":1308,\"six_bridges\":12,\"N14_hist\":{";
 bool comma=false;for(auto [a,b]:n.hist){if(comma)o<<",";comma=true;o<<"\""<<a<<"\":"<<b;}o<<"},\"T44_hist\":{";comma=false;for(auto [a,b]:t.hist){if(comma)o<<",";comma=true;o<<"\""<<a<<"\":"<<b;}o<<"}}\n";cout<<"PASS all domains, positive cycles, unions, transforms, exceptions\n";
 }catch(exception&e){cerr<<e.what()<<"\n";return 1;}}
