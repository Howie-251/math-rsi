#include <algorithm>
#include <cassert>
#include <chrono>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>

// Fixed second-copy extension. All original edges are streamed unchanged;
// each old row's new edge comes after its original smaller-labelled neighbors.
int main(int argc, char** argv) {
  assert(argc == 3);
  constexpr int oldN=346516, oldU=342225, firstClone=342290;
  constexpr int centers=4225, newN=350742, newHub=350741;
  constexpr long long oldM=14204970, newM=14547195;
  std::ifstream in(argv[1]); std::ofstream out(argv[2]);
  assert(in.good() && out.good());
  int n; long long m; in >> n >> m; assert(n==oldN && m==oldM);
  out << newN << ' ' << newM << '\n';
  std::vector<int> deg(newN), oldDeg(oldN), copyDegree(centers);
  int row=-1, extra=-1, prevU=-1, prevV=-1, writeU=-1, writeV=-1;
  long long oldEdges=0, newEdges=0, total=0, copiedPins=0, hubPins=0;
  auto write=[&](int a,int b,bool added) {
    assert(0<=a && a<b && b<newN);
    assert(a>writeU || (a==writeU && b>writeV));
    out << a << ' ' << b << '\n';
    ++deg[a]; ++deg[b]; ++total; writeU=a;writeV=b;
    if(added) ++newEdges;
  };
  auto flush=[&]() {
    if(row<0) return;
    if(oldU<=row && row<firstClone) {
      assert(extra<0); write(row,newHub,true); ++hubPins;
    } else if(extra>=0) {
      write(row,extra,true); ++copyDegree[extra-oldN]; ++copiedPins;
    }
    extra=-1;
  };
  int u,v;
  while(in >> u >> v) {
    assert(0<=u && u<v && v<oldN);
    assert(u>prevU || (u==prevU && v>prevV));
    if(u!=row) { flush(); row=u; }
    if(u<oldU && firstClone<=v && v<firstClone+centers) {
      assert(extra<0); extra=oldN+(v-firstClone);
    }
    write(u,v,false); ++oldEdges; ++oldDeg[u]; ++oldDeg[v];
    prevU=u;prevV=v;
  }
  assert(in.eof()); flush(); out.close(); assert(out.good());
  assert(oldEdges==oldM && copiedPins==342160 && hubPins==65);
  assert(newEdges==342225 && total==newM);
  std::map<int,int> hist, oldHist, copyHist;
  for(int d:deg) ++hist[d];
  for(int d:oldDeg) ++oldHist[d];
  for(int h=0;h<centers;++h) {
    assert(copyDegree[h]==oldDeg[firstClone+h]);
    assert(deg[oldN+h]==copyDegree[h]); ++copyHist[copyDegree[h]];
  }
  assert((oldHist==std::map<int,int>{{65,1},{80,65},{81,4225},{82,342225}}));
  assert((copyHist==std::map<int,int>{{80,65},{81,4160}}));
  assert((hist==std::map<int,int>{{65,2},{80,130},{81,8385},{83,342225}}));
  assert(deg[newHub]==65 && deg[346515]==65);
  std::cout << "{\"status\":\"PRODUCER_PASS_PENDING_FRESH_ACCEPTANCE\","
    << "\"n\":" << newN << ",\"m\":" << newM
    << ",\"Delta\":83,\"source_parse\":1,\"source_edges_retained\":" << oldEdges
    << ",\"new_edges\":" << newEdges << ",\"new_U_clone_edges\":" << copiedPins
    << ",\"new_hub_F_edges\":" << hubPins
    << ",\"all4225_new_copy_lists_equal_actual_first_copy\":true"
    << ",\"header_strictlex_simple\":true,\"BFS_runs\":0"
    << ",\"degree_histogram\":{\"65\":2,\"80\":130,\"81\":8385,\"83\":342225}}\n";
}
