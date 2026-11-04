// Independent finite adversarial check for the two adjacent-hole branches of N9.
// This tests compression obligations, not a theorem or all matchings of Q_5.
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';
const n = 5, size = 1 << n;
const parity = v => { let p=0; for (;v;v>>=1) p^=v&1; return p; };
const chi = (v,j) => parity(v & ~(1<<j));
const halfEdges = (j,e) => Array.from({length:size},(_,v)=>v)
  .filter(v => !(v&(1<<j)) && chi(v,j)===e).map(v=>[v,v^(1<<j)]);
const halves = Array.from({length:n},(_,j)=>[0,1].map(e=>({j,e,edges:halfEdges(j,e)}))).flat();
const contains = (P,H) => H.edges.every(([u,v])=>P[u]===v);
const compress = (P,x,y) => {
  assert.notEqual(x,y); assert.notEqual(P[x],y);
  const a=P[x],b=P[y],R=P.slice();
  R[x]=R[y]=-1; R[a]=b; R[b]=a;
  for(let u=0;u<size;u++) if(R[u]>=0) { assert.equal(R[R[u]],u); assert.notEqual(R[u],u); }
  return R;
};
function* permutations(a,pos=0) {
  if(pos===a.length) { yield a; return; }
  for(let i=pos;i<a.length;i++) {
    [a[i],a[pos]]=[a[pos],a[i]]; yield* permutations(a,pos+1);
    [a[i],a[pos]]=[a[pos],a[i]];
  }
}
const put=(P,u,v)=>{assert.equal(P[u],-1);assert.equal(P[v],-1);P[u]=v;P[v]=u;};
const result={dimension:n,root:0,hole:1,case1:{matchings:0,targets:0,choices:0},case2:{matchings:0,targets:0,choices:0},failures:0,
  scope:'Two symmetry-normalized obstruction families; independent exact enumeration, not a proof and not all Q5 matchings.'};
function check(P,y,j,eps,branch) {
  const r=0,s=1,k=0,p=P[y],H=halves.find(h=>h.j===j&&h.e===eps);
  assert.equal(parity(y),1); assert.notEqual(y,s);
  assert(contains(compress(P,r,y),H));
  assert.equal(H.edges.some(([a,b])=>(a===s&&b===p)||(b===s&&a===p)),branch===2);
  const jCount=Array.from({length:size},(_,v)=>v).filter(v=>v<P[v]&&(v^P[v])===(1<<j)).length;
  assert(jCount>=7);
  for(let l=0;l<n;l++) if(l!==j&&(branch===1||l!==k)) {
    const x=s^(1<<l); assert.notEqual(x,r); assert.notEqual(x,p); assert.notEqual(x,y);
    assert.equal(parity(x),parity(r));
    const R=compress(P,x,y); assert(halves.every(h=>!contains(R,h)));
    assert.equal(R[r],s); assert.equal(R[s],r);
    result[`case${branch}`].choices++;
  }
  result[`case${branch}`].targets++;
}
// Case 1: H is the j=k=0 half with chi_0=1; P already contains H and rs.
{
  const P=Array(size).fill(-1); for(const [a,b] of halfEdges(0,1)) put(P,a,b); put(P,0,1);
  const evens=[],odds=[]; for(let v=0;v<size;v++) if(P[v]<0) (parity(v)?odds:evens).push(v);
  for(const perm of permutations(odds)) {
    const Q=P.slice(); evens.forEach((v,i)=>put(Q,v,perm[i])); result.case1.matchings++;
    for(const y of odds) check(Q,y,0,1,1);
  }
}
// Case 2: k=0,j=1,s=1,p=3; H minus sp is forced in P, y runs through all legal T vertices.
{
  const s=1,p=3,j=1,eps=1;
  const targets=Array.from({length:size},(_,v)=>v).filter(v=>parity(v)===1&&chi(v,j)===0);
  for(const y of targets) {
    const P=Array(size).fill(-1); for(const [a,b] of halfEdges(j,eps)) if(a!==s&&b!==s) put(P,a,b);
    put(P,0,s); put(P,y,p);
    const evens=[],odds=[]; for(let v=0;v<size;v++) if(P[v]<0) (parity(v)?odds:evens).push(v);
    for(const perm of permutations(odds)) {
      const Q=P.slice(); evens.forEach((v,i)=>put(Q,v,perm[i])); result.case2.matchings++;
      check(Q,y,j,eps,2);
    }
  }
}
writeFileSync(new URL('./audit_N9_half_obligations.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
