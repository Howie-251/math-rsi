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
constexpr int N=258,Q=43,K=6;
int pw[K],product[N][N],inverse_element[N];
int multiply(int a,int b){return (a%Q+pw[a/Q]*(b%Q))%Q+Q*((a/Q+b/Q)%K);}
int inverse(int a){int j=a/Q;return (Q-pw[(K-j)%K]*(a%Q)%Q)%Q+Q*((K-j)%K);}
struct Candidate{int pattern,source_id,orbit,cursor,x,y;array<int,2>phases;array<int,4>reflections;array<int,8>S;int missing,diameter;bool connected;map<int,int>hist;};
bool make_generators(Candidate&c){int a=c.x+Q*c.phases[0],b=c.y+Q*c.phases[1];c.S={a,inverse_element[a],b,inverse_element[b],0,0,0,0};for(int j=0;j<4;++j)c.S[j+4]=c.reflections[j]+3*Q;auto s=c.S;sort(s.begin(),s.end());return s[0]!=0&&adjacent_find(s.begin(),s.end())==s.end();}
Candidate evaluate(Candidate c){
 int ds[N],queue[N],front=0,tail=1;fill(ds,ds+N,-1);ds[0]=0;queue[0]=0;
 while(front<tail){int u=queue[front++];for(int s:c.S){int v=product[u][s];if(ds[v]<0){ds[v]=ds[u]+1;queue[tail++]=v;}}}
 c.connected=tail==N;c.missing=0;c.diameter=0;c.hist.clear();
 for(int d:ds){c.hist[d]++;if(d<0||d>3)c.missing++;c.diameter=max(c.diameter,d);}if(!c.connected)c.diameter=-1;return c;
}
template<class T>void array_json(ostream&o,const T&a){o<<'[';bool first=true;for(auto x:a){if(!first)o<<',';first=false;o<<x;}o<<']';}
void save_best(const string&dir,const Candidate&c){
 ofstream edges(dir+"/production.best.edges");edges<<N<<" 1032\n";int edgecount=0;
 for(int u=0;u<N;++u)for(int s:c.S){int v=product[u][s];if(u<v){edges<<u<<' '<<v<<'\n';edgecount++;}}assert(edgecount==1032);
 ofstream out(dir+"/production.best.json");out<<"{\n\"encoding\":\"x+43*j\",\"action_root\":37,\"cursor\":"<<c.cursor<<",\"pattern_index\":"<<c.pattern<<",\"source_pattern_id\":"<<c.source_id<<",\"reflection_orbit_index\":"<<c.orbit<<",\n\"pair_phases\":";array_json(out,c.phases);out<<",\"pair_fields\":["<<c.x<<','<<c.y<<"],\n\"reflection_fields\":";array_json(out,c.reflections);out<<",\n\"S\":";array_json(out,c.S);out<<",\n\"n\":258,\"m\":1032,\"degree\":8,\"connected\":"<<(c.connected?"true":"false")<<",\"diameter\":"<<c.diameter<<",\"root_deficit_gt3_or_unreachable\":"<<c.missing<<",\"bad_unordered_pairs\":"<<129*c.missing<<",\n\"root_distance_histogram\":{";bool first=true;for(auto [d,n]:c.hist){if(!first)out<<',';first=false;out<<'"'<<d<<"\":"<<n;}out<<"}\n}\n";
}
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];double limit=stod(argv[2]);clock_t start=clock();pw[0]=1;for(int j=1;j<K;++j)pw[j]=37*pw[j-1]%Q;assert(pw[3]==42);
 for(int a=0;a<N;++a){inverse_element[a]=inverse(a);assert(multiply(a,inverse_element[a])==0&&multiply(inverse_element[a],a)==0);for(int b=0;b<N;++b)product[a][b]=multiply(a,b);}
 ifstream pf(dir+"/surviving_patterns.txt");int count;pf>>count;assert(count==3);array<int,3>sourceids;array<array<int,2>,3>phases;for(int k=0;k<3;++k)pf>>sourceids[k]>>phases[k][0]>>phases[k][1];
 ifstream rf(dir+"/reflection_representatives.txt");rf>>count;assert(count==74);vector<array<int,4>>reflections(74);for(auto&row:reflections)for(int&x:row)rf>>x;
 int done=0,legal=0,illegal=0,best_missing=N+1,connected=0;bool found=false,timeout=false;vector<int>raw_counts(222),legal_counts(222);map<int,int>hist;
 ofstream cases(dir+"/production.cases.tsv");cases<<"cursor\tpattern_index\torbit_index\tx\ty\tlegal\tmissing\tdiameter\n";
 for(int p=0;p<3&&!found&&!timeout;++p)for(int o=0;o<74&&!found&&!timeout;++o)for(int x=0;x<Q&&!found&&!timeout;++x)for(int y=0;y<Q;++y){
  if(double(clock()-start)/CLOCKS_PER_SEC>=limit){timeout=true;break;}
  Candidate c;c.pattern=p;c.source_id=sourceids[p];c.orbit=o;c.cursor=done;c.x=x;c.y=y;c.phases=phases[p];c.reflections=reflections[o];bool valid=make_generators(c);
  cases<<done<<'\t'<<p<<'\t'<<o<<'\t'<<x<<'\t'<<y<<'\t'<<valid;done++;raw_counts[p*74+o]++;
  if(!valid){illegal++;cases<<"\t-1\t-1\n";continue;}
  legal++;legal_counts[p*74+o]++;c=evaluate(c);connected+=c.connected;hist[c.missing]++;cases<<'\t'<<c.missing<<'\t'<<c.diameter<<'\n';
  if(c.missing<best_missing){best_missing=c.missing;save_best(dir,c);}
  if(c.missing==0){found=true;cout<<"FOUND_D3 cursor="<<c.cursor<<endl;break;}
 }
 cases.close();if(!found&&!timeout)assert(done==410478&&legal==404114&&illegal==6364);
 string status=found?"FOUND_D3":timeout?"CPU_LIMIT_INCOMPLETE":"COMPLETE_NO_SOLUTION";double cpu=double(clock()-start)/CLOCKS_PER_SEC;
 ofstream out(dir+"/production.terminal.json");out<<"{\n\"status\":\""<<status<<"\",\"raw_scope\":410478,\"legal_scope\":404114,\"raw_representatives_checked\":"<<done<<",\"actual_legal_graphs_checked\":"<<legal<<",\"illegal_representatives\":"<<illegal<<",\"root_BFS_runs\":"<<legal<<",\"connected_graphs_checked\":"<<connected<<",\"next_cursor\":"<<done<<",\"minimum_root_deficit\":"<<best_missing<<",\"running\":false,\"CPU_seconds\":"<<cpu<<",\n\"raw_counts_by_pattern_then_orbit\":";array_json(out,raw_counts);out<<",\n\"legal_counts_by_pattern_then_orbit\":";array_json(out,legal_counts);out<<",\n\"root_deficit_histogram\":{";bool first=true;for(auto [s,n]:hist){if(!first)out<<',';first=false;out<<'"'<<s<<"\":"<<n;}out<<"}\n}\n";out.close();
 cout<<status<<" raw="<<done<<" legal="<<legal<<" min_missing="<<best_missing<<" CPU="<<cpu<<endl;
}
