#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
using Row=array<int,5>;using Mat=array<Row,5>;
vector<Row>rows,perms;Mat A;Row caps{};long long terminal=0,doublelex=0;
map<uint64_t,Mat>representatives;long long C[21][21]{};
struct State{int r,b,sign;};vector<State>states;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}int pc(int x){return __builtin_popcount((unsigned)x);}
uint64_t encode(const Mat&M){uint64_t x=0;for(auto r:M)for(int v:r)x=x*5+v;return x;}
Mat canon(const Mat&M){Mat best{};uint64_t key=UINT64_MAX;
 for(auto p:perms){Mat N;for(int i=0;i<5;i++)for(int j=0;j<5;j++)N[i][j]=M[i][p[j]];
 sort(N.begin(),N.end());auto v=encode(N);if(v<key){key=v;best=N;}}return best;}
bool colsorted(){for(int j=1;j<5;j++)for(int i=0;i<5;i++){
 if(A[i][j-1]<A[i][j])break;if(A[i][j-1]>A[i][j])return false;}return true;}
void gen(int depth,int lo){
 if(depth==4){Row r;for(int j=0;j<5;j++)r[j]=4-caps[j];if(r<rows[lo])return;
 if(r[0]+r[1]+r[2]+r[3]+r[4]!=4)return;A[4]=r;terminal++;
 if(!colsorted())return;doublelex++;Mat N=canon(A);representatives.emplace(encode(N),N);return;}
 for(int x=lo;x<(int)rows.size();x++){bool ok=true;
 for(int j=0;j<5;j++)if(caps[j]+rows[x][j]>4)ok=false;if(!ok)continue;
 A[depth]=rows[x];for(int j=0;j<5;j++)caps[j]+=rows[x][j];gen(depth+1,x);
 for(int j=0;j<5;j++)caps[j]-=rows[x][j];}}
long long joint(const Mat&M){int ss[32][32]{};
 for(int r=1;r<32;r++){int bit=r&-r,i=__builtin_ctz((unsigned)bit),old=r^bit;
 for(int b=1;b<32;b++){int v=0;for(int j=0;j<5;j++)if(b>>j&1)v+=M[i][j];ss[r][b]=ss[old][b]+v;}}
 long long ans=0;for(auto x:states)for(auto y:states){
 if(ss[x.r][y.b]||ss[x.b][y.r])continue;
 int red=4*(pc(x.r)+pc(y.r))-ss[x.r][y.r],blue=4*(pc(x.b)+pc(y.b))-ss[x.b][y.b];
 if(red>10||blue>10)continue;ans+=x.sign*y.sign*C[20-red-blue][10-red];}return ans;}
void printmat(ostream&o,const Mat&M){o<<'[';for(int i=0;i<5;i++){if(i)o<<',';o<<'[';for(int j=0;j<5;j++){if(j)o<<',';o<<M[i][j];}o<<']';}o<<']';}
int main(int argc,char**argv){double start=cpu();string mode=argc>1?argv[1]:"profile";
 for(int a=0;a<=4;a++)for(int b=0;b<=4-a;b++)for(int c=0;c<=4-a-b;c++)for(int d=0;d<=4-a-b-c;d++)rows.push_back({a,b,c,d,4-a-b-c-d});
 Row p={0,1,2,3,4};do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
 for(int n=0;n<=20;n++){C[n][0]=C[n][n]=1;for(int k=1;k<n;k++)C[n][k]=C[n-1][k-1]+C[n-1][k];}
 for(int r=1;r<32;r++)for(int b=1;b<32;b++)if(!(r&b)&&pc(r)<=2&&pc(b)<=2)states.push_back({r,b,(pc(r)+pc(b))%2?-1:1});
 Mat I{},J{};for(int i=0;i<5;i++)for(int j=0;j<5;j++){I[i][j]=i==j?4:0;J[i][j]=i==j?0:1;}
 if(rows.size()!=70||states.size()!=110||joint(I)!=16980||joint(J)!=400)return 2;
 vector<Mat>domain;if(mode=="profile"){gen(0,0);ofstream f("MATRICES.txt");
 for(auto&entry:representatives){domain.push_back(entry.second);for(auto r:entry.second)for(int x:r)f<<x<<' ';f<<'\n';}
 ofstream g("DOMAIN_COUNTS.txt");g<<terminal<<' '<<doublelex<<' '<<domain.size()<<'\n';}
 else{ifstream f("MATRICES.txt");while(true){Mat M;bool ok=true;for(auto&r:M)for(int&v:r)if(!(f>>v))ok=false;if(!ok)break;domain.push_back(M);}
 ifstream g("DOMAIN_COUNTS.txt");long long size=0;if(!(g>>terminal>>doublelex>>size)||size!=(long long)domain.size())return 3;}
 double generation=cpu()-start,t=cpu();long long mn=200000,mx=0,checked=0,mincount=0;Mat witness{};map<long long,long long>hist;
 int limit=mode=="profile"?min(100,(int)domain.size()):(int)domain.size();
 ofstream values;if(mode!="profile"){values.open("REPRESENTATIVES.json");values<<"[\n";}
 for(int n=0;n<limit;n++){auto v=joint(domain[n]);hist[v]++;checked++;
 if(values.is_open()){if(n)values<<",\n";values<<"{\"id\":"<<n<<",\"key\":"<<encode(domain[n])<<",\"matrix\":";printmat(values,domain[n]);values<<",\"jointcount\":"<<v<<'}';}
 if(v<mn){mn=v;witness=domain[n];mincount=1;}else if(v==mn)mincount++;mx=max(mx,v);if(v<319)break;}
 if(values.is_open())values<<"\n]\n";
 ofstream f(mode=="profile"?"PROFILE.json":"RESULT.json");
 f<<"{\n\"mode\":\""<<mode<<"\",\n\"row_compositions\":"<<rows.size()<<",\n\"row_sorted_terminal_matrices\":"<<terminal<<",\n\"doublelex_terminal_matrices\":"<<doublelex<<",\n\"canonical_domain\":"<<domain.size()<<",\n\"checked\":"<<checked<<",\n\"complete\":"<<(checked==(long long)domain.size()?"true":"false")<<",\n\"minimum\":"<<mn<<",\n\"maximum\":"<<mx<<",\n\"minimizer_count\":"<<mincount<<",\n\"witness\":";printmat(f,witness);
 f<<",\n\"baseline_I4\":"<<joint(I)<<",\n\"baseline_J_minus_I\":"<<joint(J)<<",\n\"generation_cpu_seconds\":"<<generation<<",\n\"joint_count_cpu_seconds\":"<<cpu()-t<<",\n\"total_cpu_seconds\":"<<cpu()-start<<",\n\"histogram\":{";
 bool first=true;for(auto x:hist){if(!first)f<<',';first=false;f<<'\"'<<x.first<<"\":"<<x.second;}f<<"}\n}\n";
 cout<<"domain="<<domain.size()<<" terminals="<<terminal<<" doublelex="<<doublelex<<" checked="<<checked<<" min="<<mn<<" total_cpu="<<cpu()-start<<" count_cpu="<<cpu()-t<<'\n';}
