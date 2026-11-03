#include "engine.hpp"
#include "scope_tables.hpp"
#include <filesystem>
#include <sstream>
struct Position{int phase,yi,ui,vi,cur;};
Gen gens(const Position&p){int i=PHASE[p.phase][0],j=PHASE[p.phase][1],a=62+A*i,b=NON[p.yi]+61+A*j;return {a,inv[a],b,inv[b],SQ[p.ui]+A*15,NON[p.vi]+A*15};}
void posout(ostream&o,const Position&p){o<<"{\"phase_index\":"<<p.phase<<",\"i\":"<<PHASE[p.phase][0]<<",\"j\":"<<PHASE[p.phase][1]<<",\"y\":"<<NON[p.yi]<<",\"u\":"<<SQ[p.ui]<<",\"v\":"<<NON[p.vi]<<",\"yi\":"<<p.yi<<",\"ui\":"<<p.ui<<",\"vi\":"<<p.vi<<",\"cursor\":"<<p.cur<<'}';}
void saveparams(const string&base,const Position&p,const Gen&S,const Score&z,const vector<uint64_t>&mask,const string&selection){
 ostringstream row;rowout(row,S,z,mask,p.cur,p.phase,0);string s=row.str();s.pop_back();ofstream f(base+".json");f<<s<<",\"root_eccentricities\":";list(f,z.ecc);f<<",\"selection\":\""<<selection<<"\",\"parameters\":";posout(f,p);f<<"}\n";
}
void savegraph(const string&base,const Position&p,const Gen&S,const Score&z,const vector<uint64_t>&mask,const string&selection){
 saveparams(base,p,S,z,mask,selection);ofstream f(base+".edges");f<<N<<' '<<N*D/2<<'\n';for(int g=0;g<N;g++)for(int j=0;j<D;j++)if(g<adj[g][j])f<<g<<' '<<adj[g][j]<<'\n';
}
void cache(const string&base,vector<uint64_t>&mask,Score&z,bool write){
 if(write){ofstream f(base+"/preflight.cache");for(auto m:mask)f<<m<<' ';for(int x:z.miss)f<<x<<' ';for(auto r:z.layer)for(int x:r)f<<x<<' ';for(int x:z.ecc)f<<x<<' ';f<<z.bad<<'\n';}
 else{ifstream f(base+"/preflight.cache");for(auto&m:mask)f>>m;for(int&x:z.miss)f>>x;for(auto&r:z.layer)for(int&x:r)f>>x;for(int&x:z.ecc)f>>x;f>>z.bad;assert(f);}
}
struct Counts{int raw=0,pass=0,minbb=B;Stat scored;};
void counts(ostream&o,const Counts&s){o<<"{\"original_BB_evaluated\":"<<s.raw<<",\"BB_pass\":"<<s.pass<<",\"minimum_BB_missing\":";if(s.raw)o<<s.minbb;else o<<"null";o<<",\"BB_survivor_stats\":";if(s.scored.count)stats(o,s.scored);else o<<"null";o<<'}';}
int main(int argc,char**argv){
 assert(argc==4);string mode=argv[1],base=argv[2];double limit=stod(argv[3]),start=cpu();init();
 assert(vector<int>(SQ,SQ+30)==[](){auto v=powers;sort(v.begin(),v.end());return v;}());
 for(int x=1;x<P;x++){bool q=binary_search(SQ,SQ+30,x);assert(q!=binary_search(NON,NON+30,x));}
 for(int k=0;k<72;k++){assert(PHASE[k][0]>=0&&PHASE[k][0]<=15&&PHASE[k][0]%5!=0&&(PHASE[k][0]+PHASE[k][1])%5==0);}
 Position first{0,0,0,0,0};auto firstS=gens(first);
 if(mode=="preflight"){
  auto copy=firstS;sort(copy.begin(),copy.end());assert(copy.front()>0&&adjacent_find(copy.begin(),copy.end())==copy.end());for(int s:firstS)assert(binary_search(copy.begin(),copy.end(),inv[s]));
  auto mask=bbmask(firstS);build(firstS);auto z=score(mask,true);cache(base,mask,z,true);savegraph(base+"/preflight",first,firstS,z,mask,"one_actual_new_group_and_33bit_BB_sample");
  ofstream o(base+"/preflight.check.json");o<<setprecision(10)<<"{\"status\":\"PASS\",\"all_915_BB_targets_match\":true,\"actual_complete_BFS_roots\":3,\"33bit_masks_in_64bit_storage\":true,\"CPU_seconds\":"<<cpu()-start<<"}\n";
  cout<<"PREFLIGHT PASS roots="<<z.miss[0]<<','<<z.miss[1]<<','<<z.miss[2]<<" BB="<<z.layer[1][1]<<endl;return 0;
 }
 assert(mode=="run");vector<uint64_t> cachedmask(5);Score cached;cache(base,cachedmask,cached,false);
 Counts all;array<Counts,72>per;array<long long,B+1>hist{};int cur=0,minbb=B+1;long long best=LLONG_MAX;Position minpos{},next{};double bbtime=0,bfstime=0;string status="COMPLETE_NO_SOLUTION";
 for(int k=0;k<72;k++)for(int yi=0;yi<30;yi++)for(int ui=0;ui<30;ui++)for(int vi=0;vi<30;vi++){
  Position p{k,yi,ui,vi,cur};next=p;assert(cur==((k*30+yi)*30+ui)*30+vi);
  if((cur&255)==0&&cpu()-start>=limit){status="CPU_LIMIT";goto done;}
  auto S=gens(p);double tm=cpu();auto mask=cur==0?cachedmask:bbmask(S);int m=bbmissing(mask);bbtime+=cpu()-tm;
  all.raw++;per[k].raw++;hist[m]++;all.minbb=min(all.minbb,m);per[k].minbb=min(per[k].minbb,m);
  if(m<minbb){minbb=m;minpos=p;ofstream o(base+"/production.min_BB.parameters.json");posout(o,p);o<<'\n';}
  if(!m){
   all.pass++;per[k].pass++;tm=cpu();Score z;if(cur==0)z=cached;else{build(S);z=score(mask,false);}bfstime+=cpu()-tm;all.scored.add(z);per[k].scored.add(z);
   if(z.bad<best){best=z.bad;if(cur==0){saveparams(base+"/production.best",p,S,z,mask,"minimum_bad_pairs_among_actual_BB_survivors");filesystem::copy_file(base+"/preflight.edges",base+"/production.best.edges",filesystem::copy_options::overwrite_existing);}else savegraph(base+"/production.best",p,S,z,mask,"minimum_bad_pairs_among_actual_BB_survivors");cout<<"best cursor="<<cur<<" bad="<<best<<" roots="<<z.miss[0]<<','<<z.miss[1]<<','<<z.miss[2]<<endl;}
   if(!z.bad){cur++;status="D5_CANDIDATE";goto done;}
  }
  cur++;
  if(cur==10000){double elapsed=cpu()-start;ofstream o(base+"/production.first10000.json");o<<setprecision(10)<<"{\"cursor\":"<<cur<<",\"CPU_seconds\":"<<elapsed<<",\"BB_CPU_seconds\":"<<bbtime<<",\"actual_BFS_build_CPU_seconds\":"<<bfstime<<",\"other_CPU_seconds\":"<<elapsed-bbtime-bfstime<<",\"counts\":";counts(o,all);o<<"}\n";cout<<"FIRST10000 CPU="<<elapsed<<" BBpass="<<all.pass<<" minBB="<<minbb<<endl;}
  if(cur%250000==0)cout<<"progress cursor="<<cur<<" CPU="<<cpu()-start<<" BBpass="<<all.pass<<" minBB="<<minbb<<endl;
 }
done:
 bool fallback=false;
 if(!all.scored.count&&all.raw){auto S=gens(minpos);auto mask=bbmask(S);Score z;if(minpos.cur==0){z=cached;saveparams(base+"/production.best",minpos,S,z,mask,"one_minimum_BB_fallback_not_bad_pair_optimum");filesystem::copy_file(base+"/preflight.edges",base+"/production.best.edges",filesystem::copy_options::overwrite_existing);}else{build(S);z=score(mask,true);savegraph(base+"/production.best",minpos,S,z,mask,"one_minimum_BB_fallback_not_bad_pair_optimum");}fallback=true;}
 ofstream o(base+"/production.terminal.json");o<<setprecision(10)<<"{\"status\":\""<<status<<"\",\"raw_HH_scope\":729000000,\"scaled_scope\":24300000,\"safe_sign_scope\":12960000,\"formal_word_pass_scope\":1944000,\"next_cursor\":"<<cur<<",\"next_position\":";if(status=="CPU_LIMIT")posout(o,next);else o<<"null";
 o<<",\"CPU_seconds\":"<<cpu()-start<<",\"BB_CPU_seconds\":"<<bbtime<<",\"BB_survivor_BFS_build_CPU_seconds\":"<<bfstime<<",\"one_minBB_fallback_scored\":"<<(fallback?"true":"false")<<",\"preflight_result_cached_at_cursor0\":true,\"counts\":";counts(o,all);o<<",\"per_phase\":[";for(int k=0;k<72;k++){if(k)o<<',';counts(o,per[k]);}o<<"],\"BB_missing_histogram\":{";bool comma=false;for(int i=0;i<=B;i++)if(hist[i]){if(comma)o<<',';comma=true;o<<'\"'<<i<<"\":"<<hist[i];}o<<"}}\n";
 cout<<status<<" cursor="<<cur<<" CPU="<<cpu()-start<<" BBpass="<<all.pass<<" minBB="<<minbb<<endl;
}
