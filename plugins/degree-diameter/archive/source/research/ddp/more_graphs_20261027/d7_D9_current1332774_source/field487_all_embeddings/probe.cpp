#include <array>
#include <cassert>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <time.h>
using namespace std;
constexpr int Q=487,SM=57,P=54,N=SM*Q,V=N*P;
int mod(long long a,int m){int x=a%m;return x<0?x+m:x;}
int power(int a,int e,int m){int r=1;for(;e;e>>=1,a=(long long)a*a%m)if(e&1)r=(long long)r*a%m;return r;}
int crt(int a,int b){return a+57*mod((b-a)*94,487);}
double cpu(){timespec t{};clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&t);return t.tv_sec+1e-9*t.tv_nsec;}
struct Dart{int s,f,j,n,inv;};
string arr(const array<unsigned long long,10>& h){ostringstream o;o<<'[';for(int i=0;i<10;i++){if(i)o<<',';o<<h[i];}return o.str()+']';}
void write(const string&path,const string&text){ofstream o(path);o<<text<<'\n';assert(o.good());}
void checkpoint(const string&dir,const string&status,int cursor,int beta,int complete,double spent){ostringstream o;o<<"{\"status\":\""<<status<<"\",\"next_cursor\":"<<cursor<<",\"active_beta\":"<<beta<<",\"completed_cases\":"<<complete<<",\"embeddings\":18,\"native_CPU_seconds\":"<<spent<<",\"source_BFS\":0}";write(dir+"/checkpoint.tmp",o.str());assert(rename((dir+"/checkpoint.tmp").c_str(),(dir+"/checkpoint.json").c_str())==0);}
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];ifstream in(dir+"/INPUT.txt");int number;in>>number;assert(number==18);vector<int> roots(number);for(int&b:roots)in>>b;
 vector<unsigned char> dist(V);vector<unsigned int> queue(V);ofstream cases(dir+"/CASES.jsonl");assert(cases.good());double total_start=cpu();int complete=0;bool hit=false;int hitbeta=-1,hitD=-1;
 for(int index=0;index<number;index++){
  int beta=roots[index];assert(power(beta,54,Q)==1&&power(beta,27,Q)!=1&&power(beta,18,Q)!=1);checkpoint(dir,"RUNNING",index,beta,complete,cpu()-total_start);double start=cpu();
  array<int,54> ps{},pf{},pn{};ps[0]=pf[0]=pn[0]=1;int action=crt(47,beta);
  for(int k=1;k<54;k++){ps[k]=ps[k-1]*47%SM;pf[k]=pf[k-1]*beta%Q;pn[k]=(long long)pn[k-1]*action%N;}
  assert(ps[53]*47%SM==1&&pf[53]*beta%Q==1&&(long long)pn[53]*action%N==1);
  array<Dart,7>d;d[0]={10,1,33,7306,3};d[1]={2,332,2,19325,4};d[2]={2,431,16,22346,5};
  for(int k=0;k<3;k++){int j=(54-d[k].j)%54;d[k+3]={mod(-d[k].s*ps[j],SM),mod(-d[k].f*pf[j],Q),j,0,k};d[k+3].n=crt(d[k+3].s,d[k+3].f);}
  d[6]={19,0,27,9253,6};
  bool used_phase[54]{};
  for(int k=0;k<7;k++){auto a=d[k],b=d[a.inv];assert(a.n==crt(a.s,a.f)&&a.j!=0&&!used_phase[a.j]);used_phase[a.j]=true;assert((a.j+b.j)%54==0);assert((a.s+ps[a.j]*b.s)%SM==0);assert((a.f+pf[a.j]*b.f)%Q==0);assert((a.n+(long long)pn[a.j]*b.n)%N==0);}
  array<array<int,7>,54>shift{},base{};
  for(int j=0;j<54;j++)for(int k=0;k<7;k++){int ss=ps[j]*d[k].s%SM,ff=pf[j]*d[k].f%Q;shift[j][k]=crt(ss,ff);base[j][k]=((j+d[k].j)%54)*N;assert(shift[j][k]==(long long)pn[j]*d[k].n%N);}
  fill(dist.begin(),dist.end(),255);array<unsigned long long,10>hist{};int head=0,tail=1;queue[0]=0;dist[0]=0;hist[0]=1;
  while(head<tail&&tail<V){unsigned u=queue[head++];unsigned depth=dist[u];if(depth==9)continue;int phase=u/N,n=u-phase*N;for(int k=0;k<7;k++){int x=n+shift[phase][k];if(x>=N)x-=N;int v=base[phase][k]+x;if(dist[v]==255){dist[v]=depth+1;queue[tail++]=v;++hist[depth+1];}}}
  bool success=tail==V;int first=-1;if(!success)for(int v=0;v<V;v++)if(dist[v]==255){first=v;break;}
  int ecc=9;if(success)while(ecc>0&&hist[ecc]==0)--ecc;double elapsed=cpu()-start;
  ostringstream row;row<<"{\"index\":"<<index<<",\"beta\":"<<beta<<",\"full_action\":"<<action<<",\"n\":"<<V<<",\"m\":5246451,\"degree\":7,\"simple\":true,\"undirected\":true,\"connected_by_paper\":true,\"reached_R9\":"<<tail<<",\"root_R9_missing\":"<<V-tail<<",\"first_missing_id\":"<<first<<",\"histogram_0to9\":"<<arr(hist)<<",\"hit\":"<<(success?"true":"false")<<",\"actual_global_D\":";if(success)row<<ecc;else row<<"null";row<<",\"ordinary_bad_unordered_pairs\":null,\"CPU_seconds\":"<<elapsed<<",\"source_BFS\":0}";
  cases<<row.str()<<'\n';cases.flush();write(dir+"/case_"+to_string(index)+".json",row.str());++complete;
  cout<<"case "<<index<<" beta "<<beta<<" R9missing "<<V-tail<<" CPU "<<elapsed<<endl;
  if(success){
   hit=true;hitbeta=beta;hitD=ecc;write(dir+"/HIT.json",row.str());
   ostringstream rec;rec<<"{\"degree\":7,\"diameter_producer\":"<<ecc<<",\"order\":"<<V<<",\"m\":5246451,\"normal_modulus\":"<<N<<",\"phase_modulus\":54,\"action\":"<<action<<",\"small_action\":47,\"field_action\":"<<beta<<",\"field_prime\":487,\"law\":\"LEFT: (n,I)(m,J)=(n+action^I*m,I+J)\",\"vertex_encoding\":\"27759*phase+normal\",\"positive_normal_phase\":[[7306,33],[19325,2],[22346,16]],\"involution_normal_phase\":[9253,27],\"all_darts_normal_phase\":[";
   for(int k=0;k<7;k++){if(k)rec<<',';rec<<'['<<d[k].n<<','<<d[k].j<<']';}rec<<"],\"inverse_indices\":[3,4,5,0,1,2,6],\"source_BFS\":0,\"parent_acceptance_pending\":true}";write(dir+"/HIT_RECIPE.json",rec.str());
   ofstream bytes(dir+"/HIT_identity_distances.u8.bin",ios::binary);bytes.write((const char*)dist.data(),dist.size());bytes.close();checkpoint(dir,"HIT_STOP",complete,beta,complete,cpu()-total_start);break;
  }
  checkpoint(dir,index+1==number?"COMPLETE_ALL18_NO_HIT":"RUNNING",index+1,beta,complete,cpu()-total_start);
 }
 ostringstream result;result<<"{\"status\":\""<<(hit?"HIT_STOP_REMAINDER_UNTESTED":"COMPLETE_ALL18_NO_HIT")<<"\",\"embeddings_total\":18,\"embeddings_processed\":"<<complete<<",\"actual_implicit_graphs\":"<<complete<<",\"identity_R9_checks\":"<<complete<<",\"hits\":"<<(hit?1:0)<<",\"hit_beta\":"<<hitbeta<<",\"actual_global_D\":";if(hit)result<<hitD;else result<<"null";result<<",\"next_cursor\":"<<complete<<",\"untested\":"<<number-complete<<",\"source_BFS\":0,\"ordinary_bad_unordered_pairs\":null,\"native_CPU_seconds\":"<<cpu()-total_start<<'}';write(dir+"/NATIVE_RESULT.json",result.str());cout<<result.str()<<endl;
}
