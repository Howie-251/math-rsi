#include <bits/stdc++.h>
using namespace std;using Row=bitset<256>;
vector<vector<int>> basis(int n){if(n==2)return{{1,0}};vector<vector<int>>z;for(auto a:basis(n-2)){auto b=a;int p=a[n-3];b.resize(n);b[n-2]=p;b[p]=n-2;b[n-3]=n-1;b[n-1]=n-3;z.push_back(b);a.push_back(n-1);a.push_back(n-2);z.push_back(a);}return z;}
bool conn(const vector<int>&a,const vector<int>&b){int x=0,n=a.size();for(int j=1;j<=n/2;++j){x=b[a[x]];if(!x)return j==n/2;}throw runtime_error("bad pairing");}
int main(int argc,char**argv){try{
 if(argc!=3)throw runtime_error("taskfile outputfile");ifstream tasks(argv[1]);ofstream out(argv[2]);string line;int total=0,positive=0;
 while(getline(tasks,line)){if(line.empty())continue;istringstream is(line);int id,t;is>>id>>t;if(t<1||t>4)throw runtime_error("fixed count");vector<pair<int,int>>fixed;set<int>internal;for(int j=0,a,b;j<t;++j){is>>a>>b;if(!is||!internal.insert(a).second||!internal.insert(b).second)throw runtime_error("bad fixed");fixed.emplace_back(a,b);}
  ostringstream ss;ss<<"FOURTEEN_NEW_TYPES_orbit_"<<setw(3)<<setfill('0')<<id;ifstream in(ss.str()+"_pairs.bin",ios::binary);if(!in)throw runtime_error("source");vector<array<int,32>>records;set<int>K;unsigned char raw[20];
  while(in.read((char*)raw,20)){array<int,32>P;P.fill(-1);for(int j=0;j<20;j+=2){P[raw[j]]=raw[j+1];P[raw[j+1]]=raw[j];K.insert(raw[j]);K.insert(raw[j+1]);}records.push_back(P);}
  if(K.size()!=20)throw runtime_error("covered set");for(int x:internal)if(!K.count(x))throw runtime_error("fixed outside K");vector<int>V;int ix[32];fill(ix,ix+32,-1);for(int x:K)if(!internal.count(x)){ix[x]=V.size();V.push_back(x);}int n=V.size(),bound=1<<(n/2-1);auto columns=basis(n);vector<Row>piv(bound);vector<int>selected;int rank=0;
  for(int ri=0;ri<(int)records.size();++ri){auto P=records[ri];array<vector<int>,32>adj;for(int x:K)if(x<P[x]){adj[x].push_back(P[x]);adj[P[x]].push_back(x);}for(auto[a,b]:fixed){adj[a].push_back(b);adj[b].push_back(a);}set<int>seen;vector<int>Q(n,-1);bool good=true;
   for(int s:V)if(!seen.count(s)){int prev=-1,x=s;set<int>walk;
    while(true){if(!walk.insert(x).second){good=false;break;}seen.insert(x);if(x!=s&&ix[x]>=0){Q[ix[s]]=ix[x];Q[ix[x]]=ix[s];break;}int y=-1,count=0;for(int z:adj[x])if(z!=prev){y=z;++count;}if(count!=1){good=false;break;}prev=x;x=y;}
    if(!good)break;
   }
   if(!good||seen.size()!=K.size())continue;Row row;for(int j=0;j<bound;++j)row[j]=conn(Q,columns[j]);for(int j=bound-1;j>=0;--j)if(row[j]){if(piv[j].any())row^=piv[j];else{piv[j]=row;++rank;selected.push_back(ri);break;}}if(rank==bound)break;
  }
  out<<id<<' '<<t;for(auto[a,b]:fixed)out<<' '<<a<<' '<<b;out<<' '<<rank<<' '<<bound;for(int j:selected)out<<' '<<j;out<<'\n';++total;if(rank==bound)++positive;
 }
 cout<<"tested="<<total<<" full_rank="<<positive<<endl;
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
