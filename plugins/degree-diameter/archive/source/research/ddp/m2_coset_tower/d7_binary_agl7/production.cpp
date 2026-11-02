#include "production_engine.hpp"
#include <iomanip>
static array<uint64_t,2688> RZERO,RONE,PTERM,QZERO,QONE;
void init_fast(){
    array<uint64_t,64> hm{},th{};for(int x=0;x<64;x++){for(int h:HCODE)hm[x]|=1ULL<<KACTION[h][x];th[x]=transform(hm[x],1);}
    for(int g=0;g<2688;g++){
        int x=g%64,t=KCOORD[g/64][0];PTERM[g]=hm[x];int y=KACTION[(7-t)%7][x];QZERO[g]=hm[y];QONE[g]=th[y];
        if(!t)RZERO[g]=hm[x];else {int ti=1;while(t*ti%7!=1)ti++;RONE[g]=1ULL<<KACTION[LCODE[ti]][x];}
    }
}
array<uint64_t,2> fast_masks(const Generators&S){
    uint64_t m0=1,m1=1;constexpr int reverse[6]={0,1,3,2,5,4};
    for(int a=0;a<6;a++){
        int s=S[a];m0|=PTERM[s]|QZERO[s]|RZERO[s];m1|=PTERM[s]|QONE[s]|RONE[s];
        for(int b=0;b<6;b++)if(b!=reverse[a]){
            int w=gp(s,S[b]);m0|=RZERO[w];m1|=RONE[w];
            for(int c=0;c<6;c++)if(c!=reverse[b]){int z=gp(w,S[c]);m0|=RZERO[z];m1|=RONE[z];}
        }
    }
    return {m0,m1};
}
Score actual_score(array<uint64_t,2> masks){
    Score z;z.bb=masks;array<int,3> roots{0,L,L+B};
    for(int t=0;t<3;t++){
        dist.fill(-1);int front=0,end=1;que[0]=roots[t];dist[roots[t]]=0;
        while(front<end){int v=que[front++];if(dist[v]==5)continue;for(int w:adj[v])if(dist[w]<0){dist[w]=dist[v]+1;que[end++]=w;}}
        for(int v=0;v<N;v++)if(dist[v]<0){z.miss[t]++;z.layer[t][v<L?0:v<L+B?1:2]++;}
    }
    z.bad=(2688LL*z.miss[0]+448LL*z.miss[1]+64LL*z.miss[2])/2;return z;
}
struct Stat{
    long long raw=0,hh=0,bb=0,scored=0,best=LLONG_MAX;int minbb=448;
    array<int,3> mins{N,N,N};array<long long,3> zeros{};array<array<int,3>,3> lmin{};array<array<long long,3>,3> lzero{};
    long long hb=0,hbb=0;
    Stat(){for(auto&r:lmin)r.fill(N);}
    void input(){raw++;hh++;}
    void filtered(int m){minbb=min(minbb,m);if(m==0)bb++;}
    void score(const Score&z){scored++;best=min(best,z.bad);for(int i=0;i<3;i++){
        mins[i]=min(mins[i],z.miss[i]);if(!z.miss[i])zeros[i]++;
        for(int j=0;j<3;j++){lmin[i][j]=min(lmin[i][j],z.layer[i][j]);if(!z.layer[i][j])lzero[i][j]++;}}
        if(!z.miss[2])hbb++;if(!z.miss[1]&&!z.miss[2])hb++;
    }
};
void write_stat(ostream&o,const Stat&s){
    o<<"{\"raw\":"<<s.raw<<",\"legal\":"<<s.raw<<",\"invalid\":0,\"HH_pass\":"<<s.hh<<",\"BB_pass\":"<<s.bb<<",\"scored\":"<<s.scored<<",\"min_BB_missing\":"<<s.minbb<<",\"root_minimum_missing\":";list(o,s.mins);
    o<<",\"root_zero_counts\":";list(o,s.zeros);o<<",\"layer_minimum_missing\":[";for(int i=0;i<3;i++){if(i)o<<',';list(o,s.lmin[i]);}o<<"],\"layer_zero_counts\":[";for(int i=0;i<3;i++){if(i)o<<',';list(o,s.lzero[i]);}
    o<<"],\"head_and_BB_zero\":"<<s.hbb<<",\"head_and_block_root_zero\":"<<s.hb<<",\"best_scored_bad_pairs\":";if(s.scored)o<<s.best;else o<<"null";o<<'}';
}
struct Branch{int apos;array<vector<array<int,2>>,4> cc;};
int main(int argc,char**argv){
    assert(argc==4);string mode=argv[1],base=argv[3];double limit=stod(argv[2]),start=cpu();init_fast();
    if(mode=="calibrate"){
        ifstream f(base+"/profile.inputs.txt");int n;f>>n;assert(n==1200);
        for(int i=0;i<n;i++){Generators S;for(int&x:S)f>>x;assert(f);assert(fast_masks(S)==bb_masks(S));}
        ofstream out(base+"/production.BB_calibration.json");out<<"{\"saved_inputs\":1200,\"exact_mask_matches\":1200,\"new_graph_expansions\":0,\"new_BFS\":0,\"cpu_seconds\":"<<cpu()-start<<"}\n";
        cout<<"Optimized BB masks match all 1200 existing inputs; no BFS.\n";return 0;
    }
    assert(mode=="run");ifstream f(base+"/production.scope.txt");int nb;f>>nb;assert(nb==6);vector<Branch> branches(nb);
    for(auto&b:branches){f>>b.apos;for(auto&c:b.cc){int n;f>>n;c.resize(n);for(auto&v:c)f>>v[0]>>v[1];}}assert(f);
    Stat global;array<Stat,6> perbranch;array<Stat,90> peranchor;
    int anchor=-1,curbranch=0,curai=0;array<int,3> cursub{};long long cursor=0,best=LLONG_MAX;
    string status="COMPLETE_NO_SOLUTION";double time_hh=0,time_bb=0,time_bfs=0,first_bfs=0;bool printed=false;
    for(int bi=0;bi<6;bi++){
        auto&b=branches[bi];array<int,3> positions{};int p=0;for(int i=0;i<4;i++)if(i!=b.apos)positions[p++]=i;
        for(int ai=0;ai<(int)b.cc[b.apos].size();ai++){
            anchor++;array<int,4> ix{};ix[b.apos]=ai;
            for(int i=0;i<(int)b.cc[positions[0]].size();i++)for(int j=0;j<(int)b.cc[positions[1]].size();j++)for(int k=0;k<(int)b.cc[positions[2]].size();k++){
                curbranch=bi;curai=ai;cursub={i,j,k};
                if((cursor&4095)==0&&cpu()-start>=limit){status="CPU_LIMIT";goto done;}
                bool timed=cursor<1000000;double t0=timed?cpu():0;
                ix[positions[0]]=i;ix[positions[1]]=j;ix[positions[2]]=k;
                Generators S{b.cc[0][ix[0]][0],b.cc[1][ix[1]][0],b.cc[2][ix[2]][0],b.cc[2][ix[2]][1],b.cc[3][ix[3]][0],b.cc[3][ix[3]][1]};
                // HH and legality are invariants of the four disjoint verified colour lists.
                global.input();perbranch[bi].input();peranchor[anchor].input();
                double t1=timed?cpu():0;auto masks=fast_masks(S);int missing=64-__builtin_popcountll(masks[0])+6*(64-__builtin_popcountll(masks[1]));
                double t2=timed?cpu():0;if(timed){time_hh+=t1-t0;time_bb+=t2-t1;}
                global.filtered(missing);perbranch[bi].filtered(missing);peranchor[anchor].filtered(missing);
                if(!missing){
                    double bs=cpu();build(S);Score z=actual_score(masks);double bt=cpu()-bs;time_bfs+=bt;if(timed)first_bfs+=bt;
                    assert(z.layer[1][1]==0);global.score(z);perbranch[bi].score(z);peranchor[anchor].score(z);
                    if(z.bad<best){best=z.bad;save(base+"/production.best",S,z,(int)cursor);cout<<"best cursor="<<cursor<<" bad="<<best<<" roots="<<z.miss[0]<<','<<z.miss[1]<<','<<z.miss[2]<<endl;}
                    if(!z.bad){cursor++;status="D5_CANDIDATE";goto done;}
                }
                cursor++;
                if(cursor==1000000){
                    double elapsed=cpu()-start;ofstream out(base+"/production.first_million.json");out<<setprecision(10)<<"{\"raw\":"<<cursor<<",\"cpu_seconds\":"<<elapsed<<",\"HH_construction_counting_cpu\":"<<time_hh<<",\"BB_cpu\":"<<time_bb<<",\"BFS_build_cpu\":"<<first_bfs<<",\"overhead_cpu\":"<<elapsed-time_hh-time_bb-first_bfs<<",\"counts\":";write_stat(out,global);out<<"}\n";
                    cout<<"FIRST_MILLION CPU="<<elapsed<<" HH="<<time_hh<<" BB="<<time_bb<<" BFS="<<first_bfs<<" overhead="<<elapsed-time_hh-time_bb-first_bfs<<endl;printed=true;
                }
                if(cursor%1000000==0){ofstream out(base+"/production.progress.json");out<<"{\"next_cursor\":"<<cursor<<",\"cpu_seconds\":"<<cpu()-start<<",\"BB_pass\":"<<global.bb<<",\"best_scored_bad_pairs\":"<<best<<"}\n";cout<<"progress "<<cursor<<" CPU="<<cpu()-start<<" BB="<<global.bb<<endl;}
            }
        }
    }
done:
    ofstream out(base+"/production.terminal.json");out<<setprecision(10)<<"{\"status\":\""<<status<<"\",\"scope_total\":76384728,\"next_cursor\":"<<cursor<<",\"next_position\":";
    if(status=="CPU_LIMIT"){out<<"{\"branch\":"<<curbranch<<",\"anchor\":"<<curai<<",\"remaining_indices\":";list(out,cursub);out<<'}';}else out<<"null";
    out<<",\"cpu_seconds\":"<<cpu()-start<<",\"BFS_build_cpu_seconds\":"<<time_bfs<<",\"counts\":";write_stat(out,global);
    out<<",\"per_branch\":[";for(int i=0;i<6;i++){if(i)out<<',';write_stat(out,perbranch[i]);}out<<"],\"per_anchor\":[";for(int i=0;i<90;i++){if(i)out<<',';write_stat(out,peranchor[i]);}out<<"],\"statistics_population\":\"root and layer metrics only BB survivors; raw and HH counts are full processed scope\",\"random_profile_is_not_prefix\":true}\n";
    cout<<status<<" cursor="<<cursor<<" CPU="<<cpu()-start<<" BB="<<global.bb<<" best="<<best<<endl;
}
