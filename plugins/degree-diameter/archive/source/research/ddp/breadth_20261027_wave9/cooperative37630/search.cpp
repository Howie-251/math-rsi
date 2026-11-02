#include <bits/stdc++.h>
using namespace std;using U64=uint64_t;
using Pins=array<vector<int>,2>;using Missing=array<vector<U64>,2>;
int N,W,F;vector<vector<int>>adj;vector<int>eligible,deficit;vector<U64>r3,r4;U64 lastmask;clock_t began;double budget;bool limited=false,hit=false;long long greedy_scores=0,coordinate_scores=0;string dir;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
const U64*ball(int radius,int pin){return &(radius==3?r3:r4)[size_t(pin)*W];}
Missing missing(const Pins&s){
 Missing m={vector<U64>(W,~0ULL),vector<U64>(W,~0ULL)};m[0].back()=m[1].back()=lastmask;
 for(int c=0;c<2;c++)for(int p:s[c])if(p>=0){auto own=ball(4,p),other=ball(3,p);for(int w=0;w<W;w++){m[c][w]&=~own[w];m[1-c][w]&=~other[w];}}
 return m;
}
array<int,2>counts(const Missing&m){array<int,2>c{};for(int k=0;k<2;k++)for(U64 x:m[k])c[k]+=__builtin_popcountll(x);return c;}
int total(const Missing&m){auto c=counts(m);return c[0]+c[1];}
bool legal(const Pins&s,int colour,int pin){for(int p:s[colour])if(p==pin)return false;for(int p:s[1-colour])if(p==pin&&deficit[pin]<2)return false;return true;}
struct Pick{int colour=-1,pin=-1,gain=-1;long long tested=0;bool complete=true;};
Pick pick(const Pins&s,const Missing&m,vector<int>colours,bool coordinate,int old=-1,int oldgain=-1){
 Pick best;if(old>=0){best.colour=colours[0];best.pin=old;best.gain=oldgain;}
 array<vector<int>,2>active;for(int c=0;c<2;c++)for(int w=0;w<W;w++)if(m[c][w])active[c].push_back(w);
 for(int c:colours)for(int p=0;p<F;p++){
  if((p&255)==0&&cpu()>=budget){limited=true;best.complete=false;return best;}
  if(!legal(s,c,p))continue;auto own=ball(4,p),other=ball(3,p);int gain=0;
  for(int w:active[c])gain+=__builtin_popcountll(m[c][w]&own[w]);for(int w:active[1-c])gain+=__builtin_popcountll(m[1-c][w]&other[w]);
  best.tested++;if(coordinate)coordinate_scores++;else greedy_scores++;
  if(gain>best.gain){best.colour=c;best.pin=p;best.gain=gain;}
 }return best;
}
void writePins(ostream&o,const vector<int>&p){o<<'[';for(int i=0;i<(int)p.size();i++){if(i)o<<',';o<<eligible[p[i]];}o<<']';}
int main(int argc,char**argv){
 assert(argc==5);dir=argv[1];string source=argv[2],oldfile=argv[3];budget=stod(argv[4]);began=clock();
 ifstream input(source);string line;long long degree_sum=0;
 while(getline(input,line)){if(line.empty()||line[0]=='#')continue;istringstream ss(line);int u,v;ss>>u;assert(u==(int)adj.size());adj.emplace_back();while(ss>>v)adj.back().push_back(v);degree_sum+=adj.back().size();}
 N=adj.size();W=(N+63)/64;assert(N==37628&&degree_sum%2==0);long long source_m=degree_sum/2;lastmask=(N%64)?(1ULL<<(N%64))-1:~0ULL;
 vector<int>index(N,-1);int shareable=0;for(int u=0;u<N;u++){assert(adj[u].size()<=11);if(adj[u].size()<11){index[u]=eligible.size();eligible.push_back(u);deficit.push_back(11-adj[u].size());shareable+=adj[u].size()<=9;}}
 F=eligible.size();assert(F==2504&&shareable==315);r3.assign(size_t(F)*W,0);r4.assign(size_t(F)*W,0);vector<int>seen(N,0),queue(N),size3(F),size4(F);
 for(int k=0;k<F;k++){
  if((k&127)==0&&cpu()>=budget){ofstream t(dir+"/search_result.json");t<<"{\"status\":\"PREPARATION_CPU_LIMIT_NO_PROFILE\",\"balls_completed\":"<<k<<",\"CPU_seconds\":"<<cpu()<<"}\n";return 0;}
  int head=0,tail=1;queue[0]=eligible[k];seen[queue[0]]=k+1;int at3=0;
  for(int depth=1;depth<=4;depth++){int stop=tail;while(head<stop){int u=queue[head++];for(int v:adj[u])if(seen[v]!=k+1){seen[v]=k+1;queue[tail++]=v;}}if(depth==3)at3=tail;}
  auto b3=&r3[size_t(k)*W],b4=&r4[size_t(k)*W];for(int j=0;j<tail;j++){int v=queue[j];b4[v>>6]|=1ULL<<(v&63);if(j<at3)b3[v>>6]|=1ULL<<(v&63);}size3[k]=at3;size4[k]=tail;
 }
 double preparation_cpu=cpu();ofstream f3(dir+"/radius3.u64.bin",ios::binary),f4(dir+"/radius4.u64.bin",ios::binary);f3.write(reinterpret_cast<char*>(r3.data()),r3.size()*8);f4.write(reinterpret_cast<char*>(r4.data()),r4.size()*8);f3.close();f4.close();
 ofstream meta(dir+"/coverage_cache.json");meta<<"{\"source_n\":"<<N<<",\"source_edges\":"<<source_m<<",\"W_words\":"<<W<<",\"eligible_count\":"<<F<<",\"shareable_count\":"<<shareable<<",\"effective_old_capacity\":"<<F+shareable<<",\"radii\":[3,4],\"bytes_each\":"<<r3.size()*8<<",\"layout\":\"candidate-major native uint64 words, ascending eligible vertex order; closed balls\",\"eligible_vertices\":[";for(int p=0;p<F;p++){if(p)meta<<',';meta<<eligible[p];}meta<<"],\"preparation_CPU_seconds\":"<<preparation_cpu<<"}\n";meta.close();
 ifstream oldin(oldfile);int oldcount;oldin>>oldcount;assert(oldcount==11);vector<int>old(11);for(int&v:old){oldin>>v;assert(index[v]>=0);v=index[v];}
 Pins best;int bestscore=INT_MAX,beststart=-1;string beststage;bool calibrated=false;
 auto observe=[&](const Pins&s,int start,const string&stage){int val=total(missing(s));if(val<bestscore){bestscore=val;best=s;beststart=start;beststage=stage;}if(val==0){hit=true;cout<<"HIT_COVERAGE start="<<start<<" stage="<<stage<<endl;}};
 struct Sweep{int before,after,moves=0,positions=0;bool complete=false;};struct Stat{int start,initial=-1,deleted=-1;Pins initialpins;vector<Sweep>sweeps;bool initialized=false;};vector<Stat>stats;
 ofstream trace(dir+"/initial_greedy_trace.jsonl");
 for(int start=0;start<2&&!limited&&!hit;start++){
  Pins s;Stat stat;stat.start=start;
  if(start==0){
   int least=INT_MAX,del=-1;for(int d=0;d<11;d++){Pins test;for(int j=0;j<11;j++)if(j!=d)test[0].push_back(old[j]);int miss=counts(missing(test))[0];if(miss<least){least=miss;del=d;}}
   stat.deleted=eligible[old[del]];for(int j=0;j<11;j++)if(j!=del)s[0].push_back(old[j]);
  }
  while((s[0].size()<10||s[1].size()<10)&&!limited&&!hit){
   vector<int>colours;if(start==0)colours={1};else if(s[0].size()<s[1].size())colours={0};else if(s[1].size()<s[0].size())colours={1};else colours={0,1};
   colours.erase(remove_if(colours.begin(),colours.end(),[&](int c){return s[c].size()>=10;}),colours.end());auto m=missing(s);auto chosen=pick(s,m,colours,false);
   if(!chosen.complete)break;assert(chosen.pin>=0);s[chosen.colour].push_back(chosen.pin);auto now=counts(missing(s));
   trace<<"{\"start\":"<<start<<",\"colour\":"<<chosen.colour<<",\"vertex\":"<<eligible[chosen.pin]<<",\"joint_gain\":"<<chosen.gain<<",\"missA\":"<<now[0]<<",\"missB\":"<<now[1]<<"}\n";
   if(now[0]+now[1]==0)observe(s,start,"initialization");
  }
  if(limited){observe(s,start,"partial_initialization");stat.initialpins=s;stat.initial=total(missing(s));stats.push_back(stat);break;}
  stat.initialized=true;stat.initialpins=s;stat.initial=total(missing(s));observe(s,start,"initialization_complete");
  for(int sweep=0;sweep<2&&!limited&&!hit;sweep++){
   Sweep sw;sw.before=total(missing(s));
   for(int c=0;c<2&&!limited&&!hit;c++)for(int pos=0;pos<(int)s[c].size()&&!limited&&!hit;pos++){
    int oldpin=s[c][pos],prior=total(missing(s));s[c][pos]=-1;auto base_missing=missing(s);int base_score=total(base_missing);
    auto chosen=pick(s,base_missing,{c},true,oldpin,base_score-prior);if(!chosen.complete){s[c][pos]=oldpin;break;}
    s[c][pos]=chosen.pin;int predicted=base_score-chosen.gain;
    if(!calibrated){
     auto fresh=missing(s);Missing projected=base_missing;auto own=ball(4,chosen.pin),other=ball(3,chosen.pin);for(int w=0;w<W;w++){projected[c][w]&=~own[w];projected[1-c][w]&=~other[w];}
     assert(fresh==projected&&total(fresh)==predicted);auto ct=counts(fresh);ofstream cal(dir+"/first_coordinate_calibration.json");cal<<"{\"status\":\"MATCH\",\"first_formal_coordinate_proposal\":true,\"colour\":"<<c<<",\"position\":"<<pos<<",\"old_vertex\":"<<eligible[oldpin]<<",\"selected_vertex\":"<<eligible[chosen.pin]<<",\"strict_improvement\":"<<(predicted<prior?"true":"false")<<",\"A_pin_count\":"<<s[0].size()<<",\"B_pin_count\":"<<s[1].size()<<",\"full20pin_rebuild_missA\":"<<ct[0]<<",\"full20pin_rebuild_missB\":"<<ct[1]<<",\"candidate_scan_score\":"<<predicted<<",\"all37628x2_missing_bits_match\":true,\"proposal_reused_in_formal_sweep\":true,\"BFS_performed\":false}\n";calibrated=true;
    }
    assert(predicted<=prior);sw.positions++;if(predicted<prior)sw.moves++;observe(s,start,"coordinate_sweep"+to_string(sweep));
   }
   sw.after=total(missing(s));sw.complete=sw.positions==20;stat.sweeps.push_back(sw);if(!sw.moves)break;
  }
  stats.push_back(stat);cout<<"START "<<start<<" initial="<<stat.initial<<" final="<<total(missing(s))<<" best="<<bestscore<<" CPU="<<cpu()<<endl;
 }
 trace.close();assert(bestscore<INT_MAX);auto mbest=missing(best);auto finalcounts=counts(mbest);vector<int>usage(N,0);for(int c=0;c<2;c++){assert(best[c].size()<=10);set<int>unique(best[c].begin(),best[c].end());assert(unique.size()==best[c].size());for(int p:best[c])usage[eligible[p]]++;}
 for(int u=0;u<N;u++)assert(adj[u].size()+usage[u]<=11);long long newm=source_m+best[0].size()+best[1].size()+1;
 ofstream graph(dir+"/best.edges");graph<<N+2<<' '<<newm<<'\n';long long oldwritten=0;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){graph<<u<<' '<<v<<'\n';oldwritten++;}assert(oldwritten==source_m);graph<<N<<' '<<N+1<<'\n';for(int c=0;c<2;c++)for(int p:best[c])graph<<eligible[p]<<' '<<N+c<<'\n';
 ofstream params(dir+"/best_parameters.json");params<<"{\"source_n\":"<<N<<",\"source_edges\":"<<source_m<<",\"n\":"<<N+2<<",\"m\":"<<newm<<",\"new_vertices\":["<<N<<','<<N+1<<"],\"new_vertices_adjacent\":true,\"A\":";writePins(params,best[0]);params<<",\"B\":";writePins(params,best[1]);params<<",\"missA\":"<<finalcounts[0]<<",\"missB\":"<<finalcounts[1]<<",\"joint_score\":"<<bestscore<<",\"missingA\":[";
 for(int c=0;c<2;c++){bool comma=false;for(int v=0;v<N;v++)if(mbest[c][v>>6]>>(v&63)&1){if(comma)params<<',';comma=true;params<<v;}if(c==0)params<<"],\"missingB\":[";}
 params<<"],\"shared_pins\":[";bool comma=false;for(int u=0;u<N;u++)if(usage[u]==2){if(comma)params<<',';comma=true;params<<u;}params<<"],\"old_pin_degree_budget\":[";comma=false;for(int u=0;u<N;u++)if(usage[u]){if(comma)params<<',';comma=true;params<<"{\"vertex\":"<<u<<",\"old_degree\":"<<adj[u].size()<<",\"new_edges\":"<<usage[u]<<",\"new_degree\":"<<adj[u].size()+usage[u]<<'}';}params<<"],\"new_degrees\":["<<best[0].size()+1<<','<<best[1].size()+1<<"],\"all_degree_caps_checked\":true,\"best_start\":"<<beststart<<",\"best_stage\":\""<<beststage<<"\"}\n";
 ofstream t(dir+"/search_result.json");t<<"{\"status\":\""<<(hit?"HIT_EXACT_BOTH_NEW_ROOT_COVERAGE":limited?"CPU_LIMIT_INCOMPLETE_PROFILE":"TWO_FIXED_COOPERATIVE_PROFILES_COMPLETE_NO_HIT")<<"\",\"source_n\":"<<N<<",\"source_edges\":"<<source_m<<",\"new_n\":"<<N+2<<",\"new_edges\":"<<newm<<",\"eligible_vertices\":"<<F<<",\"shareable_vertices\":"<<shareable<<",\"effective_spoke_capacity\":"<<F+shareable<<",\"closedR3_R4_preparation_roots\":"<<F<<",\"preparation_depth\":4,\"preparation_CPU_seconds\":"<<preparation_cpu<<",\"greedy_candidate_scores\":"<<greedy_scores<<",\"coordinate_candidate_scores\":"<<coordinate_scores<<",\"best_joint_missing\":"<<bestscore<<",\"best_missA\":"<<finalcounts[0]<<",\"best_missB\":"<<finalcounts[1]<<",\"first_formal_coordinate_calibrated\":"<<(calibrated?"true":"false")<<",\"full_graph_generated\":true,\"source_all_root_BFS_rerun\":false,\"producer_final_root_BFS_performed\":false,\"CPU_seconds\":"<<cpu()<<",\"CPU_internal_limit_seconds\":"<<budget<<",\"starts_planned\":2,\"starts_actual\":"<<stats.size()<<",\"profiles\":[";
 for(int i=0;i<(int)stats.size();i++){auto st=stats[i];if(i)t<<',';t<<"{\"start\":"<<st.start<<",\"initialized\":"<<(st.initialized?"true":"false")<<",\"removed_old_best_pin\":"<<st.deleted<<",\"initial_joint_missing\":"<<st.initial<<",\"initial_A\":";writePins(t,st.initialpins[0]);t<<",\"initial_B\":";writePins(t,st.initialpins[1]);t<<",\"sweeps\":[";for(int j=0;j<(int)st.sweeps.size();j++){auto sw=st.sweeps[j];if(j)t<<',';t<<"{\"index\":"<<j<<",\"before\":"<<sw.before<<",\"after\":"<<sw.after<<",\"strict_replacements\":"<<sw.moves<<",\"positions_scanned\":"<<sw.positions<<",\"complete\":"<<(sw.complete?"true":"false")<<'}';}t<<"]}";}t<<"]}\n";
 if(hit)cout<<"HIT_SAVED best.edges"<<endl;
}
