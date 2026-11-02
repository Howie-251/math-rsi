#include <bits/stdc++.h>
using namespace std;
using Map=array<int,16>;
struct Mat{array<int,4>col;Map m,inv;};
int rank4(array<int,4>c){int piv[4]{},r=0;for(int v:c)for(int j=3;j>=0;j--)if(v&(1<<j)){if(piv[j])v^=piv[j];else{piv[j]=v;r++;break;}}return r;}
Mat make_mat(array<int,4>c){Mat a;a.col=c;for(int x=0;x<16;x++){int v=0;for(int j=0;j<4;j++)if(x&(1<<j))v^=c[j];a.m[x]=v;a.inv[v]=x;}return a;}
array<int,4>columns(const array<Map,4>&m,const array<int,4>&b,const array<int,4>&w){
 return {m[w[3]][m[w[2]][m[w[1]][b[w[0]]]]],m[w[3]][m[w[2]][b[w[1]]]],m[w[3]][b[w[2]]],b[w[3]]};
}
void candidate(const string&path,int ai,int bi,int bb,const Mat&A,const Mat&B,const vector<array<int,4>>&words,const string&kind){
 array<Map,4>m={A.m,B.m,B.inv,A.inv};array<int,4>b={1,bb,B.inv[bb],A.inv[1]};
 ofstream f(path);f<<"{\"kind\":\""<<kind<<"\",\"companion_index\":"<<ai<<",\"B_GL_index\":"<<bi<<",\"b1\":"<<bb<<",\"inverse_labels\":[3,2,1,0],\"matrix_columns\":[";
 for(int t=0;t<4;t++){if(t)f<<',';f<<'[';for(int j=0;j<4;j++){if(j)f<<',';f<<m[t][1<<j];}f<<']';}f<<"],\"b_codes\":[";
 for(int t=0;t<4;t++){if(t)f<<',';f<<b[t];}f<<"],\"word_checks\":[";
 for(int k=0;k<int(words.size());k++){
  if(k)f<<',';auto w=words[k];auto c=columns(m,b,w);f<<"{\"word\":[";
  for(int j=0;j<4;j++){if(j)f<<',';f<<w[j];}f<<"],\"columns\":[";
  for(int j=0;j<4;j++){if(j)f<<',';f<<c[j];}f<<"],\"rank\":"<<rank4(c)<<'}';
 }f<<"]}\n";
}
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];double limit=stod(argv[2]);clock_t started=clock();auto cpu=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};
 ifstream in(dir+"/words.txt");int wn;in>>wn;assert(wn==26);vector<array<int,4>>words(wn);
 for(auto&w:words)for(int&t:w)in>>t;
 vector<Mat>gs;
 for(int code=0;code<65536;code++){array<int,4>c;for(int j=0;j<4;j++)c[j]=(code>>(4*j))&15;if(rank4(c)==4)gs.push_back(make_mat(c));}
 assert(gs.size()==20160);
 long long examined=0,survivors=0,ranktests=0;array<long long,26>firstbad{};array<long long,8>bycompanion{};
 bool limited=false,diagnostic_saved=false;int ai=0,bi=0,bb=1;
 for(ai=0;ai<8&&!limited;ai++){
  Mat A=make_mat({2,4,8,1+2*ai});
  for(bi=0;bi<int(gs.size())&&!limited;bi++){
   const Mat&B=gs[bi];array<Map,4>m={A.m,B.m,B.inv,A.inv};
   for(bb=1;bb<16;bb++){
    if((examined&4095)==0&&cpu()>=limit){limited=true;break;}
    examined++;array<int,4>b={1,bb,B.inv[bb],A.inv[1]};
    if(!diagnostic_saved){candidate(dir+"/first_diagnostic_candidate.json",ai,bi,bb,A,B,words,"first formal canonical candidate; no bbbb filter");diagnostic_saved=true;}
    bool okay=true;
    for(int k=0;k<wn;k++){
     ranktests++;if(rank4(columns(m,b,words[k]))!=4){firstbad[k]++;okay=false;break;}
    }
    if(okay){
     survivors++;bycompanion[ai]++;
     if(survivors==1)candidate(dir+"/first_survivor.json",ai,bi,bb,A,B,words,"first all26-required-words rank4 survivor; necessary condition only");
    }
   }
  }
 }
 ofstream f(dir+"/search_result.json");
 f<<"{\"status\":\""<<(limited?"CPU_LIMIT_INCOMPLETE":survivors?"COMPLETE_REQUIRED26_SURVIVORS_EXIST":"COMPLETE_REQUIRED26_NO_GLOBAL_LABEL_MAPS")<<"\",\"canonical_space\":2419200,\"examined\":"<<examined<<",\"complete\":"<<(!limited?"true":"false")<<",\"GL4_2_count\":20160,\"companion_count\":8,\"b1_nonzero_choices\":15,\"required_words\":26,\"bbbb_prefilter_used\":false,\"nonrequired_word_tests\":0,\"rank_tests\":"<<ranktests<<",\"survivors\":"<<survivors<<",\"survivors_by_companion\":[";
 for(int k=0;k<8;k++){if(k)f<<',';f<<bycompanion[k];}f<<"],\"first_failure_words\":[";
 for(int k=0;k<wn;k++){if(k)f<<',';f<<"{\"word\":[";for(int j=0;j<4;j++){if(j)f<<',';f<<words[k][j];}f<<"],\"count\":"<<firstbad[k]<<'}';}
 f<<"],\"native_CPU_seconds\":"<<cpu()<<",\"native_soft_limit_seconds\":"<<limit<<",\"CPU_limit_reached\":"<<(limited?"true":"false")<<",\"cursor_next_companion\":"<<ai<<",\"cursor_next_B\":"<<bi<<",\"cursor_next_b1\":"<<bb<<",\"graphs_generated\":0,\"full72fibercoverage_checked\":false,\"BFS_performed\":false}\n";
 cout<<"examined="<<examined<<" survivors="<<survivors<<" nativeCPU="<<cpu()<<endl;
}
