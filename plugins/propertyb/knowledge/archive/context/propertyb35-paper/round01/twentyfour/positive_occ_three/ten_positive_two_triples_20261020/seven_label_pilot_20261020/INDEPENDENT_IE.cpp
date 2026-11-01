#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;using I64=int64_t;using U64=uint64_t;
I64 chooseN[18][6];
I64 binom(int n,int k){return n<0||k<0||k>n?0:chooseN[n][k];}
I64 field(const string&s,const string&name){auto p=s.find("\""+name+"\":");assert(p!=string::npos);return stoll(s.substr(p+name.size()+3));}
array<I64,3> prefix(const string&s){auto p=s.find("\"pair_prefix\":[");assert(p!=string::npos);string t=s.substr(p+15);replace(t.begin(),t.end(),',',' ');istringstream in(t);array<I64,3>a;for(auto&v:a){in>>v;assert(in);}return a;}
struct Count{I64 C=0,top=0,next=0,h3=0,h4=0;};
int main(int argc,char**argv){
 assert(argc>=3);clock_t start=clock();for(int n=0;n<=17;n++){chooseN[n][0]=1;for(int k=1;k<=5;k++)chooseN[n][k]=n?chooseN[n-1][k]+chooseN[n-1][k-1]:0;}
 vector<array<int,7>>perms;array<int,7>p={0,1,2,3,4,5,6};do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));assert(perms.size()==5040);
 ifstream in(argv[1]);string line;int rows=0;array<I64,15>labels{},orbits{};set<U64>canonical;I64 totalLabels=0,minMargin=100000000,minC5Margin=100000000;int minIndex=-1;
 while(getline(in,line)){
  auto at=line.find("\"vector\":[");assert(at!=string::npos);string nums=line.substr(at+10);replace(nums.begin(),nums.end(),',',' ');istringstream ss(nums);array<int,21>g;for(int&v:g){ss>>v;assert(ss);}
  int matrix[7][7]{};array<int,7>d{};vector<int>point;int z=0,E=0;
  for(int i=0;i<7;i++)for(int j=i+1;j<7;j++,z++){
   int m=g[z];assert(m>=0&&m<=4);E+=m;d[i]+=m;d[j]+=m;matrix[i][j]=matrix[j][i]=m;
   for(int t=0;t<m;t++)point.push_back((1<<i)|(1<<j));
  }
  for(int i=0;i<7;i++){assert(d[i]<=4);for(int j=d[i];j<4;j++)point.push_back(1<<i);}
  int n=point.size();assert(n==28-E&&E>=11&&E<=14&&E==field(line,"E"));
  // Independent inverse-vertex-order orbit calculation: no action table and no global image hash set.
  vector<U64>images;images.reserve(5040);
  for(auto &perm:perms){U64 code=0;int e=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++,e++)code|=U64(matrix[perm[i]][perm[j]])<<(3*e);images.push_back(code);}
  sort(images.begin(),images.end());auto uniqueEnd=unique(images.begin(),images.end());I64 orbit=uniqueEnd-images.begin();
  assert(orbit==field(line,"orbit_size"));assert(canonical.insert(images[0]).second);labels[E]+=orbit;orbits[E]++;totalLabels+=orbit;
  array<int,128>avoid{};for(int S=0;S<128;S++)for(int m:point)if(!(m&S))avoid[S]++;
  array<Count,2>result;
  I64 extension[2][5][128]{};
  for(int j=0;j<2;j++){
   int k=4+j;
   for(int S=0;S<128;S++)result[j].C+=(__builtin_popcount(unsigned(S))%2?-1:1)*binom(avoid[S],k);
   for(int q=2;q<=4;q++)for(int cover=0;cover<128;cover++){
    int missing=127^cover;I64 value=0;
    for(int S=missing;;S=(S-1)&missing){value+=(__builtin_popcount(unsigned(S))%2?-1:1)*binom(avoid[S]-q,k-q);if(!S)break;}
    extension[j][q][cover]=value;
   }
  }
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++){
   int cover=point[a]|point[b];for(int j=0;j<2;j++){I64 v=extension[j][2][cover];assert(v>=0);if(v>=result[j].top){result[j].next=result[j].top;result[j].top=v;}else result[j].next=max(result[j].next,v);}
   for(int c=b+1;c<n;c++){
    int cover3=cover|point[c];for(int j=0;j<2;j++)result[j].h3=max(result[j].h3,extension[j][3][cover3]);
    for(int e=c+1;e<n;e++){int cover4=cover3|point[e];for(int j=0;j<2;j++)result[j].h4=max(result[j].h4,extension[j][4][cover4]);}
   }
  }
  for(int j=0;j<2;j++){
   string key=j?"\"C5\":{":"\"C4\":{";auto begin=line.find(key);assert(begin!=string::npos);auto end=line.find('}',begin);string stored=line.substr(begin,end-begin+1);
   auto S=prefix(stored);assert(result[j].C==field(stored,"count"));assert(S[0]==0&&S[1]==result[j].top&&S[2]==result[j].top+result[j].next);assert(result[j].h3==field(stored,"h3"));assert(result[j].h4==field(stored,"h4"));
  }
  assert(37*result[1].top<=8*result[1].C);
  assert(292*result[1].h3<=23*result[1].C);
  assert(584*result[1].h4<=13*result[1].C);
  I64 local=100000000;
  for(int u=0;u<=2;u++)for(int v=0;v<=4-u;v++){
   I64 best=-100000000;for(int j=0;j<2;j++){I64 S=u==0?0:(u==1?result[j].top:result[j].top+result[j].next);I64 B=S+(2-u+v)*result[j].h3+(18-v)*result[j].h4;best=max(best,result[j].C-B);if(j==1){assert(result[j].C-B>0);minC5Margin=min(minC5Margin,result[j].C-B);}}assert(best>0);local=min(local,best);
  }
  assert(local==field(line,"minimum_best_margin"));assert(line.find("\"raw_strict\":true")!=string::npos);
  if(local<minMargin){minMargin=local;minIndex=rows;}rows++;
 }
 const I64 expected[4]={5229168,3535448,1198218,93708};for(int e=11;e<=14;e++)assert(labels[e]==expected[e-11]);assert(rows==3015&&canonical.size()==3015&&totalLabels==10056542&&minMargin==36&&minC5Margin==36);
 ofstream out(argv[2]);out<<"{\"PASS\":true,\"representatives\":"<<rows<<",\"pairwise_distinct_canonical_orbits\":"<<canonical.size()<<",\"orbit_image_sum\":"<<totalLabels<<",\"conditional_IE_and_raw_bounds_all_equal\":true,\"parameter_cases\":"<<12*rows<<",\"minimum_best_margin\":"<<minMargin<<",\"minimum_C5_margin\":"<<minC5Margin<<",\"uniform_h2_over_C5\":\"8/37\",\"uniform_h3_over_C5\":\"23/292\",\"uniform_h4_over_C5\":\"13/584\",\"first_minimum_index\":"<<minIndex<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"by_E\":[";
 for(int e=11;e<=14;e++){if(e>11)out<<',';out<<"{\"E\":"<<e<<",\"orbits\":"<<orbits[e]<<",\"labelled\":"<<labels[e]<<"}";}out<<"]}\n";
 cout<<"PASS reps="<<rows<<" margin="<<minMargin<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}
