#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using Mat=array<array<int,5>,5>;
using Mask=uint32_t;
int pc(Mask x){return __builtin_popcount(x);}
long long C[21][21]{};
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
struct Row {int id,J;uint64_t key;Mat m;};
struct Witness {int r0=-1,c0=-1;array<int,5> cols{};Mask T=0;};
struct Value {Row row;int patterns=0,maxK=-1,gap=0;Witness wit;long long literal=-1;};
array<Mask,5> rm,cm;array<array<Mask,5>,5> firstcell;
void labels(const Mat&m){
 rm.fill(0);cm.fill(0);for(auto&r:firstcell)r.fill(0);int k=0;
 for(int i=0;i<5;i++)for(int j=0;j<5;j++)for(int t=0;t<m[i][j];t++){
  Mask bit=Mask(1)<<k++;rm[i]|=bit;cm[j]|=bit;if(t==0)firstcell[i][j]=bit;
 }assert(k==20);
}
long long marked(int r0,int c0,Mask T){
 Mask B=rm[r0]|cm[c0];assert(!(T&B));assert(pc(T)==4);
 vector<Mask> R,S;
 for(int i=0;i<5;i++)if(!(rm[i]&B))R.push_back(rm[i]);
 for(int j=0;j<5;j++)if(!(cm[j]&B))S.push_back(cm[j]);
 long long ans=0;int nb=pc(B);
 for(int a=1;a<(1<<R.size());a++){
  Mask rr=T;for(int i=0;i<(int)R.size();i++)if(a>>i&1)rr|=R[i];
  for(int b=1;b<(1<<S.size());b++){
   Mask red=rr;for(int j=0;j<(int)S.size();j++)if(b>>j&1)red|=S[j];
   int nr=pc(red);assert(!(red&B));if(nr>10)continue;
   long long x=C[20-nr-nb][10-nr];
   ans+=((pc(a)+pc(b))%2?-x:x);
  }
 }assert(ans>=0);return ans;
}
long long literal(const Witness&w){
 Mask B=rm[w.r0]|cm[w.c0],free=((Mask(1)<<20)-1)&~(B|w.T);
 vector<Mask> bits;for(int i=0;i<20;i++)if(free>>i&1)bits.push_back(Mask(1)<<i);
 long long ans=0;
 for(int s=0;s<(1<<bits.size());s++)if(pc(s)==6){
  Mask red=w.T;for(int i=0;i<(int)bits.size();i++)if(s>>i&1)red|=bits[i];
  bool ar=false,ac=false;for(auto r:rm)if((red&r)==r)ar=true;
  for(auto c:cm)if((red&c)==c)ac=true;
  if(ar&&ac)ans++;
 }return ans;
}
void matrix(ostream&o,const Mat&m){
 o<<'[';for(int i=0;i<5;i++){if(i)o<<',';o<<'[';
  for(int j=0;j<5;j++){if(j)o<<',';o<<m[i][j];}o<<']';}o<<']';
}
int main(int argc,char**argv){
 double start=cpu();string mode=argc>1?argv[1]:"profile";
 for(int n=0;n<=20;n++){C[n][0]=C[n][n]=1;for(int k=1;k<n;k++)C[n][k]=C[n-1][k-1]+C[n-1][k];}
 ifstream in("INPUT.txt");int total;in>>total;assert(total==264);vector<Row> domain;
 for(int n=0;n<total;n++){Row v;in>>v.id>>v.key>>v.J;uint64_t key=0;
  for(auto&r:v.m)for(int&x:r){in>>x;assert(0<=x&&x<=4);key=5*key+x;}
  assert(in&&v.id==n&&key==v.key);domain.push_back(v);
 }
 int limit=mode=="profile"?5:total;vector<Value> values;long long patterns=0;
 ofstream all(mode=="profile"?"PROFILE_PATTERNS.tsv":"PATTERNS.tsv");
 all<<"id\tomit_row\tomit_col\tcol_by_row_0_to_4\tK\n";
 int minGap=1000000,minId=-1,maxAll=-1;bool failed=false;
 for(int n=0;n<limit;n++){
  Value v;v.row=domain[n];labels(v.row.m);
  for(int r0=0;r0<5;r0++)for(int c0=0;c0<5;c0++){
   array<int,4> rr{},cc{};int a=0,b=0;
   for(int i=0;i<5;i++)if(i!=r0)rr[a++]=i;
   for(int j=0;j<5;j++)if(j!=c0)cc[b++]=j;
   do{
    Mask T=0;bool ok=true;array<int,5> cols;cols.fill(-1);
    for(int i=0;i<4;i++){if(!firstcell[rr[i]][cc[i]])ok=false;
     T|=firstcell[rr[i]][cc[i]];cols[rr[i]]=cc[i];}
    if(!ok)continue;long long K=marked(r0,c0,T);v.patterns++;patterns++;
    all<<n<<'\t'<<r0<<'\t'<<c0<<'\t';
    for(int i=0;i<5;i++){if(i)all<<',';all<<cols[i];}all<<'\t'<<K<<'\n';
    if(K>v.maxK){v.maxK=int(K);v.wit={r0,c0,cols,T};}
   }while(next_permutation(cc.begin(),cc.end()));
  }
  assert(v.patterns>0);v.literal=literal(v.wit);assert(v.literal==v.maxK);
  v.gap=v.row.J-15*v.maxK;maxAll=max(maxAll,v.maxK);
  if(v.gap<minGap){minGap=v.gap;minId=n;}values.push_back(v);
  if(v.gap<=28){failed=true;break;}
 }
 ofstream out(mode=="profile"?"PROFILE.json":"RESULT.json");
 out<<"{\n\"status\":\""<<(failed?"FAIL":"PASS")<<"\",\n\"mode\":\""<<mode<<"\",\n";
 out<<"\"input_domain\":264,\n\"checked_matrices\":"<<values.size()<<",\n";
 out<<"\"complete\":"<<(values.size()==264?"true":"false")<<",\n";
 out<<"\"potential_markings_per_matrix\":600,\n\"feasible_markings_checked\":"<<patterns<<",\n";
 out<<"\"minimum_J_minus_15_maxK\":"<<minGap<<",\n\"minimum_source_id\":"<<minId<<",\n";
 out<<"\"maximum_K_over_domain\":"<<maxAll<<",\n\"cpu_seconds\":"<<cpu()-start<<",\n\"matrices\":[\n";
 for(int n=0;n<(int)values.size();n++){auto&v=values[n];if(n)out<<",\n";
  out<<"{\"id\":"<<v.row.id<<",\"key\":"<<v.row.key<<",\"matrix\":";matrix(out,v.row.m);
  out<<",\"J\":"<<v.row.J<<",\"feasible_markings\":"<<v.patterns<<",\"maxK\":"<<v.maxK;
  out<<",\"J_minus_15_maxK\":"<<v.gap<<",\"maximizer\":{\"omit_row\":"<<v.wit.r0<<",\"omit_col\":"<<v.wit.c0<<",\"col_by_row\":[";
  for(int i=0;i<5;i++){if(i)out<<',';out<<v.wit.cols[i];}
  out<<"],\"point_mask\":"<<v.wit.T<<"},\"literal_maximizer_replay\":"<<v.literal<<'}';
 }out<<"\n]}\n";
 cout<<(failed?"FAIL":"PASS")<<" checked="<<values.size()<<" markings="<<patterns<<" min="<<minGap<<" source="<<minId<<" cpu="<<cpu()-start<<'\n';
 return failed?2:0;
}
