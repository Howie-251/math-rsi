#include <bits/stdc++.h>
using namespace std;using Row=bitset<1024>;
vector<vector<int>> basis(int n){if(n==2)return{{1,0}};vector<vector<int>>z;for(auto a:basis(n-2)){auto b=a;int p=a[n-3];b.resize(n);b[n-2]=p;b[p]=n-2;b[n-3]=n-1;b[n-1]=n-3;z.push_back(b);a.push_back(n-1);a.push_back(n-2);z.push_back(a);}return z;}
bool conn(const vector<int>&a,const vector<int>&b){int x=0,n=a.size();for(int j=1;j<=n/2;++j){x=b[a[x]];if(!x)return j==n/2;}throw runtime_error("bad pairing");}
int main(){try{
 ifstream tasks("SIXTEEN_SMALLCUT_tasks.txt");ofstream out("SIXTEEN_SMALLCUT_probe.tsv"),family("SIXTEEN_SMALLCUT_avoidpair.tsv");string line;int positive=0,total=0;
 while(getline(tasks,line)){istringstream is(line);int id,n,t;string pre;is>>id>>pre>>n>>t;vector<pair<int,int>>fixed;set<int>internal;
  for(int j=0,a,b;j<t;++j){is>>a>>b;if(!internal.insert(a).second||!internal.insert(b).second)throw runtime_error("fixed overlap");fixed.emplace_back(a,b);}
  ifstream in(pre+"_pairs.bin",ios::binary);vector<array<int,32>>records;set<int>K;vector<unsigned char>raw(n);
  while(in.read((char*)raw.data(),n)){array<int,32>P;P.fill(-1);for(int j=0;j<n;j+=2){P[raw[j]]=raw[j+1];P[raw[j+1]]=raw[j];K.insert(raw[j]);K.insert(raw[j+1]);}records.push_back(P);}
  if((int)K.size()!=n)throw runtime_error("source size");for(int x:internal)if(!K.count(x))throw runtime_error("outside K");
  vector<int>V;int ix[32];fill(ix,ix+32,-1);for(int x:K)if(!internal.count(x)){ix[x]=V.size();V.push_back(x);}int bound=1<<((int)V.size()/2-1);auto columns=basis(V.size());vector<Row>piv(bound);int rank=0;vector<int>selected;vector<pair<int,vector<int>>>allq;
  for(int ri=0;ri<(int)records.size();++ri){auto P=records[ri];array<vector<int>,32>adj;for(int x:K)if(x<P[x]){adj[x].push_back(P[x]);adj[P[x]].push_back(x);}for(auto[a,b]:fixed){adj[a].push_back(b);adj[b].push_back(a);}set<int>seen;vector<int>Q(V.size(),-1);bool good=true;
   for(int s:V)if(!seen.count(s)){int prev=-1,x=s;set<int>walk;while(true){if(!walk.insert(x).second){good=false;break;}seen.insert(x);if(x!=s&&ix[x]>=0){Q[ix[s]]=ix[x];Q[ix[x]]=ix[s];break;}int y=-1,count=0;for(int z:adj[x])if(z!=prev){y=z;++count;}if(count!=1){good=false;break;}prev=x;x=y;}if(!good)break;}
   if(!good||seen.size()!=K.size())continue;allq.push_back({ri,Q});Row row;for(int j=0;j<bound;++j)row[j]=conn(Q,columns[j]);for(int j=bound-1;j>=0;--j)if(row[j]){if(piv[j].any())row^=piv[j];else{piv[j]=row;++rank;selected.push_back(ri);break;}}if(rank==bound)break;
  }
  out<<id<<' '<<rank<<' '<<bound;for(int j:selected)out<<' '<<j;out<<'\n';++total;if(rank==bound)++positive;cerr<<id<<' '<<rank<<'/'<<bound<<'\n';
  map<pair<int,int>,int>counts;for(auto&[ri,Q]:allq)for(int j=0;j<(int)V.size();++j)if(j<Q[j])++counts[{j,Q[j]}];
  int smaller=bound/2;auto smallcols=basis(V.size()-2);
  for(auto [pair,count]:counts)if(count>=smaller){auto[a,b]=pair;vector<int>VV;int jj[32];fill(jj,jj+32,-1);for(int j=0;j<(int)V.size();++j)if(j!=a&&j!=b){jj[j]=VV.size();VV.push_back(j);}vector<Row>pp(smaller);int rr=0;vector<int>ss;
   for(auto&[ri,Q]:allq)if(Q[a]==b){vector<int>small;for(int x:VV)small.push_back(jj[Q[x]]);Row row;for(int j=0;j<smaller;++j)row[j]=conn(small,smallcols[j]);for(int j=smaller-1;j>=0;--j)if(row[j]){if(pp[j].any())row^=pp[j];else{pp[j]=row;++rr;ss.push_back(ri);break;}}if(rr==smaller)break;}
   family<<id<<' '<<V[a]<<' '<<V[b]<<' '<<rr<<' '<<smaller;for(int ri:ss)family<<' '<<ri;family<<'\n';
  }
 }
 cout<<"tested="<<total<<" full_rank="<<positive<<endl;
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
