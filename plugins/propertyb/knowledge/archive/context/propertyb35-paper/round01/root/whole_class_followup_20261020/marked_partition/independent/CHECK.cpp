#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using Mask=uint32_t;using Mat=array<array<int,5>,5>;
struct Input{int id,J;Mat M;};struct Value{int id,J,patterns=0,best=-1,r0=-1,c0=-1;array<int,5> cols{};long long labelled=0,samples=0;};
array<Mask,5> R,Q;array<array<Mask,5>,5> firstpoint;vector<int> activeRows;array<int,5> mapping;Mat M;
long long totalSamples=0;long long totalPatterns=0;ofstream patternFile;
vector<Mask> freeBits;long long Kvalue;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void choose_six(int pos,int left,Mask red){
 if(left==0){totalSamples++;
  bool redRow=false,redCol=false;
  for(Mask block:R)if((red&block)==block){redRow=true;break;}
  if(!redRow)return;
  for(Mask block:Q)if((red&block)==block){redCol=true;break;}
  if(redCol)Kvalue++;return;}
 if((int)freeBits.size()-pos<left)return;
 for(int j=pos;j<=(int)freeBits.size()-left;j++)choose_six(j+1,left-1,red|freeBits[j]);
}
long long literal(int r0,int c0,Mask T){
 Mask blue=R[r0]|Q[c0];assert(!(blue&T));assert(__builtin_popcount(T)==4);
 freeBits.clear();for(int i=0;i<20;i++)if(!((blue|T)>>i&1))freeBits.push_back(Mask(1)<<i);
 assert(freeBits.size()>=8&&freeBits.size()<=12);Kvalue=0;choose_six(0,6,T);return Kvalue;
}
void positive_matchings(int depth,int used,Mask T,int r0,Value&v){
 if(depth==4){int c0=0;while(used>>c0&1)c0++;assert(c0<5);long long val=literal(r0,c0,T);
  v.patterns++;totalPatterns++;long long multiplicity=1;
  for(int r:activeRows)multiplicity*=M[r][mapping[r]];v.labelled+=multiplicity;
  patternFile<<v.id<<'\t'<<r0<<'\t'<<c0<<'\t';for(int i=0;i<5;i++){if(i)patternFile<<',';patternFile<<mapping[i];}
  patternFile<<'\t'<<val<<'\t'<<multiplicity<<'\n';
  if(val>v.best){v.best=val;v.r0=r0;v.c0=c0;v.cols=mapping;}return;}
 int r=activeRows[depth];for(int c=0;c<5;c++)if(!(used>>c&1)&&M[r][c]){
  mapping[r]=c;positive_matchings(depth+1,used|(1<<c),T|firstpoint[r][c],r0,v);mapping[r]=-1;}
}
int main(int argc,char**argv){
 double start=cpu();bool profile=argc<2||string(argv[1])=="profile";
 ifstream f("INPUT_LOCAL.txt");int n;f>>n;assert(n==264);vector<Input> inputs;
 for(int z=0;z<n;z++){Input x;f>>x.id>>x.J;for(auto&row:x.M)for(int&v:row)f>>v;assert(f&&x.id==z);inputs.push_back(x);}
 int limit=profile?5:264;patternFile.open(profile?"PROFILE_PATTERNS.tsv":"LITERAL_PATTERNS.tsv");
 patternFile<<"id\tomit_row\tomit_col\tcol_by_row\tK\tpoint_choice_multiplicity\n";
 vector<Value> out;int minGap=1000000,minId=-1;
 for(int z=0;z<limit;z++){
  M=inputs[z].M;R.fill(0);Q.fill(0);for(auto&row:firstpoint)row.fill(0);int label=0;
  // Column-major labels differ from producer's row-major point labels.
  for(int c=0;c<5;c++)for(int r=0;r<5;r++)for(int k=0;k<M[r][c];k++){
   Mask bit=Mask(1)<<label++;R[r]|=bit;Q[c]|=bit;if(k==0)firstpoint[r][c]=bit;}
  assert(label==20);for(Mask x:R)assert(__builtin_popcount(x)==4);for(Mask x:Q)assert(__builtin_popcount(x)==4);
  Value v;v.id=z;v.J=inputs[z].J;long long before=totalSamples;
  for(int omit=0;omit<5;omit++){activeRows.clear();mapping.fill(-1);for(int r=0;r<5;r++)if(r!=omit)activeRows.push_back(r);positive_matchings(0,0,0,omit,v);}
  v.samples=totalSamples-before;assert(v.patterns>0);int gap=v.J-15*v.best;
  if(gap<minGap){minGap=gap;minId=z;}out.push_back(v);
 }
 ofstream g(profile?"PROFILE.json":"RESULT.json");
 g<<"{\n\"status\":\"PASS_LITERAL_COUNTS\",\n\"checked_matrices\":"<<out.size()<<",\n\"complete\":"<<(out.size()==264?"true":"false")<<",\n\"support_patterns\":"<<totalPatterns<<",\n\"literal_red_six_subsets\":"<<totalSamples<<",\n\"minimum_J_minus_15_maxK\":"<<minGap<<",\n\"minimum_source_id\":"<<minId<<",\n\"cpu_seconds\":"<<cpu()-start<<",\n\"matrices\":[\n";
 for(size_t i=0;i<out.size();i++){auto&v=out[i];if(i)g<<",\n";g<<"{\"id\":"<<v.id<<",\"J\":"<<v.J<<",\"support_patterns\":"<<v.patterns<<",\"labelled_transversals\":"<<v.labelled<<",\"literal_red_six_subsets\":"<<v.samples<<",\"maxK\":"<<v.best<<",\"J_minus_15_maxK\":"<<v.J-15*v.best<<",\"witness\":{\"omit_row\":"<<v.r0<<",\"omit_col\":"<<v.c0<<",\"col_by_row\":[";
  for(int j=0;j<5;j++){if(j)g<<',';g<<v.cols[j];}g<<"]}}";}
 g<<"\n]}\n";cout<<"checked="<<out.size()<<" support="<<totalPatterns<<" samples="<<totalSamples<<" min="<<minGap<<" cpu="<<cpu()-start<<'\n';
}
