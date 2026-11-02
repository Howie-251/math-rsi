#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

constexpr int Q=6959,M=49,BETA=5155,N=Q*M;
const int phase[6]={1,36,45,48,13,4};
const int inverse_dart[6]={3,4,5,0,1,2};
int factor[6],ca[6],cb[6];
std::array<std::vector<uint32_t>,M> forms;
std::array<uint32_t,M> raw{};
static double cpu(){return double(std::clock())/CLOCKS_PER_SEC;}
static int power(int x,int e){int y=1;while(e){if(e&1)y=int(1LL*y*x%Q);x=int(1LL*x*x%Q);e>>=1;}return y;}
static void words(int depth,int j,int a,int b,int prev){
    forms[j].push_back(uint32_t(a*Q+b));++raw[j];
    if(depth==9)return;
    for(int d=0;d<6;++d)if(prev<0||d!=inverse_dart[prev]){
        int jj=j+phase[d];if(jj>=M)jj-=M;
        words(depth+1,jj,(a*factor[d]+ca[d])%Q,(b*factor[d]+cb[d])%Q,d);
    }
}
struct Rep{int tau;bool infinity;uint32_t mask=0;int status=0,failphase=-1,missing=-1,coverage=-1;};
struct Image{int size,firstmissing;};
std::array<int,Q> seen{};int epoch=0;
static Image image(const Rep& r,int j){
    ++epoch;int count=0;
    for(uint32_t code:forms[j]){
        int b=code%Q,a=code/Q;
        int v=r.infinity?b:(a+b*r.tau)%Q;
        if(seen[v]!=epoch){seen[v]=epoch;if(++count==Q)return{Q,-1};}
    }
    int first=0;while(seen[first]==epoch)++first;
    return{count,first};
}
static void rep_id(std::ostream& o,const Rep& r){if(r.infinity)o<<"\"infinity\"";else o<<r.tau;}
static void write_phase0(const std::string& dir,const std::vector<Rep>& reps,bool complete){
    int tested=0,failed=0,passed=0;for(const auto&r:reps)if(r.mask&1){++tested;if(r.status==1)++failed;else++passed;}
    std::ofstream f(dir+"/PHASE0_RESULT.json");f<<"{\"phase\":0,\"raw_words\":"<<raw[0]<<",\"distinct_forms\":"<<forms[0].size()<<",\"domain_size\":6959,\"new_representatives_evaluated\":"<<tested<<",\"phase0_failed\":"<<failed<<",\"phase0_survivor_count\":"<<passed<<",\"phase0_domain_complete\":"<<(complete?"true":"false")<<",\"survivors\":[";
    bool comma=false;for(const auto&r:reps)if((r.mask&1)&&r.status!=1){if(comma)f<<',';rep_id(f,r);comma=true;}f<<"]}\n";
    std::cout<<"PHASE0 evaluated="<<tested<<" survivors="<<passed<<" CPU="<<cpu()<<std::endl;
}
static long long write_graph(const std::string& dir,const Rep& r){
    int norm[6]={0,r.infinity?0:1,r.infinity?1:r.tau,0,0,0};
    for(int i=0;i<3;++i)norm[i+3]=(Q-norm[i]*factor[i+3]%Q)%Q;
    std::ofstream graph(dir+"/graph_d6_D9_n340991.edges");graph<<N<<' '<<N*3<<'\n';long long count=0;
    for(int u=0;u<N;++u){
        int j=u/Q,n=u%Q;std::array<int,6> row;
        for(int d=0;d<6;++d){int jj=j+phase[d];if(jj>=M)jj-=M;row[d]=jj*Q+(n*factor[d]+norm[d])%Q;}
        std::sort(row.begin(),row.end());assert(std::adjacent_find(row.begin(),row.end())==row.end());
        for(int v:row){assert(u!=v);if(u<v){graph<<u<<' '<<v<<'\n';++count;}}
    }
    assert(count==N*3);return count;
}
int main(int argc,char**argv){
    const std::string dir=argv[1];const double limit=std::stod(argv[2]);
    for(int d=0;d<6;++d)factor[d]=power(BETA,phase[d]);
    ca[0]=0;cb[0]=0;ca[1]=1;cb[1]=0;ca[2]=0;cb[2]=1;
    for(int d=0;d<3;++d){ca[d+3]=(Q-ca[d]*factor[d+3]%Q)%Q;cb[d+3]=(Q-cb[d]*factor[d+3]%Q)%Q;}
    words(0,0,0,0,-1);
    uint32_t totalraw=0;uint64_t totaldistinct=0;
    std::ofstream counts(dir+"/FORM_COUNTS.csv");counts<<"phase,raw_words,distinct_coefficient_pairs\n";
    for(int j=0;j<M;++j){totalraw+=raw[j];std::sort(forms[j].begin(),forms[j].end());forms[j].erase(std::unique(forms[j].begin(),forms[j].end()),forms[j].end());totaldistinct+=forms[j].size();counts<<j<<','<<raw[j]<<','<<forms[j].size()<<'\n';}
    assert(totalraw==2929687);
    std::ofstream binary(dir+"/COEFFICIENT_FORMS.u32",std::ios::binary);
    for(int j=0;j<M;++j){uint32_t count=uint32_t(forms[j].size());binary.write(reinterpret_cast<const char*>(&count),4);binary.write(reinterpret_cast<const char*>(forms[j].data()),4*count);}binary.close();
    std::ofstream schema(dir+"/FORM_SCHEMA.json");schema<<"{\"encoding\":\"native uint32;49 sequential blocks of count followed by sorted A*6959+B codes\",\"coefficient_order\":[\"cB\",\"cC\"],\"field\":6959,\"beta\":5155,\"phase_order\":49,\"total_raw_words\":"<<totalraw<<",\"total_distinct_phase_forms\":"<<totaldistinct<<",\"word_length_bound\":9,\"old_tau1512_evaluated\":false}\n";
    std::vector<Rep> reps;for(int tau=0;tau<Q;++tau)if(tau!=1512)reps.push_back({tau,false});reps.push_back({-1,true});assert(reps.size()==6959);
    std::vector<int> active;for(int i=0;i<int(reps.size());++i)active.push_back(i);
    bool timed=false,hit=false;int hitindex=-1,lastcomplete=-1;long long evaluations=0,edges=0;
    std::ofstream progress(dir+"/PHASE_PROGRESS.csv");progress<<"phase,active_before,tested,failed,survivors,complete,CPU_seconds\n";
    for(int j=0;j<=24&&!active.empty();++j){
        std::vector<int> next;int tested=0,failed=0;
        for(int index:active){
            if(cpu()>=limit){timed=true;break;}
            auto&r=reps[index];Image got=image(r,j);++tested;++evaluations;r.mask|=uint32_t(1)<<j;
            if(got.size<Q){r.status=1;r.failphase=j;r.missing=got.firstmissing;r.coverage=got.size;++failed;}
            else if(j==24){r.status=2;hit=true;hitindex=index;edges=write_graph(dir,r);break;}
            else next.push_back(index);
        }
        bool complete=tested==int(active.size());if(complete)lastcomplete=j;
        progress<<j<<','<<active.size()<<','<<tested<<','<<failed<<','<<next.size()+(hit?1:0)<<','<<(complete?1:0)<<','<<cpu()<<'\n';progress.flush();
        if(j==0)write_phase0(dir,reps,complete);
        if(hit||timed)break;active.swap(next);
    }
    int rejected=0,unknown=0;for(const auto&r:reps){if(r.status==1)++rejected;else if(r.status!=2)++unknown;}
    const bool nofamily=rejected==int(reps.size());
    std::string status=hit?"FOUND_COMPLETE_WORD_COVER_GRAPH_PENDING_ROOT_ACCEPTANCE":nofamily?"COMPLETE_NO_BETA5155_ALL_NORMAL_TRANSLATIONS_D9":"UNKNOWN_PARTIAL_PROJECTIVE_DOMAIN_CPU_CAP";
    std::ofstream repcsv(dir+"/REPRESENTATIVE_STATUS.csv");repcsv<<"representative,cB,cC,checked_phase_mask,status,failed_phase,first_missing,failed_image_cardinality\n";
    for(const auto&r:reps){if(r.infinity)repcsv<<"infinity,0,1";else repcsv<<r.tau<<",1,"<<r.tau;repcsv<<','<<r.mask<<','<<(r.status==1?"FAILED":r.status==2?"ALL_PHASE_COVER":"UNRESOLVED")<<','<<r.failphase<<','<<r.missing<<','<<r.coverage<<'\n';}
    std::ofstream rawout(dir+"/RAW_RESULT.json");rawout<<"{\"status\":\""<<status<<"\",\"beta\":5155,\"field\":6959,\"phase_modulus\":49,\"new_projective_representatives\":6959,\"raw_NB_words_generated_once\":"<<totalraw<<",\"distinct_phase_coefficient_forms\":"<<totaldistinct<<",\"representative_phase_evaluations\":"<<evaluations<<",\"new_representatives_rejected\":"<<rejected<<",\"new_representatives_unresolved\":"<<unknown<<",\"all_new_representatives_rejected\":"<<(nofamily?"true":"false")<<",\"last_phase_domain_completed\":"<<lastcomplete<<",\"time_cap_reached\":"<<(timed?"true":"false")<<",\"inherited_tau1512_recomputed\":false,\"zero_branch_graph_generated\":false,\"hit\":"<<(hit?"true":"false")<<",\"hit_representative\":";
    if(hit)rep_id(rawout,reps[hitindex]);else rawout<<"null";
    rawout<<",\"literal_edges_written\":"<<edges<<",\"run_process_CPU_seconds\":"<<cpu()<<"}\n";
    if(hit){std::ofstream h(dir+"/HIT.json");h<<"{\"status\":\"COMPLETE_WORD_COVER_TARGET_PENDING_ROOT_ACCEPTANCE\",\"field\":6959,\"beta\":5155,\"n\":340991,\"m\":1022973,\"maximum_degree\":6,\"diameter_at_most\":9,\"exact_diameter\":null,\"representative\":";rep_id(h,reps[hitindex]);h<<",\"phases_tested\":\"0..24;inverse-word correspondence covers25..48\",\"vertex_label\":\"6959*phase+normal\",\"graph\":\"graph_d6_D9_n340991.edges\",\"BFS\":0}\n";}
    std::cout<<status<<" rejected="<<rejected<<" unresolved="<<unknown<<" CPU="<<cpu()<<std::endl;
}
