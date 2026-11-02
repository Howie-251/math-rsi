#include<array>
#include<vector>
#include<algorithm>
#include<fstream>
#include<iostream>
#include<ctime>
#include<cstdint>
#include<cassert>
using namespace std;
using U=uint64_t;using Mask=array<U,4>;
int n,m,cap;vector<vector<int>> oldg;vector<pair<int,int>> es;
vector<int> bfs(const vector<vector<int>>&g,int root,vector<int>*parent=nullptr,int limit=100000){vector<int>d(g.size(),-1),q;q.reserve(g.size());d[root]=0;q.push_back(root);if(parent)parent->assign(g.size(),-1);for(size_t k=0;k<q.size();++k){int u=q[k];if(d[u]>=limit)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;if(parent)(*parent)[v]=u;q.push_back(v);}}return d;}
vector<int> path(const vector<int>&p,int v){vector<int>r;while(v>=0){r.push_back(v);v=p[v];}reverse(r.begin(),r.end());return r;}
void arr(ostream&f,const vector<int>&a){f<<'[';for(int i=0;i<int(a.size());++i){if(i)f<<',';f<<a[i];}f<<']';}
int main(){double start=double(clock())/CLOCKS_PER_SEC;ifstream in("SOURCE_CANONICAL.edges");in>>n>>m>>cap;assert(n<256);oldg.resize(n);es.resize(m);for(auto&e:es){in>>e.first>>e.second;oldg[e.first].push_back(e.second);oldg[e.second].push_back(e.first);}assert(in);
 Mask full{};for(int v=0;v<n;++v)full[v/64]|=U(1)<<(v%64);vector<Mask>R(n);for(int u=0;u<n;++u){auto d=bfs(oldg,u,nullptr,3);for(int v=0;v<n;++v)if(d[v]>=0)R[u][v/64]|=U(1)<<(v%64);}
 ofstream cache("SOURCE_R3_SUPPORTS.txt");cache<<n<<" 4\n";for(int u=0;u<n;++u){cache<<u;for(auto x:R[u])cache<<' '<<x;cache<<'\n';}
 long raw=0,overlap=0,checked=0,newpass=0,oldfail=0,oldroots=0;int best=0;bool complete=true,hit=false,diagnosed=false;int hi=-1,hj=-1;vector<pair<int,int>> hit_edges;vector<pair<int,int>> hitstats;
 ofstream rows("ALL_CUTPAIR_RESULTS.tsv");rows<<"edgei\tedgej\tnewroot_R4\tfirst_bad_oldroot\tfirst_bad_target\n";
 for(int i=0;i<m&&!hit&&complete;++i)for(int j=i+1;j<m;++j){if((raw&1023)==0&&double(clock())/CLOCKS_PER_SEC-start>7){complete=false;break;}++raw;auto[a,b]=es[i];auto[c,d]=es[j];if(a==c||a==d||b==c||b==d){++overlap;continue;}++checked;Mask cover{};int count=0;for(int k=0;k<4;++k){cover[k]=R[a][k]|R[b][k]|R[c][k]|R[d][k];count+=__builtin_popcountll(cover[k]);}best=max(best,count);if(cover!=full){rows<<i<<'\t'<<j<<"\t0\t-1\t-1\n";continue;}++newpass;
 auto g=oldg;g.push_back({});vector<int>P={a,b,c,d};auto erase_edge=[&](int u,int v){auto it=find(g[u].begin(),g[u].end(),v);assert(it!=g[u].end());g[u].erase(it);};erase_edge(a,b);erase_edge(b,a);erase_edge(c,d);erase_edge(d,c);for(int p:P){g[p].push_back(n);g[n].push_back(p);}for(auto&v:g)assert(v.size()<=size_t(cap));
 vector<int>order=P;for(int u=0;u<n;++u)if(find(P.begin(),P.end(),u)==P.end())order.push_back(u);bool good=true;int br=-1,bt=-1;vector<pair<int,int>> stats;
 for(int root:order){vector<int>parent;auto dd=bfs(g,root,&parent);++oldroots;int bad=-1,ecc=0;for(int v=0;v<=n;++v){ecc=max(ecc,dd[v]);if(dd[v]<0||dd[v]>4){bad=v;break;}}stats.push_back({root,ecc});if(bad>=0){++oldfail;good=false;br=root;bt=bad;if(!diagnosed){diagnosed=true;vector<int>op;auto od=bfs(oldg,root,&op);ofstream w("FIRST_OLD_FAILURE.json");w<<"{\"edgeindices\":["<<i<<','<<j<<"],\"cuts\":[["<<a<<','<<b<<"],["<<c<<','<<d<<"]],\"newroot_cover_pass\":true,\"oldroot\":"<<root<<",\"target\":"<<bad<<",\"newdistance\":"<<dd[bad]<<",\"source_distance\":"<<(bad<n?od[bad]:-1)<<",\"newroute\":";arr(w,path(parent,bad));w<<",\"one_source_route\":";arr(w,path(op,bad));w<<"}\n";}break;}}
 rows<<i<<'\t'<<j<<"\t1\t"<<br<<'\t'<<bt<<'\n';
 if(good){auto dd=bfs(g,n);assert(all_of(dd.begin(),dd.end(),[](int x){return x>=0&&x<=4;}));stats.push_back({n,*max_element(dd.begin(),dd.end())});hit=true;hi=i;hj=j;hitstats=stats;for(int u=0;u<=n;++u)for(int v:g[u])if(u<v)hit_edges.push_back({u,v});break;}
 }
 long expected=long(m)*(m-1)/2;for(auto&v:oldg)expected-=long(v.size())*(v.size()-1)/2;
 if(complete&&!hit)assert(checked==expected);
 if(hit){ofstream e("CANDIDATE.edges");e<<n+1<<' '<<hit_edges.size()<<'\n';for(auto[u,v]:hit_edges)e<<u<<' '<<v<<'\n';ofstream p("HIT_PARAMETERS.json");p<<"{\"n\":"<<n+1<<",\"m\":"<<hit_edges.size()<<",\"maxdegree\":"<<cap<<",\"cutindices\":["<<hi<<','<<hj<<"],\"cuts\":[["<<es[hi].first<<','<<es[hi].second<<"],["<<es[hj].first<<','<<es[hj].second<<"]],\"producer_roots\":"<<n+1<<",\"producer_D4\":true,\"fresh_Lean_ARIS\":\"PENDING\"}\n";ofstream t("PRODUCER_ROOT_STATS.tsv");for(auto[u,ecc]:hitstats)t<<u<<'\t'<<ecc<<'\n';}
 ofstream r("NATIVE_RESULT.json");r<<"{\"status\":\""<<(hit?"FULL_GRAPH_HIT_PRODUCER_PASS_PENDING_FRESH":complete?"COMPLETE_NO_ALL_FIXED_SOURCE_TWO_CUT_STAR":"UNKNOWN_NATIVE_CPU_CAP")<<"\",\"raw_edgepairs\":"<<raw<<",\"shared_endpoint_pairs\":"<<overlap<<",\"legal_pairs_checked\":"<<checked<<",\"domain_expected\":"<<expected<<",\"domain_complete\":"<<(complete&&!hit?"true":"false")<<",\"newroot_R4_pass\":"<<newpass<<",\"candidate_oldroot_fail\":"<<oldfail<<",\"candidate_oldroot_BFS\":"<<oldroots<<",\"source_depth3_support_queries\":"<<n<<",\"source_singlepair_counterexample_query\":"<<(diagnosed?1:0)<<",\"source_D4_revalidation_BFS\":0,\"maximum_newroot_oldpoint_coverage\":"<<best<<",\"full_hit\":"<<(hit?"true":"false")<<",\"CPU\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";
 cout<<(hit?"HIT":complete?"COMPLETE_NO":"UNKNOWN")<<" legal="<<checked<<" newrootpass="<<newpass<<" oldfail="<<oldfail<<" CPU="<<double(clock())/CLOCKS_PER_SEC-start<<endl;
}
