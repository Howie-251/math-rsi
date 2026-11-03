#include <cstdint>
extern "C" {
void support_counts(const uint64_t*r3,const uint64_t*r4,int n,int w,uint32_t*out){
    for(int t=0;t<n;++t){uint32_t s=0;for(int k=0;k<w;++k){s+=__builtin_popcountll(r3[(int64_t)t*w+k]);s+=__builtin_popcountll(r4[(int64_t)t*w+k]);}out[t]=s;}
}
void row_nnz(const uint64_t*r3,const uint64_t*r4,const int32_t*rows,int m,int w,int32_t*out){
    for(int i=0;i<m;++i){int32_t s=0;for(int k=0;k<w;++k)s+=__builtin_popcountll(r3[(int64_t)rows[i]*w+k]|r4[(int64_t)rows[i]*w+k]);out[i]=s;}
}
void fill_rows(const uint64_t*r3,const uint64_t*r4,const int32_t*rows,int m,int w,const int32_t*ptr,int32_t*cols,double*val){
    for(int i=0;i<m;++i){int at=ptr[i];for(int k=0;k<w;++k){
        uint64_t a=r3[(int64_t)rows[i]*w+k],b=r4[(int64_t)rows[i]*w+k],u=a|b;
        while(u){int j=__builtin_ctzll(u);cols[at]=64*k+j;val[at]=((a>>j)&1)+((b>>j)&1);++at;u&=u-1;}
    }}
}
void evaluate_double(const uint64_t*r3,const uint64_t*r4,const double*x,int n,int w,double*out){
    for(int t=0;t<n;++t){double sum=0;for(int k=0;k<w;++k){
        uint64_t a=r3[(int64_t)t*w+k],b=r4[(int64_t)t*w+k],u=a|b;
        while(u){int j=__builtin_ctzll(u);sum+=x[64*k+j]*(((a>>j)&1)+((b>>j)&1));u&=u-1;}
    }out[t]=sum;}
}
void evaluate_integer(const uint64_t*r3,const uint64_t*r4,const int64_t*x,int n,int w,int64_t*out){
    for(int t=0;t<n;++t){int64_t sum=0;for(int k=0;k<w;++k){
        uint64_t a=r3[(int64_t)t*w+k],b=r4[(int64_t)t*w+k],u=a|b;
        while(u){int j=__builtin_ctzll(u);sum+=x[64*k+j]*(((a>>j)&1)+((b>>j)&1));u&=u-1;}
    }out[t]=sum;}
}
}
