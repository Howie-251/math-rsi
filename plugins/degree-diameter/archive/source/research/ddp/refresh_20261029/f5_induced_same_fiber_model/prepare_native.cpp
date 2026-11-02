#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int N=3750,D=20,BW=(N+63)/64;
struct Stop{};
int main(int argc,char**argv){
    if(argc!=5)return 2;
    const double start=double(clock())/CLOCKS_PER_SEC,allowance=stod(argv[4]);
    auto cpu=[&](){return double(clock())/CLOCKS_PER_SEC-start;};
    const string dir=argv[3];
    uint64_t processed=0,clauses=0,onlines=0,offlines=0,two_paths=0,three_paths=0;
    int current_fiber=0,current_x=0,current_y=1;
    string phase="read_inputs";
    struct Row{int pairs=0,online=0,offline=0,two=0,three=0;array<uint32_t,7> on_example{},off_example{};};
    array<Row,30> fiber{};
    auto failure=[&](const string&status,const string&error){
        ofstream f(dir+"/NATIVE_RESULT.json");
        f<<"{\"status\":\""<<status<<"\",\"error\":\""<<error
         <<"\",\"phase\":\""<<phase<<"\",\"next_or_current_fiber\":"<<current_fiber
         <<",\"next_or_current_x\":"<<current_x<<",\"next_or_current_y\":"<<current_y
         <<",\"completed_pairs\":"<<processed<<",\"completed_clauses\":"<<clauses
         <<",\"CPU_seconds\":"<<cpu()<<"}\n";
    };
    try{
        array<array<uint16_t,D>,N> adj;
        ifstream source(argv[1],ios::binary);
        source.read(reinterpret_cast<char*>(adj.data()),sizeof(adj));
        if(source.gcount()!=sizeof(adj))throw runtime_error("Adjacency cache size mismatch");
        vector<array<uint64_t,BW>> bits(N);
        for(int x=0;x<N;++x)for(int y:adj[x])bits[x][y/64]|=uint64_t(1)<<(y%64);
        auto adjacent=[&](int x,int y){return bool(bits[x][y/64]>>(y%64)&1);};
        map<array<int,5>,int> flags;
        ifstream inf(argv[2]);int z;array<int,5> key;
        while(inf>>z){for(int&i:key)inf>>i;flags[key]=z;}
        if(flags.size()!=3000)throw runtime_error("Expected 3000 restored OR5 flags");
        set<int> used_flags;
        ofstream out(dir+"/same_fiber.added.cnf");
        ofstream records(dir+"/ROUTES.u32le.bin",ios::binary);
        phase="complete_pair_route_enumeration";
        for(int ctl=0;ctl<30;++ctl){
            current_fiber=ctl;
            for(int x=125*ctl;x<125*(ctl+1);++x){
                current_x=x;
                for(int y=x+1;y<125*(ctl+1);++y){
                    current_y=y;
                    if(processed%256==0 && cpu()>=allowance)throw Stop{};
                    if(adjacent(x,y))throw runtime_error("Unexpected same-fiber direct edge");
                    vector<int> common;
                    for(int a:adj[x])if(adjacent(a,y))common.push_back(a);
                    sort(common.begin(),common.end());
                    vector<pair<int,int>> paths;
                    for(int a:adj[x])for(int b:adj[y])if(adjacent(a,b))paths.emplace_back(a,b);
                    sort(paths.begin(),paths.end());
                    if(paths.size()!=2)throw runtime_error("Three-walk count differs from two");
                    array<int,4> middle={paths[0].first,paths[0].second,paths[1].first,paths[1].second};
                    auto sorted_middle=middle;sort(sorted_middle.begin(),sorted_middle.end());
                    if(adjacent_find(sorted_middle.begin(),sorted_middle.end())!=sorted_middle.end())
                        throw runtime_error("The two middle pairs overlap");
                    int flag=0;
                    if(common.size()==5){
                        copy(common.begin(),common.end(),key.begin());
                        auto found=flags.find(key);
                        if(found==flags.end())throw runtime_error("Five common neighbors lack restored OR5 flag");
                        flag=found->second;used_flags.insert(flag);++onlines;++fiber[ctl].online;
                    }else if(common.empty()){++offlines;++fiber[ctl].offline;}
                    else throw runtime_error("Two-walk count is neither zero nor five");
                    for(int a:{middle[0],middle[1]})for(int b:{middle[2],middle[3]}){
                        out<<-(x+1)<<' '<<-(y+1)<<' ';
                        if(flag)out<<flag<<' ';
                        out<<a+1<<' '<<b+1<<" 0\n";++clauses;
                    }
                    array<uint32_t,7> row={uint32_t(x),uint32_t(y),uint32_t(middle[0]),uint32_t(middle[1]),
                                          uint32_t(middle[2]),uint32_t(middle[3]),uint32_t(flag)};
                    records.write(reinterpret_cast<const char*>(row.data()),sizeof(row));
                    if(flag && fiber[ctl].online==1)fiber[ctl].on_example=row;
                    if(!flag && fiber[ctl].offline==1)fiber[ctl].off_example=row;
                    ++processed;++fiber[ctl].pairs;two_paths+=common.size();three_paths+=paths.size();
                    fiber[ctl].two+=common.size();fiber[ctl].three+=paths.size();
                }
            }
        }
        if(processed!=232500 || onlines!=30000 || offlines!=202500 || clauses!=930000)
            throw runtime_error("Global pair or clause count mismatch");
        for(const auto&f:fiber)if(f.pairs!=7750 || f.online!=1000 || f.offline!=6750 || f.two!=5000 || f.three!=15500)
            throw runtime_error("Per-fiber route count mismatch");
        if(used_flags.size()!=3000)throw runtime_error("Not all 3000 OR5 flags used");
        out.close();records.close();
        if(!out || !records)throw runtime_error("Output write failed");
        phase="save_counts";
        ofstream calibration(dir+"/FIBER_CALIBRATION.json");
        calibration<<"[";
        auto write_row=[&](const array<uint32_t,7>&r){calibration<<'[';for(int i=0;i<7;++i){if(i)calibration<<',';calibration<<r[i];}calibration<<']';};
        for(int ctl=0;ctl<30;++ctl){
            if(ctl)calibration<<',';
            const auto&f=fiber[ctl];
            calibration<<"{\"fiber\":"<<ctl<<",\"pairs\":"<<f.pairs<<",\"online_pairs\":"<<f.online
                       <<",\"offline_pairs\":"<<f.offline<<",\"two_walks_total\":"<<f.two
                       <<",\"three_walks_total\":"<<f.three<<",\"clauses\":"<<f.pairs*4
                       <<",\"all_four_middle_vertices_distinct\":true,\"online_example\":";
            write_row(f.on_example);calibration<<",\"offline_example\":";write_row(f.off_example);calibration<<'}';
        }
        calibration<<"]\n";
        ofstream result(dir+"/NATIVE_RESULT.json");
        result<<"{\"status\":\"COMPLETE_SAME_FIBER_ROUTE_CLAUSES\",\"pairs\":"<<processed
              <<",\"online_pairs\":"<<onlines<<",\"offline_pairs\":"<<offlines
              <<",\"two_walks_total\":"<<two_paths<<",\"three_walks_total\":"<<three_paths
              <<",\"additional_variables\":0,\"additional_clauses\":"<<clauses
              <<",\"all_four_middle_vertices_distinct\":true,\"reused_OR5_flags\":"<<used_flags.size()
              <<",\"source_cache_reads\":1,\"source_edge_text_reads\":0,\"BFS_runs\":0,\"solver_calls\":0"
              <<",\"route_record_schema\":[\"x\",\"y\",\"a\",\"b\",\"c\",\"d\",\"OR5_flag_or0\"]"
              <<",\"route_record_encoding\":\"7 little-endian uint32 per pair, old vertex labels; lexicographic fiber/x/y order\""
              <<",\"CPU_seconds\":"<<cpu()<<"}\n";
        cout<<"COMPLETE pairs "<<processed<<" clauses "<<clauses<<" CPU "<<cpu()<<'\n';
        return 0;
    }catch(const Stop&){failure("CPU_BUDGET_STOP","native budget reached");return 3;}
    catch(const exception&e){failure("ROUTE_COUNT_OR_INPUT_MISMATCH",e.what());return 2;}
}
