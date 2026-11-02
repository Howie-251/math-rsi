#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
constexpr int N=330;
int pw[10];
int mul(int a,int b){return ((a%11+pw[(a/11)%10]*(b%11))%11)+11*((a/11+b/11)%30);}
int inv(int a){int z=a/11;return ((11-(pw[(10-z%10)%10]*(a%11))%11)%11)+11*((30-z)%30);}
struct Candidate{int source_id,pattern_index,projective_index,anchor;array<int,4>phase,field;array<int,8>S;int missing,diameter;bool connected;map<int,int>hist;};
Candidate evaluate(Candidate c){
 int adj[N][8];set<int>uniqueS(c.S.begin(),c.S.end());assert(uniqueS.size()==8&&!uniqueS.count(0));
 for(int s:c.S)assert(uniqueS.count(inv(s)));
 for(int u=0;u<N;++u)for(int t=0;t<8;++t)adj[u][t]=mul(u,c.S[t]);
 int ds[N],q[N],front=0,tail=1;fill(ds,ds+N,-1);ds[0]=0;q[0]=0;
 while(front<tail){int u=q[front++];for(int v:adj[u])if(ds[v]<0){ds[v]=ds[u]+1;q[tail++]=v;}}
 c.missing=0;c.diameter=0;c.hist.clear();c.connected=tail==N;
 for(int d:ds){c.hist[d]++;if(d<0||d>3)c.missing++;c.diameter=max(c.diameter,d);}
 if(!c.connected)c.diameter=-1;
 return c;
}
template<class T>void array_json(ostream&o,const T&a){o<<'[';bool first=true;for(auto x:a){if(!first)o<<',';first=false;o<<x;}o<<']';}
void save_best(const string&dir,const Candidate&c){
 ofstream e(dir+"/production.best.edges");e<<N<<" 1320\n";int edges=0;
 for(int u=0;u<N;++u)for(int s:c.S){int v=mul(u,s);if(u<v){e<<u<<' '<<v<<'\n';edges++;}}assert(edges==1320);
 ofstream f(dir+"/production.best.json");
 f<<"{\n\"encoding\":\"x + 11*z; j=z mod10,w=z mod3\",\n\"pattern_index\":"<<c.pattern_index<<",\"source_pattern_id\":"<<c.source_id<<",\"projective_index\":"<<c.projective_index<<",\"anchor_slot\":"<<c.anchor<<",\n\"phases\":";array_json(f,c.phase);f<<",\n\"fields\":";array_json(f,c.field);f<<",\n\"S\":";array_json(f,c.S);
 f<<",\n\"n\":330,\"m\":1320,\"degree\":8,\"connected\":"<<(c.connected?"true":"false")<<",\"diameter\":"<<c.diameter<<",\"root_deficit_gt3_or_unreachable\":"<<c.missing<<",\"bad_unordered_pairs\":"<<165*c.missing<<",\n\"root_distance_histogram\":{";
 bool first=true;for(auto [d,n]:c.hist){if(!first)f<<',';first=false;f<<'"'<<d<<"\":"<<n;}f<<"}\n}\n";
}
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];double limit=stod(argv[2]);clock_t start=clock();pw[0]=1;for(int j=1;j<10;++j)pw[j]=2*pw[j-1]%11;
 for(int a=0;a<N;++a)assert(mul(a,inv(a))==0&&mul(inv(a),a)==0);
 ifstream in(dir+"/survivor_patterns.txt");int pattern_count;in>>pattern_count;assert(pattern_count==135);
 vector<Candidate>patterns(pattern_count);for(int k=0;k<pattern_count;++k){Candidate&c=patterns[k];in>>c.source_id;for(int&t:c.phase)in>>t;c.pattern_index=k;c.anchor=0;while(c.phase[c.anchor]%10==0)c.anchor++;}
 int done=0,best_missing=N+1;bool found=false,timeout=false;vector<int>completed(pattern_count,0);map<int,int>scorehist;Candidate best;
 ofstream cases(dir+"/production.cases.tsv");cases<<"cursor\tpattern_index\tsource_pattern_id\tprojective_index\tx0\tx1\tx2\tx3\tmissing\tdiameter\n";
 for(int k=0;k<pattern_count&&!found&&!timeout;++k){
  vector<int>free;for(int j=0;j<4;++j)if(j!=patterns[k].anchor)free.push_back(j);int pindex=0;
  for(int lead=0;lead<3&&!found&&!timeout;++lead){int count=1;for(int j=lead+1;j<3;++j)count*=11;
   for(int code=0;code<count;++code){
    if(double(clock()-start)/CLOCKS_PER_SEC>=limit){timeout=true;break;}
    Candidate c=patterns[k];c.projective_index=pindex++;c.field.fill(0);c.field[free[lead]]=1;int v=code;
    for(int j=lead+1;j<3;++j){c.field[free[j]]=v%11;v/=11;}
    for(int j=0;j<4;++j){c.S[2*j]=c.field[j]+11*c.phase[j];c.S[2*j+1]=inv(c.S[2*j]);}
    c=evaluate(c);cases<<done<<'\t'<<k<<'\t'<<c.source_id<<'\t'<<c.projective_index;for(int x:c.field)cases<<'\t'<<x;cases<<'\t'<<c.missing<<'\t'<<c.diameter<<'\n';
    done++;completed[k]++;scorehist[c.missing]++;
    if(c.missing<best_missing){best_missing=c.missing;best=c;save_best(dir,best);}
    if(c.missing==0){found=true;cout<<"FOUND_D3 cursor="<<done-1<<" pattern="<<k<<" projective="<<c.projective_index<<endl;break;}
   }
  }
  if(!found&&!timeout)assert(pindex==133);
 }
 cases.close();if(!found&&!timeout)assert(done==17955);
 double cpu=double(clock()-start)/CLOCKS_PER_SEC;string status=found?"FOUND_D3":timeout?"CPU_LIMIT_INCOMPLETE":"COMPLETE_NO_SOLUTION";
 ofstream out(dir+"/production.terminal.json");out<<"{\n\"status\":\""<<status<<"\",\"scope\":17955,\"patterns\":135,\"projective_classes_per_pattern\":133,\"actual_Cayley_graphs_checked\":"<<done<<",\"root_BFS_runs\":"<<done<<",\"next_cursor\":"<<done<<",\"minimum_root_deficit\":"<<best_missing<<",\"running\":false,\"CPU_seconds\":"<<cpu<<",\n\"completed_per_pattern\":";array_json(out,completed);out<<",\n\"root_deficit_histogram\":{";bool first=true;for(auto [s,n]:scorehist){if(!first)out<<',';first=false;out<<'"'<<s<<"\":"<<n;}out<<"}\n}\n";out.close();
 cout<<status<<" checked="<<done<<" min_missing="<<best_missing<<" CPU="<<cpu<<endl;
}
