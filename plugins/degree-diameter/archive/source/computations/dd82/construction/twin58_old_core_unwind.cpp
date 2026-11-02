// Undo three saturated old-core additions, delete three auxiliary edges,
// and assign the six released old degree slots to all six auxiliary slots.
#define main previous_unrestricted_descent_main
#include "twin_seed_unrestricted_switch.cpp"
#undef main
int original_label(int v){return v<41?v:v+2;}
template<class Edges> void edgesjson(std::ostream&o,const Edges&es,bool original=false){
 o<<'[';bool comma=false;for(auto [u,v]:es){if(comma)o<<',';comma=true;edgejson(o,original?Edge{original_label(u),original_label(v)}:Edge{u,v});}o<<']';
}
int main(int argc,char**argv){
 assert(argc==3);const std::string source=argv[1],prefix=argv[2];std::ifstream in(source);int m;in>>n>>m;assert(n==58&&m==232);all=(1ULL<<n)-1;State seed{};
 for(int k=0;k<m;k++){int u,v;in>>u>>v;assert(0<=u&&u<v&&v<n&&!(seed[u]>>v&1));toggle(seed,{u,v});}
 assert(score(seed)==21);for(int u=0;u<n;u++)assert(__builtin_popcountll(seed[u])==8);
 const std::array<Edge,3>undo={Edge{3,12},Edge{9,14},Edge{28,29}};
 const std::array<int,6>old={3,9,12,14,28,29};State base=seed;
 for(Edge e:undo){assert(base[e.first]>>e.second&1);toggle(base,e);}
 std::vector<Edge>aux;for(int u=40;u<=47;u++)for(int v=u+1;v<=47;v++)if(seed[u]>>v&1)aux.emplace_back(u,v);assert(aux.size()==10);
 for(int u:old){assert(__builtin_popcountll(base[u])==7);assert((seed[u]&(((1ULL<<48)-1)^((1ULL<<40)-1)))==0);}
 const clock_t start=clock();constexpr double budget=10;bool complete=true;long long choices=0,rejected=0,valid=0;int best=100000;State bestgraph{};
 std::array<Edge,3>bestdeleted{};std::array<Edge,6>bestadded{};std::map<int,long long>hist;
 for(int a=0;a<10&&complete;a++)for(int b=a+1;b<10&&complete;b++)for(int c=b+1;c<10&&complete;c++){
  std::array<Edge,3>deleted={aux[a],aux[b],aux[c]};State partial=base;for(Edge e:deleted)toggle(partial,e);
  std::array<int,6>slots={aux[a].first,aux[a].second,aux[b].first,aux[b].second,aux[c].first,aux[c].second};
  std::array<int,6>permutation={0,1,2,3,4,5};
  do{
   choices++;State g=partial;std::array<Edge,6>added{};bool legal=true;
   for(int k=0;k<6;k++){added[k]=norm(old[k],slots[permutation[k]]);if(g[added[k].first]>>added[k].second&1){legal=false;break;}toggle(g,added[k]);}
   if(!legal)rejected++;
   else{int bad=score(g);valid++;hist[bad]++;if(bad<best){best=bad;bestgraph=g;bestdeleted=deleted;bestadded=added;}}
   if((choices&511)==0&&double(clock()-start)/CLOCKS_PER_SEC>=budget){complete=false;break;}
  }while(std::next_permutation(permutation.begin(),permutation.end()));
 }
 assert(choices==valid+rejected);if(complete)assert(choices==120*720);assert(valid>0);save(bestgraph,prefix+".best.edges");
 std::vector<Edge>bestedges;for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(bestgraph[u]>>v&1)bestedges.emplace_back(u,v);
 std::ofstream graph(prefix+".best.json");graph<<"{\"n\":58,\"edges\":";edgesjson(graph,bestedges);graph<<"}\n";
 std::ofstream o(prefix+".json");o<<"{\"source\":\""<<source<<"\",\"scope\":\"Undo three specified old edges, all triples of the ten source auxiliary edges, all 720 assignments of six old slots to six distinguished released auxiliary slots; no resulting-graph deduplication\",\"n\":58,\"m\":232,\"initial_bad_pairs\":21,\"complete_for_stated_choices\":"<<(complete?"true":"false")<<",\"choice_limit\":86400,\"choices\":"<<choices<<",\"rejected_existing_or_duplicate_attachment\":"<<rejected<<",\"valid_choices\":"<<valid<<",\"minimum_bad_pairs\":"<<best<<",\"cpu_budget_seconds\":10,\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"threads\":1,\"removed_old_edges_order58\":";edgesjson(o,undo);
 o<<",\"source_auxiliary_edges_order58\":";edgesjson(o,aux);o<<",\"best_removed_auxiliary_edges_order58\":";edgesjson(o,bestdeleted);
 o<<",\"best_added_attachment_edges_order58\":";edgesjson(o,bestadded);o<<",\"best_removed_auxiliary_edges_original60\":";edgesjson(o,bestdeleted,true);
 o<<",\"best_added_attachment_edges_original60\":";edgesjson(o,bestadded,true);o<<",\"bad_pair_histogram\":{";bool comma=false;
 for(auto [bad,num]:hist){if(comma)o<<',';comma=true;o<<'"'<<bad<<"\":"<<num;}o<<"}}\n";
 std::cout<<"choices "<<choices<<" valid "<<valid<<" rejected "<<rejected<<" complete "<<complete<<" best "<<best<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
