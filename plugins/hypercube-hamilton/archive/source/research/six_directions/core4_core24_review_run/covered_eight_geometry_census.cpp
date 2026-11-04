// Exhaustive hole geometry only. No matching feasibility or P6 conclusion.
// g++ -O3 -std=c++17 covered_eight_geometry_census.cpp -o covered_eight_geometry_census.exe
// Usage: executable OUTPUT_DIRECTORY
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
int pc(unsigned x){return __builtin_popcount(x);}
constexpr bool good[4][5]={{false,true,true,false,false},
 {false,true,true,true,false},{false,false,true,true,true},
 {false,false,false,true,false}};
using Geometry=array<unsigned char,7>;
struct Entry{U count=0;Geometry representative{};};
void geom(ostream&out,const Geometry&g){
 out<<"{\"Z\":["<<int(g[0])<<","<<int(g[1])<<","<<int(g[2])<<"],\"W\":[";
 for(int i=3;i<7;i++){if(i>3)out<<",";out<<int(g[i]);}out<<"]}";
}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 string dir=argv[1];ofstream out(dir+"/covered_eight_geometry_census.json");
 if(!out)return 3;
 out<<"{\"scope\":\"all normalized covered-target hole geometries; no matching feasibility claim\","
 <<"\"root\":0,\"record_format\":\"7 unsigned bytes: sorted Z[3], sorted W[4]; target in filename\","
 <<"\"review_independence\":\"same-family\",\"acceptance_status\":\"provisional\",\"p6_proved\":false,"
 <<"\"targets\":[";
 bool comma=false;
 for(int v:{1,7,31}){
  U total=0,residual=0,none_near=0;
  array<U,20> rowhist{};array<U,7> splithist{};
  map<int,Entry> signatures;map<U,Entry> patterns;
  Geometry no_near_rep{};bool have_no_near=false;
  string filename="covered_eight_residual_"+to_string(v)+".bin";
  ofstream records(dir+"/"+filename,ios::binary);if(!records)return 4;
  vector<int> even,odd;
  for(int x=1;x<64;x++)if(pc(x)%2==0)even.push_back(x);
  for(int x=0;x<64;x++)if(pc(x)%2==1 && x!=v)odd.push_back(x);
  assert(even.size()==31 && odd.size()==31);
  for(int i=0;i<31;i++)for(int j=i+1;j<31;j++)for(int k=j+1;k<31;k++){
   int z[3]={even[i],even[j],even[k]};
   vector<int> allowed;
   for(int w:odd)if(pc(w^z[0])!=1 && pc(w^z[1])!=1 && pc(w^z[2])!=1)allowed.push_back(w);
   int aa[6];for(int q=0;q<6;q++){
    int ones=((z[0]>>q)&1)+((z[1]>>q)&1)+((z[2]>>q)&1);
    aa[q]=((v>>q)&1)?ones:3-ones;
   }
   int n=allowed.size();
   for(int p=0;p<n;p++)for(int q=p+1;q<n;q++)
   for(int r=q+1;r<n;r++)for(int s=r+1;s<n;s++){
    int w[4]={allowed[p],allowed[q],allowed[r],allowed[s]};
    ++total;array<int,6> rows{};bool found=false;
    for(int t=0;t<6;t++){
     int ones=((w[0]>>t)&1)+((w[1]>>t)&1)+((w[2]>>t)&1)+((w[3]>>t)&1);
     int b=((v>>t)&1)?ones:4-ones;
     rows[t]=5*aa[t]+b;if(good[aa[t]][b]){found=true;break;}
    }
    if(found)continue;
    ++residual;Geometry g={(unsigned char)z[0],(unsigned char)z[1],(unsigned char)z[2],
     (unsigned char)w[0],(unsigned char)w[1],(unsigned char)w[2],(unsigned char)w[3]};
    records.write(reinterpret_cast<const char*>(g.data()),7);
    int signature=0,splitcount=0;
    for(int row:rows){
     ++rowhist[row];int a=row/5,b=row%5;
     if(a==1||a==2){
      ++splitcount;
      if(a==1&&b==0)signature|=1;
      else if(a==1&&b==4)signature|=2;
      else if(a==2&&b==0)signature|=4;
      else if(a==2&&b==1)signature|=8;
      else assert(false);
     }
    }
    assert(signature!=0);++splithist[splitcount];
    auto&sg=signatures[signature];if(!sg.count)sg.representative=g;++sg.count;
    if(!(signature&(2|8))){++none_near;if(!have_no_near){no_near_rep=g;have_no_near=true;}}
    sort(rows.begin(),rows.end());U key=0;for(int row:rows)key=(key<<5)|row;
    auto&pat=patterns[key];if(!pat.count)pat.representative=g;++pat.count;
   }
  }
  records.close();
  if(comma)out<<",";comma=true;
  out<<"{\"v\":"<<v<<",\"eligible_geometries\":"<<total<<",\"no_good_cut\":"<<residual
   <<",\"record_file\":\""<<filename<<"\",\"without_a1b4_or_a2b1\":"<<none_near
   <<",\"without_near_representative\":";if(have_no_near)geom(out,no_near_rep);else out<<"null";
  out<<",\"bad_row_occurrences\":[";bool sep=false;
  for(int row=0;row<20;row++)if(rowhist[row]){
   if(sep)out<<",";sep=true;out<<"{\"a\":"<<row/5<<",\"b\":"<<row%5<<",\"count\":"<<rowhist[row]<<"}";
  }
  out<<"],\"splitting_coordinate_count_histogram\":[";
  for(int i=0;i<=6;i++){if(i)out<<",";out<<splithist[i];}
  out<<"],\"split_signature_bit_order\":[\"a1b0\",\"a1b4\",\"a2b0\",\"a2b1\"],\"split_signatures\":[";sep=false;
  for(auto&[key,e]:signatures){if(sep)out<<",";sep=true;
   out<<"{\"mask\":"<<key<<",\"count\":"<<e.count<<",\"representative\":";geom(out,e.representative);out<<"}";
  }
  out<<"],\"sorted_row_multisets\":[";sep=false;
  for(auto&[key,e]:patterns){if(sep)out<<",";sep=true;
   U copy=key;array<int,6> rows{};for(int i=5;i>=0;i--){rows[i]=copy&31;copy>>=5;}
   out<<"{\"rows\":[";for(int i=0;i<6;i++){if(i)out<<",";out<<"["<<rows[i]/5<<","<<rows[i]%5<<"]";}
   out<<"],\"count\":"<<e.count<<",\"representative\":";geom(out,e.representative);out<<"}";
  }
  out<<"]}";out.flush();
  cout<<"v="<<v<<" eligible="<<total<<" residual="<<residual<<" no_a1b4_or_a2b1="<<none_near
   <<" row_multisets="<<patterns.size()<<"\n";
 }
 out<<"]}\n";
}
