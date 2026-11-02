
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define NUMGEN 6
#define TRUE   1
#define FALSE  0

FILE *resul,*info;

unsigned int M,N,A,D;
unsigned int GEN[NUMGEN];
unsigned int HIES[900000],usdegen[NUMGEN];
unsigned int quants,diam,avgdst,generat;
unsigned int  Avals[2000];
clock_t start, end;   
 
long ORDRE;
double mquants[100];

int* valid_units(int m, int n);
unsigned int invers(unsigned int x);
unsigned int elevaA(unsigned int x);
unsigned int producte(unsigned int x, unsigned int y);
void calcula();
void guarda();
void guardatot();



/****************************************/ 
int main(void)
{   int i, j, k, l, a, g, x, y, inv,u,v, minidx, maxinv, maxiter, Dplusone, mingenval, minavgdst, oldavgdst, newavgdst, tottest, trobat, geninv[20000];    double runtime;

srand(time(0));

/* poss values

Z_49  A_41   Z_6763
[25,1254],[18,541], [47,4642] -> 170329, 122275, 322503

*/
 /* ******************** */
 
 
        M = 49;   N = 6763;   D = 9;
int   Avals[] =  { 41 };  //  331 387  Alexis Rodriguez  


      
    
    ORDRE = M * N;  
    quants = 1 + NUMGEN;
    start = clock();
    maxinv = ORDRE;
            
           
time_t currentTime;
time(&currentTime);
// Format the time as a string
char formattedTime[20]; // Adjust the size based on your needs
struct tm *timeInfo;
timeInfo = localtime(&currentTime);   
// Customize the format as needed
strftime(formattedTime, sizeof(formattedTime), "\n %Y-%m-%d %H:%M", timeInfo);
// Print the formatted time
printf("%s\n", formattedTime);


for (a = 0; a < sizeof(Avals)/sizeof(int); a++) {
A=Avals[a];
maxinv=0;    
for (i=0; i<ORDRE; i++){
 	 inv=invers(i);
         if (i == inv) {
                geninv[maxinv] = i;
                maxinv = maxinv+1;
                 }
           }
 printf(" maxinv= %d\n",maxinv);           

/*
 for (k=0;k<maxinv;k++){
 	    inv=invers(geninv[k]);
            x=geninv[k] / N;
            y=geninv[k] %N;
            u= inv/N;
            v= inv % N;
            printf("idx: %d -> %d  [%d %d] \t /inv. %d [%d %d] \n",k,geninv[k],x,y, inv,u,v);
            }
*/
                       

                             
if (maxinv > 0){
for (i=0; i<3; i++){
Dplusone=0;
tottest=1;
              
            GEN[0] =   170329;
            GEN[1] = invers(GEN[0]);
             GEN[2] =  122275;
            GEN[3] = invers(GEN[2]);
            GEN[4] =   322503;
            GEN[5] = invers(GEN[4]);
          
              calcula();
                if ((diam <= D) && (generat == 1)) {
                        for(k=0; k<NUMGEN; k=k+2){
                              y=(GEN[k])%N;
                              x=((GEN[k]-y)/N) % M;
                              v=(invers(GEN[k]))%N;
                              u=((invers(GEN[k])-v)/N) % M;
                              printf("[%d,%d]<>[%d,%d]:",x,y,u,v);
                             }
                         guardatot();
                         end = clock();
                         runtime = ((double) (end - start)) / CLOCKS_PER_SEC;
                         printf("i = %d, Time elapsed: %.2f seconds\n", i, runtime);
                         exit(0);
                      } // if diam 

    newavgdst=avgdst;
   minavgdst=avgdst;

             printf("%s  i=%d, [%dx(%d)%d] (%d,%d)=%ld, diam: %d, minavdst: %d, avdst: %d, D+1: %d of %d  --- ", formattedTime, i, M, A, N,NUMGEN,D, ORDRE, diam, minavgdst, avgdst, Dplusone, tottest);
              for(g=0; g<NUMGEN; g++){
                   printf("%d, ",GEN[g]);
                  }              
            printf("\n");
 printf("%d, ",GEN[0]);
 printf("%d, ",invers(GEN[0]));
  printf("%d, ",GEN[2]);
 printf("%d, ",invers(GEN[2]));
 printf("%d, ",GEN[4]);
 printf("%d, ",invers(GEN[4]));
            printf("\n");
     exit(0);
      

    for (j=1; j <  2; j++){
 
           tottest += 1;
          
           
            GEN[0] =  170329; 
            GEN[1] = invers(GEN[0]);
             GEN[2] = 122275; 
            GEN[3] = invers(GEN[2]);
            GEN[4] =  322503;
            GEN[5] = invers(GEN[4]);
    
             calcula();
                      if ((diam <= D) && (generat == 1)) {
                         for(k=0; k<NUMGEN; k=k+2){
                              y=(GEN[k])%N;
                              x=((GEN[k]-y)/N) % M;
                              v=(invers(GEN[k]))%N;
                              u=((invers(GEN[k])-v)/N) % M;
                              printf("[%d,%d]<>[%d,%d]:",x,y,u,v);
                             }
                        guardatot();
                         end = clock();
                         runtime = ((double) (end - start)) / CLOCKS_PER_SEC;
                         printf("i = %d, Time elapsed: %.2f seconds\n", i, runtime);
                         exit(0);
                          }  // if diam 
                             
             if (diam == D+1) {
                 Dplusone = Dplusone+1;
                 }
             if (avgdst < minavgdst) {
                 minavgdst = avgdst;
                 }
                 
                                  
 
        } // for j
                    end = clock();
//            runtime = ((double) (end - start)) / CLOCKS_PER_SEC;

time_t currentTime;
time(&currentTime);
// Format the time as a string
char formattedTime[20]; // Adjust the size based on your needs
struct tm *timeInfo;
timeInfo = localtime(&currentTime);   
// Customize the format as needed
strftime(formattedTime, sizeof(formattedTime), "%Y-%m-%d %H:%M", timeInfo);


            float percent = ((float) Dplusone / tottest) * 100;
             printf("%s  i=%d, [%dx(%d)%d] (%d,%d)=%ld, diam: %d, minavdst: %d, avdst: %d, D+1: %d of %d (%.1f%%) --- ", formattedTime, i, M, A, N,NUMGEN,D, ORDRE, diam, minavgdst, avgdst, Dplusone, tottest, percent);
              for(g=0; g<NUMGEN; g++){
                   printf("%d, ",GEN[g]);
                  }              
            printf("\n");



                tottest=0;;
                 Dplusone=0;
                 minavgdst=999999999;
    }  // for i
  } // if maxinv
printf("\n");
} /* for a */
}

/****************************************/

int* valid_units(int m, int n) {
    int i, j;
    int order, temp;
    int* units = (int*) malloc(n * sizeof(int));
    int num_units = 0;

    for (i = 1; i < n; i++) {
        order = 1;
        temp = i % n;
        
        for (j = 1; j <= n; j++) {
            temp = (temp * i) % n;
            if (temp == 1) {
                order = j;
                break;
            }
        }
        
        if (m % order == 0) {
            units[num_units] = i;
            num_units++;
        }
    }
    
    // Resize the array to only the necessary size
    units = (int*) realloc(units, num_units * sizeof(int));
    
    return units;
}

/****************************************/
unsigned int invers(unsigned int x)
      {
      unsigned int x1,x2,z1,z2;
      x1=x/N;
      x2=x%N;
      z1=(M-x1)%M;
      z2=(N-(x2*(elevaA(z1))%N))%N;
      return(z1*N+z2);
      }
/****************************************/

unsigned  int elevaA(unsigned int x)
     {
      unsigned int i;
      unsigned int y,y1;
      if (x==0)
      return(1);
      y=A;
      for (i=1;i<x;i++)
	{
	y1=y*A;
	y=y1% N;
	}
      return(y);
      }

/****************************************/
unsigned int producte(unsigned int x, unsigned int y)
    {
     unsigned int x1,x2,y1,y2,z1,z2;
     x1=x / N;
     x2 = x % N;
     y1 = y / N;
     y2 = y % N;
     z1 = (x1+y1 ) % M ;
     z2 = (x2*elevaA(y1) + y2) % N;
     return(z1*N+z2);
     }
/****************************************/
void guarda()
 /***** es guarda el resultat en un fitxer  *****/
{
unsigned int i,ordre;
char filename[50];

ordre=ORDRE; 

sprintf(filename, "grf%d.res",ordre);

if((resul=fopen(filename,"a"))==NULL)
          perror("** ERROR, no es pot obrir el fitxer de dades bones**");

fprintf(resul,"M= %d, N= %d, A= %d,  ORD= %d\n",M,N,A,M*N);
fprintf(resul,"diam=%d\n",diam);
for(i=0;i<NUMGEN;i++)
fprintf(resul,"Generador[%d]  invers / %d / =  %d \t  (%d)\n",i,GEN[i], invers(GEN[i]), usdegen[i]);
fprintf(resul,"Generador[%d]=%d\t (%d)\n",i,GEN[i],usdegen[i]);
i=0;
while(mquants[i]!=0)
     {
     fprintf(resul,"nivell %d\t %g\n",i,mquants[i]);
     i++;
      }
fclose(resul);
}

/****************************************/
void guardatot()
 /***** es guarda T el resultat en un fitxer , incloent adjacencies*****/
{
unsigned int i,j,k,ordre,m,n,x,y,u,v,a;
char filename[50];

ordre=ORDRE; m = M; n = N; a = A;

sprintf(filename, "allinfogrf%d_%d_%d_%d.txt",ordre,m,n,a);

if((info=fopen(filename,"a"))==NULL)
          perror("** ERROR, no es pot obrir el fitxer de dades bones**");
fprintf(info,"(%d,%d)=%d | M=%d, N=%d, A=%d\n",NUMGEN,D,M*N,M,N,A);
fprintf(info,"diam=%d\n",diam);
fprintf(info,"avddst=%d\n",avgdst);
for(i=0;i<NUMGEN;i++){
       y=(GEN[i])%N;
       x=((GEN[i]-y)/N) % M;
   fprintf(info,"Generador[%d]=%d  [ %d,%d ] \t /inv. %d/ \t (%d)\n",i,GEN[i],x,y, invers(GEN[i]),usdegen[i]);
   }
for(i=0;i<NUMGEN;i=i+2){
       y=(GEN[i])%N;
       x=((GEN[i]-y)/N) % M;
       v=(invers(GEN[i]))%N;
       u=((invers(GEN[i])-v)/N) % M;
        fprintf(info,"[%d,%d ]<>[%d,%d ]:",x,y,u,v);
   }
fprintf(info,"\n levels\n "); 
i=0;
while(mquants[i]!=0)
     {
     fprintf(info,"%d\t %g\n",i,mquants[i]);
     i++;
      }
fprintf(info,"\n");
end = clock();
double runtime = ((double) (end - start)) / CLOCKS_PER_SEC;
fprintf(info,"Runtime: %.2f seconds\n",  runtime);
 
for (j=0;j<ORDRE;j++)
   {
   for (k=0;k<NUMGEN;k++)
     fprintf(info,"  %d",producte(GEN[k],j));
   fprintf(info,"\n");
   }
fprintf(info,"\n\n");     
fclose(info);
}


/*****************************************/
/***** calcul el diametre del graf   compta les vegades que s'utilitza un generador   *****/

void calcula()
{
 unsigned int quantsvell,nivell,diamvell,k,j,i;

 diam=0;
 quants=1+NUMGEN;

 for (i=0;i<100;i++)
       mquants[i]=0;

 mquants[0]=1;
 mquants[1]=NUMGEN;

/***** inicialitzar a 0  HIES[j] (a quin nivell apareix el node j) i
 usdegen[i](nombre de vegades que s'utilitza el generador i) *****/

 for (j=0;j<ORDRE;j++)
       HIES[j]=0;


 /***** posar 1 a HIES i usdegen pels generadors *****/
 for (j=0;j<NUMGEN;j++)
      {
      HIES[GEN[j]]=1;
      usdegen[j]=1;
      }

  for(nivell=2;quants<ORDRE;nivell++)
      {
      quantsvell=quants; /* per cada nivell guarda el # de nodes */
       for(i=0;i<NUMGEN;i++)
	   {
	    for(j=0;j<ORDRE;j++) /*multiplica un generador
			   per un node existent*/
		 {
		   if(HIES[j]==nivell-1)
			{
			 k=producte(GEN[i],j);
			 if (HIES[k]==0 && k!=0)
			   {
			   HIES[k]=nivell;
			   quants++;
			   usdegen[i]++;
			   }       /*anota node nou*/
			 }
		 }      /*acaba de multiplicar GEN[i] pels nodes
			   de nivell anterior*/
	   } /*canvia de generador */
	   if (quantsvell==quants)
	      {
	      /* no es genera tot el graf*/
	      generat=0;
	      return;
	      }
       mquants[nivell]=(double)(quants-quantsvell);
      } /*canvia de nivell*/
      if (quants==ORDRE)   generat=1;
      {
      diam=nivell-1;
      
      avgdst=0;
      for (int n = 0; n < nivell; n++) {
        avgdst+= mquants[n]*n;
      }
      /*
      printf("avgdst  %d\n",avgdst);
      */
      }
}
/****************************************/

