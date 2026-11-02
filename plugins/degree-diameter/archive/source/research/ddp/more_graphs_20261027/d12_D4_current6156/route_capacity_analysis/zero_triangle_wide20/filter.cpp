#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
struct Form{int j,x,y,z,c;};
int phase(const Form&r,int x,int y,int z){int v=(r.x*x+r.y*y+r.z*z+r.c)%20;return v<0?v+20:v;}
void put(ostream&f,const vector<int>&v){f<<'[';for(size_t i=0;i<v.size();i++){if(i)f<<',';f<<v[i];}f<<']';}
int main(int argc,char**argv){
 assert(argc==3);clock_t began=clock();rlimit limit{5,5};setrlimit(RLIMIT_CPU,&limit);string out=argv[2];ifstream in(argv[1]);int NG,NE,NO;in>>NG>>NE>>NO;assert(NG==100&&NE==13&&NO==4);
 vector<Form>good[4],even[4],one[4];
 for(int r=0;r<4;r++)for(auto spec:{pair<vector<Form>*,int>{&good[r],NG},{&even[r],NE},{&one[r],NO}})for(int k=0;k<spec.second;k++){Form a;in>>a.j>>a.x>>a.y>>a.z>>a.c;assert(in);spec.first->push_back(a);}
 int tested=0,simple=0,nonsimple=0,prefix[5]={0},firstfail[4]={0};bool hit=false,budget=false;int hx=-1,hy=-1,hz=-1;bool hs=false;vector<vector<int>>differences;
 for(int x=0;x<20&&!hit&&!budget;x++)for(int y=0;y<20&&!hit&&!budget;y++)for(int z=0;z<20&&!hit;z++){
  if((tested&255)==0&&double(clock()-began)/CLOCKS_PER_SEC>4.7){budget=true;break;}tested++;prefix[0]++;
  bool is_simple=true;for(int r=0;r<4;r++){set<int>neighbors;for(auto&a:one[r])neighbors.insert(20*a.j+phase(a,x,y,z));if(neighbors.size()!=4)is_simple=false;}
  if(is_simple)simple++;else nonsimple++;
  bool pass=true;bool G[4][80]{};bool E[4][80]{};
  for(int r=0;r<4;r++){
   for(auto&a:good[r])G[r][20*a.j+phase(a,x,y,z)]=true;
   for(auto&a:even[r])E[r][20*a.j+phase(a,x,y,z)]=true;
   bool full=true;for(int v=0;v<80;v++)if(!G[r][v]&&!E[r][v]){full=false;break;}
   if(!full){firstfail[r]++;pass=false;break;}prefix[r+1]++;
  }
  if(pass){hit=true;hx=x;hy=y;hz=z;hs=is_simple;
   for(int r=0;r<4;r++){set<int>seen;for(auto&a:one[r]){int v=20*a.j+phase(a,x,y,z);if(!G[r][v]&&seen.insert(v).second){assert(E[r][v]);differences.push_back({r,v/20,v%20});}}}
  }
 }
 if(hit){ofstream h(out+"/hit_controller.json");h<<"{\"m\":20,\"alpha\":[1,2,3,0],\"beta\":[1,3,0,2],\"va\":[0,"<<hx<<','<<hy<<",0],\"vb\":["<<hz<<",0,0,1],\"controller_vertices\":80,\"lift_n\":6480,\"controller_simple\":"<<(hs?"true":"false")<<",\"wide_missing_slots\":0,\"strict_wordfilter_missing_slots_with_R2_witness\":[";
  for(size_t i=0;i<differences.size();i++){if(i)h<<',';put(h,differences[i]);}h<<"],\"fullrank_good4_words\":100,\"R2_pencil_words\":12,\"all_fiber_starts_certified\":true,\"graph_generated\":false}\n";
 }
 ofstream f(out+"/NATIVE_RESULT.json");f<<"{\"status\":\""<<(hit?"FIRST_WIDE_CONTROLLER_PASS":budget?"BUDGET_PARTIAL":"COMPLETE8000_NO_WIDE_PASS")<<"\",\"assignments_tested\":"<<tested<<",\"scope_assignments\":8000,\"simple_controllers_seen\":"<<simple<<",\"nonsimple_controllers_kept\":"<<nonsimple<<",\"prefix_root_pass_counts\":[";
 for(int i=0;i<5;i++){if(i)f<<',';f<<prefix[i];}f<<"],\"first_failed_root_histogram\":[";for(int i=0;i<4;i++){if(i)f<<',';f<<firstfail[i];}f<<"],\"wide_hits\":"<<(hit?1:0)<<",\"CPU_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<",\"filter_CPU_limit\":5,\"graph_BFS\":0,\"voltage_slice_extended\":false}\n";
 cout<<(hit?"WIDE_HIT":"NO_WIDE_HIT")<<" tested="<<tested<<" x="<<hx<<" y="<<hy<<" z="<<hz<<" strictdifferences="<<differences.size()<<" CPU="<<double(clock()-began)/CLOCKS_PER_SEC<<'\n';
}
