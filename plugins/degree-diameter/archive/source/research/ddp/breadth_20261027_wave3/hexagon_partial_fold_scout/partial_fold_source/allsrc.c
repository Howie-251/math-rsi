/* An all-sources BFS in C, sharing no code with verify_witness.py, so that a claimed
   (n, d, k) can be checked twice by two independent implementations. That is the standing
   rule for anything entering this note: rebuild it in different code before writing it up.

   usage:  allsrc FILE EXPECT_N EXPECT_D EXPECT_K [HAS_HEADER]
   e.g.    xzcat anc/graph_d10k5_n33397_regular.edges.xz > reg.edges
           gcc -O2 -fopenmp -o allsrc anc/allsrc.c && ./allsrc reg.edges 33397 10 5 1

   It prints the degree range, the count of self-loops and duplicate adjacencies, the
   number of sources that cannot reach the whole graph, the full eccentricity histogram,
   and PASS or FAIL against the claim. A FAIL prints why. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>

int main(int argc,char**argv){
  if(argc<5){fprintf(stderr,"usage: %s FILE EXPECT_N EXPECT_D EXPECT_K [HAS_HEADER]\n",argv[0]);return 2;}
  const char*path=argv[1]; long EN=atol(argv[2]); int ED=atoi(argv[3]);
  int EK=atoi(argv[4]); int hdr = (argc>5)?atoi(argv[5]):0;
  FILE*f=fopen(path,"r"); if(!f){perror("open");return 2;}
  long cap=1<<20,ne=0; long*eu=malloc(cap*sizeof(long)),*ev=malloc(cap*sizeof(long));
  char line[256]; long maxid=-1; long hn=-1,hm=-1; int first=1;
  while(fgets(line,sizeof line,f)){
    long a,b; if(sscanf(line,"%ld %ld",&a,&b)!=2) continue;
    if(first&&hdr){hn=a;hm=b;first=0;continue;}
    first=0;
    if(ne==cap){cap*=2;eu=realloc(eu,cap*sizeof(long));ev=realloc(ev,cap*sizeof(long));}
    eu[ne]=a;ev[ne]=b;ne++;
    if(a>maxid)maxid=a; if(b>maxid)maxid=b;
  }
  fclose(f);
  long n=maxid+1;
  printf("parsed: n=%ld m=%ld", n, ne);
  if(hdr) printf("  (header said n=%ld m=%ld)", hn, hm);
  printf("\n");
  if(hdr && (hn!=n||hm!=ne)){printf("HEADER MISMATCH\n");return 1;}
  long*deg=calloc(n,sizeof(long));
  /* dedupe check + self loops */
  long selfloops=0;
  for(long i=0;i<ne;i++){ if(eu[i]==ev[i]){selfloops++;continue;} deg[eu[i]]++; deg[ev[i]]++; }
  long*off=malloc((n+1)*sizeof(long)); off[0]=0;
  for(long i=0;i<n;i++) off[i+1]=off[i]+deg[i];
  long*pos=malloc(n*sizeof(long)); memcpy(pos,off,n*sizeof(long));
  int*adj=malloc(off[n]*sizeof(int));
  for(long i=0;i<ne;i++){ if(eu[i]==ev[i])continue; adj[pos[eu[i]]++]=(int)ev[i]; adj[pos[ev[i]]++]=(int)eu[i]; }
  long mind=n,maxd=0; for(long i=0;i<n;i++){ if(deg[i]<mind)mind=deg[i]; if(deg[i]>maxd)maxd=deg[i]; }
  /* duplicate-edge detection */
  long dup=0;
  for(long v=0;v<n;v++){
    long s=off[v],e=off[v+1];
    /* insertion sort small lists */
    for(long i=s+1;i<e;i++){int x=adj[i];long j=i-1;while(j>=s&&adj[j]>x){adj[j+1]=adj[j];j--;}adj[j+1]=x;}
    for(long i=s+1;i<e;i++) if(adj[i]==adj[i-1]) dup++;
  }
  printf("degrees: min=%ld max=%ld  selfloops=%ld  duplicate_adjacencies=%ld\n",mind,maxd,selfloops,dup);
  long ecc_hist[64]; memset(ecc_hist,0,sizeof ecc_hist);
  long disconnected=0; int global_max=0;
  #pragma omp parallel
  {
    int*dist=malloc(n*sizeof(int)); int*q=malloc(n*sizeof(int));
    long loc[64]; memset(loc,0,sizeof loc); long locdis=0; int locmax=0;
    #pragma omp for schedule(dynamic,256)
    for(long s=0;s<n;s++){
      for(long i=0;i<n;i++) dist[i]=-1;
      long head=0,tail=0; dist[s]=0; q[tail++]=(int)s; int ecc=0; long seen=1;
      while(head<tail){ int u=q[head++]; int du=dist[u];
        for(long i=off[u];i<off[u+1];i++){ int w=adj[i]; if(dist[w]<0){dist[w]=du+1; if(du+1>ecc)ecc=du+1; q[tail++]=w; seen++;} } }
      if(seen<n) locdis++;
      if(ecc<64) loc[ecc]++;
      if(ecc>locmax) locmax=ecc;
    }
    #pragma omp critical
    { for(int i=0;i<64;i++) ecc_hist[i]+=loc[i]; disconnected+=locdis; if(locmax>global_max) global_max=locmax; }
    free(dist);free(q);
  }
  printf("disconnected sources: %ld\n",disconnected);
  printf("eccentricity histogram:");
  for(int i=0;i<64;i++) if(ecc_hist[i]) printf(" {%d: %ld}",i,ecc_hist[i]);
  printf("\nDIAMETER %d  MAXDEG %ld\n",global_max,maxd);
  int ok = (disconnected==0 && global_max<=EK && maxd<=ED && n==EN && dup==0 && selfloops==0);
  printf("CLAIM n=%ld d<=%d k<=%d : %s\n", EN, ED, EK, ok?"PASS":"FAIL");
  return ok?0:1;
}
