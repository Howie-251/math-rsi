#include <bits/stdc++.h>
using namespace std;
using Ed=pair<int,int>;using Mat=vector<Ed>;
vector<Mat> cs,rs;vector<array<int,32>> group;
void pairings(vector<int>v,Mat &cur,vector<Mat>&out){if(v.empty()){auto f=cur;sort(f.begin(),f.end());out.push_back(f);return;}int a=v[0];for(int j=1;j<(int)v.size();j++){int b=v[j];auto w=v;w.erase(w.begin()+j);w.erase(w.begin());cur.push_back({a,b});pairings(w,cur,out);cur.pop_back();}}
Mat transform(const Mat&f,const array<int,32>&t){Mat r;for(auto[a,b]:f){int u=t[a],v=t[b];if(u>v)swap(u,v);r.push_back({u,v});}sort(r.begin(),r.end());return r;}
int main(){vector<int>C={16,17,18,20,24,27,29,30};set<int>H={0,3,5,6,8,15,23,25,26,28};vector<int>R;for(int x=0;x<32;x++)if(!H.count(x)&&find(C.begin(),C.end(),x)==C.end())R.push_back(x);assert(R.size()==14);
 array<int,3>p={0,1,2};do{array<int,32>t;for(int x=0;x<32;x++){t[x]=x&24;for(int i=0;i<3;i++)t[x]|=((x>>i)&1)<<p[i];}group.push_back(t);}while(next_permutation(p.begin(),p.end()));
 Mat cur;pairings(C,cur,cs);pairings(R,cur,rs);assert(cs.size()==105&&rs.size()==135135);sort(cs.begin(),cs.end());
 ofstream out("A10_ORBIT2_canonical_inputs.bin",ios::binary),report("A10_ORBIT2_canonical_counts.json");assert(out&&report);uint64_t total=0,weighted=0;int cores=0;report<<"{\"status\":\"CANONICAL_DOMAIN_GENERATED_CYCLE_CERTIFICATES_PENDING\",\"record_bytes\":22,\"rows\":[";
 for(auto &f:cs){bool canonical=true;vector<int>stab;for(int g=0;g<6;g++){auto v=transform(f,group[g]);if(v<f)canonical=false;if(v==f)stab.push_back(g);}if(!canonical)continue;uint64_t count=0,weight=0;
 for(auto &r:rs){bool keep=true;int fixed=0;for(int g:stab){auto v=transform(r,group[g]);if(v<r){keep=false;break;}if(v==r)fixed++;}if(!keep)continue;assert(fixed>0&&6%fixed==0);count++;weight+=6/fixed;for(auto[a,b]:f){out.put(char(a));out.put(char(b));}for(auto[a,b]:r){out.put(char(a));out.put(char(b));}}
 if(cores++)report<<',';report<<"{\"C_matching\":[";for(int j=0;j<4;j++){if(j)report<<',';report<<'['<<f[j].first<<','<<f[j].second<<']';}report<<"],\"C_orbit_size\":"<<6/stab.size()<<",\"C_stabilizer_size\":"<<stab.size()<<",\"canonical_R_matchings\":"<<count<<",\"weighted_full_matchings\":"<<weight<<'}';total+=count;weighted+=weight;
 }
 assert(cores==23&&total==2366577&&weighted==14189175);report<<"],\"C_orbits\":"<<cores<<",\"canonical_records\":"<<total<<",\"weighted_matching_cover\":"<<weighted<<",\"cycle_claimed\":false}\n";cout<<"records="<<total<<" weighted="<<weighted<<" bytes="<<22*total<<endl;
}
