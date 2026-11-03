#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>

// Six independent ten-vertex fibers, uniform bipartite interface degrees.
// Every row has sum eight. Internal return capacity forces square sum >=17;
// summed cross-fiber capacity forces <=22. Parity makes the lower bound 18.
using Row = std::array<int,5>;
std::vector<Row> rows;
int q[6][6]{};
unsigned long long complete=0, surviving=0, nodes=0;
std::ofstream out;
std::clock_t start;
bool capped=false;

void make_rows(Row &r,int p,int sum,int sq) {
  if(p==5) {if(sum==8 && sq>=18 && sq<=22) rows.push_back(r); return;}
  for(int x=0;x<=4 && sum+x<=8;++x) {
    if(sq+x*x>22) continue;
    r[p]=x; make_rows(r,p+1,sum+x,sq+x*x);
  }
}
void dfs(int i) {
  if(capped) return;
  if((++nodes & 65535)==0 && double(std::clock()-start)/CLOCKS_PER_SEC>=10) {
    capped=true; return;
  }
  if(i==6) {
    ++complete;
    for(int a=0;a<6;++a) for(int b=a+1;b<6;++b) {
      int paths=q[a][b];
      for(int k=0;k<6;++k) paths+=q[a][k]*q[k][b];
      if(paths<10) return;
    }
    if(surviving++) out << ",\n";
    out << "[";
    for(int a=0;a<6;++a) {
      if(a) out << ",";
      out << "[";
      for(int b=0;b<6;++b) {if(b) out << ",";out << q[a][b];}
      out << "]";
    }
    out << "]";
    return;
  }
  for(const auto &r: rows) {
    bool fits=true;
    for(int j=0;j<i;++j) if(r[j]!=q[i][j]) {fits=false;break;}
    if(!fits) continue;
    for(int j=i+1;j<6;++j) q[i][j]=q[j][i]=r[j-1];
    dfs(i+1);
    if(capped) return;
  }
}
int main(int argc,char **argv) {
  if(argc!=2) return 2;
  Row r{};make_rows(r,0,0,0);
  out.open(argv[1]);out << "{\"matrices\":[\n";
  start=std::clock();dfs(0);
  const double cpu=double(std::clock()-start)/CLOCKS_PER_SEC;
  out << "\n],\"row_patterns\":" << rows.size()
      << ",\"row_compatible_labeled_matrices\":" << complete
      << ",\"survivors\":" << surviving
      << ",\"nodes\":" << nodes
      << ",\"status\":\"" << (capped?"CPU_LIMIT":"COMPLETE")
      << "\",\"cpu_seconds\":" << cpu << "}\n";
  std::cout << "rows="<<rows.size()<<" complete="<<complete
            <<" survivors="<<surviving<<" cpu="<<cpu
            <<" status="<<(capped?"CPU_LIMIT":"COMPLETE")<<"\n";
}
