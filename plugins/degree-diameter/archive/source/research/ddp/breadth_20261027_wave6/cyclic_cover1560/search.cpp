#include <bits/stdc++.h>
using namespace std;
struct Form{int slot;unsigned char value;};
struct State{vector<Form>forms;vector<array<int,13>>counts;int missing=0;};
int main(int argc,char**argv){
 assert(argc==4);string dir=argv[1],source=argv[2];double cpu_limit=stod(argv[3]);clock_t began=clock();
 auto cpu=[&](){return double(clock()-began)/CLOCKS_PER_SEC;};
 ifstream input(dir+"/forms.txt");int n,m,q,fc;input>>n>>m>>q>>fc;assert(n==120&&m==360&&q==13&&fc==241);
 vector<int>free(fc);for(int&e:free)input>>e;
 vector<Form>forms;vector<vector<pair<int,int>>>influence(m);
 for(int slot=0;slot<n*n;slot++){int count;input>>count;assert(count>=13);for(int j=0;j<count;j++){
  int size;input>>size;int id=forms.size();forms.push_back({slot,0});
  for(int k=0;k<size;k++){int e,c;input>>e>>c;assert(0<=e&&e<m&&0<c&&c<13);influence[e].push_back({id,c});}
 }}assert(input&&!forms.empty());
 ifstream basein(source);int bn,bm;basein>>bn>>bm;assert(bn==n&&bm==m);vector<pair<int,int>>edges(m);for(auto&[u,v]:edges)basein>>u>>v;
 auto initialize=[&](const array<int,360>&z){
  State s;s.forms=forms;s.counts.resize(n*n);for(auto&c:s.counts)c.fill(0);s.missing=n*n*13;
  for(int e:free)for(auto[id,c]:influence[e])s.forms[id].value=(s.forms[id].value+c*z[e])%13;
  for(auto f:s.forms)if(s.counts[f.slot][f.value]++==0)s.missing--;
  assert(s.missing%2==0);return s;
 };
 auto apply=[&](State&s,int edge,int delta){
  for(auto[id,c]:influence[edge]){
   auto&f=s.forms[id];int old=f.value;int next=(old+c*delta)%13;if(next<0)next+=13;
   if(--s.counts[f.slot][old]==0)s.missing++;
   if(s.counts[f.slot][next]++==0)s.missing--;
   f.value=next;
  }
 };
 array<int,360>bestz{};int best=INT_MAX,proposals=0,completed=0;bool limited=false,hit=false,calibrated=false;
 struct Stat{uint64_t seed;int initial,final,best,proposals=0,accepted=0;};vector<Stat>stats;
 const uint64_t seeds[2]={2026102761301ULL,2026102761302ULL};
 for(int start=0;start<2&&!limited&&!hit;start++){
  mt19937_64 rng(seeds[start]);uniform_int_distribution<int>voltage(0,12),edgeid(0,fc-1);uniform_real_distribution<double>unit(0,1);
  array<int,360>z{};for(int e:free)z[e]=voltage(rng);State current=initialize(z);
  Stat ss;ss.seed=seeds[start];ss.initial=current.missing;ss.best=current.missing;
  if(current.missing<best){best=current.missing;bestz=z;}
  for(int k=0;k<2000;k++){
   if((k&31)==0&&cpu()>=cpu_limit){limited=true;break;}
   int e=free[edgeid(rng)],old=z[e],next;do{next=voltage(rng);}while(next==old);
   int prior=current.missing,delta=next-old;z[e]=next;apply(current,e,delta);proposals++;ss.proposals++;
   assert(current.missing%2==0);
   if(!calibrated){
    State direct=initialize(z);assert(direct.missing==current.missing&&direct.counts==current.counts);
    for(int i=0;i<(int)direct.forms.size();i++)assert(direct.forms[i].value==current.forms[i].value);
    ofstream c(dir+"/first_incremental_calibration.json");
    c<<"{\"status\":\"MATCH\",\"first_formal_proposal\":true,\"edge_id\":"<<e<<",\"old_voltage\":"<<old<<",\"new_voltage\":"<<next<<",\"before_score\":"<<prior<<",\"incremental_score\":"<<current.missing<<",\"fresh_all_forms_score\":"<<direct.missing<<",\"all14400x13_slot_counts_match\":true,\"all_form_values_match\":true,\"graph_BFS_performed\":false}\n";calibrated=true;
   }
   if(current.missing<best){best=current.missing;bestz=z;}
   ss.best=min(ss.best,current.missing);
   if(current.missing==0){hit=true;ss.accepted++;break;}
   double temperature=100.0*pow(2.0/100.0,double(k)/1999.0);
   if(current.missing<=prior||unit(rng)<exp(-double(current.missing-prior)/temperature))ss.accepted++;
   else{apply(current,e,-delta);z[e]=old;assert(current.missing==prior);}
  }
  ss.final=current.missing;stats.push_back(ss);if(ss.proposals==2000)completed++;
  cout<<"PROFILE "<<start<<" proposals="<<ss.proposals<<" best_missing_states="<<ss.best<<" CPU="<<cpu()<<endl;
 }
 State final=initialize(bestz);
 assert(final.missing==best);vector<int>rootmissing(n,0);vector<int>masks(n*n,0);
 for(int slot=0;slot<n*n;slot++)for(int s=0;s<13;s++)if(final.counts[slot][s]==0){rootmissing[slot/n]++;masks[slot]|=1<<s;}
 ofstream params(dir+"/best_parameters.json");params<<"{\"base_vertices\":120,\"sheets\":13,\"n\":1560,\"m\":4680,\"degree\":6,\"encoding\":\"id=13*base_vertex+sheet\",\"positive_voltage_rule\":\"(u,i)--(v,i+z_e mod13), baseedge u<v\",\"missing_root_target_sheet_states\":"<<best<<",\"all_lift_ordered_pairs_distance_gt5_count\":"<<13LL*best<<",\"voltages_by_source_edge_id\":[";
 for(int e=0;e<m;e++){if(e)params<<',';params<<bestz[e];}params<<"],\"representative_root_missing_counts\":[";
 for(int u=0;u<n;u++){if(u)params<<',';params<<rootmissing[u];}params<<"],\"missing_state_masks_by_root_target\":[";
 for(int i=0;i<n*n;i++){if(i)params<<',';params<<masks[i];}params<<"]}\n";
 set<pair<int,int>>lift;vector<int>degree(n*13,0);
 for(int e=0;e<m;e++){auto[u,v]=edges[e];for(int s=0;s<13;s++){int a=13*u+s,b=13*v+(s+bestz[e])%13;assert(a!=b);lift.insert(minmax(a,b));}}
 assert(lift.size()==4680);ofstream ef(dir+"/best.edges");ef<<"1560 4680\n";for(auto[u,v]:lift){ef<<u<<' '<<v<<'\n';degree[u]++;degree[v]++;}assert(all_of(degree.begin(),degree.end(),[](int d){return d==6;}));
 ofstream terminal(dir+"/search_result.json");terminal<<"{\"status\":\""<<(hit?"HIT_ALL_ROOT_TARGET_SHEET_COVERAGE":limited?"CPU_LIMIT_PARTIAL_PROFILE":"TWO_FIXED_VOLTAGE_PROFILES_FAILED")<<"\",\"starts_planned\":2,\"starts_started\":"<<stats.size()<<",\"starts_completed\":"<<completed<<",\"proposals_per_start_limit\":2000,\"proposals_actual\":"<<proposals<<",\"sparse_forms\":"<<forms.size()<<",\"slots_scored_each_state\":14400,\"states_per_slot\":13,\"best_missing_root_target_sheet_states\":"<<best<<",\"best_all_lift_ordered_badpairs_gt5\":"<<13LL*best<<",\"initial_incremental_calibration\":"<<(calibrated?"true":"false")<<",\"cover_generated\":true,\"cover_vertices\":1560,\"cover_edges\":4680,\"cover_min_degree\":6,\"cover_max_degree\":6,\"BFS_performed\":false,\"CPU_seconds\":"<<cpu()<<",\"CPU_internal_limit_seconds\":"<<cpu_limit<<",\"profiles\":[";
 for(int i=0;i<(int)stats.size();i++){auto s=stats[i];if(i)terminal<<',';terminal<<"{\"seed\":"<<s.seed<<",\"initial_score\":"<<s.initial<<",\"final_score\":"<<s.final<<",\"best_score\":"<<s.best<<",\"proposals\":"<<s.proposals<<",\"accepted\":"<<s.accepted<<'}';}terminal<<"]}\n";
 if(hit)cout<<"HIT_SAVED best.edges"<<endl;
}
