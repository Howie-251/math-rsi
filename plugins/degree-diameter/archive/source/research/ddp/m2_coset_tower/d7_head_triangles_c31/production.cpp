#include "production_engine.hpp"
#include <sstream>
struct Position{int branch,index,j,other;long long cursor;};
struct Option{array<int,4>s{};int len;};
array<vector<Option>,5> opts;
array<long long,5> branchsize{},branchstart{};
void make_options(){
 vector<int>I;vector<array<int,2>>Q;
 for(int g=1;g<L;g++)if((g/P)%3==0){if(inv[g]==g)I.push_back(g);else if(g<inv[g])Q.push_back({g,inv[g]});}
 assert(I.size()==31&&Q.size()==449);
 for(int a=0;a<31;a++)for(int b=a+1;b<31;b++)for(int c=b+1;c<31;c++)for(int d=c+1;d<31;d++)opts[0].push_back({{I[a],I[b],I[c],I[d]},4});
 for(auto q:Q)for(int a=0;a<31;a++)for(int b=a+1;b<31;b++)opts[1].push_back({{q[0],q[1],I[a],I[b]},4});
 for(int a=0;a<449;a++)for(int b=a+1;b<449;b++)if(Q[a][0]%P||Q[b][0]%P)opts[2].push_back({{Q[a][0],Q[a][1],Q[b][0],Q[b][1]},4});
 for(int a=0;a<31;a++)for(int b=a+1;b<31;b++)opts[3].push_back({{I[a],I[b],0,0},2});
 for(auto q:Q)if(q[0]%P)opts[4].push_back({{q[0],q[1],0,0},2});
 array<int,5>want{31465,208785,100485,465,435};long long total=0;
 for(int b=0;b<5;b++){assert(int(opts[b].size())==want[b]);branchstart[b]=total;branchsize[b]=1LL*opts[b].size()*16*(b<3?1:929);total+=branchsize[b];}
 assert(total==18829360);
}
Gen generators(const Position&pos){
 int a=32+A*pos.j;Gen S{a,inv[a]};
 if(pos.branch>=3){int c=pos.other%P+P+A*(pos.other/P);assert(c!=a);S.push_back(c);S.push_back(inv[c]);}
 auto&o=opts[pos.branch][pos.index];for(int i=0;i<o.len;i++)S.push_back(o.s[i]);assert(S.size()==6);return S;
}
void posout(ostream&o,const Position&p){o<<"{\"branch\":"<<p.branch<<",\"internal_index\":"<<p.index<<",\"anchor_j\":"<<p.j<<",\"second_cross_w1_index\":"<<p.other<<",\"cursor\":"<<p.cursor<<'}';}
void saveprod(const string&base,const Position&p,const Gen&S,const Score&z,const vector<uint32_t>&mask,const string&selection){
 ostringstream row;rowout(row,S,z,mask,int(p.cursor),p.branch,p.index);string rs=row.str();rs.pop_back();
 ofstream o(base+".json");o<<rs<<",\"selection\":\""<<selection<<"\",\"position\":";posout(o,p);o<<"}\n";
 ofstream f(base+".edges");f<<N<<' '<<N*D/2<<'\n';for(int g=0;g<N;g++)for(int j=0;j<D;j++)if(g<adj[g][j])f<<g<<' '<<adj[g][j]<<'\n';
}
struct ProdStat{long long raw=0,bbpass=0;int minbb=INT_MAX;Stat scored;};
void statout(ostream&o,const ProdStat&s){
 o<<"{\"HH_legal_inputs_checked\":"<<s.raw<<",\"BB_pass\":"<<s.bbpass<<",\"minimum_BB_missing\":";if(s.raw)o<<s.minbb;else o<<"null";
 o<<",\"BB_survivor_stats\":";if(s.scored.count)stats(o,s.scored);else o<<"null";o<<'}';
}
int main(int argc,char**argv){
 assert(argc==4);string mode=argv[1],base=argv[2];double limit=stod(argv[3]),start=cpu();init();make_options();
 if(mode=="prepare"){
  ifstream f(base+"/production.calibration.txt");int n;f>>n;assert(n==1400);
  for(int i=0;i<n;i++){Gen S(6);for(int&g:S)f>>g;auto masks=bbmask(S);for(int j=0;j<5;j++){uint32_t expected;f>>expected;assert(expected==masks[j]);}}assert(f);
  ofstream o(base+"/production.iterator_check.json");o<<setprecision(10)<<"{\"status\":\"ACTUAL_ITERATOR_AND_SAVED_BB_MATCHED\",\"actual_branch_internal_counts\":[";
  for(int b=0;b<5;b++){if(b)o<<',';o<<opts[b].size();}o<<"],\"actual_branch_input_counts\":";list(o,branchsize);o<<",\"actual_scope\":18829360,\"saved_BFS_BB_masks_matched\":1400,\"new_graphs\":0,\"new_BFS\":0,\"CPU_seconds\":"<<cpu()-start<<"}\n";
  cout<<"ITERATOR 18829360; all 1400 saved BB masks match; no new graph/BFS."<<endl;return 0;
 }
 assert(mode=="run");
 ProdStat all;array<ProdStat,5> per;array<long long,466>hist{};long long cur=0,best=LLONG_MAX;int minbb=466;Position minimum{},next{};
 double bbtime=0,bfstime=0;string status="COMPLETE_NO_SOLUTION";long long joint=0;ofstream jointfile(base+"/production.block_head_complete.jsonl");
 for(int b=0;b<5;b++)for(int k=0;k<int(opts[b].size());k++)for(int j=0;j<16;j++)for(int ci=(b<3?-1:0);ci<(b<3?0:930);ci++){
  if(b>=3&&ci==P*j+1)continue;
  Position p{b,k,j,ci,cur};next=p;
  if((cur&255)==0&&cpu()-start>=limit){status="CPU_LIMIT";goto done;}
  long long formula=branchstart[b]+(1LL*k*16+j)*(b<3?1:929)+(b<3?0:ci-(ci>P*j+1));assert(formula==cur);
  auto S=generators(p);double t=cpu();auto masks=bbmask(S);int miss=bbmissing(masks);bbtime+=cpu()-t;
  all.raw++;per[b].raw++;hist[miss]++;all.minbb=min(all.minbb,miss);per[b].minbb=min(per[b].minbb,miss);
  if(miss<minbb){minbb=miss;minimum=p;}
  if(!miss){
   all.bbpass++;per[b].bbpass++;t=cpu();build(S);auto z=score(masks,false);bfstime+=cpu()-t;all.scored.add(z);per[b].scored.add(z);
   if(!z.miss[1]&&!z.miss[2]){joint++;jointfile<<"{\"position\":";posout(jointfile,p);jointfile<<",\"graph\":";rowout(jointfile,S,z,masks,int(cur),b,k);jointfile<<"}\n";if(joint==1){jointfile.flush();cout<<"FIRST_COMPLETE_BLOCK_HEAD cursor="<<cur<<" leafmiss="<<z.miss[0]<<endl;}}
   if(z.bad<best){best=z.bad;saveprod(base+"/production.best",p,S,z,masks,"minimum_bad_pairs_among_BB_survivors_in_completed_prefix");cout<<"best cursor="<<cur<<" bad="<<best<<" roots="<<z.miss[0]<<','<<z.miss[1]<<','<<z.miss[2]<<endl;}
   if(!z.bad){cur++;status="D5_CANDIDATE";goto done;}
  }
  cur++;
  if(cur==100000){double elapsed=cpu()-start;ofstream o(base+"/production.first100k.json");o<<setprecision(10)<<"{\"cursor\":"<<cur<<",\"CPU_seconds\":"<<elapsed<<",\"BB_CPU_seconds\":"<<bbtime<<",\"actual_BFS_build_CPU_seconds\":"<<bfstime<<",\"other_CPU_seconds\":"<<elapsed-bbtime-bfstime<<",\"counts\":";statout(o,all);o<<"}\n";cout<<"FIRST_100K CPU="<<elapsed<<" BB="<<bbtime<<" BFS="<<bfstime<<" BBpass="<<all.bbpass<<endl;}
  if(cur%1000000==0)cout<<"progress cursor="<<cur<<" CPU="<<cpu()-start<<" BBpass="<<all.bbpass<<" best="<<best<<" completeBH="<<joint<<endl;
 }
done:
 bool fallback=false;
 if(!all.scored.count&&all.raw){auto S=generators(minimum);auto mask=bbmask(S);build(S);auto z=score(mask,true);saveprod(base+"/production.best",minimum,S,z,mask,"one_minBB_fallback_not_a_bad_pair_optimum");fallback=true;}
 ofstream o(base+"/production.terminal.json");o<<setprecision(10)<<"{\"status\":\""<<status<<"\",\"parent_marked_scope\":35305050,\"safe_16_anchor_scope\":18829360,\"next_cursor\":"<<cur<<",\"next_position\":";
 if(status=="CPU_LIMIT")posout(o,next);else o<<"null";
 o<<",\"CPU_seconds\":"<<cpu()-start<<",\"BB_CPU_seconds\":"<<bbtime<<",\"actual_BFS_build_CPU_seconds\":"<<bfstime<<",\"one_minBB_fallback_scored\":"<<(fallback?"true":"false")<<",\"profile_was_not_prefix\":true,\"counts\":";statout(o,all);
 o<<",\"per_branch\":[";for(int b=0;b<5;b++){if(b)o<<',';statout(o,per[b]);}o<<"],\"BB_missing_histogram\":{";bool first=true;for(int i=0;i<=465;i++)if(hist[i]){if(!first)o<<',';first=false;o<<'\"'<<i<<"\":"<<hist[i];}o<<"}}\n";
 cout<<status<<" cursor="<<cur<<" CPU="<<cpu()-start<<" BBpass="<<all.bbpass<<" best="<<best<<" completeBH="<<joint<<endl;
}
