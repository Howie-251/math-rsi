#include <bits/stdc++.h>
using namespace std;
using Map=array<int,16>;
struct Mat {array<int,4> col;Map m,inv;int cyclic_mask;};
int rank4(array<int,4> c){int piv[4]={},r=0;for(int v:c){for(int j=3;j>=0;j--)if(v&(1<<j)){if(piv[j])v^=piv[j];else{piv[j]=v;r++;break;}}}return r;}
Mat make_mat(array<int,4> c){Mat a;a.col=c;a.cyclic_mask=0;for(int x=0;x<16;x++){int v=0;for(int j=0;j<4;j++)if(x&(1<<j))v^=c[j];a.m[x]=v;a.inv[v]=x;}for(int b=1;b<16;b++){int v=b;array<int,4> cs;for(int i=0;i<4;i++){cs[i]=v;v=a.m[v];}if(rank4(cs)==4)a.cyclic_mask|=1<<b;}return a;}
bool full_word(const array<Map,4>& m,const array<int,4>& b,const array<int,4>& w){
 int x0=m[w[3]][m[w[2]][m[w[1]][b[w[0]]]]];
 int x1=m[w[3]][m[w[2]][b[w[1]]]];
 int x2=m[w[3]][b[w[2]]];
 int x3=b[w[3]];
 return rank4({x0,x1,x2,x3})==4;
}
int main(int argc,char** argv){
 clock_t started=clock();vector<Mat> gs;
 for(int packed=0;packed<65536;packed++){array<int,4> c;for(int j=0;j<4;j++)c[j]=(packed>>(4*j))&15;if(rank4(c)==4)gs.push_back(make_mat(c));}
 const array<int,4> inv={1,0,3,2};vector<array<int,4>> words;
 for(int a=0;a<4;a++)for(int b=0;b<4;b++)if(b!=inv[a])for(int c=0;c<4;c++)if(c!=inv[b])for(int d=0;d<4;d++)if(d!=inv[c])words.push_back({a,b,c,d});
 assert(gs.size()==20160 && words.size()==108);
 if(argc==2 && string(argv[1])=="--first-rank-candidate"){
  Mat A=make_mat({2,4,8,1});int bi=0;while(!gs[bi].cyclic_mask)bi++;
  auto& B=gs[bi];int bb=1;while(!(B.cyclic_mask&(1<<bb)))bb++;
  array<Map,4> maps={A.m,A.inv,B.m,B.inv};array<int,4> bs={1,A.inv[1],bb,B.inv[bb]};
  cout<<"{\"kind\":\"first bbbb-passing candidate in the formal enumeration\",\"companion_index\":0,\"B_index\":"<<bi<<",\"b_b\":"<<bb<<",\"matrix_columns\":[";
  for(int t=0;t<4;t++){if(t)cout<<',';cout<<'[';for(int j=0;j<4;j++){if(j)cout<<',';cout<<maps[t][1<<j];}cout<<']';}cout<<"],\"b_codes\":[";
  for(int t=0;t<4;t++){if(t)cout<<',';cout<<bs[t];}cout<<"],\"inverse_symbols\":[1,0,3,2],\"words\":[";
  for(int wi=0;wi<108;wi++){if(wi)cout<<',';cout<<'[';for(int j=0;j<4;j++){if(j)cout<<',';cout<<words[wi][j];}cout<<']';}cout<<"],\"ranks\":[";
  for(int wi=0;wi<108;wi++){auto w=words[wi];int r=rank4({maps[w[3]][maps[w[2]][maps[w[1]][bs[w[0]]]]],maps[w[3]][maps[w[2]][bs[w[1]]]],maps[w[3]][bs[w[2]]],bs[w[3]]});assert(full_word(maps,bs,w)==(r==4));if(wi)cout<<',';cout<<r;}
  cout<<"],\"rank_and_formal_boolean_routine_agree\":true,\"CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<"}\n";return 0;
 }
 long long cyclic_pairs=0;for(auto& B:gs)cyclic_pairs+=__builtin_popcount((unsigned)B.cyclic_mask);
 long long examined=0,passed_bbbb=0,rank_tests=0;array<long long,108> first_bad={};
 bool found=false,limited=false;int ai=-1,bi=-1,bb=-1,hitai=-1,hitbi=-1,hitbb=-1;
 for(ai=0;ai<8&&!found&&!limited;ai++){
  Mat A=make_mat({2,4,8,1+2*ai});
  for(bi=0;bi<(int)gs.size()&&!found&&!limited;bi++){
   auto& B=gs[bi];array<Map,4> maps={A.m,A.inv,B.m,B.inv};
   for(bb=1;bb<16;bb++){
    if((examined&4095)==0 && double(clock()-started)/CLOCKS_PER_SEC>=54.0){limited=true;break;}
    examined++;
    if(!(B.cyclic_mask&(1<<bb)))continue;
    passed_bbbb++;array<int,4> bs={1,A.inv[1],bb,B.inv[bb]};bool okay=true;
    for(int wi=0;wi<108;wi++){rank_tests++;if(!full_word(maps,bs,words[wi])){first_bad[wi]++;okay=false;break;}}
    if(okay){found=true;hitai=ai;hitbi=bi;hitbb=bb;break;}
   }
  }
 }
 cout<<"{\"status\":\""<<(found?"FOUND_UNIVERSAL_BINARY_LENGTH4_CHART":limited?"TIME_LIMIT_INCOMPLETE":"EXHAUSTIVE_NORMALIZED_SPACE_NO_CHART")<<"\",\"GL4_2_count\":"<<gs.size()<<",\"words\":"<<words.size()<<",\"B_cyclic_b_pairs\":"<<cyclic_pairs<<",\"canonical_space\":2419200,\"examined\":"<<examined<<",\"passed_bbbb\":"<<passed_bbbb<<",\"word_rank_tests\":"<<rank_tests<<",\"CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"CPU_limit_reached\":"<<(limited?"true":"false")<<",\"complete\":"<<(!found&&!limited?"true":"false")<<",\"cursor_companion_next\":"<<ai<<",\"cursor_B_next\":"<<bi<<",\"cursor_b_next\":"<<bb<<",\"inverse_symbols\":[1,0,3,2],\"first_bad_word_counts\":[";
 for(int i=0;i<108;i++){if(i)cout<<',';cout<<first_bad[i];}cout<<']';
 if(found){Mat A=make_mat({2,4,8,1+2*hitai});auto& B=gs[hitbi];cout<<",\"hit_companion\":"<<hitai<<",\"hit_B_index\":"<<hitbi<<",\"b_a\":1,\"b_b\":"<<hitbb<<",\"A_a_columns\":[";for(int j=0;j<4;j++){if(j)cout<<',';cout<<A.col[j];}cout<<"],\"A_b_columns\":[";for(int j=0;j<4;j++){if(j)cout<<',';cout<<B.col[j];}cout<<']';}
 cout<<"}\n";
}
