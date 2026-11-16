// Finite inputs for the universal cross routing proof. No graph BFS.
#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using V=array<unsigned char,7>;
using L=array<int,10>;
const int N=66430;
int A[9][9],M[9][9],negateF[9],inverseF[9];
void require(bool b,const char*why){if(!b)throw runtime_error(why);}
int code(const V&p){int n=0;for(int x:p)n=9*n+x;return n;}
V normalize(V p){int first=0;while(first<7&&!p[first])first++;require(first<7,"zero point");int factor=inverseF[p[first]];for(auto&x:p)x=M[factor][x];return p;}
int norm(const V&p){int t=0;for(int i=0;i<3;i++)t=A[t][M[p[i]][p[i+4]]];return A[t][negateF[M[p[3]][p[3]]]];}
V cross(const V&p,const V&q){V r{};for(int i=0;i<3;i++){int j=(i+1)%3,k=(i+2)%3;
 r[i]=A[A[M[p[3]][q[i]]][negateF[M[q[3]][p[i]]]]][A[M[p[4+j]][q[4+k]]][negateF[M[p[4+k]][q[4+j]]]]];
 r[4+i]=A[A[M[q[3]][p[4+i]]][negateF[M[p[3]][q[4+i]]]]][A[M[p[j]][q[k]]][negateF[M[p[k]][q[j]]]]];
 r[3]=A[r[3]][A[M[p[i]][q[4+i]]][negateF[M[p[4+i]][q[i]]]]];}return r;}
template<class T>vector<T>read(const string&p,int count){ifstream f(p,ios::binary);vector<T>x(count);f.read((char*)x.data(),count*sizeof(T));require(bool(f)&&f.peek()==EOF,"binary size");return x;}
int main(int argc,char**argv){try{require(argc==3,"input output");double start=double(clock())/CLOCKS_PER_SEC;string input=argv[1],out=argv[2];
 for(int a=0;a<9;a++)for(int b=0;b<9;b++){A[a][b]=(a%3+b%3)%3+3*((a/3+b/3)%3);M[a][b]=((a%3*(b%3)-a/3*(b/3))%3+3)%3+3*((a%3*(b/3)+a/3*(b%3))%3);if(!A[a][b])negateF[a]=b;if(a&&M[a][b]==1)inverseF[a]=b;}
 auto points=read<V>(input+"/point_coords.u8.bin",N);auto lines=read<L>(input+"/line_points.i32.bin",N);
 vector<int>index(4782969,-1);for(int p=0;p<N;p++){require(normalize(points[p])==points[p]&&norm(points[p])==0,"point not normalized null");int key=code(points[p]);require(index[key]<0,"duplicate coordinates");index[key]=p;}
 vector<vector<int>>inc(N);
 for(int i=0;i<N;i++){
  const auto&line=lines[i];require(is_sorted(line.begin(),line.end())&&adjacent_find(line.begin(),line.end())==line.end(),"line repeated point");require(i==0||lines[i-1]<line,"duplicate or unsorted projective line");
  for(int p:line)require(p>=0&&p<N,"line point id");auto p=points[line[0]],q=points[line[1]];require(p!=q&&cross(p,q)==V{},"basis not Tits collinear");
  L span;for(int c=0;c<9;c++){V v{};for(int j=0;j<7;j++)v[j]=A[p[j]][M[c][q[j]]];int found=index[code(normalize(v))];require(found>=0,"span point absent");span[c]=found;}span[9]=line[1];sort(span.begin(),span.end());require(span==line,"cache line differs from complete projective span");
  for(int a:line)inc[a].push_back(i);
 }
 vector<int>star;star.reserve(100);for(int p=0;p<N;p++){require(inc[p].size()==10,"point degree not10");star.clear();for(int l:inc[p])star.insert(star.end(),lines[l].begin(),lines[l].end());sort(star.begin(),star.end());star.erase(unique(star.begin(),star.end()),star.end());require(star.size()==91&&binary_search(star.begin(),star.end(),p),"local star not91");}
 ofstream f(out);f<<"{\"status\":\"ALL_FINITE_CROSS_ROUTING_INPUTS_PASS\",\"points_checked\":66430,\"coordinate_map_injective\":true,\"all_points_nonzero_normalized_null\":true,\"lines_checked\":66430,\"every_line_full_projective_span\":true,\"every_line_basis_cross_zero\":true,\"projective_lines_distinct\":true,\"point_incidence_degrees\":10,\"all_local_projective_stars\":91,\"source_BFS\":0,\"geometry_regenerated\":false,\"new_graphs\":0,\"Lean\":0,\"CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";cout<<"PASS all66430 finite point/line/star bindings\n";return 0;
 }catch(const exception&e){cerr<<e.what()<<'\n';return 1;}}
