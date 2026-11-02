#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
int stepq[816][6],invport[6];uint32_t shifts[48][6];uint8_t addpair[65536];
vector<uint32_t>forms[816];long long words=0;
uint32_t pluscode(uint32_t a,uint32_t b){
 return uint32_t(addpair[((a&255)<<8)|(b&255)])
 |uint32_t(addpair[(((a>>8)&255)<<8)|((b>>8)&255)])<<8
 |uint32_t(addpair[(((a>>16)&255)<<8)|((b>>16)&255)])<<16
 |uint32_t(addpair[((a>>24)<<8)|(b>>24)])<<24;
}
void visit(int q,uint32_t code,int last,int depth){
 forms[q].push_back(code);words++;if(depth==8)return;int h=q/17;
 for(int s=0;s<6;s++)if(last<0||s!=invport[last])visit(stepq[q][s],pluscode(code,shifts[h][s]),s,depth+1);
}
void u32(ostream&f,uint32_t x){char b[4];for(int i=0;i<4;i++)b[i]=(x>>(8*i))&255;f.write(b,4);}
int main(int argc,char**argv){
 assert(argc==3);clock_t start=clock();rlimit lim{2,2};setrlimit(RLIMIT_CPU,&lim);ifstream in(argv[1]);string out=argv[2];int q,h,k;in>>q>>h>>k;assert(q==816&&h==48&&k==6);
 for(int&i:invport)in>>i;for(auto&row:stepq)for(int&i:row)in>>i;for(auto&row:shifts)for(auto&i:row)in>>i;
 for(int a=0;a<256;a++)for(int b=0;b<256;b++)addpair[(a<<8)|b]=((a%16+b%16)%11)|((((a>>4)+(b>>4))%11)<<4);
 visit(0,0,-1,0);assert(words==585937);
 ofstream binary(out+"/q11_matrix_forms.bin",ios::binary);binary.write("QMF1",4);for(uint32_t x:{1,11,816,2,4})u32(binary,x);
 vector<size_t>offsets(816);vector<int>counts(816);long long total=0;int minimum=INT_MAX;
 for(int q=0;q<816;q++){
  auto&v=forms[q];sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());counts[q]=v.size();minimum=min(minimum,counts[q]);total+=v.size();
  u32(binary,q);u32(binary,v.size());offsets[q]=binary.tellp();for(auto code:v)u32(binary,code);
 }
 vector<int>priority(816);iota(priority.begin(),priority.end(),0);stable_sort(priority.begin(),priority.end(),[&](int a,int b){return counts[a]<counts[b];});
 ofstream f(out+"/q11_matrix_forms.meta.json");f<<"{\"status\":\"READY_COMPLETE_Q11_GENERIC_MATRIX_FORMS\",\"binary\":\"q11_matrix_forms.bin\",\"header\":\"QMF1 plusLEu32[1,11,816,2,4],24bytes\",\"slot_stream\":\"LEu32[slot,count] then countLEu32packedforms\",\"coefficient_encoding\":\"8nibbles rowmajor2x4,inputsVBx,VBy,VCx,VCy; normaloutputrowsx/y;coefficients0..10\",\"Q_encoding\":\"q=17h+c,h=u+3v\",\"words_length0through8\":"<<words<<",\"minimum_forms\":"<<minimum<<",\"total_distinct_forms\":"<<total<<",\"whole_family_capacity_excluded\":"<<(minimum<121?"true":"false")<<",\"slots\":[";
 for(int q=0;q<816;q++){if(q)f<<',';f<<"{\"slot\":"<<q<<",\"H\":"<<q/17<<",\"c17\":"<<q%17<<",\"count\":"<<counts[q]<<",\"form_byte_offset\":"<<offsets[q]<<'}';}
 f<<"],\"priority_slot_ids\":[";for(int i=0;i<816;i++){if(i)f<<',';f<<priority[i];}f<<"],\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"parameter_evaluations\":0,\"graph_generation\":false,\"BFS\":0}\n";
 cout<<"READY matrixforms min="<<minimum<<" total="<<total<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
