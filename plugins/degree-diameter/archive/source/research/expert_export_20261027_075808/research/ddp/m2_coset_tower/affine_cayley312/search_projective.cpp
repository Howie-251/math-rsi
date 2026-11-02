#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
constexpr int N=312;
int pw[12];
int phase_add(int a,int b){return (a%12+b%12)%12+12*((a/12+b/12)%2);}
int mul(int a,int b){return (a%13+pw[(a/13)%12]*(b%13))%13+13*phase_add(a/13,b/13);}
int inv(int a){int h=a/13,j=h%12,w=h/12;return (13-pw[(12-j)%12]*(a%13)%13)%13+13*((12-j)%12+12*w);}
struct Candidate{
 int source_id,pattern_index,pairs,reflection_a,reflection_b,central,projective_index,anchor;
 vector<int>phase,field;array<int,8>S;
 int missing,diameter;bool connected;map<int,int>hist;
};
bool generators(Candidate&c){
 int k=0;
 for(int j=0;j<c.pairs;++j){int s=c.field[j]+13*c.phase[j];c.S[k++]=s;c.S[k++]=inv(s);}
 for(int j=c.pairs;j<int(c.phase.size());++j){int s=c.field[j]+13*c.phase[j];assert(inv(s)==s);c.S[k++]=s;}
 if(c.central)c.S[k++]=156;
 assert(k==8);auto sorted=c.S;sort(sorted.begin(),sorted.end());
 return sorted[0]!=0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end();
}
Candidate evaluate(Candidate c){
 int adj[N][8];for(int u=0;u<N;++u)for(int t=0;t<8;++t)adj[u][t]=mul(u,c.S[t]);
 int ds[N],q[N],front=0,tail=1;fill(ds,ds+N,-1);ds[0]=0;q[0]=0;
 while(front<tail){int u=q[front++];for(int v:adj[u])if(ds[v]<0){ds[v]=ds[u]+1;q[tail++]=v;}}
 c.missing=0;c.diameter=0;c.hist.clear();c.connected=tail==N;
 for(int d:ds){c.hist[d]++;if(d<0||d>3)c.missing++;c.diameter=max(c.diameter,d);}
 if(!c.connected)c.diameter=-1;
 return c;
}
template<class T>void array_json(ostream&o,const T&a){o<<'[';bool first=true;for(auto x:a){if(!first)o<<',';first=false;o<<x;}o<<']';}
void save_best(const string&dir,const Candidate&c,int cursor){
 ofstream e(dir+"/production.best.edges");e<<N<<" 1248\n";int edges=0;
 for(int u=0;u<N;++u)for(int s:c.S){int v=mul(u,s);if(u<v){e<<u<<' '<<v<<'\n';edges++;}}assert(edges==1248);
 ofstream f(dir+"/production.best.json");
 f<<"{\n\"encoding\":\"x + 13*(j+12*w)\",\"cursor\":"<<cursor<<",\n\"pattern_index\":"<<c.pattern_index<<",\"source_pattern_id\":"<<c.source_id<<",\"pair_count\":"<<c.pairs<<",\"reflection_6_0_count\":"<<c.reflection_a<<",\"reflection_6_1_count\":"<<c.reflection_b<<",\"central_involution_count\":"<<c.central<<",\"projective_index\":"<<c.projective_index<<",\"anchor_slot\":"<<c.anchor<<",\n\"variable_component_phases\":";array_json(f,c.phase);f<<",\n\"fields\":";array_json(f,c.field);f<<",\n\"S\":";array_json(f,c.S);
 f<<",\n\"n\":312,\"m\":1248,\"degree\":8,\"connected\":"<<(c.connected?"true":"false")<<",\"diameter\":"<<c.diameter<<",\"root_deficit_gt3_or_unreachable\":"<<c.missing<<",\"bad_unordered_pairs\":"<<156*c.missing<<",\n\"root_distance_histogram\":{";
 bool first=true;for(auto [d,n]:c.hist){if(!first)f<<',';first=false;f<<'"'<<d<<"\":"<<n;}f<<"}\n}\n";
}
int power13(int n){int r=1;while(n--)r*=13;return r;}
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];double limit=stod(argv[2]);clock_t start=clock();pw[0]=1;for(int j=1;j<12;++j)pw[j]=2*pw[j-1]%13;
 assert(pw[6]==12);for(int a=0;a<N;++a)assert(mul(a,inv(a))==0&&mul(inv(a),a)==0);
 ifstream in(dir+"/survivor_patterns.txt");int pattern_count;in>>pattern_count;assert(pattern_count==370);
 vector<Candidate>patterns(pattern_count);vector<int>scope(pattern_count);
 for(int k=0;k<pattern_count;++k){Candidate&c=patterns[k];in>>c.source_id>>c.pairs>>c.reflection_a>>c.reflection_b>>c.central;int m=c.pairs+c.reflection_a+c.reflection_b;c.phase.resize(m);for(int j=0;j<c.pairs;++j)in>>c.phase[j];for(int j=c.pairs;j<c.pairs+c.reflection_a;++j)c.phase[j]=6;for(int j=c.pairs+c.reflection_a;j<m;++j)c.phase[j]=18;c.pattern_index=k;c.anchor=0;while(c.phase[c.anchor]%12==0)c.anchor++;scope[k]=(power13(m-1)-1)/12;}
 int done=0,legal=0,illegal=0,best_missing=N+1;bool found=false,timeout=false;vector<int>completed(pattern_count,0),legal_per_pattern(pattern_count,0);map<int,int>scorehist;Candidate best;
 ofstream cases(dir+"/production.cases.tsv");cases<<"cursor\tpattern_index\tsource_pattern_id\tprojective_index\tlegal\tmissing\tdiameter\n";
 for(int k=0;k<pattern_count&&!found&&!timeout;++k){
  vector<int>free;for(int j=0;j<int(patterns[k].phase.size());++j)if(j!=patterns[k].anchor)free.push_back(j);int pindex=0;
  for(int lead=0;lead<int(free.size())&&!found&&!timeout;++lead){int count=power13(free.size()-lead-1);
   for(int code=0;code<count;++code){
    if(double(clock()-start)/CLOCKS_PER_SEC>=limit){timeout=true;break;}
    Candidate c=patterns[k];c.projective_index=pindex++;c.field.assign(c.phase.size(),0);c.field[free[lead]]=1;int v=code;
    for(int j=lead+1;j<int(free.size());++j){c.field[free[j]]=v%13;v/=13;}
    bool valid=generators(c);cases<<done<<'\t'<<k<<'\t'<<c.source_id<<'\t'<<c.projective_index<<'\t'<<valid;
    int cursor=done++;completed[k]++;
    if(!valid){illegal++;cases<<"\t-1\t-1\n";continue;}
    legal++;legal_per_pattern[k]++;c=evaluate(c);cases<<'\t'<<c.missing<<'\t'<<c.diameter<<'\n';scorehist[c.missing]++;
    if(c.missing<best_missing){best_missing=c.missing;best=c;save_best(dir,best,cursor);}
    if(c.missing==0){found=true;cout<<"FOUND_D3 cursor="<<cursor<<" pattern="<<k<<" projective="<<c.projective_index<<endl;break;}
   }
  }
  if(!found&&!timeout)assert(pindex==scope[k]);
 }
 cases.close();if(!found&&!timeout)assert(done==252258);
 double cpu=double(clock()-start)/CLOCKS_PER_SEC;string status=found?"FOUND_D3":timeout?"CPU_LIMIT_INCOMPLETE":"COMPLETE_NO_SOLUTION";
 ofstream out(dir+"/production.terminal.json");out<<"{\n\"status\":\""<<status<<"\",\"scope\":252258,\"patterns\":370,\"raw_representatives_checked\":"<<done<<",\"illegal_representatives\":"<<illegal<<",\"actual_legal_Cayley_graphs_checked\":"<<legal<<",\"root_BFS_runs\":"<<legal<<",\"next_cursor\":"<<done<<",\"minimum_root_deficit\":"<<best_missing<<",\"running\":false,\"CPU_seconds\":"<<cpu<<",\n\"scope_per_pattern\":";array_json(out,scope);out<<",\n\"completed_per_pattern\":";array_json(out,completed);out<<",\n\"legal_per_pattern\":";array_json(out,legal_per_pattern);out<<",\n\"root_deficit_histogram\":{";bool first=true;for(auto [s,n]:scorehist){if(!first)out<<',';first=false;out<<'"'<<s<<"\":"<<n;}out<<"}\n}\n";out.close();
 cout<<status<<" raw="<<done<<" legal="<<legal<<" illegal="<<illegal<<" min_missing="<<best_missing<<" CPU="<<cpu<<endl;
}
