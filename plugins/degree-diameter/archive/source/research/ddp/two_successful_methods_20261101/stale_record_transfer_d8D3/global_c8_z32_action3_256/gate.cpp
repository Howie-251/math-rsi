#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Vec = array<int,4>;
struct Word { int phase; Vec coeff; vector<int> darts; };
int main(int argc,char**argv){
  string dir=argv[1];double limit=stod(argv[2]);clock_t start=clock();
  auto timedout=[&](){return double(clock()-start)/CLOCKS_PER_SEC>=limit;};
  array<int,8> powers{};powers[0]=1;for(int j=1;j<8;++j)powers[j]=(3*powers[j-1])&31;
  if(((3*powers[7])&31)!=1){cerr<<"action not C8\n";return 2;}
  array<int,8> phase,noise;
  for(int j=0;j<4;++j){phase[2*j]=j+1;noise[2*j]=1;phase[2*j+1]=(8-j-1)%8;noise[2*j+1]=(-powers[phase[2*j+1]])&31;}
  vector<Word> words;vector<int> path;
  function<void(int,int,Vec)> walk=[&](int p,int last,Vec coeff){
    words.push_back({p,coeff,path});if(path.size()==3)return;
    for(int dart=0;dart<8;++dart){if(last>=0&&dart==(last^1))continue;
      Vec next;for(int j=0;j<4;++j)next[j]=(powers[phase[dart]]*coeff[j])&31;
      next[dart/2]=(next[dart/2]+noise[dart])&31;
      path.push_back(dart);walk((p+phase[dart])%8,dart,next);path.pop_back();
    }
  };
  walk(0,-1,Vec{});
  array<map<Vec,int>,8> maps;array<int,8> raw{};
  ofstream wordout(dir+"/ALL457_WORDS.tsv");wordout<<"word_id\tlength\tphase\tc0\tc1\tc2\tc3\tdarts\n";
  for(int id=0;id<(int)words.size();++id){auto&w=words[id];++raw[w.phase];maps[w.phase].emplace(w.coeff,id);
    wordout<<id<<'\t'<<w.darts.size()<<'\t'<<w.phase;for(int c:w.coeff)wordout<<'\t'<<c;wordout<<'\t';for(size_t i=0;i<w.darts.size();++i){if(i)wordout<<',';wordout<<w.darts[i];}wordout<<'\n';}
  wordout.close();if(words.size()!=457){cerr<<"word count\n";return 3;}
  array<vector<Vec>,8> forms;bool capacity=true;int firstbadphase=-1;
  ofstream formout(dir+"/DISTINCT_FORMS.tsv");formout<<"phase\tlocal_id\tc0\tc1\tc2\tc3\tfirst_word_id\n";
  for(int p=0;p<8;++p){if(maps[p].size()<32){capacity=false;if(firstbadphase<0)firstbadphase=p;}
    for(auto&entry:maps[p]){formout<<p<<'\t'<<forms[p].size();for(int c:entry.first)formout<<'\t'<<c;formout<<'\t'<<entry.second<<'\n';forms[p].push_back(entry.first);}}
  formout.close();
  long long normalization=0,disconnected=0,tested=0;array<long long,4> firstodd_counts{};array<long long,9> degreehist{};
  array<array<long long,33>,8> coverhist{};array<int,8> maximum{};array<long long,8> fullcount{};
  array<Vec,8> single_argmax{};array<int,8> first_full_id;first_full_id.fill(-1);
  bool hit=false,complete=false,budget=false;Vec hit_b{};int hit_degree=0;
  array<uint32_t,8> hit_masks{};array<array<int,32>,8> hit_routes{};
  ofstream params(dir+"/ALL_NORMALIZED_CONNECTED_PARAMETERS.tsv");
  params<<"id\tfirst_odd_index\tb0\tb1\tb2\tb3\tactual_degree\tcover0\tcover1\tcover2\tcover3\tcover4\tcover5\tcover6\tcover7\tfirst_failed_phase\tfirst_missing_normal\n";
  if(capacity){
    for(int pivot=0;pivot<4&&!hit&&!budget;++pivot){
      Vec b{};
      function<void(int)> visit=[&](int i){
        if(hit||budget)return;
        if(i<4){
          if(i==pivot){b[i]=1;visit(i+1);}
          else for(int x=0;x<32&&!hit&&!budget;x+=(i<pivot?2:1)){b[i]=x;visit(i+1);}
          return;
        }
        ++normalization;
        if((b[0]&1)==1&&(b[1]&1)==0&&(b[2]&1)==1&&(b[3]&1)==0){++disconnected;return;}
        if(timedout()){budget=true;return;}
        ++firstodd_counts[pivot];int degree=(b[3]==0||b[3]==16)?7:8;++degreehist[degree];
        array<uint32_t,8> masks{};array<int,8> counts{};int failed=-1,missing=-1;
        for(int p=0;p<8;++p){
          uint32_t mask=0;for(auto&f:forms[p]){int y=(f[0]*b[0]+f[1]*b[1]+f[2]*b[2]+f[3]*b[3])&31;mask|=1u<<y;}
          masks[p]=mask;int count=__builtin_popcount(mask);counts[p]=count;++coverhist[p][count];
          if(count>maximum[p]){maximum[p]=count;single_argmax[p]=b;}
          if(count==32){++fullcount[p];if(first_full_id[p]<0)first_full_id[p]=tested;}
          else if(failed<0){failed=p;missing=__builtin_ctz(~mask);}
        }
        params<<tested<<'\t'<<pivot;for(int x:b)params<<'\t'<<x;params<<'\t'<<degree;for(int c:counts)params<<'\t'<<c;params<<'\t'<<failed<<'\t'<<missing<<'\n';
        ++tested;
        if(failed<0){
          hit=true;hit_b=b;hit_degree=degree;hit_masks=masks;
          for(auto&v:hit_routes)v.fill(-1);
          for(int id=0;id<(int)words.size();++id){auto&w=words[id];int y=0;for(int j=0;j<4;++j)y+=w.coeff[j]*b[j];y&=31;if(hit_routes[w.phase][y]<0)hit_routes[w.phase][y]=id;}
        }
      };
      visit(0);
    }
    complete=!hit&&!budget&&normalization==61440&&disconnected==4096&&tested==57344;
  }
  params.close();
  if(hit){
    vector<pair<int,int>> generators;
    for(int j=0;j<4;++j){int a=j+1;generators.push_back({a,hit_b[j]});int inv=(8-a)%8;generators.push_back({inv,(-powers[inv]*hit_b[j])&31});}
    sort(generators.begin(),generators.end());generators.erase(unique(generators.begin(),generators.end()),generators.end());
    if(generators.size()!=(size_t)hit_degree){cerr<<"degree binding\n";return 4;}
    set<pair<int,int>> edges;
    for(int u=0;u<256;++u){int a=u/32,b=u%32;for(auto[c,d]:generators){int v=32*((a+c)%8)+((b*powers[c]+d)&31);if(u==v){cerr<<"loop\n";return 5;}edges.insert(minmax(u,v));}}
    ofstream graph(dir+"/graph_d8_D3_n256.edges");graph<<256<<' '<<edges.size()<<'\n';for(auto[u,v]:edges)graph<<u<<' '<<v<<'\n';
    ofstream routes(dir+"/HIT_ALL256_SHORT_ROUTES.tsv");routes<<"phase\tnormal\tvertex\tword_id\n";for(int p=0;p<8;++p)for(int y=0;y<32;++y)routes<<p<<'\t'<<y<<'\t'<<32*p+y<<'\t'<<hit_routes[p][y]<<'\n';
  }
  string status=!capacity?"COMPLETE_NO_FIXED_GLOBAL256_BY_COEFFICIENT_CAPACITY":hit?"FULL256_WORD_COVER_HIT_PENDING_FRESH_ACCEPTANCE":complete?"COMPLETE_NO_FIXED_GLOBAL256_ALL_NORMALS":"UNKNOWN_GLOBAL256_CPU_CAP";
  ofstream out(dir+"/NATIVE_RESULT.json");
  out<<"{\"status\":\""<<status<<"\",\"raw_words\":"<<words.size()<<",\"capacity_pass\":"<<(capacity?"true":"false")<<",\"first_capacity_failed_phase\":"<<firstbadphase<<",\"phases\":[";
  for(int p=0;p<8;++p){if(p)out<<',';out<<"{\"phase\":"<<p<<",\"raw_words\":"<<raw[p]<<",\"distinct_coefficient_forms\":"<<forms[p].size()<<",\"maximum_actual_cover\":"<<maximum[p]<<",\"actual_full_cover_count\":"<<fullcount[p]<<",\"first_full_parameter_id\":"<<first_full_id[p]<<",\"first_max_parameter\":[";for(int j=0;j<4;++j){if(j)out<<',';out<<single_argmax[p][j];}out<<"],\"coverage_histogram\":[";for(int c=0;c<33;++c){if(c)out<<',';out<<coverhist[p][c];}out<<"]}";}
  out<<"],\"normalized_representatives_visited\":"<<normalization<<",\"disconnected_parity_skipped\":"<<disconnected<<",\"connected_parameters_checked\":"<<tested<<",\"expected_connected_domain\":57344,\"connected_domain_complete\":"<<(complete?"true":"false")<<",\"first_odd_counts\":[";for(int j=0;j<4;++j){if(j)out<<',';out<<firstodd_counts[j];}out<<"],\"degree7_checked\":"<<degreehist[7]<<",\"degree8_checked\":"<<degreehist[8]<<",\"full_hit\":"<<(hit?"true":"false")<<",\"hit_normals\":[";for(int j=0;j<4;++j){if(j)out<<',';out<<hit_b[j];}out<<"],\"hit_degree\":"<<hit_degree<<",\"CPU_cap_stop\":"<<(budget?"true":"false")<<",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
  cout<<status<<"; tested="<<tested<<"; fullhit="<<hit<<"; capacity="<<capacity<<'\n';
}
