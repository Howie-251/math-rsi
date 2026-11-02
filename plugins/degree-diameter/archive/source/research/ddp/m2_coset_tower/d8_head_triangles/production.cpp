#include "production_engine.hpp"
#include "production_extra.hpp"
#include <cstdint>
#include <iomanip>
struct Bits{
    array<uint64_t,3> w{};
    void add(int x){w[x/64]|=1ULL<<(x%64);}
    void merge(const Bits&b){for(int i=0;i<3;i++)w[i]|=b.w[i];}
    int count()const{return __builtin_popcountll(w[0])+__builtin_popcountll(w[1])+__builtin_popcountll(w[2]);}
};
static array<Bits,147> HM;
void init_masks(){for(int x=0;x<147;x++)for(int h=0;h<7;h++)HM[x].add(KACTION[h][x]);}
array<Bits,6> full_bb(const Generators&S){
    array<Bits,6>M;Bits p;p.add(0);p.add(49);p.add(98);
    for(int s:S)p.merge(HM[s%147]);
    for(int j=0;j<6;j++){
        M[j]=p;
        for(int s:S){int js=KCOORD[s/147][1],x=s%147;M[j].merge(HM[KACTION[7*((j-js+6)%6)][x]]);}
    }
    auto insert=[&](int g){M[KCOORD[g/147][1]].merge(HM[g%147]);};insert(0);
    array<int,7> reverse{};for(int i=0;i<7;i++){reverse[i]=-1;for(int j=0;j<7;j++)if(S[j]==GINV[S[i]])reverse[i]=j;assert(reverse[i]>=0);}
    for(int a=0;a<7;a++){
        int s=S[a];insert(s);
        for(int b=0;b<7;b++)if(b!=reverse[a]){
            int v=gp(s,S[b]);insert(v);
            for(int c=0;c<7;c++)if(c!=reverse[b])insert(gp(v,S[c]));
        }
    }
    return M;
}
int missing(const array<Bits,6>&M){int ans=0;for(auto&m:M)ans+=147-m.count();return ans;}
struct Key{int branch,index,ja,jb;long long scope;array<int,3>internal;};
Generators gens(const Key&k,int ba,int bb){int a=50+147*(ba+7*k.ja),b=56+147*(bb+7*k.jb);return {a,GINV[a],b,GINV[b],k.internal[0],k.internal[1],k.internal[2]};}
void params(ostream&o,const Generators&S,const Key&k,int keyidx,int ba,int bb,int filtered,int bbmissing,const Score*z,const string&selection){
    o<<"{\"selection\":\""<<selection<<"\",\"filtered_cursor\":"<<filtered<<",\"original_scope_cursor\":"<<k.scope+7*ba+bb<<",\"branch\":"<<k.branch<<",\"passing_key_index\":"<<keyidx<<",\"internal_index\":"<<k.index<<",\"cross_K_codes\":["<<ba+7*k.ja<<','<<bb+7*k.jb<<"],\"S\":";list(o,S);o<<",\"original_BB_missing\":"<<bbmissing;
    if(z){o<<",\"root_missing\":";list(o,z->miss);o<<",\"root_missing_by_target_layer\":[";for(int i=0;i<3;i++){if(i)o<<',';list(o,z->layer[i]);}o<<"],\"bad_unordered_pairs\":"<<z->bad;}
    o<<'}';
}
void save_graph(const string&base,const Generators&S,const Key&k,int ki,int ba,int bb,int cur,int miss,const Score&z,const string&selection){
    ofstream p(base+".json");params(p,S,k,ki,ba,bb,cur,miss,&z,selection);p<<'\n';
    ofstream f(base+".edges");f<<N<<' '<<N*D/2<<'\n';for(int g=0;g<N;g++)for(int h:adj[g])if(g<h)f<<g<<' '<<h<<'\n';
}
struct Stat{
    int checked=0,bbpass=0,scored=0,minbb=882;long long best=LLONG_MAX;
    array<int,3> mins{N,N,N},zeros{};array<array<int,3>,3>lm{},lz{};int joint=0;
    Stat(){for(auto&r:lm)r.fill(N);}
    void test(int m){checked++;minbb=min(minbb,m);if(!m)bbpass++;}
    void evaluated(const Score&z){scored++;best=min(best,z.bad);for(int i=0;i<3;i++){mins[i]=min(mins[i],z.miss[i]);if(!z.miss[i])zeros[i]++;for(int j=0;j<3;j++){lm[i][j]=min(lm[i][j],z.layer[i][j]);if(!z.layer[i][j])lz[i][j]++;}}if(!z.miss[1]&&!z.miss[2])joint++;}
};
void statout(ostream&o,const Stat&s){
    o<<"{\"original_BB_evaluated\":"<<s.checked<<",\"original_BB_pass\":"<<s.bbpass<<",\"fully_scored_BB_survivors\":"<<s.scored<<",\"min_BB_on_quotient_passes\":";if(s.checked)o<<s.minbb;else o<<"null";
    o<<",\"root_minimum_missing_among_BB_passes\":";if(s.scored)list(o,s.mins);else o<<"null";
    o<<",\"root_zero_counts_among_BB_passes\":";list(o,s.zeros);o<<",\"head_and_block_zero\":"<<s.joint<<",\"best_bad_pairs_among_BB_passes\":";if(s.scored)o<<s.best;else o<<"null";
    o<<",\"layer_minimum_missing_among_BB_passes\":";if(s.scored){o<<'[';for(int i=0;i<3;i++){if(i)o<<',';list(o,s.lm[i]);}o<<']';}else o<<"null";
    o<<",\"layer_zero_counts_among_BB_passes\":[";for(int i=0;i<3;i++){if(i)o<<',';list(o,s.lz[i]);}o<<"]}";
}
int main(int argc,char**argv){
    assert(argc==4);string mode=argv[1],base=argv[3];double limit=stod(argv[2]),start=cpu();init_masks();
    if(mode=="calibrate"){
        ifstream in(base+"/profile.inputs.txt"),expected(base+"/production.expected_BB.txt"),masks(base+"/production.expected_sample_masks.txt");int n;in>>n;assert(n==1200);
        for(int i=0;i<n;i++){Generators S;for(int&g:S)in>>g;int want;expected>>want;auto M=full_bb(S);assert(missing(M)==want);
            if(i==0)for(int j=0;j<6;j++)for(int b=0;b<3;b++){uint64_t x;masks>>x;assert(x==M[j].w[b]);}}
        ofstream out(base+"/production.BB_calibration.json");out<<"{\"saved_BFS_BB_count_matches\":1200,\"independent_full_882_target_mask_match\":true,\"new_graphs\":0,\"new_BFS\":0,\"cpu_seconds\":"<<cpu()-start<<"}\n";cout<<"Original six masks match 1200 saved BB counts and the independent 882-target sample.\n";return 0;
    }
    assert(mode=="run");ifstream f(base+"/production.inputs.txt");int nk;f>>nk;assert(nk==4704);vector<Key>keys(nk);for(auto&k:keys)f>>k.branch>>k.index>>k.ja>>k.jb>>k.scope>>k.internal[0]>>k.internal[1]>>k.internal[2];assert(f);
    Stat all;array<Stat,5>branches;array<long long,883>hist{};int cur=0,minbb=883,bestki=-1,bestba=0,bestbb=0,mincur=-1;long long best=LLONG_MAX;
    double bbtime=0,bfstime=0;string status="COMPLETE_NO_SOLUTION";int currentki=0,currentba=0,currentbb=0;
    for(int ki=0;ki<nk;ki++)for(int ba=0;ba<7;ba++)for(int bb=0;bb<7;bb++){
        currentki=ki;currentba=ba;currentbb=bb;if((cur&255)==0&&cpu()-start>=limit){status="CPU_LIMIT";goto done;}
        auto&k=keys[ki];auto S=gens(k,ba,bb);double t=cpu();auto M=full_bb(S);int miss=missing(M);bbtime+=cpu()-t;
        all.test(miss);branches[k.branch].test(miss);hist[miss]++;
        if(miss<minbb){minbb=miss;bestki=ki;bestba=ba;bestbb=bb;mincur=cur;ofstream p(base+"/production.min_BB.json");params(p,S,k,ki,ba,bb,cur,miss,nullptr,"minimum_original_BB_among_quotient_passes");p<<'\n';}
        if(!miss){
            t=cpu();build(S);Score z=score(false);bfstime+=cpu()-t;assert(z.layer[1][1]==0);all.evaluated(z);branches[k.branch].evaluated(z);
            if(z.bad<best){best=z.bad;save_graph(base+"/production.best",S,k,ki,ba,bb,cur,miss,z,"minimum_bad_pairs_among_original_BB_survivors");cout<<"best cursor="<<cur<<" bad="<<best<<" roots="<<z.miss[0]<<','<<z.miss[1]<<','<<z.miss[2]<<endl;}
            if(!z.bad){cur++;status="D5_CANDIDATE";goto done;}
        }
        cur++;
        if(cur==10000){double elapsed=cpu()-start;ofstream o(base+"/production.first_stage.json");o<<setprecision(10)<<"{\"original_BB_inputs\":"<<cur<<",\"cpu_seconds\":"<<elapsed<<",\"original_BB_cpu_seconds\":"<<bbtime<<",\"actual_BFS_build_cpu_seconds\":"<<bfstime<<",\"other_cpu_seconds\":"<<elapsed-bbtime-bfstime<<",\"counts\":";statout(o,all);o<<"}\n";cout<<"FIRST_10000 CPU="<<elapsed<<" BB="<<bbtime<<" BFS="<<bfstime<<" originalBBpass="<<all.bbpass<<endl;}
        if(cur%50000==0)cout<<"progress "<<cur<<" CPU="<<cpu()-start<<" originalBBpass="<<all.bbpass<<" minBB="<<minbb<<endl;
    }
done:
    bool fallback=false;
    if(!all.scored&&bestki>=0){auto&k=keys[bestki];auto S=gens(k,bestba,bestbb);double t=cpu();build(S);Score z=score(true);bfstime+=cpu()-t;save_graph(base+"/production.best",S,k,bestki,bestba,bestbb,mincur,minbb,z,"one_minimum_original_BB_fallback_not_a_scored_population_minimum");fallback=true;}
    ofstream o(base+"/production.terminal.json");o<<setprecision(10)<<"{\"status\":\""<<status<<"\",\"full_normalized_scope\":28894320,\"quotient_rejected_original_inputs\":28663824,\"quotient_pass_scope\":230496,\"next_filtered_cursor\":"<<cur<<",\"next_position\":";
    if(status=="CPU_LIMIT")o<<"{\"key_index\":"<<currentki<<",\"ba\":"<<currentba<<",\"bb\":"<<currentbb<<'}';else o<<"null";
    o<<",\"cpu_seconds\":"<<cpu()-start<<",\"original_BB_cpu_seconds\":"<<bbtime<<",\"actual_BFS_build_cpu_seconds\":"<<bfstime<<",\"one_minBB_fallback_scored\":"<<(fallback?"true":"false")<<",\"counts\":";statout(o,all);
    o<<",\"per_branch\":[";for(int i=0;i<5;i++){if(i)o<<',';statout(o,branches[i]);}o<<"],\"original_BB_missing_histogram\":{";bool first=true;for(int i=0;i<=882;i++)if(hist[i]){if(!first)o<<',';first=false;o<<'\"'<<i<<"\":"<<hist[i];}o<<"}}\n";
    cout<<status<<" checked="<<cur<<" CPU="<<cpu()-start<<" originalBBpass="<<all.bbpass<<" minBB="<<minbb<<endl;
}
