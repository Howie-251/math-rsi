// One complete-or-capped quotient profile of four edge-orbit replacements.
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Matrix=array<unsigned char,144>;
struct Orb {int id,a,b,d;};
struct Saved {Matrix matrix;array<int,4> removed;array<int,8> added;int pairing;};
vector<array<int,8>> pairings;
void make_pairings(int used,array<int,8>& pairs,int level){
    if(level==4){pairings.push_back(pairs);return;}
    int first=0;while(used&(1<<first))++first;
    for(int next=first+1;next<8;++next)if(!(used&(1<<next))){
        pairs[2*level]=first;pairs[2*level+1]=next;
        make_pairings(used|(1<<first)|(1<<next),pairs,level+1);
    }
}
void edge(Matrix& m,int a,int b,int delta){
    if(a==b)m[12*a+a]+=2*delta;
    else {m[12*a+b]+=delta;m[12*b+a]+=delta;}
}
bool diagonal_capacity(const Matrix& m){
    for(int a=0;a<12;++a){
        if(m[12*a+a]!=0 && m[12*a+a]!=2)return false;
        for(int b=a+1;b<12;++b)if(m[12*a+b]>5)return false;
    }
    return true;
}
bool row_types(const Matrix& m){
    for(int a=0;a<12;++a){
        int counts[6]={};
        for(int b=0;b<12;++b)if(a!=b)++counts[m[12*a+b]];
        if(counts[4] || counts[5])return false;
        int x=counts[1],y=counts[2],z=counts[3];bool good;
        if(m[12*a+a]==2)good=(z==0 && ((x==6 && y==0)||(x==4 && y==1)));
        else good=(z==0 && ((x==4 && y==2)||(x==2 && y==3)||(x==0 && y==4)))
                   ||(z==1 && ((x==5 && y==0)||(x==3 && y==1)));
        if(!good)return false;
    }
    return true;
}
bool nonnegative_defect(const Matrix& m){
    for(int a=0;a<12;++a)for(int b=a;b<12;++b){
        int d=int(m[12*a+b])-5-(a==b?7:0);
        for(int c=0;c<12;++c)d+=int(m[12*a+c])*int(m[12*b+c]);
        if(d<0)return false;
    }
    return true;
}
void matrix_json(ostream& f,const Matrix& m){
    f<<'[';for(int a=0;a<12;++a){if(a)f<<',';f<<'[';
        for(int b=0;b<12;++b){if(b)f<<',';f<<int(m[12*a+b]);}f<<']';}f<<']';
}
int main(int argc,char** argv){
    if(argc!=4)return 2;
    double start=double(clock())/CLOCKS_PER_SEC,budget=stod(argv[3]);
    auto wall=chrono::steady_clock::now();
    ifstream in(argv[1]);int n;in>>n;if(n!=48)return 3;
    vector<Orb> old(n);Matrix original{};
    for(auto& o:old){in>>o.id>>o.a>>o.b>>o.d;edge(original,o.a,o.b,1);}
    int loops=0;for(auto o:old)loops+=o.a==o.b;if(loops!=12)return 4;
    for(int a=0;a<12;++a){int sum=0;for(int b=0;b<12;++b){sum+=original[12*a+b];
        if(a!=b && original[12*a+b]>1)return 5;}
        if(sum!=8 || original[12*a+a]!=2)return 6;}
    array<int,8> p{};make_pairings(0,p,0);if(pairings.size()!=105)return 7;
    uint64_t deletes_started=0,deletes_finished=0,raw=0,diag=0,rows=0,defect=0,eligible=0;
    array<uint64_t,5> deletion_counts{};array<uint64_t,13> defect_by_zero{};
    vector<Saved> saved;set<Matrix> saved_keys;bool additional_unsaved=false,complete=true;
    array<int,4> cursor{};int cursor_pairing=-1;
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)for(int k=j+1;k<n;++k)for(int l=k+1;l<n;++l){
        array<int,4> selected={i,j,k,l};int loop_count=0;
        for(int t:selected)loop_count+=old[t].a==old[t].b;
        if(loop_count<2)continue;
        ++deletes_started;++deletion_counts[loop_count];
        Matrix base=original;array<int,8> endpoints{};
        for(int z=0;z<4;++z){auto o=old[selected[z]];cursor[z]=o.id;
            endpoints[2*z]=o.a;endpoints[2*z+1]=o.b;edge(base,o.a,o.b,-1);}
        for(size_t pi=0;pi<pairings.size();++pi){
            cursor_pairing=int(pi);
            if((raw&1023)==0 && double(clock())/CLOCKS_PER_SEC-start>=budget){complete=false;goto done;}
            ++raw;Matrix m=base;array<int,8> additions{};
            for(int z=0;z<4;++z){int a=endpoints[pairings[pi][2*z]],b=endpoints[pairings[pi][2*z+1]];
                if(a>b)swap(a,b);additions[2*z]=a;additions[2*z+1]=b;edge(m,a,b,1);}
            if(!diagonal_capacity(m))continue;++diag;
            if(!row_types(m))continue;++rows;
            if(!nonnegative_defect(m))continue;++defect;
            int zero=0;for(int a=0;a<12;++a)zero+=m[12*a+a]==0;
            ++defect_by_zero[zero];
            // The already proved zero/one-independent-orbit cases are recorded,
            // not silently conflated with new target-relevant quotient survivors.
            if(zero<2)continue;++eligible;
            if(!saved_keys.count(m)){
                if(saved.size()<20){saved_keys.insert(m);saved.push_back(Saved{m,cursor,additions,int(pi)});}
                else additional_unsaved=true;
            }
        }
        ++deletes_finished;
    }
done:
    ofstream f(argv[2]);f<<setprecision(12);
    f<<"{\"complete\":"<<(complete?"true":"false")<<",\"stop_reason\":\""
     <<(complete?"full_domain_exhausted":"cpu_budget_partial_domain")<<"\",\"expected_deletion_sets\":49995,"
     <<"\"expected_parameter_choices\":5249475,\"deletion_sets_started\":"<<deletes_started
     <<",\"deletion_sets_finished\":"<<deletes_finished<<",\"deletion_sets_by_loop_count\":[";
    for(int t=0;t<5;++t){if(t)f<<',';f<<deletion_counts[t];}
    f<<"],\"raw_pairing_choices\":"<<raw<<",\"diagonal_and_capacity_pass\":"<<diag
     <<",\"seven_row_types_pass\":"<<rows<<",\"nonnegative_defect_pass\":"<<defect
     <<",\"defect_pass_by_independent_orbit_count\":[";
    for(int z=0;z<13;++z){if(z)f<<',';f<<defect_by_zero[z];}
    f<<"],\"target_relevant_parameter_choices\":"<<eligible
     <<",\"counts_are_parameter_choices_not_unique_matrices\":true,\"additional_unsaved_distinct_matrix_seen\":"
     <<(additional_unsaved?"true":"false")<<",\"last_deletion_orbit_ids\":[";
    for(int z=0;z<4;++z){if(z)f<<',';f<<cursor[z];}
    f<<"],\"last_pairing_index\":"<<cursor_pairing<<",\"initial_matrix\":";matrix_json(f,original);
    f<<",\"saved_distinct_matrices\":[";
    for(size_t si=0;si<saved.size();++si){if(si)f<<',';auto& s=saved[si];
        f<<"{\"matrix\":";matrix_json(f,s.matrix);f<<",\"removed_orbit_ids\":[";
        for(int z=0;z<4;++z){if(z)f<<',';f<<s.removed[z];}f<<"],\"added_quotient_edges\":[";
        for(int z=0;z<4;++z){if(z)f<<',';f<<'['<<s.added[2*z]<<','<<s.added[2*z+1]<<']';}
        f<<"],\"pairing_index\":"<<s.pairing<<'}';}
    f<<"],\"profile_cpu_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start
     <<",\"profile_wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-wall).count()
     <<",\"profile_cpu_budget_seconds\":"<<budget<<"}\n";
    cout<<"complete "<<complete<<" choices "<<raw<<" D_pass "<<defect<<" relevant "<<eligible<<" saved "<<saved.size()<<endl;
}
