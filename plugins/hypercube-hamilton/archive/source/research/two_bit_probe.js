// Exhaustive unlabeled partitions of the 3-cube into at most four cells.
// Floating-point screening on a finite noise grid: NOT a proof.
const fs = require('fs');
const n=3, N=1<<n;
const ps=[0,.001,.01,.05,.1,.2,.3,.4,.45,.49,.499,.5];
const h=p=>p<=0||p>=1?0:-p*Math.log2(p)-(1-p)*Math.log2(1-p);
const pop=x=>{let k=0;while(x){k+=x&1;x>>=1;}return k;};
const matrices=ps.map(p=>Array.from({length:N},(_,x)=>Array.from({length:N},(_,y)=>p**pop(x^y)*(1-p)**(n-pop(x^y)))));
let count=0;
const rows=ps.map(p=>({p,benchmark:2*(1-h(p)),max:-Infinity,partition:null}));
function evaluate(a){
 count++;
 const sizes=[0,0,0,0];for(const v of a)sizes[v]++;
 const H=sizes.reduce((s,c)=>c?s-(c/N)*Math.log2(c/N):s,0);
 matrices.forEach((W,j)=>{
  let conditional=0;
  for(let y=0;y<N;y++){
   const probs=[0,0,0,0]; for(let x=0;x<N;x++)probs[a[x]]+=W[x][y];
   conditional+=probs.reduce((s,p)=>p>0?s-p*Math.log2(p):s,0)/N;
  }
  const I=H-conditional;
  if(I>rows[j].max){rows[j].max=I;rows[j].partition=[...a];}
 });
}
function visit(a,m){if(a.length===N)return evaluate(a);for(let v=0;v<=Math.min(m+1,3);v++)visit([...a,v],Math.max(m,v));}
visit([0],0);
for(const r of rows)r.excess=r.max-r.benchmark;
const out={scope:'n=3, all set partitions into at most 4 cells, finite p grid only',arithmetic:'IEEE-754 double, no interval certification',count,rows};
fs.writeFileSync(__dirname+'/two_bit_probe.json',JSON.stringify(out,null,2));
console.log(JSON.stringify(out,null,2));
