#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct Graph {
    unsigned edgeMask;
    vector<unsigned> neighbor, closed;
    vector<int> degree;
};
struct Witness {
    bool present=false;
    unsigned graph=0;
    vector<unsigned> owners;
    vector<int> a,d;
    int cap=0, weighted=0;
};
struct Stats {
    int M,t;
    uint64_t assignments=0, configs=0, routeValid=0;
    uint64_t validEmpty=0, validMulti=0, validEmptyMulti=0;
    uint64_t validSingletonNonempty=0;
    int minCap=999;
    map<int,uint64_t> histogram;
    Witness minimum, empty, multi, emptyMulti;
};

static void arrayOut(ostream& o,const vector<unsigned>& v) {
    o<<'[';for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}o<<']';
}
static void intArrayOut(ostream& o,const vector<int>& v) {
    o<<'[';for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}o<<']';
}
static void witnessOut(ostream& o,const Witness& w) {
    if(!w.present){o<<"null";return;}
    o<<"{\"helper_graph_edge_mask\":"<<w.graph<<",\"owner_subset_masks_by_class\":";
    arrayOut(o,w.owners);o<<",\"a_by_helper\":";intArrayOut(o,w.a);
    o<<",\"d_by_helper\":";intArrayOut(o,w.d);
    o<<",\"minimal_cap\":"<<w.cap<<",\"sum_a_times_d_plus2\":"<<w.weighted<<'}';
}
static Witness getWitness(const Graph& g,const vector<unsigned>& owners,
                          const vector<int>& a,int cap,int weighted) {
    Witness w;w.present=true;w.graph=g.edgeMask;w.owners=owners;
    w.a=a;w.d=g.degree;w.cap=cap;w.weighted=weighted;return w;
}

static Stats check(int M,int t) {
    Stats st;st.M=M;st.t=t;
    const unsigned all=(1u<<t)-1;
    vector<pair<int,int>> edges;
    for(int i=0;i<t;++i)for(int j=i+1;j<t;++j)edges.emplace_back(i,j);
    vector<Graph> graphs;
    for(unsigned em=0;em<(1u<<edges.size());++em) {
        Graph g;g.edgeMask=em;g.neighbor.assign(t,0);g.degree.assign(t,0);
        for(unsigned i=0;i<edges.size();++i)if(em&(1u<<i)) {
            auto [a,b]=edges[i];g.neighbor[a]|=1u<<b;g.neighbor[b]|=1u<<a;
            ++g.degree[a];++g.degree[b];
        }
        g.closed.resize(1u<<t);
        for(unsigned s=0;s<=all;++s) {
            unsigned covered=s;
            for(int h=0;h<t;++h)if(s&(1u<<h))covered|=g.neighbor[h];
            g.closed[s]=covered;
        }
        graphs.push_back(g);
    }
    const uint64_t nassign=uint64_t(1)<<(t*M);
    vector<unsigned> owners(M);
    vector<int> a(t);
    for(uint64_t code=0;code<nassign;++code) {
        ++st.assignments;
        fill(a.begin(),a.end(),0);
        bool hasEmpty=false,hasMulti=false;
        for(int c=0;c<M;++c) {
            unsigned s=(code>>(t*c))&all;owners[c]=s;
            hasEmpty|=(s==0);hasMulti|=(__builtin_popcount(s)>1);
            for(int h=0;h<t;++h)if(s&(1u<<h))++a[h];
        }
        for(const Graph& g:graphs) {
            ++st.configs;
            bool valid=true;
            for(int c=0;c<M;++c)if((owners[c]|g.closed[owners[c^1]])!=all) {
                valid=false;break;
            }
            if(!valid)continue;
            ++st.routeValid;
            st.validEmpty+=hasEmpty;st.validMulti+=hasMulti;
            st.validEmptyMulti+=(hasEmpty&&hasMulti);
            st.validSingletonNonempty+=(!hasEmpty&&!hasMulti);
            int cap=0,weighted=0,quadraticSum=0;
            for(int h=0;h<t;++h)cap=max(cap,a[h]+g.degree[h]);
            for(int h=0;h<t;++h) {
                weighted+=a[h]*(g.degree[h]+2);
                quadraticSum+=(cap-g.degree[h])*(g.degree[h]+2);
            }
            const int bound=(cap+2)*(cap+2)/4;
            bool pointwiseRouteCount=true;
            for(int c=0;c<M;++c) {
                int count=__builtin_popcount(owners[c])+__builtin_popcount(owners[c^1]);
                for(int h=0;h<t;++h)if(owners[c^1]&(1u<<h))count+=g.degree[h];
                pointwiseRouteCount&=(t<=count);
            }
            if(!pointwiseRouteCount || M*t>weighted || weighted>quadraticSum ||
               quadraticSum>t*bound || M>bound) {
                ofstream fail("INDEPENDENT_UNIFORM_MULTICOPY_COUNTEREXAMPLE.json");
                fail<<"{\"M\":"<<M<<",\"t\":"<<t<<",\"witness\":";
                witnessOut(fail,getWitness(g,owners,a,cap,weighted));fail<<"}\n";
                throw string("COUNTEREXAMPLE");
            }
            ++st.histogram[cap];
            if(cap<st.minCap) {
                st.minCap=cap;st.minimum=getWitness(g,owners,a,cap,weighted);
            }
            if(hasEmpty&&!st.empty.present)st.empty=getWitness(g,owners,a,cap,weighted);
            if(hasMulti&&!st.multi.present)st.multi=getWitness(g,owners,a,cap,weighted);
            if(hasEmpty&&hasMulti&&!st.emptyMulti.present)
                st.emptyMulti=getWitness(g,owners,a,cap,weighted);
        }
    }
    return st;
}

int main() {
    try {
        vector<Stats> results;
        results.push_back(check(4,4));results.push_back(check(6,3));
        ofstream out("INDEPENDENT_UNIFORM_MULTICOPY_TOY_RESULT.json");
        out<<"{\"status\":\"PASS_NO_FINITE_COUNTEREXAMPLE\",\"matching\":\"T(c)=c xor1\","
              "\"owner_representation\":\"arbitrary subsets of all t helpers, bit h means h owns at least one clone in class c\","
              "\"routes_are_center_necessary_condition_only\":true,\"cases\":[";
        uint64_t total=0,valid=0;
        for(size_t i=0;i<results.size();++i) {
            if(i)out<<',';auto& s=results[i];total+=s.configs;valid+=s.routeValid;
            out<<"{\"M\":"<<s.M<<",\"t\":"<<s.t<<",\"owner_assignments\":"<<s.assignments
               <<",\"configurations\":"<<s.configs<<",\"route_valid\":"<<s.routeValid
               <<",\"route_valid_with_empty_class\":"<<s.validEmpty
               <<",\"route_valid_with_multi_owner_class\":"<<s.validMulti
               <<",\"route_valid_with_both\":"<<s.validEmptyMulti
               <<",\"route_valid_all_classes_singleton_nonempty\":"<<s.validSingletonNonempty
               <<",\"minimum_helper_cap\":"<<s.minCap<<",\"cap_histogram\":{";
            bool first=true;for(auto [cap,n]:s.histogram) {
                if(!first)out<<',';first=false;out<<'"'<<cap<<"\":"<<n;
            }
            out<<"},\"minimum_cap_witness\":";witnessOut(out,s.minimum);
            out<<",\"first_empty_class_witness\":";witnessOut(out,s.empty);
            out<<",\"first_multi_owner_witness\":";witnessOut(out,s.multi);
            out<<",\"first_empty_and_multi_owner_witness\":";witnessOut(out,s.emptyMulti);
            out<<'}';
        }
        out<<"],\"total_configurations\":"<<total<<",\"total_route_valid\":"<<valid
           <<",\"counterexamples\":0}\n";
        cout<<"PASS configurations="<<total<<" route_valid="<<valid<<'\n';
        return 0;
    } catch(const string& e) {cerr<<e<<'\n';return 2;}
}
