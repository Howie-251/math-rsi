#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
struct Row {int ord,a,b,v,reach,D,far,first;bool inherited;vector<int> hist;};
int main(int argc,char**argv){
 assert(argc==4);string input=argv[1],out=argv[2];double budget=stod(argv[3]);clock_t start=clock();
 ifstream f(input,ios::binary);uint32_t n;f.read((char*)&n,4);assert(n==20400);
 vector<vector<uint32_t>> data(8,vector<uint32_t>(n));for(auto&r:data)f.read((char*)r.data(),4*n);assert(f);
 auto &alpha=data[0],&beta=data[7];
 vector<vector<uint32_t>> ap(16,vector<uint32_t>(n));iota(ap[0].begin(),ap[0].end(),0);
 for(int k=1;k<16;k++)for(int u=0;u<int(n);u++)ap[k][u]=alpha[ap[k-1][u]];
 vector<Row> rows={ {28,1,4,4,int(n),11,31,-1,true,{}},
                   {31,1,5,1,int(n),11,392,-1,true,{}},
                   {135,5,4,3,int(n),11,16,-1,true,{}} };
 set<int>skip={28,31,135};int tested=0,hit=-1,last=-1;string status="COMPLETE_213_NEW_PLUS3_INHERITED_NO_HIT";
 vector<array<uint32_t,4>> adj(n);vector<uint32_t>second(n),invsecond(n);vector<int>d(n),q(n);
 int aa[4]={1,3,5,7};
 for(int ia=0;ia<4&&hit<0;ia++)for(int b=0;b<=8&&hit<0;b++)for(int v=0;v<6&&hit<0;v++){
  int ord=ia*54+b*6+v;if(skip.count(ord))continue;
  if(double(clock()-start)/CLOCKS_PER_SEC>budget-.10){status="UNKNOWN_CPU_LIMIT";goto done;}
  int a=aa[ia];last=ord;auto&nv=data[1+v];
  for(int u=0;u<int(n);u++){second[u]=nv[beta[ap[b][u]]];invsecond[second[u]]=u;}
  bool valid=true;
  for(int u=0;u<int(n);u++){
   adj[u]={ap[a][u],ap[16-a][u],second[u],invsecond[u]};auto r=adj[u];sort(r.begin(),r.end());
   if(r[0]==r[1]||r[1]==r[2]||r[2]==r[3]||binary_search(r.begin(),r.end(),u))valid=false;
  }
  if(!valid){status="THEORY_OR_IMPLEMENTATION_MISMATCH_NONSIMPLE";goto done;}
  fill(d.begin(),d.end(),-1);int lo=0,hi=1;q[0]=0;d[0]=0;int ecc=0;
  while(lo<hi){int u=q[lo++];for(auto w:adj[u])if(d[w]<0){d[w]=d[u]+1;ecc=max(ecc,d[w]);q[hi++]=w;}}
  if(hi!=int(n)){status="THEORY_OR_IMPLEMENTATION_MISMATCH_DISCONNECTED";goto done;}
  vector<int>hist(ecc+1);int far=0,first=-1;for(int u=0;u<int(n);u++){hist[d[u]]++;if(d[u]>10){far++;if(first<0)first=u;}}
  rows.push_back({ord,a,b,v,hi,ecc,far,first,false,hist});tested++;
  if(ecc<=10){
   hit=ord;status="FIRST_COMPLETE_NEW_D4_D10_GRAPH";
   ofstream edges(out+"/graph_d4_D10_n20400.edges");edges<<n<<' '<<2*n<<'\n';
   for(int u=0;u<int(n);u++)for(auto w:adj[u])if(u<int(w))edges<<u<<' '<<w<<'\n';
   ofstream perms(out+"/HIT_PERMUTATIONS.u32le.bin",ios::binary);
   perms.write((char*)ap[a].data(),4*n);perms.write((char*)ap[16-a].data(),4*n);
   perms.write((char*)second.data(),4*n);perms.write((char*)invsecond.data(),4*n);
   ofstream distances(out+"/HIT_ROOT0_DISTANCES.u8.bin",ios::binary);for(int z:d){uint8_t b=z;distances.write((char*)&b,1);}
   cout<<"HIT ordinal="<<ord<<" a="<<a<<" b="<<b<<" vindex="<<v<<" D="<<ecc<<endl;
  }
 }
 done:
 sort(rows.begin(),rows.end(),[](auto&a,auto&b){return a.ord<b.ord;});
 ofstream j(out+"/NATIVE_RESULT.json");j<<"{\"status\":\""<<status<<"\",\"fixed_cases\":216,\"inherited_D11_cases\":3,\"new_cases_tested\":"<<tested
 <<",\"untested_new_cases\":"<<213-tested<<",\"last_new_ordinal\":"<<last<<",\"hit_ordinal\":"<<hit
 <<",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"rows\":[";
 bool sep=false;for(auto&r:rows){if(sep)j<<',';sep=true;j<<"{\"ordinal\":"<<r.ord<<",\"a\":"<<r.a<<",\"b\":"<<r.b<<",\"v_index\":"<<r.v
 <<",\"inherited\":"<<(r.inherited?"true":"false")<<",\"n\":"<<n<<",\"m\":"<<2*n<<",\"degree\":4,\"connected\":true,\"global_D\":"<<r.D
 <<",\"root_reached\":"<<r.reach<<",\"root_targets_outside_R10\":"<<r.far<<",\"first_target_outside_R10\":";
 if(r.inherited)j<<"null";else j<<r.first;j<<",\"root_distance_histogram\":[";
 for(size_t k=0;k<r.hist.size();k++){if(k)j<<',';j<<r.hist[k];}j<<"]}";}
 j<<"]}\n";
}
