#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
constexpr int Q=31,M=30,N=930,D=11;
uint16_t multiply_right[N][N],inverse_element[N],queue_vertices[N];
int16_t distances[N];
int powers[M];
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
U pow31(int n){U r=1;while(n--)r*=31;return r;}
U projective(int n){return (pow31(n)-1)/30;}
template<class T>void list(ostream&o,const T&v){o<<'[';bool comma=false;for(auto x:v){if(comma)o<<',';comma=true;o<<x;}o<<']';}
struct Pattern{U source_cursor,scope;int rank,dimension,anchor;array<int,5>phases;int basis[5][5]{};};
struct Position{int pattern,lead;U tail_code,projective_index,global_cursor;};
struct Score{int missing,eccentricity,visited;};
struct Counts{U raw=0,legal=0,illegal=0;int minimum=N+1;};
void init(){
 powers[0]=1;for(int j=1;j<M;j++)powers[j]=powers[j-1]*3%Q;
 assert(powers[15]==30&&powers[10]==25&&powers[6]==16);
 for(int s=0;s<N;s++){
  int sx=s%Q,sj=s/Q;inverse_element[s]=(Q-powers[(M-sj)%M]*sx%Q)%Q+Q*((M-sj)%M);
  for(int u=0;u<N;u++)multiply_right[s][u]=(u%Q+powers[u/Q]*sx)%Q+Q*((u/Q+sj)%M);
 }
 for(int s=0;s<N;s++)assert(multiply_right[s][inverse_element[s]]==0&&multiply_right[inverse_element[s]][s]==0);
}
array<int,6> reconstruct(const Pattern&p,const array<int,5>&z){
 array<int,6>fields{};int col=0;
 for(int original=0;original<6;original++)if(original!=p.anchor){
  int value=0;for(int k=0;k<p.dimension;k++)value+=p.basis[k][col]*z[k];
  fields[original]=value%Q;col++;
 }assert(col==5);return fields;
}
bool generators(const Pattern&p,const array<int,6>&fields,array<int,D>&S){
 for(int i=0;i<5;i++){int s=fields[i]+Q*p.phases[i];S[2*i]=s;S[2*i+1]=inverse_element[s];}
 S[10]=fields[5]+Q*15;assert(inverse_element[S[10]]==S[10]);auto sorted=S;sort(sorted.begin(),sorted.end());
 return sorted[0]!=0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end();
}
Score full_bfs(const array<int,D>&S){
 const uint16_t*neighbors[D];for(int k=0;k<D;k++)neighbors[k]=multiply_right[S[k]];
 fill(distances,distances+N,int16_t(-1));distances[0]=0;queue_vertices[0]=0;
 int front=0,tail=1,within3=1,eccentricity=0;
 while(front<tail){
  int u=queue_vertices[front++],depth=distances[u]+1;
  #pragma GCC unroll 11
  for(int k=0;k<D;k++){
   int v=neighbors[k][u];
   if(distances[v]<0){distances[v]=depth;queue_vertices[tail++]=v;within3+=depth<=3;eccentricity=depth;}
  }
 }
 return {N-within3,tail==N?eccentricity:-1,tail};
}
void posout(ostream&o,const Position&p){o<<"{\"pattern_index\":"<<p.pattern<<",\"lead\":"<<p.lead<<",\"tail_code\":"<<p.tail_code<<",\"projective_index\":"<<p.projective_index<<",\"global_cursor\":"<<p.global_cursor<<'}';}
void save_best(const string&base,const Pattern&p,const Position&position,const array<int,5>&z,const array<int,6>&fields,const array<int,D>&S,const Score&score){
 ofstream edges(base+"/d11_production.best.edges");edges<<N<<' '<<N*D/2<<'\n';int count=0;
 for(int u=0;u<N;u++)for(int s:S){int v=multiply_right[s][u];if(u<v){edges<<u<<' '<<v<<'\n';count++;}}
 assert(count==N*D/2);
 map<int,int>hist;for(int d:distances)hist[d]++;
 ofstream out(base+"/d11_production.best.json");out<<"{\"selection\":\"minimum_root_deficit_among_actual_legal_evaluated_prefix\",\"n\":930,\"m\":5115,\"degree\":11,\"encoding\":\"x+31*j\",\"r\":3,\"source_symbolic_cursor\":"<<p.source_cursor<<",\"position\":";posout(out,position);
 out<<",\"pair_phases\":";list(out,p.phases);out<<",\"involution_phase\":15,\"anchor_component\":"<<p.anchor<<",\"nullspace_rank\":"<<p.rank<<",\"nullspace_dimension\":"<<p.dimension<<",\"nullspace_coefficients_z\":[";for(int k=0;k<p.dimension;k++){if(k)out<<',';out<<z[k];}
 out<<"],\"fields\":";list(out,fields);out<<",\"S\":";list(out,S);out<<",\"root_deficit_gt3_or_unreachable\":"<<score.missing<<",\"bad_unordered_pairs\":"<<465LL*score.missing<<",\"diameter\":"<<score.eccentricity<<",\"connected\":"<<(score.visited==N?"true":"false")<<",\"root_vertices_reached\":"<<score.visited<<",\"root_distance_histogram\":{";bool comma=false;for(auto[d,c]:hist){if(comma)out<<',';comma=true;out<<'\"'<<d<<"\":"<<c;}out<<"}}\n";
}
void counts(ostream&o,const Counts&c){o<<"{\"raw_marked_inputs\":"<<c.raw<<",\"legal_generating_sets\":"<<c.legal<<",\"illegal_generating_sets\":"<<c.illegal<<",\"complete_single_root_BFS_runs\":"<<c.legal<<",\"minimum_root_deficit\":";if(c.legal)o<<c.minimum;else o<<"null";o<<'}';}
int main(int argc,char**argv){
 assert(argc==3);string base=argv[1];double limit=stod(argv[2]),start=cpu();init();
 ifstream input(base+"/d11_production.inputs.txt");int n;input>>n;assert(n==38);vector<Pattern>patterns(n);
 U expected=0;for(auto&p:patterns){input>>p.source_cursor>>p.rank>>p.dimension>>p.anchor>>p.scope;for(int&j:p.phases)input>>j;for(int k=0;k<p.dimension;k++)for(int j=0;j<5;j++)input>>p.basis[k][j];assert(p.dimension==5-p.rank&&p.scope==projective(p.dimension));expected+=p.scope;}assert(input&&expected==8260050);
 bool example_checked=false;for(auto&p:patterns)if(p.phases==array<int,5>{1,1,4,11,12}){array<int,5>z{1,0,0,0,0};auto x=reconstruct(p,z);assert((x==array<int,6>{0,15,25,1,0,0}));example_checked=true;}assert(example_checked);
 Counts all;vector<Counts>per(n);array<U,N+1>hist{};U cursor=0;int best=N+1;Position next{};bool timeout=false,found=false;double bfs_cpu=0;
 for(int k=0;k<n;k++){
  const Pattern&p=patterns[k];U local=0;
  for(int lead=0;lead<p.dimension;lead++)for(U code=0;code<pow31(p.dimension-lead-1);code++){
   Position position{k,lead,code,local,cursor};next=position;
   if((cursor&1023)==0&&cpu()-start>=limit){timeout=true;goto done;}
   array<int,5>z{};z[lead]=1;U digits=code;for(int j=lead+1;j<p.dimension;j++){z[j]=digits%31;digits/=31;}
   // No original-field leading-coordinate test: only z is normalized.
   auto fields=reconstruct(p,z);array<int,D>S;bool valid=generators(p,fields,S);
   all.raw++;per[k].raw++;cursor++;local++;
   if(!valid){all.illegal++;per[k].illegal++;}
   else{
    all.legal++;per[k].legal++;double timer=cpu();auto score=full_bfs(S);bfs_cpu+=cpu()-timer;
    hist[score.missing]++;all.minimum=min(all.minimum,score.missing);per[k].minimum=min(per[k].minimum,score.missing);
    if(score.missing<best){best=score.missing;save_best(base,p,position,z,fields,S,score);cout<<"BEST cursor="<<position.global_cursor<<" source="<<p.source_cursor<<" missing="<<best<<" D="<<score.eccentricity<<" CPU="<<cpu()-start<<endl;}
    if(!score.missing){found=true;goto done;}
   }
   if(cursor==1000||cursor%1000000==0){ofstream progress(base+"/d11_production.progress.json");progress<<setprecision(12)<<"{\"cursor\":"<<cursor<<",\"CPU_seconds\":"<<cpu()-start<<",\"BFS_CPU_seconds\":"<<bfs_cpu<<",\"counts\":";counts(progress,all);progress<<"}\n";cout<<"PROGRESS cursor="<<cursor<<" CPU="<<cpu()-start<<" BFS_CPU="<<bfs_cpu<<" legal="<<all.legal<<" best="<<best<<endl;}
  }
  assert(local==p.scope);cout<<"PATTERN_COMPLETE index="<<k<<" source="<<p.source_cursor<<" checked="<<local<<" legal="<<per[k].legal<<" best="<<per[k].minimum<<" CPU="<<cpu()-start<<endl;
 }
done:
 string status=found?"FOUND_D3":timeout?"CPU_LIMIT_INCOMPLETE":"COMPLETE_NO_SOLUTION";if(!found&&!timeout)assert(cursor==8260050);
 ofstream out(base+"/d11_production.terminal.json");out<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"scope\":\"degree11 five inverse pairs plus one reflection, 38 surviving tight-linear modes only\",\"raw_scope\":8260050,\"patterns\":38,\"next_cursor\":"<<cursor<<",\"next_position\":";
 if(timeout)posout(out,next);else out<<"null";
 out<<",\"counts\":";counts(out,all);out<<",\"per_pattern\":[";for(int k=0;k<n;k++){if(k)out<<',';out<<"{\"source_symbolic_cursor\":"<<patterns[k].source_cursor<<",\"expected_marked_inputs\":"<<patterns[k].scope<<",\"counts\":";counts(out,per[k]);out<<'}';}
 out<<"],\"root_deficit_histogram\":{";bool comma=false;for(int j=0;j<=N;j++)if(hist[j]){if(comma)out<<',';comma=true;out<<'\"'<<j<<"\":"<<hist[j];}out<<"},\"CPU_seconds\":"<<cpu()-start<<",\"complete_BFS_CPU_seconds\":"<<bfs_cpu<<",\"running\":false,\"other_37_four_pair_modes_not_searched\":true,\"degree12_not_searched\":true}\n";
 cout<<status<<" cursor="<<cursor<<" CPU="<<cpu()-start<<" legal="<<all.legal<<" best="<<best<<endl;
}
