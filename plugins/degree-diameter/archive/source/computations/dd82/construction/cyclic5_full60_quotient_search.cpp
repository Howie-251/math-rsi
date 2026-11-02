// One continuous quotient annealing trajectory; no voltage or graph search.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using Matrix = array<int,144>;
using Edge = pair<int,int>;

void change(Matrix& m, Edge e, int delta) {
    auto [a,b]=e;
    if(a==b) m[12*a+a]+=2*delta;
    else {m[12*a+b]+=delta; m[12*b+a]+=delta;}
}
Edge canonical(int a,int b) {return minmax(a,b);}
bool domain(const Matrix& m) {
    for(int a=0;a<12;++a) {
        if(m[12*a+a]!=0 && m[12*a+a]!=2) return false;
        int sum=0;
        for(int b=0;b<12;++b) {
            if(a!=b && (m[12*a+b]<0 || m[12*a+b]>3)) return false;
            sum+=m[12*a+b];
        }
        if(sum!=8) return false;
    }
    return true;
}
int odd_double_components(const Matrix& m) {
    array<bool,12> seen{};int count=0;
    for(int start=0;start<12;++start)if(!seen[start]) {
        array<int,12> queue{};int head=0,tail=1;queue[0]=start;seen[start]=true;
        bool all_two=true;
        while(head<tail) {
            int a=queue[head++],degree=0;
            for(int b=0;b<12;++b)if(a!=b && m[12*a+b]==2) {
                ++degree;
                if(!seen[b]){seen[b]=true;queue[tail++]=b;}
            }
            all_two=all_two && degree==2;
        }
        if(all_two && tail>=3 && tail%2==1)++count;
    }
    return count;
}
int evaluate(const Matrix& m,Matrix& d,int& zeros) {
    zeros=0;int negative=0;
    for(int a=0;a<12;++a) {
        zeros+=m[12*a+a]==0;
        for(int b=a;b<12;++b) {
            int x=m[12*a+b]-5-(a==b?7:0);
            for(int c=0;c<12;++c) x+=m[12*a+c]*m[12*c+b];
            d[12*a+b]=d[12*b+a]=x;
            if(x<0) negative-=x*(a==b?1:2);
        }
    }
    return negative+8*max(0,2-zeros)+2*odd_double_components(m);
}
void matrix_json(ostream& out,const Matrix& m) {
    out<<'[';
    for(int a=0;a<12;++a) {
        if(a)out<<',';out<<'[';
        for(int b=0;b<12;++b){if(b)out<<',';out<<m[12*a+b];}
        out<<']';
    }
    out<<']';
}
struct Improvement {unsigned long long proposal;int score,zeros;double cpu;Matrix m;};
int main(int argc,char** argv) {
    if(argc!=5)return 2;
    const double cpu_budget=stod(argv[3]),wall_budget=stod(argv[4]);
    const double cpu_start=double(clock())/CLOCKS_PER_SEC;
    const auto wall_start=chrono::steady_clock::now();
    ifstream input(argv[1]);Matrix current{};
    for(int& x:current)if(!(input>>x))return 3;
    if(!domain(current))return 4;
    Matrix initial=current,defect{};
    vector<Edge> edges;
    for(int a=0;a<12;++a)for(int b=a;b<12;++b)
        for(int k=0;k<(a==b?current[12*a+b]/2:current[12*a+b]);++k)
            edges.push_back({a,b});
    if(edges.size()!=48)return 5;
    int zeros=0,score=evaluate(current,defect,zeros);
    if(zeros!=0 || score!=16)return 6;
    Matrix best=current,best_defect=defect,first_departure{};
    int best_score=score,best_zeros=zeros;
    bool departed=false,found=false;
    unsigned long long proposals=0,valid=0,unchanged=0,accepted=0,uphill=0,nonzero_defect_accepted=0;
    vector<Improvement> trace{{0,score,zeros,0,current}};
    mt19937_64 random(20261013);
    uniform_int_distribution<int> choose(0,47);
    uniform_real_distribution<double> uniform(0.0,1.0);
    double temperature=3.5,elapsed=0;
    string stop="cpu_budget";
    while(true) {
        if((proposals&1023)==0) {
            elapsed=double(clock())/CLOCKS_PER_SEC-cpu_start;
            double wall=chrono::duration<double>(chrono::steady_clock::now()-wall_start).count();
            if(elapsed>=cpu_budget){stop="cpu_budget";break;}
            if(wall>=wall_budget){stop="wall_budget";break;}
            double progress=min(1.0,max(elapsed/cpu_budget,wall/wall_budget));
            temperature=3.5*pow(0.25/3.5,progress);
        }
        ++proposals;
        int i=choose(random),j=choose(random);if(i==j)continue;
        auto [a,b]=edges[i];auto [c,d]=edges[j];
        Edge first,second;
        if(random()&1) {first=canonical(a,c);second=canonical(b,d);}
        else {first=canonical(a,d);second=canonical(b,c);}
        Matrix trial=current;
        change(trial,edges[i],-1);change(trial,edges[j],-1);
        change(trial,first,1);change(trial,second,1);
        if(trial==current){++unchanged;continue;}
        if(!domain(trial))continue;
        ++valid;
        Matrix trial_defect{};int trial_zeros=0;
        int trial_score=evaluate(trial,trial_defect,trial_zeros);
        const int delta=trial_score-score;
        if(delta>0 && uniform(random)>=exp(-double(delta)/temperature))continue;
        ++accepted;if(delta>0)++uphill;
        if(any_of(trial_defect.begin(),trial_defect.end(),[](int x){return x<0;}))++nonzero_defect_accepted;
        edges[i]=first;edges[j]=second;
        current=trial;defect=trial_defect;score=trial_score;zeros=trial_zeros;
        if(!departed){first_departure=current;departed=true;}
        if(score<best_score) {
            best=current;best_defect=defect;best_score=score;best_zeros=zeros;
            trace.push_back({proposals,score,zeros,double(clock())/CLOCKS_PER_SEC-cpu_start,current});
        }
        if(score==0) {found=true;stop="quotient_found";break;}
    }
    ofstream out(argv[2]);out<<setprecision(15);
    out<<"{\"found\":"<<(found?"true":"false")<<",\"complete_enumeration\":false,\"stop_reason\":\""<<stop
       <<"\",\"rng_seed\":20261013,\"trajectories\":1,\"state_resets\":0,\"proposals\":"<<proposals
       <<",\"domain_valid_changed_proposals\":"<<valid<<",\"unchanged_proposals\":"<<unchanged
       <<",\"accepted\":"<<accepted<<",\"accepted_uphill\":"<<uphill
       <<",\"accepted_with_negative_defect\":"<<nonzero_defect_accepted
       <<",\"best_score\":"<<best_score<<",\"best_independent_orbits\":"<<best_zeros
       <<",\"last_score\":"<<score<<",\"temperature_start\":3.5,\"temperature_final\":"<<temperature
       <<",\"cpu_budget_seconds\":"<<cpu_budget<<",\"wall_budget_seconds\":"<<wall_budget
       <<",\"search_cpu_seconds\":"<<double(clock())/CLOCKS_PER_SEC-cpu_start
       <<",\"search_wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-wall_start).count()
       <<",\"initial_matrix\":";matrix_json(out,initial);
    out<<",\"best_matrix\":";matrix_json(out,best);
    out<<",\"best_defect\":";matrix_json(out,best_defect);
    out<<",\"last_matrix\":";matrix_json(out,current);
    out<<",\"last_defect\":";matrix_json(out,defect);
    out<<",\"departed_initial\":"<<(departed?"true":"false");
    if(departed){out<<",\"first_departure_matrix\":";matrix_json(out,first_departure);}
    out<<",\"improvement_trace\":[";
    for(size_t k=0;k<trace.size();++k){
        if(k)out<<',';auto& x=trace[k];
        out<<"{\"proposal\":"<<x.proposal<<",\"score\":"<<x.score<<",\"independent_orbits\":"<<x.zeros
           <<",\"cpu_seconds\":"<<x.cpu<<",\"matrix\":";matrix_json(out,x.m);out<<'}';
    }
    out<<"]}\n";
    cout<<"found "<<found<<" best "<<best_score<<" proposals "<<proposals<<" accepted "<<accepted<<endl;
}
