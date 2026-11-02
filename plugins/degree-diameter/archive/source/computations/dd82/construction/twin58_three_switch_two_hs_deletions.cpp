// One genuine three-edge-switch neighborhood of the new HS-derived order58 seed.
// Reuse the exact endpoint score identity; never load or search the Brown seed.
#define main previous_brown_three_switch_main
#include "brown58_three_switch.cpp"
#undef main
int original_label(int v){return v<41?v:v+2;}
void edge_list(std::ostream&o,const std::vector<Edge>&es){o<<'[';for(unsigned i=0;i<es.size();i++){if(i)o<<',';o<<'['<<es[i].first<<','<<es[i].second<<']';}o<<']';}
int main(int argc,char**argv){
 assert(argc==4);const std::string source=argv[1],hs_source=argv[2],prefix=argv[3];std::ifstream input(source);int n,m;input>>n>>m;assert(n==58&&m==232);
 Graph g{},hs{};std::vector<Edge>edges,hsedges;
 for(int i=0;i<m;i++){int u,v;input>>u>>v;assert(0<=u&&u<v&&v<58&&!(g[u]>>v&1));toggle(g,u,v);}
 for(int u=0;u<58;u++){assert(pc(g[u])==8);for(int v=u+1;v<58;v++)if(g[u]>>v&1)edges.emplace_back(u,v);}
 std::ifstream reference(hs_source);int nn,mm;reference>>nn>>mm;assert(nn==60&&mm==240);
 for(int i=0;i<mm;i++){int u,v;reference>>u>>v;if((u<40||u>=50)&&(v<40||v>=50)){u-=u>=50?2:0;v-=v>=50?2:0;toggle(hs,u,v);hsedges.emplace_back(u,v);}}
 assert(hsedges.size()==175);int initial_deleted=0;for(auto [u,v]:hsedges)initial_deleted+=!(g[u]>>v&1);assert(initial_deleted==1);
 const Graph original=g;Graph old_missing{};int initial=full_score(g);assert(initial==21);for(int u=0;u<58;u++)old_missing[u]=missing(g,u);
 std::vector<Matching>patterns;Matching work{};
 std::function<void(unsigned,int)> rec=[&](unsigned used,int depth){
  if(depth==3){patterns.push_back(work);return;}int a=0;while(used>>a&1)++a;
  for(int b=a+1;b<6;b++)if(!(used>>b&1)&&a/2!=b/2){work[depth]={a,b};rec(used|(1U<<a)|(1U<<b),depth+1);}
 };rec(0,0);assert(patterns.size()==8);
 const clock_t began=clock();uint64_t triples=0,disjoint=0,legal=0,filtered=0,scored=0,fullchecks=0;bool complete=true,target=false;
 int best=100000,best_deleted=-1;Graph bestgraph{};Matching bestremove{},bestadd{};std::map<int,uint64_t>hist,deletedhist;
 for(int i=0;i<230&&complete&&!target;i++)for(int j=i+1;j<231&&complete&&!target;j++)for(int k=j+1;k<232;k++){
  triples++;
  if((triples&4095)==0&&double(clock()-began)/CLOCKS_PER_SEC>=10){complete=false;break;}
  const std::array<int,6>v={edges[i].first,edges[i].second,edges[j].first,edges[j].second,edges[k].first,edges[k].second};
  Bits endpoints=0;for(int w:v)endpoints|=Bits(1)<<w;if(pc(endpoints)!=6)continue;disjoint++;
  int removed_hs=0,old_count=0,old_inside=0;
  for(int p=0;p<3;p++)removed_hs+=(hs[v[2*p]]>>v[2*p+1])&1;
  for(int w:v){old_count+=pc(old_missing[w]);old_inside+=pc(old_missing[w]&endpoints);}old_count-=old_inside/2;
  for(int p=0;p<3;p++)toggle(g,v[2*p],v[2*p+1]);
  for(const auto&pattern:patterns){
   bool valid=true;Matching added{};int added_hs=0;
   for(int p=0;p<3;p++){auto [a,b]=pattern[p];added[p]=std::minmax(v[a],v[b]);if(g[v[a]]>>v[b]&1){valid=false;break;}added_hs+=(hs[v[a]]>>v[b])&1;}
   if(!valid)continue;legal++;const int net_deleted=initial_deleted+removed_hs-added_hs;
   if(net_deleted<2){filtered++;continue;}
   for(auto [a,b]:added)toggle(g,a,b);
   int new_count=0,new_inside=0;for(int w:v){Bits bad=missing(g,w);new_count+=pc(bad);new_inside+=pc(bad&endpoints);}
   const int value=initial-old_count+new_count-new_inside/2;
   if((scored&65535)==0){assert(value==full_score(g));fullchecks++;}
   scored++;hist[value]++;deletedhist[net_deleted]++;
   if(value<best){best=value;bestgraph=g;bestremove={edges[i],edges[j],edges[k]};bestadd=added;best_deleted=net_deleted;}
   if(value==0){target=true;write_graph(g,prefix+".valid.edges");}
   for(auto [a,b]:added)toggle(g,a,b);if(target)break;
  }
  for(int p=0;p<3;p++)toggle(g,v[2*p],v[2*p+1]);assert(g==original);if(target)break;
 }
 assert(scored>0&&legal==filtered+scored);if(complete&&!target)assert(triples==2054360);
 write_graph(bestgraph,prefix+".best.edges");std::vector<Edge>deleted,addedold;
 for(auto [u,v]:hsedges)if(!(bestgraph[u]>>v&1))deleted.emplace_back(original_label(u),original_label(v));
 for(int u=0;u<58;u++)if(u<40||u>=48)for(int v=u+1;v<58;v++)if((v<40||v>=48)&&(bestgraph[u]>>v&1)&&!(hs[u]>>v&1))addedold.emplace_back(original_label(u),original_label(v));
 assert(int(deleted.size())==best_deleted&&full_score(bestgraph)==best);
 std::ofstream o(prefix+".json");o<<"{\"source\":\""<<source<<"\",\"hs_reference_source\":\""<<hs_source<<"\",\"scope\":\"All genuine switches deleting three pairwise disjoint seed edges and adding a disjoint perfect matching on their six endpoints; added edges must be absent; final graph must delete at least two original HS50 edges\",\"pattern_definition\":\"15 perfect matchings minus original1 minus6 retaining one original edge gives8 genuine three-edge changes; two-edge switches are excluded\",\"n\":58,\"m\":232,\"cpu_budget_seconds\":10,\"cpu_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<",\"threads\":1,\"complete_neighborhood\":"<<(complete&&!target?"true":"false")<<",\"stop_reason\":\""<<(target?"valid_target_found":complete?"complete_neighborhood":"cpu_cap")<<"\",\"initial_bad_pairs\":21,\"initial_net_hs_deletions\":1,\"edge_triples_visited\":"<<triples<<",\"disjoint_edge_triples\":"<<disjoint<<",\"patterns_per_disjoint_triple\":8,\"legal_three_switches\":"<<legal<<",\"rejected_for_fewer_than_two_hs_deletions\":"<<filtered<<",\"eligible_moves_scored\":"<<scored<<",\"incremental_scores_checked_against_full\":"<<fullchecks<<",\"minimum_bad_pairs\":"<<best<<",\"best_net_hs_deletions\":"<<best_deleted<<",\"best_removed_order58\":";write_matching(o,bestremove);
 o<<",\"best_added_order58\":";write_matching(o,bestadd);o<<",\"best_deleted_hs_edges_original60\":";edge_list(o,deleted);o<<",\"best_added_old_edges_original60\":";edge_list(o,addedold);
 o<<",\"bad_pair_histogram\":";write_hist(o,hist);o<<",\"net_hs_deletion_histogram\":";write_hist(o,deletedhist);o<<"}\n";
 std::cout<<"complete "<<(complete&&!target)<<" legal "<<legal<<" eligible "<<scored<<" min "<<best<<" net HS deleted "<<best_deleted<<" CPU "<<double(clock()-began)/CLOCKS_PER_SEC<<'\n';
}
