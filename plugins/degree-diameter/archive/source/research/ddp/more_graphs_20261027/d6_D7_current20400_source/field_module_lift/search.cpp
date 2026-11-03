#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
uint32_t u32(istream&f){uint32_t x;f.read((char*)&x,4);assert(f);return x;}
struct Model{string name;int q,L;vector<uint8_t>add,neg,act;vector<array<uint8_t,4>>cases;};
int main(int argc,char**argv){
 clock_t begun=clock();auto cpu=[&](){return double(clock()-begun)/CLOCKS_PER_SEC;};double limit=stod(argv[3]);string dir=argv[2];
 ifstream input(argv[1],ios::binary);char magic[4];input.read(magic,4);assert(string(magic,4)=="FML1");assert(u32(input)==4);
 array<uint16_t,6>genQ;array<uint16_t,3>invH;array<array<uint16_t,6>,816>moveQ;
 input.read((char*)genQ.data(),12);input.read((char*)invH.data(),6);input.read((char*)moveQ.data(),816*6*2);
 vector<Model>models;
 for(int mi=0;mi<4;mi++){Model m;int len=u32(input);m.name.resize(len);input.read(m.name.data(),len);m.q=u32(input);m.L=m.q*m.q;int count=u32(input);
  m.add.resize(m.L*m.L);m.neg.resize(m.L);m.act.resize(48*m.L);m.cases.resize(count);
  input.read((char*)m.add.data(),m.add.size());input.read((char*)m.neg.data(),m.neg.size());input.read((char*)m.act.data(),m.act.size());input.read((char*)m.cases.data(),size_t(count)*4);assert(input);models.push_back(move(m));}
 ofstream cases(dir+"/cases.tsv");cases<<"model\tordinal\ttuple\tlegal\tvisited\teccentricity\taccepted\n";
 int processed=0,legal=0,connected=0,disconnected=0,illegal=0,bfses=0,lastmodel=-1,lastcase=-1;bool hit=false,limited=false;vector<int>modeldone(4),modellegal(4),modelconnected(4);
 for(int mi=0;mi<4;mi++){
  auto&m=models[mi];int L=m.L,n=816*L;vector<int>d(n),queue(n);
  for(int ci=0;ci<int(m.cases.size());ci++){
   lastmodel=mi;lastcase=ci;auto t=m.cases[ci];array<int,6>vec,ids;
   array<int,3>positive={0,int(t[0])+m.q*int(t[1]),int(t[2])+m.q*int(t[3])};
   for(int s=0;s<3;s++){vec[2*s]=positive[s];vec[2*s+1]=m.neg[m.act[invH[s]*L+positive[s]]];}
   for(int s=0;s<3;s++)assert(m.add[positive[s]*L+m.act[(genQ[2*s]/17)*L+vec[2*s+1]]]==0);
   for(int k=0;k<6;k++)ids[k]=L*genQ[k]+vec[k];
   auto sorted=ids;sort(sorted.begin(),sorted.end());bool valid=sorted[0]!=0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end();
   ++processed;++modeldone[mi];
   if(!valid){++illegal;cases<<m.name<<'\t'<<ci<<"\t["<<int(t[0])<<','<<int(t[1])<<','<<int(t[2])<<','<<int(t[3])<<"]\t0\t0\t-1\t0\n";continue;}
   ++legal;++modellegal[mi];array<array<uint8_t,6>,48>increment;
   for(int h=0;h<48;h++)for(int k=0;k<6;k++)increment[h][k]=m.act[h*L+vec[k]];
   fill(d.begin(),d.end(),-1);int lo=0,hi=0;d[0]=0;queue[hi++]=0;int ecc=0;
   while(lo<hi){int u=queue[lo++],q=u/L,z=u-q*L,h=q/17;
    for(int k=0;k<6;k++){int v=L*moveQ[q][k]+m.add[z*L+increment[h][k]];if(d[v]<0){d[v]=d[u]+1;ecc=max(ecc,d[v]);queue[hi++]=v;}}
   }
   ++bfses;bool full=hi==n;connected+=full;disconnected+=!full;modelconnected[mi]+=full;bool accept=full&&ecc<=7;
   cases<<m.name<<'\t'<<ci<<"\t["<<int(t[0])<<','<<int(t[1])<<','<<int(t[2])<<','<<int(t[3])<<"]\t1\t"<<hi<<'\t'<<ecc<<'\t'<<accept<<'\n';
   if(ci==0){cout<<"CONTROL "<<m.name<<" visited "<<hi<<" ecc "<<ecc<<endl;}
   if(accept){
    hit=true;ofstream out(dir+"/FIRST_HIT.json");out<<"{\"model\":\""<<m.name<<"\",\"q\":"<<m.q<<",\"case_ordinal\":"<<ci<<",\"normal_tuple\":[";
    for(int j=0;j<4;j++){if(j)out<<',';out<<int(t[j]);}
    out<<"],\"n\":"<<n<<",\"m\":"<<3*n<<",\"degree\":6,\"connected\":true,\"simple\":true,\"actual_global_D\":"<<ecc<<",\"ordinary_bad_unordered_pairs_targetD7\":0,\"root\":0,\"roots_BFS\":1,\"distance_histogram\":[";
    vector<int>hist(ecc+1);for(int x:d)hist[x]++;for(size_t j=0;j<hist.size();j++){if(j)out<<',';out<<hist[j];}
    out<<"],\"positive_and_true_inverse_generator_ids\":[";
    for(int j=0;j<6;j++){if(j)out<<',';out<<ids[j];}out<<"],\"independent_acceptance_pending\":true}\n";
    ofstream edges(dir+"/graph_d6_D7_n"+to_string(n)+".edges");edges<<n<<' '<<3*n<<'\n';long long written=0;
    for(int u=0;u<n;u++){int q=u/L,z=u-q*L,h=q/17;for(int k=0;k<6;k++){int v=L*moveQ[q][k]+m.add[z*L+increment[h][k]];if(u<v){edges<<u<<' '<<v<<'\n';++written;}}}
    assert(written==3LL*n);goto done;
   }
   if(cpu()>limit){limited=true;goto done;}
  }
  cout<<"MODEL_DONE "<<m.name<<" cases "<<modeldone[mi]<<" connected "<<modelconnected[mi]<<" CPU "<<cpu()<<endl;
 }
done:
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"FIRST_COMPLETE_HIT":limited?"UNKNOWN_CPU_LIMIT":"ALL_PREPLANNED_SETTINGS_COMPLETE_NO_HIT")
  <<"\",\"preplanned_settings\":2625,\"settings_processed\":"<<processed<<",\"legal_six_generator_cases\":"<<legal<<",\"illegal_generator_cases\":"<<illegal
  <<",\"connected_cases\":"<<connected<<",\"disconnected_cases\":"<<disconnected<<",\"actual_new_Cayley_root_BFS\":"<<bfses
  <<",\"hit\":"<<(hit?"true":"false")<<",\"CPU_limited\":"<<(limited?"true":"false")<<",\"cursor\":{\"model_index\":"<<lastmodel<<",\"case_ordinal\":"<<lastcase<<"},\"models\":[";
 for(int mi=0;mi<4;mi++){if(mi)out<<',';out<<"{\"name\":\""<<models[mi].name<<"\",\"q\":"<<models[mi].q<<",\"n\":"<<816*models[mi].L<<",\"preplanned_settings\":"<<models[mi].cases.size()<<",\"processed\":"<<modeldone[mi]<<",\"legal\":"<<modellegal[mi]<<",\"connected\":"<<modelconnected[mi]<<'}';}
 out<<"],\"native_CPU_seconds\":"<<cpu()<<",\"source_BFS_repeated\":0,\"complete_edgefiles_exported\":"<<(hit?1:0)<<"}\n";
 cout<<(hit?"HIT":limited?"UNKNOWN":"COMPLETE_NO_HIT")<<" settings "<<processed<<" CPU "<<cpu()<<endl;
}
