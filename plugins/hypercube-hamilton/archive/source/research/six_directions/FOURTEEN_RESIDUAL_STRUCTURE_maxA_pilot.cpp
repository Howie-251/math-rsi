#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
struct Option{int q,t,w,b,c,perm;array<int,32>inverse;int cached=0;};
vector<int>E,O,T,order,partner;int ei[32],oi[32];vector<vector<int>>adj;
vector<array<int,32>> maps;vector<array<unsigned char,32>> comp[5];vector<Option>options;
U total=0,positive=0,limitCount=1000,tests=0;int orbit;bool stopped=false;string stem;
ofstream cert,fail;array<U,12> sizes{};array<U,5>casecounts{};
int root(array<unsigned char,14>&p,int x){while(p[x]!=x)x=p[x];return x;}
bool compatible(const Option&o,int row,const vector<pair<int,int>>&edges){
 ++tests;array<unsigned char,14>p;for(int i=0;i<14;++i)p[i]=i;
 auto &labels=comp[o.c][row];
 for(auto[x,y]:edges){int a=labels[o.inverse[x]],b=labels[o.inverse[y]];assert(a<14&&b<14);a=root(p,a);b=root(p,b);if(a==b)return false;p[a]=b;}
 return true;
}
void emit(U used,int size){
 if(total>=limitCount){stopped=true;return;}++total;++sizes[size];
 if(total%100000==0)cerr<<"orbit="<<orbit<<" tested="<<total<<" positive_before="<<positive<<"\n";
 vector<pair<int,int>> original;for(int i=0;i<(int)O.size();++i)if(partner[i]>=0)original.push_back({O[i],E[partner[i]]});
 int hv=partner[oi[31]]<0?-1:E[partner[oi[31]]];
 for(int optionindex=0;optionindex<(int)options.size();++optionindex){
  auto &o=options[optionindex];if(used>>ei[o.q]&1)continue;
  vector<pair<int,int>> modified;for(auto[x,y]:original)if(x!=31)modified.push_back({x,y});
  if(hv>=0)modified.push_back({o.w,hv});
  assert((int)modified.size()==size);
  for(int k=0;k<(int)comp[o.c].size();++k){int sindex=(o.cached+k)%comp[o.c].size();
   if(!compatible(o,sindex,modified))continue;
   o.cached=sindex;array<unsigned char,32>rec;rec.fill(255);vector<pair<int,int>>sorted=original;
   for(auto&e:sorted)if(e.first>e.second)swap(e.first,e.second);sort(sorted.begin(),sorted.end());
   int at=0;for(auto[x,y]:sorted){rec[at++]=x;rec[at++]=y;}
   rec[22]=size;rec[23]=o.q;rec[24]=o.t;rec[25]=o.w;rec[26]=o.b;rec[27]=o.c;
   rec[28]=sindex&255;rec[29]=sindex>>8;rec[30]=o.perm;rec[31]=hv>=0;
   cert.write((char*)rec.data(),32);++positive;++casecounts[o.c];return;
  }
 }
 fail<<"{\"star_orbit\":"<<orbit<<",\"maximal_index\":"<<total-1<<",\"edges\":[";
 bool comma=false;for(auto[x,y]:original){if(comma)fail<<',';comma=true;fail<<'['<<x<<','<<y<<']';}
 fail<<"],\"unmatched_even\":[";comma=false;for(int i=0;i<15;++i)if(!(used>>i&1)){if(comma)fail<<',';comma=true;fail<<E[i];}
 fail<<"],\"stored_forests_each_case\":8031,\"all_eligible_options_exhausted\":true,\"not_a_counterexample\":true}\n";
 cout<<"UNHIT orbit="<<orbit<<" index="<<total-1<<endl;stopped=true;
}
void search(int step,int used,int required,int size){
 if(stopped)return;
 if(__builtin_popcount(unsigned(required&~used))>int(O.size())-step)return;
 if(step==(int)O.size()){if(!(required&~used))emit(used,size);return;}
 int i=order[step],x=O[i];
 for(int e:adj[i])if(!(used>>e&1)){partner[i]=e;search(step+1,used|(1<<e),required,size+1);if(stopped)return;}
 if(find(T.begin(),T.end(),x)==T.end()){
  partner[i]=-1;int all=0;for(int e:adj[i])all|=1<<e;search(step+1,used,required|all,size);
 }
 partner[i]=-2;
}
void loadforests(string file,int which,int q,int b,int t){
 ifstream f(file,ios::binary);array<unsigned char,32>raw;
 while(f.read((char*)raw.data(),32)){
  array<unsigned char,32>p,degree{},label;for(int i=0;i<32;++i)p[i]=i;
  auto find=[&](int x){while(p[x]!=x)x=p[x];return x;};bool opening=false;
  set<pair<int,int>>seen;
  for(int i=0;i<32;i+=2){int x=raw[i],y=raw[i+1];assert(x<y&&__builtin_popcount(unsigned(x^y))==1&&seen.insert({x,y}).second);++degree[x];++degree[y];int a=find(x),b=find(y);assert(a!=b);p[a]=b;if((x==q&&y==t)||(y==q&&x==t))opening=true;}
  assert(opening);label.fill(255);map<int,int> ids;
  for(int x=0;x<32;++x){assert(degree[x]==(x==0||x==31?0:x==q||x==b?2:1));if(degree[x]){int r=find(x);if(!ids.count(r))ids[r]=ids.size();label[x]=ids[r];}}
  assert(ids.size()==14);comp[which].push_back(label);
 }
 assert(f.eof()&&f.gcount()==0&&comp[which].size()==(which==0||which==3?8031:7998));
}
int main(int argc,char**argv){
 if(argc<4)return 2;string dir=argv[1];orbit=stoi(argv[2]);limitCount=stoull(argv[3]);stem=dir+"/FOURTEEN_RESIDUAL_STRUCTURE_maxA_pilot_"+to_string(orbit);
 if(argc>4)stem=dir+"/"+string(argv[4]);
 ifstream tfile(dir+"/FOURTEEN_RESIDUAL_STRUCTURE_maxA_T_"+to_string(orbit)+".txt");int tx;while(tfile>>tx)T.push_back(tx);assert(T.size()==6);
 fill(ei,ei+32,-1);fill(oi,oi+32,-1);for(int x=1;x<32;++x)if(__builtin_popcount(unsigned(x))%2==0){ei[x]=E.size();E.push_back(x);}else if(__builtin_popcount(unsigned(x))>=3&&x!=14){oi[x]=O.size();O.push_back(x);}
 adj.resize(O.size());partner.assign(O.size(),-2);for(int i=0;i<(int)O.size();++i)for(int j=0;j<15;++j)if(__builtin_popcount(unsigned(O[i]^E[j]))==1)adj[i].push_back(j);
 for(int x:T)order.push_back(oi[x]);for(int i=0;i<(int)O.size();++i)if(find(order.begin(),order.end(),i)==order.end())order.push_back(i);
 array<int,5>perm{0,1,2,3,4};do{array<int,32>tr{};for(int x=0;x<32;++x)for(int i=0;i<5;++i)tr[x]|=((x>>perm[i])&1)<<i;maps.push_back(tr);}while(next_permutation(perm.begin(),perm.end()));
 ifstream opt(dir+"/FOURTEEN_RESIDUAL_STRUCTURE_maxA_options_"+to_string(orbit)+".bin",ios::binary);array<unsigned char,6>rec;
 while(opt.read((char*)rec.data(),6)){Option o;o.q=rec[0];o.t=rec[1];o.w=rec[2];o.b=rec[3];o.c=rec[4];o.perm=rec[5];assert(o.c>=0&&o.c<5);for(int x=0;x<32;++x)o.inverse[maps[o.perm][x]]=x;options.push_back(o);}
 loadforests(dir+"/TWELVE_ROOT_STAR_OPENING_case_00_forests.bin",0,3,4,7);
 loadforests(dir+"/TWELVE_ROOT_STAR_OPENING_case_01_forests.bin",1,3,4,11);
 loadforests(dir+"/TWELVE_ROOT_STAR_OPENING_case_02_forests.bin",2,15,1,14);
 loadforests(dir+"/TWELVE_ROOT_STAR_OPENING_case_03_forests.bin",3,15,1,7);
 loadforests(dir+"/TWELVE_ROOT_STAR_OPENING_case_04_forests.bin",4,15,16,7);

 cert.open(stem+"_certificates.bin",ios::binary);fail.open(stem+"_unhit.jsonl");search(0,0,0,0);
 ofstream out(stem+".json");out<<"{\"status\":\"PRODUCER_COMPATIBILITY_SEARCH\",\"star_orbit\":"<<orbit<<",\"tested_maximal_matchings\":"<<total<<",\"positive\":"<<positive<<",\"unhit\":"<<total-positive<<",\"component_kernel_tests\":"<<tests<<",\"case00_positive\":"<<casecounts[0]<<",\"case03_positive\":"<<casecounts[1]<<",\"limit\":"<<limitCount<<",\"entire_maximal_domain_enumerated\":"<<(!stopped?"true":"false")<<",\"certificate_bytes_per_record\":32,\"star_Q6_closed\":false,\"monotonic_extension_lemma_accepted\":false}\n";
 cout<<"orbit="<<orbit<<" tested="<<total<<" positive="<<positive<<" kerneltests="<<tests<<endl;
}
