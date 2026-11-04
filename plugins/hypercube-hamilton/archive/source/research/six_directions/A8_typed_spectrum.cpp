#include <bits/stdc++.h>
using namespace std;
struct Mask {uint64_t lo=0,hi=0;void set(int i){if(i<64)lo|=1ull<<i;else hi|=1ull<<(i-64);}bool meet(Mask b)const{return (lo&b.lo)||(hi&b.hi);}bool operator<(Mask b)const{return tie(lo,hi)<tie(b.lo,b.hi);}};
struct DS {int p[40];DS(){iota(p,p+40,0);}int get(int a){return p[a]==a?a:p[a]=get(p[a]);}bool join(int a,int b){a=get(a);b=get(b);if(a==b)return false;p[a]=b;return true;}};
vector<pair<int,int>> patterns[96];int np=0;vector<vector<pair<int,int>>> pairings;map<uint32_t,int> ranks;
vector<pair<int,int>> cur;
void shortPM(vector<int> v,int x,int y){if(v.empty()){patterns[np]=cur;patterns[np].push_back({15,x});patterns[np].push_back({15,y});np++;return;}int a=v[0];for(int j=1;j<(int)v.size();j++)if(__builtin_popcount(a^v[j])==1){auto w=v;int b=v[j];w.erase(w.begin()+j);w.erase(w.begin());cur.push_back({a,b});shortPM(w,x,y);cur.pop_back();}}
void genpair(vector<int> v){if(v.empty()){uint32_t k=0;for(auto[a,b]:cur)k|=(uint32_t(b)<<(4*a))|(uint32_t(a)<<(4*b));ranks[k]=pairings.size();pairings.push_back(cur);return;}int a=v[0];for(int j=1;j<(int)v.size();j++){auto w=v;int b=v[j];w.erase(w.begin()+j);w.erase(w.begin());cur.push_back({a,b});genpair(w);cur.pop_back();}}
array<unsigned char,16> am;vector<int> ap;int c;ofstream af;
struct Type {uint64_t count=0;array<unsigned char,16> rep;};map<Mask,Type> types;uint64_t acount=0,asum=0;int amin=1000,amax=0;
void avisit(){vector<int>T={1,2,4};T.insert(T.end(),ap.begin(),ap.end());Mask m;
 for(int k=0;k<np;k++){DS d;bool ok=true;for(int a=0;a<16;a++)if(am[a]<16&&a<am[a])d.join(a,am[a]);for(auto[a,b]:patterns[k])if(!d.join(a,b)){ok=false;break;}if(!ok)continue;
 uint32_t key=0;for(int a=0;a<(int)T.size();a++){int mate=-1;for(int b=0;b<(int)T.size();b++)if(a!=b&&d.get(T[a])==d.get(T[b])){assert(mate==-1);mate=b;}assert(mate>=0);key|=uint32_t(mate)<<(4*a);}assert(ranks.count(key));m.set(ranks.at(key));}
 int card=__builtin_popcountll(m.lo)+__builtin_popcountll(m.hi);assert(card>0);amin=min(amin,card);amax=max(amax,card);asum+=card;
 af.write((char*)am.data(),16);af.write((char*)&m,16);auto &t=types[m];if(!t.count)t.rep=am;t.count++;acount++;
}
void apair(vector<int>v){if(v.empty()){avisit();return;}int a=v[0];for(int j=1;j<(int)v.size();j++){auto w=v;int b=v[j];w.erase(w.begin()+j);w.erase(w.begin());am[a]=b;am[b]=a;apair(w);am[a]=am[b]=255;}}
void aport(vector<int>v,int start){if((int)ap.size()==c){vector<int>rem;for(int x:v)if(find(ap.begin(),ap.end(),x)==ap.end())rem.push_back(x);apair(rem);return;}for(int j=start;j<(int)v.size();j++){ap.push_back(v[j]);aport(v,j+1);ap.pop_back();}}
int main(int argc,char**argv){assert(argc==2);c=stoi(argv[1]);assert(c==1||c==3||c==5);int ns[]={7,11,13,14};for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){vector<int>v;for(int x=1;x<15;x++)if(x!=ns[i]&&x!=ns[j])v.push_back(x);shortPM(v,ns[i],ns[j]);}assert(np==96);
 vector<int>v(c+3);iota(v.begin(),v.end(),0);genpair(v);am.fill(255);vector<int>avail;for(int x=1;x<16;x++)if(x!=1&&x!=2&&x!=4&&x!=15)avail.push_back(x);
 string stem="A8_typed_c"+to_string(c);af.open(stem+"_A.bin",ios::binary);aport(avail,0);af.close();cerr<<"c="<<c<<" patterns="<<np<<" A="<<acount<<" types="<<types.size()<<" spectrum="<<amin<<".."<<amax<<endl;
 ifstream bf("A8_three_bridge_low_B_c"+to_string(c)+".bin",ios::binary);ofstream masks(stem+"_B.bin",ios::binary),fails(stem+"_zero_examples.txt");array<unsigned char,16>bm;uint64_t bc=0,bperm=0,zero=0,ztypes=0;map<Mask,uint64_t>btypes;int bmin=1000,bmax=0;
 while(bf.read((char*)bm.data(),16)){bc++;vector<int>bp;for(int x=0;x<16;x++)if(bm[x]==255&&x!=7&&x!=11&&x!=13)bp.push_back(x);assert((int)bp.size()==c);vector<int>perm(c);iota(perm.begin(),perm.end(),0);
 do{Mask good;for(int r=0;r<(int)pairings.size();r++){DS d;bool ok=true;for(int x=0;x<16;x++)if(bm[x]<16&&x<bm[x])d.join(x,bm[x]);for(int k=0;k<3;k++)d.join(16+k,1<<k);for(int k=0;k<c;k++)d.join(19+k,bp[perm[k]]);for(auto[a,b]:pairings[r])if(!d.join(16+a,16+b)){ok=false;break;}if(ok&&d.get(0)!=d.get(8))good.set(r);}
 int card=__builtin_popcountll(good.lo)+__builtin_popcountll(good.hi);bmin=min(bmin,card);bmax=max(bmax,card);btypes[good]++;bperm++;
 masks.write((char*)bm.data(),16);for(int x:perm)masks.put((char)x);masks.write((char*)&good,16);
 for(auto &[m,t]:types)if(!m.meet(good)){zero+=t.count;ztypes++;if(ztypes<=100){fails<<"A";for(auto x:t.rep)fails<<' '<<int(x);fails<<" B";for(auto x:bm)fails<<' '<<int(x);fails<<" permutation";for(int x:perm)fails<<' '<<x;fails<<" multiplicity "<<t.count<<'\n';}}
 }while(next_permutation(perm.begin(),perm.end()));}
 assert(bf.eof()&&bf.gcount()==0);
 ofstream report(stem+"_result.json");report<<"{\"crossings\":"<<c<<",\"short_patterns\":"<<np<<",\"pairings\":"<<pairings.size()<<",\"A_inputs\":"<<acount<<",\"A_types\":"<<types.size()<<",\"A_spectrum_min\":"<<amin<<",\"A_spectrum_max\":"<<amax<<",\"A_total_pairings\":"<<asum<<",\"B_inputs\":"<<bc<<",\"B_bijections\":"<<bperm<<",\"B_types\":"<<btypes.size()<<",\"B_spectrum_min\":"<<bmin<<",\"B_spectrum_max\":"<<bmax<<",\"zero_type_pairs\":"<<ztypes<<",\"zero_original_input_pairs\":"<<zero<<",\"closure_claimed\":false}\n";
 cerr<<"B="<<bc<<" permutations="<<bperm<<" Btypes="<<btypes.size()<<" zero="<<zero<<" typezeros="<<ztypes<<endl;
}
