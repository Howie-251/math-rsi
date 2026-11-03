using Mat=std::array<int,4>;
Mat mm(Mat a,Mat b){return{FA[FM[a[0]][b[0]]][FM[a[1]][b[2]]],FA[FM[a[0]][b[1]]][FM[a[1]][b[3]]],FA[FM[a[2]][b[0]]][FM[a[3]][b[2]]],FA[FM[a[2]][b[1]]][FM[a[3]][b[3]]]};}
int mv(Mat a,int v){return FA[FM[a[0]][v%9]][FM[a[1]][v/9]]+9*FA[FM[a[2]][v%9]][FM[a[3]][v/9]];}
bool verify_candidate(int scalar,const std::array<int,6>&t,const std::string&dir){
 using namespace std;const int GN=9720,N=19440;Mat I={1,0,0,1},K={1,2,0,2},beta={0,2,1,2},alpha;
 for(int k=0;k<4;k++)alpha[k]=FM[scalar][K[k]];
 array<Mat,9>ap;array<Mat,4>bp;ap[0]=bp[0]=I;for(int v=1;v<=8;v++)ap[v]=mm(ap[v-1],alpha);for(int u=1;u<=3;u++)bp[u]=mm(bp[u-1],beta);
 assert(ap[8]==I&&bp[3]==I&&mm(alpha,beta)==mm(bp[2],alpha));
 array<Mat,24>rho;for(int v=0;v<8;v++)for(int u=0;u<3;u++)rho[u+3*v]=mm(bp[u],ap[v]);
 int chi[8];chi[0]=1;for(int v=1;v<8;v++)chi[v]=chi[v-1]*2%5;
 auto hm=[](int h,int k){int u=h%3,v=h/3,a=k%3,b=k/3;return(u+(v%2?-a:a)+3)%3+3*((v+b)%8);};
 auto qm=[&](int q,int r){int z=q%5,h=q/5,w=r%5,k=r/5;return(z+chi[h/3]*w)%5+5*hm(h,k);};
 auto vneg=[](int v){return FN[v%9]+9*FN[v/9];};
 array<int,9>vq={0,66,74,114,22,15,105,69,71},vv={};
 vv[1]=t[0]+9*t[1];vv[3]=t[2]+9*t[3];vv[7]=t[4]+9*t[5];
 for(int pos:{1,3,5,7}){int neg=pos+1,h=vq[pos]/5,u=h%3,v=h/3,hi=(-(v%2?-1:1)*u+3)%3+3*((8-v)%8),zi=(5-chi[hi/3]*(vq[pos]%5)%5)%5;
  assert(vq[neg]==zi+5*hi);vv[neg]=vneg(mv(rho[hi],vv[pos]));assert(qm(vq[pos],vq[neg])==0);
 }
 array<array<int,9>,120>qnext;array<array<int,9>,24>shift;array<array<int,81>,81>vadd;
 for(int q=0;q<120;q++)for(int k=0;k<9;k++)qnext[q][k]=qm(q,vq[k]);
 for(int h=0;h<24;h++)for(int k=0;k<9;k++)shift[h][k]=mv(rho[h],vv[k]);
 for(int x=0;x<81;x++)for(int y=0;y<81;y++)vadd[x][y]=FA[x%9][y%9]+9*FA[x/9][y/9];
 const int targets[2][5]={{1,1,1,0,0},{0,0,0,1,1}},darts[2][5]={{0,1,3,5,6},{0,2,4,7,8}};
 vector<array<int,5>>adj(N);
 for(int node=0;node<N;node++){int base=node/GN,g=node%GN,z=g%81,q=g/81,h=q/5;
  for(int k=0;k<5;k++){int d=darts[base][k];adj[node][k]=targets[base][k]*GN+81*qnext[q][d]+vadd[z][shift[h][d]];}
  auto row=adj[node];sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end()&&find(row.begin(),row.end(),node)==row.end());}
 for(int u=0;u<N;u++)for(int v:adj[u])assert(find(adj[v].begin(),adj[v].end(),u)!=adj[v].end());
 bool pass=true;int globalD=0;ofstream result(dir+"/ACTUAL_GRAPH_RESULT.json");result<<"{\"scalar\":"<<scalar<<",\"n\":19440,\"m\":48600,\"degree\":5,\"simple\":true,\"undirected\":true,\"roots\":[";
 for(int rb=0;rb<2;rb++){vector<int>d(N,-1),queue(N);int lo=0,hi=0,root=rb*GN;d[root]=0;queue[hi++]=root;while(lo<hi){int u=queue[lo++];for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;queue[hi++]=v;}}
  int ecc=*max_element(d.begin(),d.end());globalD=max(globalD,ecc);pass&=hi==N&&ecc<=8;vector<int>hist(ecc+1);for(int x:d)if(x>=0)hist[x]++;
  if(rb)result<<',';result<<"{\"root\":"<<root<<",\"visited\":"<<hi<<",\"eccentricity\":"<<ecc<<",\"distance_histogram\":[";
  for(size_t j=0;j<hist.size();j++){if(j)result<<',';result<<hist[j];}result<<"]}";
 }
 result<<"],\"accepted_D8\":"<<(pass?"true":"false")<<",\"actual_global_D\":"<<globalD<<",\"complete_orbit_root_BFS\":2,\"voltage_ids\":[";
 for(int k=0;k<9;k++){if(k)result<<',';result<<81*vq[k]+vv[k];}result<<"]}\n";
 if(pass){ofstream edges(dir+"/graph_d5_D8_n19440.edges");edges<<"19440 48600\n";long long count=0;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){edges<<u<<' '<<v<<'\n';++count;}assert(count==48600);}
 return pass;
}
