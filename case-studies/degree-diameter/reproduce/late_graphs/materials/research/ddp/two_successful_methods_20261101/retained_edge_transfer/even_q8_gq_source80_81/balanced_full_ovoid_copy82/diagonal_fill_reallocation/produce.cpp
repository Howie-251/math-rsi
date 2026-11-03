#include <cstdio>
#include <cstdlib>
#include <vector>
#include <array>
#include <map>
#include <utility>
struct Reader {
  FILE*f;char b[1<<20];size_t at=0,n=0;
  int get(){if(at==n){n=fread(b,1,sizeof(b),f);at=0;if(!n)return EOF;}return b[at++];}
  bool next(int&v){int c;do{c=get();if(c==EOF)return false;}while(c<=32);v=0;do{v=v*10+c-'0';c=get();}while(c>32&&c!=EOF);return true;}
};
struct Writer {
  FILE*f;char b[1<<20];size_t n=0;
  void flush(){if(n){if(fwrite(b,1,n,f)!=n)std::abort();n=0;}}
  void number(int x){char t[16];int k=0;do{t[k++]=char('0'+x%10);x/=10;}while(x);while(k)b[n++]=t[--k];}
  void pair(int a,int c){if(n+32>sizeof(b))flush();number(a);b[n++]=' ';number(c);b[n++]='\n';}
};
static void require(bool p){if(!p)std::abort();}
int main(int argc,char**argv){
  require(argc==4);
  constexpr int oldn=346515,newn=346516,m=14204970,fill=342225,source_n=342290,hub=346515;
  std::array<int,65>target;target.fill(-1);
  FILE*df=fopen(argv[3],"r");require(df);int j,c,dc=0;
  while(fscanf(df,"%d%d",&j,&c)==2){require(j>=0&&j<65&&target[j]<0&&c>=342290&&c<oldn);target[j]=c;++dc;}fclose(df);require(dc==65);
  FILE*in=fopen(argv[1],"rb");FILE*out=fopen(argv[2],"wb");require(in&&out);Reader rd{in};Writer wr{out};int n0,m0;require(rd.next(n0)&&rd.next(m0)&&n0==oldn&&m0==m);
  wr.pair(newn,m);std::vector<unsigned short>degree(newn,0);std::array<bool,65>removed{};
  int oldcount=0,written=0,oldsource=0,keptsource=0,nextadd=0,removedcount=0;std::pair<int,int>prev{-1,-1},prevout{-1,-1};
  auto emit=[&](int a,int b){require(a>=0&&a<b&&b<newn&&prevout<std::make_pair(a,b));prevout={a,b};wr.pair(a,b);++degree[a];++degree[b];++written;if(b<source_n)++keptsource;};
  int a,b;
  while(rd.next(a)){require(rd.next(b));require(a>=0&&a<b&&b<oldn&&prev<std::make_pair(a,b));prev={a,b};++oldcount;if(b<source_n)++oldsource;
    while(nextadd<65&&fill+nextadd<a){emit(fill+nextadd,hub);++nextadd;}
    if(a>=fill&&a<fill+65&&b==target[a-fill]){require(!removed[a-fill]);removed[a-fill]=true;++removedcount;}
    else emit(a,b);
  }
  while(nextadd<65){emit(fill+nextadd,hub);++nextadd;}
  wr.flush();require(fclose(out)==0);fclose(in);
  require(oldcount==m&&written==m&&removedcount==65&&oldsource==13862745&&keptsource==oldsource);
  std::map<int,int>hist;for(int d:degree)++hist[d];require(hist==std::map<int,int>{{65,1},{80,65},{81,4225},{82,342225}});
  require(degree[hub]==65);for(int x=0;x<65;++x)require(degree[target[x]]==80&&degree[fill+x]==82);
  printf("{\"status\":\"FIXED346516_STREAM_PRODUCER_PASS\",\"n\":%d,\"m\":%d,\"max_degree\":82,\"source_H_edges_retained\":%d,\"input_edges_parsed\":%d,\"deleted\":%d,\"inserted\":65,\"output_edges\":%d,\"degree_histogram\":{\"65\":1,\"80\":65,\"81\":4225,\"82\":342225},\"BFS_runs\":0}\n",newn,m,keptsource,oldcount,removedcount,written);
}
