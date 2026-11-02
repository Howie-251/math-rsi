// One deterministic descent in the C7-invariant eight-orbit graph domain with two fixed vertices.
// Each edge orbit has seven actual edges; quotient loops contribute degree two.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using Rows=array<uint64_t,58>;
struct Orbit { int a,b,d; vector<pair<int,int>> edges; };
struct Move { vector<int> old_ids,new_ids; int pairing=-1; };
struct Level {
    int index,start_score,best_score;
    uint64_t single_choices=0,pair_choices=0,legal_evaluations=0;
    bool complete=true,accepted=false;
    double cpu=0,wall=0;
    Move move;
};
static vector<Orbit> orbitals;
static array<array<vector<int>,8>,8> by_pair;
static string outdir;
static double start_cpu,budget;
static int initial_score;
static constexpr uint64_t ALL=(uint64_t(1)<<58)-1;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void toggle(Rows& rows,int id){
    for(auto [u,v]:orbitals[id].edges){rows[u]^=uint64_t(1)<<v;rows[v]^=uint64_t(1)<<u;}
}
int score(const Rows& rows){
    // Exact full-graph count, using translation invariance only to avoid repeats.
    int directed=0;
    for(int a=0;a<10;++a){
        int u=(a<2?a:2+7*(a-2));uint64_t covered=rows[u]|(uint64_t(1)<<u),left=rows[u];
        while(left){int v=__builtin_ctzll(left);left&=left-1;covered|=rows[v];}
        directed+=(a<2?1:7)*__builtin_popcountll(ALL&~covered);
    }
    if(directed%2)throw runtime_error("Odd representative directed bad count");
    return directed/2;
}
vector<int> replace_ids(const vector<int>& current,const Move& move){
    vector<int> result;
    for(int id:current)if(find(move.old_ids.begin(),move.old_ids.end(),id)==move.old_ids.end())result.push_back(id);
    result.insert(result.end(),move.new_ids.begin(),move.new_ids.end());
    sort(result.begin(),result.end());
    return result;
}
void list_json(ostream& f,const vector<int>& xs){
    f<<'[';for(size_t i=0;i<xs.size();++i){if(i)f<<',';f<<xs[i];}f<<']';
}
void move_json(ostream& f,const Move& move){
    f<<"{\"removed_orbits\":";list_json(f,move.old_ids);
    f<<",\"added_orbits\":";list_json(f,move.new_ids);
    f<<",\"pairing_index\":"<<move.pairing<<'}';
}
void save_graph(const string& stem,const vector<int>& ids,const Rows& rows,int bad,
                const Move& move,bool selected_from_complete_neighborhood){
    if(ids.size()!=31)throw runtime_error("Orbit count changed");
    for(auto row:rows)if(__builtin_popcountll(row)!=8)throw runtime_error("Degree changed");
    int edges=0;for(int u=0;u<58;++u)for(int v=u+1;v<58;++v)edges+=(rows[u]>>v)&1;
    if(edges!=232 || score(rows)!=bad)throw runtime_error("Saved graph mismatch");
    ofstream f(outdir+"/"+stem+".json"),e(outdir+"/"+stem+".edges");
    f<<"{\"n\":58,\"bad_pairs_exact\":"<<bad<<",\"selected_from_complete_neighborhood\":"
      <<(selected_from_complete_neighborhood?"true":"false")<<",\"selected_orbits\":";
    list_json(f,ids);f<<",\"selected_parameters\":[";
    for(size_t i=0;i<ids.size();++i){if(i)f<<',';const auto& o=orbitals[ids[i]];
        f<<"{\"index\":"<<ids[i]<<",\"a\":"<<o.a<<",\"b\":"<<o.b<<",\"shift\":"<<o.d<<'}';}
    f<<"],\"move\":";move_json(f,move);f<<",\"edges\":[";e<<"58 232\n";bool first=true;
    for(int u=0;u<58;++u)for(int v=u+1;v<58;++v)if((rows[u]>>v)&1){
        if(!first)f<<',';first=false;f<<'['<<u<<','<<v<<']';e<<u<<' '<<v<<'\n';}
    f<<"]}\n";
}
Level examine(int index,const vector<int>& current,const Rows& original){
    double c0=cpu();auto w0=chrono::steady_clock::now();
    Level result;result.index=index;result.start_score=result.best_score=score(original);
    Rows rows=original;array<bool,220> present{};for(int id:current)present[id]=true;
    auto evaluate=[&](Move move){
        if((result.legal_evaluations&1023)==0 && cpu()-start_cpu>=budget){result.complete=false;return false;}
        for(int id:move.new_ids)if(present[id] && find(move.old_ids.begin(),move.old_ids.end(),id)==move.old_ids.end())return true;
        if(move.new_ids.size()==2 && move.new_ids[0]==move.new_ids[1])return true;
        vector<int> old_sorted=move.old_ids,new_sorted=move.new_ids;
        sort(old_sorted.begin(),old_sorted.end());sort(new_sorted.begin(),new_sorted.end());
        if(old_sorted==new_sorted)return true;
        ++result.legal_evaluations;
        for(int id:move.old_ids)toggle(rows,id);for(int id:move.new_ids)toggle(rows,id);
        int bad=score(rows);
        if(bad<result.best_score){
            result.best_score=bad;result.move=move;
            save_graph("level"+to_string(index)+".best_so_far",replace_ids(current,move),rows,bad,move,false);
        }
        for(int id:move.new_ids)toggle(rows,id);for(int id:move.old_ids)toggle(rows,id);
        return true;
    };
    for(int id:current){
        const auto& o=orbitals[id];
        for(int target:by_pair[o.a][o.b]){
            ++result.single_choices;
            if(!evaluate(Move{{id},{target},-1}))goto finished;
        }
    }
    for(size_t i=0;i<current.size();++i)for(size_t j=i+1;j<current.size();++j){
        int left=current[i],right=current[j];const auto& l=orbitals[left];const auto& r=orbitals[right];
        int endpoints[4]={l.a,l.b,r.a,r.b};
        const int matchings[3][4]={{0,1,2,3},{0,2,1,3},{0,3,1,2}};
        for(int pairing=0;pairing<3;++pairing){
            int a=endpoints[matchings[pairing][0]],b=endpoints[matchings[pairing][1]];
            int c=endpoints[matchings[pairing][2]],d=endpoints[matchings[pairing][3]];
            if(a>b)swap(a,b);if(c>d)swap(c,d);
            for(int x:by_pair[a][b])for(int y:by_pair[c][d]){
                ++result.pair_choices;
                if(!evaluate(Move{{left,right},{x,y},pairing}))goto finished;
            }
        }
    }
finished:
    result.cpu=cpu()-c0;result.wall=chrono::duration<double>(chrono::steady_clock::now()-w0).count();
    return result;
}
void write_report(const vector<Level>& levels,int best,int accepted,const string& reason,double wall){
    ofstream f(outdir+"/search.json");f<<setprecision(12);
    f<<"{\"initial_bad_pairs\":"<<initial_score<<",\"best_bad_pairs\":"<<best<<",\"accepted_moves\":"<<accepted
     <<",\"stop_reason\":\""<<reason<<"\",\"search_cpu_seconds\":"<<cpu()-start_cpu
     <<",\"search_wall_seconds\":"<<wall<<",\"search_cpu_budget_seconds\":"<<budget
     <<",\"counts_are_parameter_choices_not_unique_graphs\":true,\"levels\":[";
    for(size_t i=0;i<levels.size();++i){if(i)f<<',';const auto& l=levels[i];
        f<<"{\"level\":"<<l.index<<",\"start_bad_pairs\":"<<l.start_score<<",\"best_bad_pairs\":"<<l.best_score
         <<",\"single_choices\":"<<l.single_choices<<",\"pair_choices\":"<<l.pair_choices
         <<",\"legal_nonidentity_evaluations\":"<<l.legal_evaluations
         <<",\"complete\":"<<(l.complete?"true":"false")<<",\"accepted\":"<<(l.accepted?"true":"false")
         <<",\"cpu_seconds\":"<<l.cpu<<",\"wall_seconds\":"<<l.wall<<",\"best_move\":";
        move_json(f,l.move);f<<'}';}
    f<<"]}\n";
}
int main(int argc,char** argv){
    if(argc!=4)return 2;
    start_cpu=cpu();auto wall_start=chrono::steady_clock::now();
    outdir=argv[2];budget=stod(argv[3]);
    ifstream input(argv[1]);int count,selected_count;input>>count>>selected_count>>initial_score;
    if(count!=220 || selected_count!=31)return 3;
    vector<int> current;Rows rows{};
    int fixed_edges;input>>fixed_edges;if(fixed_edges!=15)return 7;
    for(int i=0;i<fixed_edges;++i){int u,v;input>>u>>v;rows[u]|=uint64_t(1)<<v;rows[v]|=uint64_t(1)<<u;}
    for(int i=0;i<count;++i){
        int id,a,b,d,selected;input>>id>>a>>b>>d>>selected;
        if(id!=i || a>b)return 4;
        Orbit o{a,b,d,{}};
        for(int t=0;t<7;++t){int u=2+7*a+t,v=2+7*b+(t+d)%7;if(u>v)swap(u,v);o.edges.emplace_back(u,v);}
        sort(o.edges.begin(),o.edges.end());
        if(unique(o.edges.begin(),o.edges.end())!=o.edges.end())return 5;
        orbitals.push_back(o);by_pair[a][b].push_back(id);
        if(selected){current.push_back(id);toggle(rows,id);}
    }
    if(current.size()!=31 || score(rows)!=initial_score)return 6;
    save_graph("state000",current,rows,initial_score,Move{},false);
    save_graph("candidate.best",current,rows,initial_score,Move{},false);
    vector<Level> levels;int accepted=0,best=initial_score;string reason;
    for(int index=0;;++index){
        Level result=examine(index,current,rows);
        if(result.best_score<best){
            for(int id:result.move.old_ids)toggle(rows,id);for(int id:result.move.new_ids)toggle(rows,id);
            current=replace_ids(current,result.move);best=result.best_score;result.accepted=true;++accepted;
            string number=to_string(accepted);number=string(3-number.size(),'0')+number;
            save_graph("state"+number,current,rows,best,result.move,result.complete);
            save_graph("candidate.best",current,rows,best,result.move,result.complete);
        }
        levels.push_back(result);
        cout<<"level "<<index<<" start "<<result.start_score<<" best "<<best<<" evaluations "
            <<result.legal_evaluations<<" complete "<<result.complete<<endl;
        if(best==0)reason="target_found";
        else if(!result.complete)reason="cpu_budget_partial_neighborhood";
        else if(!result.accepted)reason="complete_neighborhood_no_strict_improvement";
        else if(cpu()-start_cpu>=budget)reason="cpu_budget_after_complete_level";
        write_report(levels,best,accepted,reason.empty()?"running":reason,
            chrono::duration<double>(chrono::steady_clock::now()-wall_start).count());
        if(!reason.empty())break;
    }
}
