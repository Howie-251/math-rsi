#include <array>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
int main() {
  std::ifstream in("DISTINCT_FORMS.tsv");
  std::string line; std::getline(in,line);
  std::vector<std::array<int,7>> forms;
  while(std::getline(in,line)) {
    std::istringstream s(line);int a,b;s>>a>>b;
    std::array<int,7> f{};for(int &v:f)s>>v;
    if(a==0&&b==0)forms.push_back(f);
  }
  if(forms.size()!=50)return 2;
  std::cout<<"{\"status\":\"COMPLETE_M50_ROOT00_NECESSARY_RESIDUE_GATE\",\"forms\":50,\"moduli\":[";
  bool first=true;
  for(int q:{2,5}) {
    int total=1;for(int i=0;i<6;i++)total*=q;
    int pass=0;std::array<int,5> perA{};
    std::ofstream out("M50_MOD"+std::to_string(q)+"_PASS_PROFILES.tsv");
    out<<"alpha0\talpha1\talpha2\tsigma\ttau\trho\n";
    for(int z=0;z<total;z++) {
      int z0=z;std::array<int,6> v{};
      for(int &x:v){x=z0%q;z0/=q;}
      std::array<int,5> count{};
      for(auto f:forms) {
        int t=f[6]*(25%q);for(int i=0;i<6;i++)t+=f[i]*v[i];
        t%=q;if(t<0)t+=q;count[t]++;
      }
      bool ok=true;for(int i=0;i<q;i++)if(count[i]!=50/q)ok=false;
      if(ok){pass++;perA[v[0]]++;for(int i=0;i<6;i++){if(i)out<<'\t';out<<v[i];}out<<'\n';}
    }
    if(!first)std::cout<<',';first=false;
    std::cout<<"{\"q\":"<<q<<",\"tested\":"<<total<<",\"passing\":"<<pass<<",\"passing_per_alpha0_residue\":[";
    for(int i=0;i<q;i++){if(i)std::cout<<',';std::cout<<perA[i];}
    std::cout<<"]}";
  }
  std::cout<<"],\"controller_searches\":0,\"graphs\":0}\n";
}
