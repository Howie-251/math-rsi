#include <cstdint>
#include <omp.h>
extern "C" void evaluate(long n,const int32_t* sh,const uint16_t* fi,const uint8_t* vi,const double* p,const double* f,const double* v,double* out){
#pragma omp parallel for num_threads(2) schedule(static)
for(long r=0;r<n;r++){
 double z=0;for(int j=0;j<4;j++)z+=p[sh[4*r+j]];z*=.25;
 double a=0;for(int j=0;j<24;j++)a+=f[fi[24*r+j]];z+=a/24.;
 a=0;for(int j=0;j<48;j++)a+=v[vi[48*r+j]];z+=a/48.;out[r]=z;
}}
