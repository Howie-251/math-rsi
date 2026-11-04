#include <bits/stdc++.h>
using namespace std;
using Row=bitset<256>;
vector<vector<int>> basis(int n){
 if(n==2)return {{1,0}};vector<vector<int>> out;
 for(auto a:basis(n-2)){auto b=a;int p=a[n-3];b.resize(n);b[n-2]=p;b[p]=n-2;b[n-3]=n-1;b[n-1]=n-3;out.push_back(b);a.push_back(n-1);a.push_back(n-2);out.push_back(a);}return out;
}
bool conn(const vector<int>&a,const vector<int>&b){int x=0;for(int j=1;j<=9;++j){x=b[a[x]];if(!x)return j==9;}throw runtime_error("bad pair");}
int main(){try{
 auto columns=basis(18);ifstream tasks("FOURTEEN_FIXED_EDGE_tasks.txt");ofstream out("FOURTEEN_FIXED_EDGE_probe.tsv");int id,a,b,total=0,positive=0;
 while(tasks>>id>>a>>b){ostringstream ss;ss<<"FOURTEEN_NEW_TYPES_orbit_"<<setw(3)<<setfill('0')<<id;ifstream in(ss.str()+"_pairs.bin",ios::binary);if(!in)throw runtime_error("missing source");
  vector<vector<int>> records;unsigned char raw[20];set<int>K;
  while(in.read((char*)raw,20)){vector<int> P(32,-1);for(int j=0;j<20;j+=2){P[raw[j]]=raw[j+1];P[raw[j+1]]=raw[j];K.insert(raw[j]);K.insert(raw[j+1]);}records.push_back(P);}
  if(K.size()!=20||!K.count(a)||!K.count(b))throw runtime_error("bad covered set");
  vector<int>V;int ix[32];fill(ix,ix+32,-1);for(int x:K)if(x!=a&&x!=b){ix[x]=V.size();V.push_back(x);}array<Row,256>piv;int rank=0;vector<int>selected;
  for(int ri=0;ri<(int)records.size();++ri){auto P=records[ri];if(P[a]==b)continue;int c=P[a],d=P[b];P[c]=d;P[d]=c;vector<int>Q(18);for(int j=0;j<18;++j){Q[j]=ix[P[V[j]]];if(Q[j]<0)throw runtime_error("compression");}Row row;for(int j=0;j<256;++j)row[j]=conn(Q,columns[j]);
   for(int j=255;j>=0;--j)if(row[j]){if(piv[j].any())row^=piv[j];else{piv[j]=row;++rank;selected.push_back(ri);break;}}
   if(rank==256)break;
  }
  out<<id<<' '<<a<<' '<<b<<' '<<rank;for(int i:selected)out<<' '<<i;out<<'\n';++total;if(rank==256)++positive;
 }
 cout<<"tested="<<total<<" full_rank="<<positive<<endl;
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
