#include <filesystem>
struct Graph {
 vector<vector<int>> adj; int m=0; vector<int> stamp,depth,queue; int tag=0;
 Graph(const string&file){ifstream f(file);int n,a,b;f>>n>>m;if(n!=42403||m!=245949)throw runtime_error("source binding");adj.resize(n);int cnt=0;while(f>>a>>b){if(a<0||b<0||a>=n||b>=n||a==b)throw runtime_error("edge");adj[a].push_back(b);adj[b].push_back(a);cnt++;}if(cnt!=m)throw runtime_error("edgecount");for(auto&r:adj){sort(r.begin(),r.end());if(r.size()>12||adjacent_find(r.begin(),r.end())!=r.end())throw runtime_error("source simple/degree");}resize();}
 void resize(){stamp.resize(adj.size());depth.resize(adj.size());queue.resize(adj.size());}
 int bfs(const vector<int>&roots,int radius,array<int,5>*layers=nullptr){tag++;int h=0,t=0;if(layers)layers->fill(0);for(int r:roots){stamp[r]=tag;depth[r]=0;queue[t++]=r;if(layers)(*layers)[0]++;}while(h<t){int v=queue[h++];if(depth[v]==radius)continue;for(int w:adj[v])if(stamp[w]!=tag){stamp[w]=tag;depth[w]=depth[v]+1;queue[t++]=w;if(layers)(*layers)[depth[w]]++;}}return t;}
 void add(const vector<int>&pins){int n=adj.size();adj.push_back(pins);for(int v:pins){if(adj[v].size()>=12)throw runtime_error("selected saturated");adj[v].push_back(n);}m+=pins.size();resize();}
};
int main(int argc,char**argv){try{
 if(argc==2&&string(argv[1])=="--control"){control();return 0;}if(argc!=5)return 2;
 string out=argv[1],rawplanes=argv[2],source=argv[3];double start=cpu();Budget budget;budget.end=start+stod(argv[4]);Graph g(source);
 ifstream pf(rawplanes);int np;pf>>np;if(np!=754)throw runtime_error("plane domain");vector<int>planeids(np);vector<vector<vector<int>>>raw(np,vector<vector<int>>(91));
 for(int i=0;i<np;i++){pf>>planeids[i];for(auto&r:raw[i]){int n;pf>>n;r.resize(n);for(int&v:r)pf>>v;}}if(!pf)throw runtime_error("raw plane input");
 ofstream sequences(out+"/ADDITIONS.jsonl"),stepresults(out+"/STEP_RESULTS.jsonl"),allplanes(out+"/PER_PLANE.jsonl");int accepted=0;string terminal="MAX8_ACCEPTED";long long totalP=0;vector<vector<int>>allpins;
 for(int step=0;step<8;step++){
  double stepstart=cpu();int n=g.adj.size(),nt=n-41356;vector<int>ids,index(n,-1);for(int v=0;v<n;v++)if(g.adj[v].size()<12){index[v]=ids.size();ids.push_back(v);}int nf=ids.size(),nw=(nf+63)/64;vector<Plane>planes;int impossible=0;
  for(int i=0;i<np;i++){auto lines=raw[i];bool possible=true;for(auto&r:lines){vector<int>filtered;for(int v:r)if(v<n&&index[v]>=0)filtered.push_back(index[v]);r=move(filtered);if(r.empty())possible=false;}if(possible)planes.push_back(plane_(planeids[i],lines));else{impossible++;allplanes<<"{\"step\":"<<step<<",\"plane_id\":"<<planeids[i]<<",\"status\":\"IMPOSSIBLE_CURRENT_DEGREE\"}\n";}}
  sort(planes.begin(),planes.end(),[](const Plane&a,const Plane&b){return a.pins.size()==b.pins.size()?a.id<b.id:a.pins.size()<b.pins.size();});
  vector<Bits>rows(nt,Bits(nw));int rootsdone=0;long long providercount=0;
  for(int r=41356;r<n;r++){if(!budget.check())break;int reached=g.bfs(vector<int>{r},4);for(int q=0;q<reached;q++){int k=index[g.queue[q]];if(k>=0){rows[r-41356][k/64]|=1ULL<<(k%64);providercount++;}}rootsdone++;}
  if(rootsdone!=nt){terminal="UNKNOWN_PROVIDER_PREPARATION_LIMIT";stepresults<<"{\"step\":"<<step<<",\"source_n\":"<<n<<",\"status\":\""<<terminal<<"\",\"completed_provider_roots\":"<<rootsdone<<",\"required_provider_roots\":"<<nt<<"}\n";break;}
  Tail tail(nf,nt,move(rows),budget);bool hit=false;int hitplane=-1;vector<int>hitcore,hittail,hitpins;array<long long,13>hist{};int reachedplanes=0;long long thisP=0,completeP=0;array<int,5>layers{};int actualcovered=0;
  for(size_t pi=0;pi<planes.size();pi++){
   if(!budget.check())break;reachedplanes++;string status="ACTIVE";
   auto visit=[&](uint64_t mask){vector<int>core;for(size_t k=0;k<planes[pi].pins.size();k++)if(mask>>k&1)core.push_back(planes[pi].pins[k]);thisP++;totalP++;hist[core.size()]++;
    if(tail.complete(core,12)){hitplane=planes[pi].id;for(int k:core)hitcore.push_back(ids[k]);for(int k:tail.solution)hittail.push_back(ids[k]);hitpins=hitcore;hitpins.insert(hitpins.end(),hittail.begin(),hittail.end());sort(hitpins.begin(),hitpins.end());if(hitpins.size()>12||adjacent_find(hitpins.begin(),hitpins.end())!=hitpins.end())throw runtime_error("candidate size/simple");for(int v:hitpins)if(g.adj[v].size()>=12)throw runtime_error("capacity");actualcovered=g.bfs(hitpins,4,&layers);if(actualcovered!=n)throw runtime_error("provider candidate fails complete actual current R4");hit=true;status="HIT_ACTUAL_R4_PASS";return true;}
    if(budget.stopped){status="UNKNOWN_LIMIT";return true;}completeP++;return false;};
   Core en(planes[pi],budget,12,visit);en.dfs(0,0,{});if(!hit)status=budget.stopped?"UNKNOWN_LIMIT":"EXHAUSTED";
   allplanes<<"{\"step\":"<<step<<",\"plane_id\":"<<planes[pi].id<<",\"available_pins\":"<<planes[pi].pins.size()<<",\"status\":\""<<status<<"\",\"core_nodes\":"<<en.nodes<<",\"minimal_blockers\":"<<en.leaves<<"}\n";
   if(hit||budget.stopped){for(size_t j=pi+1;j<planes.size();j++)allplanes<<"{\"step\":"<<step<<",\"plane_id\":"<<planes[j].id<<",\"status\":\"NOT_REACHED\"}\n";break;}
  }
  if(hit){
   int newv=n;g.add(hitpins);accepted++;allpins.push_back(hitpins);
   sequences<<"{\"step\":"<<step<<",\"source_n\":"<<n<<",\"source_m\":"<<g.m-int(hitpins.size())<<",\"new_vertex\":"<<newv<<",\"order\":"<<g.adj.size()<<",\"size\":"<<g.m<<",\"plane_id\":"<<hitplane<<",\"core\":"<<ints(hitcore)<<",\"tail\":"<<ints(hittail)<<",\"pins\":"<<ints(hitpins)<<",\"actual_R4_covered\":"<<actualcovered<<",\"R4_layers\":[";for(int k=0;k<5;k++){if(k)sequences<<',';sequences<<layers[k];}sequences<<"],\"max_degree\":12,\"old_edges_retained\":true,\"current_free_count\":"<<nf<<",\"peripheral_targets\":"<<nt<<",\"provider_roots_completed\":"<<rootsdone<<",\"provider_positive_bits\":"<<providercount<<",\"CPU\":"<<cpu()-stepstart<<"}\n";sequences.flush();
  }else terminal=budget.stopped?"UNKNOWN_WHOLE_CPU_LIMIT":"COMPLETE_NO_IN_CURRENT754_SUFFICIENT_PLANE_DOMAIN";
  stepresults<<"{\"step\":"<<step<<",\"source_n\":"<<n<<",\"status\":\""<<(hit?"ACCEPTED_ACTUAL_R4_PASS":terminal)<<"\",\"all754_planes_in_domain\":true,\"degree_impossible_planes\":"<<impossible<<",\"reached_planes\":"<<reachedplanes<<",\"P_tail_checks\":"<<thisP<<",\"exhausted_tails\":"<<completeP<<",\"tail_nodes\":"<<tail.nodes<<",\"blocker_hist\":[";for(int k=0;k<13;k++){if(k)stepresults<<',';stepresults<<hist[k];}stepresults<<"],\"CPU\":"<<cpu()-stepstart<<"}\n";stepresults.flush();
  cout<<"STEP "<<step<<" source="<<n<<" accepted="<<hit<<" plane="<<hitplane<<" P="<<thisP<<" CPU="<<cpu()-stepstart<<" whole="<<cpu()-start<<endl;
  if(!hit)break;if(!budget.check()){terminal="UNKNOWN_WHOLE_CPU_LIMIT_AFTER_ACCEPTED_GRAPH";break;}
 }
 string edgefile="graph_d12_D5_n"+to_string(g.adj.size())+".edges";ofstream edges(out+"/"+edgefile);edges<<g.adj.size()<<' '<<g.m<<'\n';long long ec=0;int maxd=0;for(int u=0;u<int(g.adj.size());u++){maxd=max(maxd,int(g.adj[u].size()));for(int v:g.adj[u])if(u<v){edges<<u<<' '<<v<<'\n';ec++;}}if(ec!=g.m||maxd>12)throw runtime_error("final edgecount/degree");edges.close();
 ofstream result(out+"/NATIVE_RESULT.json");result<<"{\"status\":\""<<terminal<<"\",\"running\":false,\"source_n\":42403,\"accepted_new_graphs\":"<<accepted<<",\"final_n\":"<<g.adj.size()<<",\"final_m\":"<<g.m<<",\"max_degree\":"<<maxd<<",\"final_edgefile\":\""<<edgefile<<"\",\"P_tail_checks\":"<<totalP<<",\"native_CPU\":"<<cpu()-start<<",\"providers_recomputed_from_current_full_graph\":true,\"all754_original_planes_in_domain_each_step\":true,\"tail_all_current_free_except_core\":true,\"old_edges_retained\":true,\"source_D5_inherited\":true,\"complete_Lean\":false,\"further_continuation_authorized\":false}\n";
 cout<<"FINAL "<<terminal<<" accepted="<<accepted<<" n="<<g.adj.size()<<" CPU="<<cpu()-start<<endl;return 0;
 }catch(const exception&e){cerr<<"ERROR "<<e.what()<<endl;return 1;}}
