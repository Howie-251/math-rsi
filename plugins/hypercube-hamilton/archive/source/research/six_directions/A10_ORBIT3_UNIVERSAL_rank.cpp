#include <bits/stdc++.h>
using namespace std;
using Mat=array<unsigned char,22>;
vector<vector<int>> make_basis(int n){
 if(n==2)return {{1,0}};
 vector<vector<int>> out;
 for(auto m:make_basis(n-2)){
  auto zero=m;int partner=m[n-3];zero.resize(n);
  zero[n-2]=partner;zero[partner]=n-2;zero[n-3]=n-1;zero[n-1]=n-3;
  out.push_back(zero);
  m.push_back(n-1);m.push_back(n-2);out.push_back(m);
 }
 return out;
}
bool connected(const Mat &a,const vector<int>&b){
 // Follow alternating edges; one component contains all vertices iff
 // 11 iterations return to the initial vertex for the first time.
 int u=0;
 for(int k=1;k<=11;k++){
  u=b[a[u]];
  if(u==0)return k==11;
 }
 throw runtime_error("invalid involution");
}
int main(int argc,char**argv){
 if(argc!=3)return 2;
 vector<int>K={3,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,28,31};
 int idx[32];fill(idx,idx+32,-1);for(int i=0;i<22;i++)idx[K[i]]=i;
 auto X=make_basis(22);if(X.size()!=1024)return 3;
 // Check the permutation submatrix exactly (basis partner=complement).
 for(int a=0;a<1024;a++){Mat m;copy(X[a].begin(),X[a].end(),m.begin());
  for(int b=0;b<1024;b++)if(connected(m,X[b])!=(b==(a^1023)))return 4;
 }
 cerr<<"basis submatrix PASS\n";
 ifstream in(argv[1],ios::binary);if(!in)return 5;
 array<bitset<1024>,1024> pivots,combos;
 vector<bitset<1024>> originalrows;
 vector<array<char,22>> originalmatchings;
 vector<int>selected;int row=0;char raw[22];
 while(in.read(raw,22)){
  Mat m;m.fill(255);for(int i=0;i<22;i+=2){
   int a=(unsigned char)raw[i],b=(unsigned char)raw[i+1];
   if(a>=32||b>=32||idx[a]<0||idx[b]<0||a==b)return 6;
   if(m[idx[a]]!=255||m[idx[b]]!=255)return 7;
   m[idx[a]]=idx[b];m[idx[b]]=idx[a];
  }
  bitset<1024>v;for(int a=0;a<1024;a++)v[a]=connected(m,X[a]);
  auto original=v;bitset<1024>combo;
  if(selected.size()<1024)combo[selected.size()]=1;
  for(int a=1023;a>=0;a--)if(v[a]){
   if(pivots[a].any()){v^=pivots[a];combo^=combos[a];}
   else{pivots[a]=v;combos[a]=combo;selected.push_back(row);
    originalrows.push_back(original);array<char,22>rec;copy(raw,raw+22,rec.begin());originalmatchings.push_back(rec);break;}
  }
  row++;if(row%2000==0)cerr<<"rows="<<row<<" rank="<<selected.size()<<"\n";
 }
 if(!in.eof()||in.gcount()!=0)return 8;
 ofstream out(argv[2]);out<<"{\"status\":\"RANK_COMPUTED\",\"rows\":"<<row
 <<",\"rank_GF2\":"<<selected.size()<<",\"full_rank_sufficient_certificate\":"
 <<(selected.size()==1024?"true":"false")<<",\"selected_row_indices\":[";
 for(size_t i=0;i<selected.size();i++){if(i)out<<',';out<<selected[i];}out<<"]}\n";
 cout<<"rows="<<row<<" rank="<<selected.size()<<"\n";
 string prefix=string(argv[2]);prefix=prefix.substr(0,prefix.size()-5);
 auto dumpbits=[](ofstream&f,const bitset<1024>&b){for(int j=0;j<128;j++){unsigned char c=0;for(int k=0;k<8;k++)if(b[8*j+k])c|=1<<k;f.put(char(c));}};
 ofstream mat(prefix+"_matrix.bin",ios::binary),sel(prefix+"_selected_pairs.bin",ios::binary),
  tri(prefix+"_pivots.bin",ios::binary),comb(prefix+"_combos.bin",ios::binary),cols(prefix+"_columns.bin",ios::binary);
 for(size_t i=0;i<originalrows.size();i++){dumpbits(mat,originalrows[i]);sel.write(originalmatchings[i].data(),22);}
 for(int i=0;i<1024;i++){dumpbits(tri,pivots[i]);dumpbits(comb,combos[i]);
  vector<pair<int,int>> edges;for(int j=0;j<22;j++)if(j<X[i][j])edges.push_back({K[j],K[X[i][j]]});sort(edges.begin(),edges.end());
  for(auto[a,b]:edges){cols.put(char(a));cols.put(char(b));}
 }
}
