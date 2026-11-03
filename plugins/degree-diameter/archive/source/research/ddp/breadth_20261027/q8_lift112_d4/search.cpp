#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
constexpr int R=14,Q=8,N=112,E=28,F=15,DEG=4;
int mul(int x,int y){int a=x&1,b=(x>>1)&1,c=x>>2,u=y&1,v=(y>>1)&1,d=y>>2;return (a^u)+2*(b^v)+4*(c^d^(a&u)^(b&v)^(b&u));}
int inv(int x){return (x&3)?x^4:x;}
array<int,E>U,V;array<int,F>freeids;array<vector<array<int,3>>,R>base;
struct State{array<int,E>h{};int deficit=R*N+1;array<int,R>miss{};int diameter=-1;};
State best,current,neighbor;array<array<int,DEG>,N>bestadj{};
long long evals=0,scans=0,moves=0,kicks=0;int started=0,completed=0,segments=0,st=-1,seg=-1,roundid=-1,slot=-1,val=-1;
bool hit=false,limited=false;clock_t began;double budget;string dir;ofstream events;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
template<class T>void arr(ostream&o,const T&a){o<<'[';bool f=true;for(auto x:a){if(!f)o<<',';f=false;o<<x;}o<<']';}
void sj(ostream&o,const State&s){o<<"{\"voltages\":";arr(o,s.h);o<<",\"root_misses\":";arr(o,s.miss);o<<",\"sum_deficits\":"<<s.deficit<<",\"diameter\":"<<s.diameter<<'}';}
array<array<int,DEG>,N> graph(const State&s){array<array<int,DEG>,N>a;for(int i=0;i<R;i++)for(int g=0;g<Q;g++){int k=0;for(auto d:base[i]){int h=s.h[d[1]];if(d[2])h=inv(h);a[8*i+g][k++]=8*d[0]+mul(g,h);}assert(k==4);sort(a[8*i+g].begin(),a[8*i+g].end());}return a;}
vector<int> evaluate(State&s){auto a=graph(s);vector<int>all;all.reserve(R*N);s.deficit=0;s.diameter=0;bool connected=true;
 for(int i=0;i<R;i++){int d[N],q[N],head=0,tail=1;fill(d,d+N,-1);d[8*i]=0;q[0]=8*i;while(head<tail){int u=q[head++];for(int v:a[u])if(d[v]<0){d[v]=d[u]+1;q[tail++]=v;}}s.miss[i]=0;for(int x:d){s.miss[i]+=(x<0||x>4);s.diameter=max(s.diameter,x);all.push_back(x);}s.deficit+=s.miss[i];connected&=tail==N;}
 if(!connected)s.diameter=-1;evals++;if(s.deficit<best.deficit){best=s;bestadj=a;events<<"{\"evaluation\":"<<evals<<",\"CPU_seconds\":"<<cpu()<<",\"candidate\":";sj(events,s);events<<"}\n";events.flush();cout<<"BEST deficits="<<s.deficit<<" bad="<<4*s.deficit<<" D="<<s.diameter<<" CPU="<<cpu()<<endl;}hit|=s.deficit==0;return all;}
bool expired(){if(cpu()<budget)return false;limited=true;return true;}
bool scan(){neighbor=current;for(slot=0;slot<F;slot++)for(val=0;val<Q;val++)if(val!=current.h[freeids[slot]]){if(expired())return false;auto x=current;x.h[freeids[slot]]=val;evaluate(x);if(x.deficit<neighbor.deficit)neighbor=x;if(hit)return false;}scans++;return true;}
int main(int argc,char**argv){assert(argc==3);dir=argv[1];budget=stod(argv[2]);began=clock();ifstream in(dir+"/input.txt");int e;in>>e;assert(e==E);for(int k=0;k<E;k++){in>>U[k]>>V[k];base[U[k]].push_back({V[k],k,0});base[V[k]].push_back({U[k],k,1});}for(int&x:freeids)in>>x;int n;in>>n;assert(n==12);vector<State>starts(n);for(auto&s:starts)for(int&h:s.h)in>>h;vector<int>expectedadj(N*DEG),expecteddist(R*N);for(int&x:expectedadj)in>>x;for(int&x:expecteddist)in>>x;
 events.open(dir+"/improvements.jsonl");ofstream trace(dir+"/segments.jsonl");mt19937_64 rng(20261027143ULL);
 for(st=0;st<n&&!hit&&!limited;st++){if(expired())break;current=starts[st];auto d=evaluate(current);started++;if(st==0){auto a=graph(current);int k=0;for(auto row:a)for(int x:row)assert(x==expectedadj[k++]);assert(d==expecteddist);ofstream o(dir+"/first_cpp_check.json");o<<"{\"all448_adjacencies_match_independent_Python\":true,\"all1568_fourteen_root_distances_match\":true,\"first_score_reused\":true}\n";}
  for(seg=0;seg<3&&!hit&&!limited;seg++){int accepted=0;for(roundid=0;roundid<12&&!hit&&!limited;roundid++){if(!scan())break;if(neighbor.deficit>=current.deficit)break;current=neighbor;moves++;accepted++;}if(hit||limited)break;segments++;trace<<"{\"start\":"<<st<<",\"segment\":"<<seg<<",\"accepted\":"<<accepted<<",\"sum_deficits\":"<<current.deficit<<"}\n";trace.flush();if(seg<2){int a=rng()%15,b=rng()%14;if(b>=a)b++;for(int j:{a,b}){int e=freeids[j];current.h[e]=(current.h[e]+1+rng()%7)%8;}evaluate(current);kicks++;}}
  if(!hit&&!limited)completed++;
 }
 ofstream edge(dir+"/best.edges");edge<<N<<" 224\n";int count=0;for(int u=0;u<N;u++)for(int v:bestadj[u])if(u<v){edge<<u<<' '<<v<<'\n';count++;}assert(count==224);
 ofstream b(dir+"/best.json");b<<"{\"n\":112,\"m\":224,\"degree\":4,\"target_D\":4,\"bad_unordered_pairs\":"<<4*best.deficit<<",\"candidate\":";sj(b,best);b<<"}\n";
 ofstream o(dir+"/terminal.json");o<<"{\"status\":\""<<(hit?"FOUND_D4":limited?"CPU_LIMIT_PREFIX_SAVED":"COMPLETE_12_START_PROFILE_NO_D4")<<"\",\"running\":false,\"found_D4\":"<<(hit?"true":"false")<<",\"starts_scope\":12,\"starts_started\":"<<started<<",\"starts_completed\":"<<completed<<",\"segments_completed\":"<<segments<<",\"full105_neighbor_scans\":"<<scans<<",\"strict_moves\":"<<moves<<",\"two_distinct_coordinate_kicks\":"<<kicks<<",\"fourteen_root_evaluations\":"<<evals<<",\"BFS_roots_scored\":"<<14*evals<<",\"best_sum_deficits\":"<<best.deficit<<",\"best_bad_unordered_pairs\":"<<4*best.deficit<<",\"production_CPU_seconds\":"<<cpu()<<",\"scope_exhausted\":"<<(!hit&&!limited?"true":"false")<<",\"entire_voltage_family_exhausted\":false,\"cursor\":{\"start\":"<<st<<",\"segment\":"<<seg<<",\"round\":"<<roundid<<",\"free_slot\":"<<slot<<",\"value\":"<<val<<"},\"current\":";sj(o,current);o<<",\"best_neighbor_seen\":";sj(o,neighbor);o<<",\"pending\":[\"root independent final saved-edge verification\"]}\n";
 cout<<"TERMINAL eval="<<evals<<" bad="<<4*best.deficit<<" D="<<best.diameter<<" CPU="<<cpu()<<endl;
}
