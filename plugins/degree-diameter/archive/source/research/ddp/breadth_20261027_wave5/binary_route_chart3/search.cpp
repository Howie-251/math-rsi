#include <bits/stdc++.h>
using namespace std;
using Map=array<int,8>;
struct Mat{array<int,3> columns;Map apply,inverse;};
int rank3(array<int,3> columns){
 int pivots[3]={},rank=0;
 for(int v:columns)for(int bit=2;bit>=0;bit--)if(v&(1<<bit)){
  if(pivots[bit])v^=pivots[bit];else{pivots[bit]=v;rank++;break;}
 }
 return rank;
}
Mat make_mat(array<int,3> columns){
 Mat m;m.columns=columns;
 for(int x=0;x<8;x++){int y=0;for(int bit=0;bit<3;bit++)if(x&(1<<bit))y^=columns[bit];m.apply[x]=y;m.inverse[y]=x;}
 return m;
}
array<int,3> columns_for(const array<Map,4>&maps,const array<int,4>&vectors,array<int,3>w){
 return {maps[w[2]][maps[w[1]][vectors[w[0]]]],maps[w[2]][vectors[w[1]]],vectors[w[2]]};
}
int main(int argc,char**argv){
 assert(argc==2);string out=argv[1];clock_t started=clock();
 vector<Mat> matrices;
 for(int code=0;code<512;code++){
  array<int,3> columns;for(int i=0;i<3;i++)columns[i]=(code>>(3*i))&7;
  if(rank3(columns)==3)matrices.push_back(make_mat(columns));
 }
 const array<int,4> inverse={1,0,3,2};vector<array<int,3>>words;
 for(int a=0;a<4;a++)for(int b=0;b<4;b++)if(b!=inverse[a])for(int c=0;c<4;c++)if(c!=inverse[b])words.push_back({a,b,c});
 assert(matrices.size()==168&&words.size()==36);
 long long examined=0,passed_AAA=0,passed_AAA_BBB=0,rank_tests=0,best_ties=0;
 long long full_rank_histogram[37]={};
 bool found=false,limited=false;int best_good=-1,best_A=-1,best_B=-1,best_b=-1;
 array<int,36> best_ranks{};
 int aaa_index=-1,bbb_index=-1;
 for(int i=0;i<36;i++){if(words[i]==array<int,3>{0,0,0})aaa_index=i;if(words[i]==array<int,3>{2,2,2})bbb_index=i;}
 for(int ai=0;ai<168&&!found&&!limited;ai++)for(int bi=0;bi<168&&!found&&!limited;bi++){
  const Mat&A=matrices[ai];const Mat&B=matrices[bi];array<Map,4>maps={A.apply,A.inverse,B.apply,B.inverse};
  for(int bb=1;bb<8;bb++){
   if((examined&4095)==0&&double(clock()-started)/CLOCKS_PER_SEC>=10){limited=true;break;}
   examined++;array<int,4>vectors={1,A.inverse[1],bb,B.inverse[bb]};array<int,36>ranks{};
   // AAA/BBB are checked first; the remaining ranks are retained even on a
   // failure so the saved best is global among all examined normalized inputs.
   ranks[aaa_index]=rank3(columns_for(maps,vectors,words[aaa_index]));rank_tests++;
   ranks[bbb_index]=rank3(columns_for(maps,vectors,words[bbb_index]));rank_tests++;
   if(ranks[aaa_index]==3){passed_AAA++;if(ranks[bbb_index]==3)passed_AAA_BBB++;}
   int good=0;
   for(int wi=0;wi<36;wi++){
    if(wi!=aaa_index&&wi!=bbb_index){ranks[wi]=rank3(columns_for(maps,vectors,words[wi]));rank_tests++;}
    good+=ranks[wi]==3;
   }
   full_rank_histogram[good]++;
   if(good>best_good){best_good=good;best_A=ai;best_B=bi;best_b=bb;best_ranks=ranks;best_ties=1;}
   else if(good==best_good)best_ties++;
   if(good==36){found=true;break;}
  }
 }
 const Mat&A=matrices[best_A];const Mat&B=matrices[best_B];array<Map,4>maps={A.apply,A.inverse,B.apply,B.inverse};
 array<int,4>vectors={1,A.inverse[1],best_b,B.inverse[best_b]};
 ofstream best(out+"/best_candidate.json");
 best<<"{\"field\":2,\"dimension\":3,\"length\":3,\"kind\":\"maximum full-rank-word count, first lex input on ties\",\"A_index\":"<<best_A<<",\"B_index\":"<<best_B<<",\"v_A\":1,\"v_B\":"<<best_b<<",\"full_rank_words\":"<<best_good<<",\"inverse_symbols\":[1,0,3,2],\"matrix_columns\":[";
 for(int t=0;t<4;t++){if(t)best<<',';best<<'[';for(int j=0;j<3;j++){if(j)best<<',';best<<maps[t][1<<j];}best<<']';}
 best<<"],\"b_codes\":[";for(int t=0;t<4;t++){if(t)best<<',';best<<vectors[t];}
 best<<"],\"words\":[";for(int i=0;i<36;i++){if(i)best<<',';best<<'['<<words[i][0]<<','<<words[i][1]<<','<<words[i][2]<<']';}
 best<<"],\"ranks\":[";for(int i=0;i<36;i++){if(i)best<<',';best<<best_ranks[i];}
 best<<"],\"controllability_columns\":[";
 for(int i=0;i<36;i++){if(i)best<<',';auto cs=columns_for(maps,vectors,words[i]);best<<'['<<cs[0]<<','<<cs[1]<<','<<cs[2]<<']';}
 best<<"]}\n";
 ofstream result(out+"/search_result.json");
 result<<"{\"status\":\""<<(found?"FOUND_UNIVERSAL_BINARY_LENGTH3_CHART":limited?"TIME_LIMIT_INCOMPLETE":"EXHAUSTIVE_NORMALIZED_SPACE_NO_CHART")<<"\",\"GL3_2_count\":168,\"words\":36,\"normalization\":\"vA=(1,0,0) only; all A,B in GL3(2), all nonzero vB\",\"normalized_inputs_planned\":197568,\"examined\":"<<examined<<",\"passed_AAA\":"<<passed_AAA<<",\"passed_AAA_and_BBB\":"<<passed_AAA_BBB<<",\"word_rank_tests\":"<<rank_tests<<",\"best_full_rank_words\":"<<best_good<<",\"best_tie_count\":"<<best_ties<<",\"hit\":"<<(found?"true":"false")<<",\"complete\":"<<(!found&&!limited?"true":"false")<<",\"CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"CPU_internal_limit_seconds\":10,\"CPU_limit_reached\":"<<(limited?"true":"false")<<",\"full_rank_word_count_histogram\":{ ";
 bool comma=false;for(int i=0;i<=36;i++)if(full_rank_histogram[i]){if(comma)result<<',';comma=true;result<<'"'<<i<<"\":"<<full_rank_histogram[i];}
 result<<"}}\n";
}
