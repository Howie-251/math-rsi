#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
void ints(ostream&f,const vector<int>&a){f<<'[';for(size_t i=0;i<a.size();i++){if(i)f<<',';f<<a[i];}f<<']';}
int main(int argc,char**argv){
 assert(argc==6);int DEG=stoi(argv[5]);assert(DEG==11||DEG==12);clock_t start=clock();rlimit limit{6,7};setrlimit(RLIMIT_CPU,&limit);
 string mode=argv[1],input=argv[2],pinsfile=argv[3],prefix=argv[4];
 ifstream f(input);int n;long long m;f>>n>>m;vector<vector<int>>g(n);vector<pair<int,int>>edges;edges.reserve(m);
 for(long long i=0;i<m;i++){int u,v;f>>u>>v;g[u].push_back(v);g[v].push_back(u);edges.push_back({u,v});}
 vector<int>pins;ifstream pf(pinsfile);for(int p;pf>>p;)pins.push_back(p);
 vector<int>degrees,blocked;set<int>pinset(pins.begin(),pins.end());assert(pinset.size()==pins.size()&&pins.size()<=size_t(DEG));
 for(int p:pins){assert(0<=p&&p<n);degrees.push_back(g[p].size());if(g[p].size()>=size_t(DEG))blocked.push_back(p);}
 ofstream out(prefix+".json");
 out<<"{\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"pins\":";ints(out,pins);out<<",\"pin_current_degrees\":";ints(out,degrees);
 if(!blocked.empty()){out<<",\"status\":\"DEGREE_INFEASIBLE\",\"blocked\":";ints(out,blocked);out<<",\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";return 0;}
 vector<int>d(n,-1),q(n);int h=0,t=0;for(int p:pins){d[p]=0;q[t++]=p;}
 while(h<t){int u=q[h++];if(d[u]==4)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q[t++]=v;}}
 vector<int>missing;for(int u=0;u<n;u++)if(d[u]<0)missing.push_back(u);
 out<<",\"missing_count\":"<<missing.size()<<",\"covered_count\":"<<n-missing.size()<<",\"missing\":";ints(out,missing);
 if(mode=="verify"||missing.empty()){out<<",\"status\":\""<<(mode=="verify"?"FULL_SELECTED_R4_CHECK_COMPLETE":"PREP_COMPLETE")<<"\",\"exact_anchors\":[]"<<",\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";return 0;}
 assert(mode=="prepare");int T=missing.size(),W=(T+63)/64;
 vector<U>cur(size_t(n)*W),next;
 for(int j=0;j<T;j++)cur[size_t(missing[j])*W+j/64]|=U(1)<<(j%64);
 for(int step=0;step<4;step++){
  next=cur;
  for(auto[u,v]:edges)for(int w=0;w<W;w++){next[size_t(u)*W+w]|=cur[size_t(v)*W+w];next[size_t(v)*W+w]|=cur[size_t(u)*W+w];}
  cur.swap(next);
 }
 map<vector<U>,int>distinct;int eligible=0,zerocover=0;
 for(int u=0;u<n;u++)if(g[u].size()<size_t(DEG)&&!pinset.count(u)){
  eligible++;vector<U>mask(cur.begin()+size_t(u)*W,cur.begin()+size_t(u+1)*W);
  bool any=any_of(mask.begin(),mask.end(),[](U v){return v!=0;});if(!any){zerocover++;continue;}distinct.emplace(move(mask),u);
 }
 vector<pair<int,vector<U>>>rows;for(auto&[mask,u]:distinct)rows.emplace_back(u,mask);sort(rows.begin(),rows.end());
 int K=rows.size();vector<int>representatives;for(auto&r:rows)representatives.push_back(r.first);
 ofstream binary(prefix+".masks.u64.bin",ios::binary);for(auto&r:rows)binary.write((char*)r.second.data(),W*sizeof(U));binary.close();
 vector<U>full(W,~U(0));if(T%64)full.back()=(U(1)<<(T%64))-1;
 vector<int>anchors;bool found=false,exacttwo=(DEG-int(pins.size())>=2);long long firsttested=0;
 for(auto&r:rows)if(r.second==full){anchors={r.first};found=true;break;}
 int KW=(K+63)/64;vector<U>coverers(size_t(T)*KW);vector<int>counts(T);
 for(int i=0;i<K;i++)for(int w=0;w<W;w++){U bits=rows[i].second[w];while(bits){int bit=__builtin_ctzll(bits),target=64*w+bit;coverers[size_t(target)*KW+i/64]|=U(1)<<(i%64);counts[target]++;bits&=bits-1;}}
 vector<int>zeroTargets;for(int j=0;j<T;j++)if(counts[j]==0)zeroTargets.push_back(missing[j]);
 if(!found&&zeroTargets.empty()&&DEG-int(pins.size())>=2){
  vector<int>order(T);iota(order.begin(),order.end(),0);sort(order.begin(),order.end(),[&](int a,int b){return pair(counts[a],missing[a])<pair(counts[b],missing[b]);});
  vector<U>candidate(KW);
  for(int i=0;i<K;i++){
   if((i&127)==0&&double(clock()-start)/CLOCKS_PER_SEC>4.5){exacttwo=false;break;}firsttested++;
   fill(candidate.begin(),candidate.end(),~U(0));if(K%64)candidate.back()=(U(1)<<(K%64))-1;
   for(int w=0;w<i/64;w++)candidate[w]=0;
   if(i%64==63)candidate[i/64]=0;else candidate[i/64]&=~((U(1)<<(i%64+1))-1);
   bool any=true;
   for(int j:order)if(!(rows[i].second[j/64]>>(j%64)&1)){
    any=false;for(int w=0;w<KW;w++){candidate[w]&=coverers[size_t(j)*KW+w];any|=candidate[w]!=0;}if(!any)break;
   }
   if(any){int j=-1;for(int w=0;w<KW;w++)if(candidate[w]){j=64*w+__builtin_ctzll(candidate[w]);break;}if(j>=0){anchors={rows[i].first,rows[j].first};found=true;break;}}
  }
 }
 out<<",\"status\":\"PREP_COMPLETE\",\"eligible_anchors\":"<<eligible<<",\"zero_coverage_anchors_removed\":"<<zerocover
  <<",\"unique_nonzero_masks\":"<<K<<",\"mask_words_per_row\":"<<W<<",\"representatives\":";ints(out,representatives);
 out<<",\"zero_cover_targets\":";ints(out,zeroTargets);out<<",\"exact_one_or_two_found\":"<<(found?"true":"false")
  <<",\"exact_two_complete\":"<<(exacttwo?"true":"false")<<",\"exact_two_first_masks_tested\":"<<firsttested<<",\"exact_anchors\":";ints(out,anchors);
 out<<",\"target_coverage_counts\":";ints(out,counts);out<<",\"mask_bit_order\":\"little target-index bits per nativeu64 row\",\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
}
