#include <bits/stdc++.h>
using namespace std;
const int N=66430; int A[9][9],M[9][9],NI[9],IV[9];
using P=array<unsigned char,7>; using L=array<int,10>;
double cpu(){return double(clock())/CLOCKS_PER_SEC;} double limitCPU;
void check(){if(cpu()>limitCPU)throw runtime_error("UNKNOWN_CPU_LIMIT");}
int code(const P&x){int c=0;for(int a:x)c=c*9+a;return c;}
P norm(P x){int s=0;while(s<7&&!x[s])s++;if(s==7)throw runtime_error("zero coordinate");int t=IV[x[s]];for(auto&v:x)v=M[t][v];return x;}
template<class T> vector<T> binary(const string&path,size_t count){ifstream f(path,ios::binary);vector<T>x(count);f.read((char*)x.data(),count*sizeof(T));if(!f||f.peek()!=EOF)throw runtime_error("binary size "+path);return x;}
int main(int argc,char**argv){try{
 if(argc!=3)return 2;string out=argv[1];limitCPU=stod(argv[2]);double start=cpu();
 for(int a=0;a<9;a++)for(int b=0;b<9;b++){
  A[a][b]=(a%3+b%3)%3+3*((a/3+b/3)%3);
  M[a][b]=((a%3*(b%3)-a/3*(b/3))%3+3)%3+3*((a%3*(b/3)+a/3*(b%3))%3);
 }for(int a=0;a<9;a++){for(int b=0;b<9;b++){if(A[a][b]==0)NI[a]=b;if(a&&M[a][b]==1)IV[a]=b;}}
 auto pts=binary<P>(out+"/point_coords.u8.bin",N);auto tau=binary<int>(out+"/tau.i32.bin",2*N);
 auto pi=binary<unsigned short>(out+"/pi.u16.bin",N);auto eps=binary<unsigned char>(out+"/eps.u8.bin",N);
 vector<int>idx(4782969,-1);for(int p=0;p<N;p++){if(norm(pts[p])!=pts[p])throw runtime_error("unnormalized");idx[code(pts[p])]=p;}
 int eq[6][4]={{1,2,3,4},{5,4,3,2},{2,0,3,5},{6,5,3,0},{0,1,3,6},{4,6,3,1}};
 vector<L>lines;lines.reserve(N);
 for(int xp=0;xp<N;xp++){
  if(xp%128==0)check();auto x=pts[xp];int rows[6][7]={};
  for(int k=0;k<6;k++){auto e=eq[k];rows[k][e[1]]=A[rows[k][e[1]]][x[e[0]]];rows[k][e[0]]=A[rows[k][e[0]]][NI[x[e[1]]]];rows[k][e[3]]=A[rows[k][e[3]]][NI[x[e[2]]]];rows[k][e[2]]=A[rows[k][e[2]]][x[e[3]]];}
  vector<int>pivot;int rank=0;
  for(int c=0;c<7;c++){int pr=rank;while(pr<6&&!rows[pr][c])pr++;if(pr==6)continue;for(int j=0;j<7;j++)swap(rows[pr][j],rows[rank][j]);int iv=IV[rows[rank][c]];for(int j=0;j<7;j++)rows[rank][j]=M[iv][rows[rank][j]];
   for(int i=0;i<6;i++)if(i!=rank&&rows[i][c]){int f=rows[i][c];for(int j=0;j<7;j++)rows[i][j]=A[rows[i][j]][NI[M[f][rows[rank][j]]]];}pivot.push_back(c);rank++;
  }
  if(rank!=4)continue;vector<P>basis;
  for(int c=0;c<7;c++)if(find(pivot.begin(),pivot.end(),c)==pivot.end()){P b{};b[c]=1;for(int i=0;i<rank;i++)b[pivot[i]]=NI[rows[i][c]];basis.push_back(b);}
  array<int,91>plane;int count=0;
  for(int lead=0;lead<3;lead++)for(int a=0;a<(lead==0?9:1);a++)for(int b=0;b<(lead<2?9:1);b++){
   P v{};for(int j=0;j<7;j++)v[j]=lead==0?A[A[basis[0][j]][M[a][basis[1][j]]]][M[b][basis[2][j]]]:lead==1?A[basis[1][j]][M[b][basis[2][j]]]:basis[2][j];
   int id=idx[code(norm(v))];if(id<0)throw runtime_error("kernel point off quadric");plane[count++]=id;
  }if(count!=91)throw runtime_error("PG2 count");sort(plane.begin(),plane.end());if(adjacent_find(plane.begin(),plane.end())!=plane.end())throw runtime_error("PG2 duplicate");
  array<bool,91>seen{};int through=0;
  for(int k=0;k<91;k++)if(plane[k]!=xp&&!seen[k]){
   P y=pts[plane[k]];L line;for(int t=0;t<9;t++){P z{};for(int j=0;j<7;j++)z[j]=A[x[j]][M[t][y[j]]];int id=idx[code(norm(z))];if(id<0)throw runtime_error("line off quadric");line[t]=id;}line[9]=plane[k];sort(line.begin(),line.end());
   if(adjacent_find(line.begin(),line.end())!=line.end())throw runtime_error("line duplicate");
   for(int id:line){auto it=lower_bound(plane.begin(),plane.end(),id);if(it==plane.end()||*it!=id)throw runtime_error("line outside Tits kernel");seen[it-plane.begin()]=true;}
   lines.push_back(line);through++;
  }if(through!=10)throw runtime_error("local10 lines");
  if(xp%4096==0){ofstream f(out+"/PROGRESS.json");f<<"{\"points_done\":"<<xp<<",\"lines_kept\":"<<lines.size()<<",\"CPU\":"<<cpu()<<"}\n";}
 }
 sort(lines.begin(),lines.end());lines.erase(unique(lines.begin(),lines.end()),lines.end());if(lines.size()!=N)throw runtime_error("global line domain "+to_string(lines.size()));
 vector<vector<int>>padj(N);for(int l=0;l<N;l++)for(int p:lines[l])padj[p].push_back(N+l);
 vector<int>tinv(2*N,-1);for(int u=0;u<2*N;u++){int v=tau[u];if(v<0||v>=2*N||tinv[v]!=-1||(u<N)==(v<N))throw runtime_error("tau permutation/part");tinv[v]=u;}
 int fix2=0;for(int u=0;u<2*N;u++){if(tau[tau[tau[tau[u]]]]!=u)throw runtime_error("tau order4");fix2+=tau[tau[u]]==u;}
 if(fix2!=728)throw runtime_error("tau fixed728");
 for(int p=0;p<N;p++){if(padj[p].size()!=10)throw runtime_error("incidence point degree");L image;for(int j=0;j<10;j++)image[j]=tau[padj[p][j]];sort(image.begin(),image.end());if(image!=lines[tau[p]-N])throw runtime_error("tau actual incidence");}
 check();double geometryCPU=cpu()-start;{ofstream f(out+"/line_points.i32.bin",ios::binary);f.write((char*)lines.data(),N*sizeof(L));}
 vector<pair<int,int>>edges;edges.reserve(210000);vector<int>sigma(N);int maxpi=-1;
 for(int p=0;p<N;p++){int l=eps[p]?tau[p]:tinv[p];sigma[p]=l;maxpi=max(maxpi,int(pi[p]));for(int q:lines[l-N])if(q!=p){int u=pi[p],v=pi[q];if(u==v)throw runtime_error("merged loop");edges.emplace_back(min(u,v),max(u,v));}}
 if(maxpi!=37470)throw runtime_error("core n");sort(edges.begin(),edges.end());edges.erase(unique(edges.begin(),edges.end()),edges.end());int corem=edges.size();
 {ofstream f(out+"/sigma.i32.bin",ios::binary);f.write((char*)sigma.data(),N*sizeof(int));}
 ifstream sf(out+"/source.edges");int sn,sm;sf>>sn>>sm;if(sn!=37631)throw runtime_error("source n");int a,b,oldcount=0,outer=0;
 while(sf>>a>>b){oldcount++;if(a>=37471||b>=37471){edges.emplace_back(min(a,b),max(a,b));outer++;}}if(oldcount!=sm)throw runtime_error("source m");
 ifstream pf(out+"/pins.txt");vector<int>pins;while(pf>>a)pins.push_back(a);if(pins.size()!=10)throw runtime_error("10pins");for(int p:pins)edges.emplace_back(p,37631);
 sort(edges.begin(),edges.end());if(adjacent_find(edges.begin(),edges.end())!=edges.end())throw runtime_error("duplicate full edge");vector<int>degrees(37632);for(auto[u,v]:edges){if(u<0||v>=37632||u==v)throw runtime_error("full edge");degrees[u]++;degrees[v]++;}
 int maxd=*max_element(degrees.begin(),degrees.end());
 {ofstream f(out+"/candidate37632.edges");f<<37632<<' '<<edges.size()<<'\n';for(auto[u,v]:edges)f<<u<<' '<<v<<'\n';}
 {ofstream f(out+"/degrees.u8.bin",ios::binary);for(int d:degrees)f.put(char(d));}
 check();ofstream f(out+"/NATIVE_RESULT.json");f<<"{\"status\":\"TRUE_SIGMA_CORE_BOUND\",\"n\":37632,\"m\":"<<edges.size()<<",\"core_n\":37471,\"core_m\":"<<corem<<",\"retained_exterior_edges\":"<<outer<<",\"new_pins\":10,\"max_degree\":"<<maxd<<",\"actual_geometry_tau_verified\":true,\"line_count\":66430,\"incidence_degree\":10,\"tau_order\":4,\"tau2_fixed\":728,\"geometry_CPU\":"<<geometryCPU<<",\"native_CPU\":"<<cpu()-start<<",\"peripheral_distance_checked\":false,\"old_sigma_identity_claimed\":false}\n";
 cout<<"TRUE_SIGMA_CORE_BOUND n37632 maxdegree"<<maxd<<" CPU"<<cpu()-start<<endl;return 0;
 }catch(const exception&e){cerr<<e.what()<<endl;return 1;}}
