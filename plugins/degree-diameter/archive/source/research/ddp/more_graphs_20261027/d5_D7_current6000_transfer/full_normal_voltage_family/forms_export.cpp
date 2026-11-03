#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
struct Step{int dart,to;uint64_t shift;};
Step steps[240][5];int rev[9]={0,2,1,4,3,6,5,8,7};uint8_t addpair[65536];int fieldadd[9][9];
vector<uint64_t>forms[480];long long words;int rootbase;
uint64_t pluscode(uint64_t a,uint64_t b){uint64_t r=0;for(int k=0;k<6;k++)r|=uint64_t(addpair[(((a>>(8*k))&255)<<8)|((b>>(8*k))&255)])<<(8*k);return r;}
void visit(int state,uint64_t code,int last,int depth){
 forms[240*rootbase+state].push_back(code);words++;if(depth==8)return;
 for(auto s:steps[state])if(last<0||s.dart!=rev[last])visit(s.to,pluscode(code,s.shift),s.dart,depth+1);
}
void u32(ostream&f,uint32_t x){char b[4];for(int i=0;i<4;i++)b[i]=(x>>(8*i))&255;f.write(b,4);}
void u64(ostream&f,uint64_t x){char b[8];for(int i=0;i<8;i++)b[i]=(x>>(8*i))&255;f.write(b,8);}
int main(int argc,char**argv){
 assert(argc==3);clock_t start=clock();rlimit lim{2,2};setrlimit(RLIMIT_CPU,&lim);ifstream in(argv[1]);string dir=argv[2];int models;in>>models;assert(models==2);
 for(auto&row:fieldadd)for(auto&v:row)in>>v;
 for(int a=0;a<256;a++)for(int b=0;b<256;b++)if((a&15)<9&&(a>>4)<9&&(b&15)<9&&(b>>4)<9)addpair[(a<<8)|b]=fieldadd[a&15][b&15]|(fieldadd[a>>4][b>>4]<<4);
 ofstream bin(dir+"/normal6_matrix_forms.bin",ios::binary);bin.write("NMF1",4);for(uint32_t x:{1,9,2,480,12})u32(bin,x);
 ofstream meta(dir+"/normal6_matrix_forms.meta.json");meta<<"{\"status\":\"READY_COMPLETE_TWO_MODEL_NORMAL6_MATRIX_FORMS\",\"binary\":\"normal6_matrix_forms.bin\",\"header\":\"NMF1 plus LEu32[1,9,2,480,12],24bytes\",\"coefficient_encoding\":\"uint64 12nibbles rowmajor2x6; inputsVAx,VAy,VBx,VBy,VDx,VDy; GF9labels0..8\",\"slot_encoding\":\"rootbase*240+targetbase*120+q; q=z+5h; h=u+3v\",\"models\":[";
 int overallmin=INT_MAX;long long overalltotal=0,allwords=0;
 for(int model=0;model<models;model++){
  int scalar;in>>scalar;assert(scalar==(model?8:4));for(auto&row:steps)for(auto&s:row)in>>s.dart>>s.to>>s.shift;
  for(auto&v:forms)v.clear();words=0;
  for(rootbase=0;rootbase<2;rootbase++){long long before=words;visit(120*rootbase,0,-1,0);assert(words-before==109226);}
  u32(bin,scalar);vector<int>counts(480);vector<size_t>offsets(480);long long total=0;int minimum=INT_MAX;
  for(int slot=0;slot<480;slot++){
   auto&v=forms[slot];sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());counts[slot]=v.size();minimum=min(minimum,counts[slot]);total+=v.size();
   u32(bin,slot);u32(bin,v.size());offsets[slot]=bin.tellp();for(auto c:v)u64(bin,c);
  }
  vector<int>priority(480);iota(priority.begin(),priority.end(),0);stable_sort(priority.begin(),priority.end(),[&](int a,int b){return counts[a]<counts[b];});
  if(model)meta<<',';meta<<"{\"scalar\":"<<scalar<<",\"minimum_forms\":"<<minimum<<",\"total_distinct_forms\":"<<total<<",\"whole_model_capacity_excluded\":"<<(minimum<81?"true":"false")<<",\"word_paths\":"<<words<<",\"slots\":[";
  for(int slot=0;slot<480;slot++){if(slot)meta<<',';int q=slot%120;meta<<"{\"slot\":"<<slot<<",\"root_base\":"<<slot/240<<",\"target_base\":"<<(slot%240)/120<<",\"z\":"<<q%5<<",\"H\":"<<q/5<<",\"count\":"<<counts[slot]<<",\"form_byte_offset\":"<<offsets[slot]<<'}';}
  meta<<"],\"priority_slot_ids\":[";for(int i=0;i<480;i++){if(i)meta<<',';meta<<priority[i];}meta<<"]}";
  overallmin=min(overallmin,minimum);overalltotal+=total;allwords+=words;
  cout<<"scalar="<<scalar<<" min="<<minimum<<" forms="<<total<<" words="<<words<<'\n';
 }
 double cpu=double(clock()-start)/CLOCKS_PER_SEC;
 meta<<"],\"minimum_forms\":"<<overallmin<<",\"total_distinct_forms\":"<<overalltotal<<",\"word_paths\":"<<allwords<<",\"native_CPU_seconds\":"<<cpu<<",\"parameter_evaluations\":0,\"graphs\":0,\"BFS\":0}\n";
 ofstream result(dir+"/FORMS_EXPORT_RESULT.json");result<<"{\"status\":\"READY_COMPLETE_TWO_MODEL_NORMAL6_MATRIX_FORMS\",\"binary\":\"normal6_matrix_forms.bin\",\"metadata\":\"normal6_matrix_forms.meta.json\",\"models\":2,\"slots_per_model\":480,\"words_per_root\":109226,\"word_paths_total\":"<<allwords<<",\"total_distinct_forms\":"<<overalltotal<<",\"minimum_forms\":"<<overallmin<<",\"native_CPU_seconds\":"<<cpu<<",\"parameter_evaluations\":0,\"graphs\":0,\"BFS\":0}\n";
}
