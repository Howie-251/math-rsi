// Producer replay/integrity check; deliberately not an independent proof review.
#define main producer_scan_main
#include "FOURTEEN_REUSE_scan.cpp"
#undef main
U get(const unsigned char*p,int n){U x=0;for(int j=0;j<n;++j)x|=U(p[j])<<(8*j);return x;}
int main(){try{
 for(int x=0;x<64;++x)for(int d=0;d<6;++d)projection[d][x]=(x&((1<<d)-1))|((x>>(d+1))<<d);
 int at=0;fill(oi,oi+32,-1);for(int x=0;x<32;++x)if(__builtin_popcount(unsigned(x))%2)oi[x]=at++;
 string names[4]={"T26","T15","T17","T63"};for(int j=0;j<4;++j){ifstream f("HIGHER_Q5_FULL_"+names[j]+"_lookup.txt");U x;while(f>>x)old[j].insert(x);}
 ifstream reg("FOURTEEN_REUSE_registry.txt");Key k;Value val;while(reg>>k.m>>k.j>>k.o>>val.R>>val.family>>val.id)registry.emplace(k,val);
 U all=0,positives=0,remaining=0;
 for(int v:{1,7,31})for(int free=0;free<2;++free){string tag="h14_v"+to_string(v)+"_"+(free?"free":"covered");ifstream in("HIGHER_Q5_FULL_residual_"+tag+".bin",ios::binary),wi("FOURTEEN_REUSE_witness_"+tag+".bin",ios::binary),rem("FOURTEEN_REUSE_remaining_"+tag+".bin",ios::binary);need(bool(in)&&bool(wi)&&bool(rem),"sanity input");unsigned char rec[13],w[32],r[13];bool has=bool(wi.read((char*)w,32));if(!has)need(!wi.gcount(),"witness partial");uint32_t index=0;
  while(in.read((char*)rec,13)){if(has){need(get(w,4)>=index,"witness order/duplicate");}
   if(has&&get(w,4)==index){int d=w[4],family=w[5],id=get(w+6,2);U S=get(w+8,8),H=1;B M=get(w+16,4),J=get(w+20,4),O=get(w+24,4),R=get(w+28,4);need(d<6,"cut");for(int j=0;j<13;++j)H|=U(1)<<rec[j];vector<int>za,zb,wa,wb;for(int j=0;j<6;++j)(((rec[j]>>d&1)==(v>>d&1))?za:zb).push_back(rec[j]);for(int j=6;j<13;++j)(((rec[j]>>d&1)==(v>>d&1))?wa:wb).push_back(rec[j]);int s=int(za.size())+1-int(wa.size());bool even=s>=0;if(!even)s=-s;need(!even||!wa.empty(),"even branch b0");U pool=0;for(int x:even?za:wa)if(even||(x!=(1<<d)&&(!free||x!=v)))pool|=U(1)<<x;need(!(S&~pool)&&__builtin_popcountll(S)==s,"source legality");B mm=0,jj=0,oo=0;for(int x:even?zb:wb)mm|=B(1)<<projection[d][x];for(int x:even?wb:zb)jj|=B(1)<<projection[d][x];for(int x=0;x<64;++x)if(S>>x&1){int y=x^(1<<d);need(!(H>>y&1),"mirror originally free");oo|=B(1)<<projection[d][y];}jj|=oo;need(mm==M&&jj==J&&oo==O,"actual masks");auto found=hit(M,J,O,(v>>d)&1);need(found.family==family&&found.id==id&&found.R==R,"membership replay");++positives;has=bool(wi.read((char*)w,32));if(!has)need(!wi.gcount(),"witness partial tail");
   }else{need(bool(rem.read((char*)r,13))&&equal(rec,rec+13,r),"remaining source-order bytes");++remaining;}
   ++index;++all;
  }
  need(!in.gcount()&&!has,"source/witness trailing records");need(!rem.read((char*)r,13)&&!rem.gcount(),"remaining trailing bytes");cout<<"checked "<<tag<<" "<<index<<endl;
 }
 need(all==9484443&&positives==9436232&&remaining==48211,"sanity totals");ofstream out("FOURTEEN_REUSE_sanity.json");out<<"{\"status\":\"PRODUCER_SANITY_ONLY\",\"source_records\":"<<all<<",\"all_selected_actual_witnesses_replayed\":"<<positives<<",\"all_remaining_source_order_records_compared\":"<<remaining<<",\"all_pass\":true,\"independent_application_acceptance\":false}\n";
}catch(const exception&e){cerr<<e.what()<<endl;return 1;}return 0;}
