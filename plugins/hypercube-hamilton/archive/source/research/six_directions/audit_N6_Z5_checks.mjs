// Independent adversarial checks for N6 coordinate choice and Z5 path surgery.
// Run: node audit_N6_Z5_checks.mjs
import fs from 'node:fs';
const pop=x=>{let k=0;for(;x;x&=x-1)k++;return k;};
const ek=(a,b)=>a<b?`${a},${b}`:`${b},${a}`;
const edges=p=>p.slice(1).map((v,i)=>[p[i],v]);
const insist=(p,m)=>{if(!p)throw new Error(m);};
let seed=0x62a51;
const rng=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/2**32;};
const shuffle=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(rng()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;};
const coordinate=[];
for(let n=3;n<=10;n++){
  const odd=Array.from({length:1<<n},(_,i)=>i).filter(i=>pop(i)%2);
  let pairs=0,choices=0,minSafe=n;
  for(const s of odd.filter(s=>pop(s)>1))for(const y of odd){
    if(s===y)continue;
    const safe=Array.from({length:n},(_,i)=>i).filter(i=>!((s&y)&(1<<i)));
    insist(safe.length>=2,'fewer than two safe coordinates');minSafe=Math.min(minSafe,safe.length);pairs++;
    for(const l of safe){
      const x=s^(1<<l);insist(x!==0&&x!==s&&x!==y,'endpoint collision');choices++;
      for(let j=0;j<n;j++){
        const f=v=>pop(v&~(1<<j))%2;
        insist(!(f(0)===f(s)&&f(s)===f(x)&&f(x)===f(y)),'half-layer complement collision');
      }
    }
  }
  coordinate.push({n,pairs,choices,minSafe});
}

// Exact alternating-block DFS: all prescribed pairs, only short connectors.
function localPath(P,start,end){
  const mate=Array(32),id=Array(32);P.forEach(([a,b],i)=>{mate[a]=b;mate[b]=a;id[a]=id[b]=i;});
  const all=(1<<P.length)-1,tail=id[end],seen=new Set();
  function dfs(current,mask){
    if(mask===all)return current===end?[]:null;
    const key=mask*32+current;if(seen.has(key))return null;seen.add(key);
    for(let j=0;j<5;j++){
      const q=current^(1<<j),b=1<<id[q];if(mask&b)continue;
      if(id[q]===tail&&((mask|b)!==all||mate[q]!==end))continue;
      const rest=dfs(mate[q],mask|b);if(rest!==null)return[q,mate[q],...rest];
    }return null;
  }
  const rest=dfs(mate[start],1<<id[start]);return rest===null?null:[start,mate[start],...rest];
}

const nearPerfect=[];
for(const mask of [7,11,31]){
  const P=Array.from({length:32},(_,i)=>i).filter(i=>pop(i)%2===0).map(i=>[i,i^mask]);
  const mate=new Map(P.flatMap(([a,b])=>[[a,b],[b,a]]));
  const r=0,s=mask,L=P.filter(e=>!e.includes(r));
  insist(P.every(e=>pop(e[0]^e[1])>1),'expected zero short matching edges');
  for(let y=1;y<32;y++){
    if(pop(y)%2!==1||y===s)continue;
    const l=Array.from({length:5},(_,i)=>i).find(i=>!((s&y)&(1<<i))&&(s^(1<<i))!==mate.get(y));
    const x=s^(1<<l),k=localPath(P,x,y);insist(k!==null,'N6 local path failure');
    const pos=k.indexOf(r);insist(k[pos+1]===s,'N6 wrong auxiliary edge orientation');
    const out=[...k.slice(0,pos+1).reverse(),...k.slice(pos+1)];
    const le=new Set(L.map(e=>ek(...e))),oe=new Set(edges(out).map(e=>ek(...e)));
    insist(out.length===32&&new Set(out).size===32&&out[0]===r&&out.at(-1)===y,'N6 not Hamilton');
    insist([...le].every(e=>oe.has(e)),'N6 lost original edge');
    insist(edges(out).every(e=>le.has(ek(...e))||pop(e[0]^e[1])===1),'N6 leaked artificial long edge');
    nearPerfect.push({mask,r,s,y,l,x,inputMatching:L,intermediatePath:k,finalPath:out});
  }
}

const records=[];let trials=0;
for(let sample=0;sample<48;sample++){
  let accepted=false;
  for(let attempt=0;attempt<2000&&!accepted;attempt++){
    trials++;
    // Start with a true Gray path. Reorder even-length chunks joined only by
    // prescribed matching edges, producing original long edges when possible.
    let kb=Array.from({length:32},(_,i)=>32+(i^(i>>1)));
    const oddPositions=Array.from({length:15},(_,i)=>2*i+1).filter(i=>pop(kb[i]^kb[0])>1);
    const zp=oddPositions[Math.floor(rng()*oddPositions.length)];
    const blocks=[];for(let i=2;i<zp-1;i+=2)blocks.push(kb.slice(i,i+2));
    kb=[...kb.slice(0,2),...shuffle(blocks).flat(),...kb.slice(zp-1)];
    const t=kb[0],z=kb[zp],a=kb[31],c=t^32,w=a^32;
    insist(pop(t^z)>1&&pop(t^z)%2===1,'bad B holes');
    const LB=[];for(let i=1;i<zp;i+=2)LB.push([kb[i],kb[i+1]]);for(let i=zp+1;i<32;i+=2)LB.push([kb[i],kb[i+1]]);
    const D=shuffle(LB.filter(e=>!e.includes(a))).slice(0,sample%6);
    const ds=new Set(D.map(e=>ek(...e))),XB=D.flat(),XA=XB.map(x=>x^32);
    const us=Array.from({length:32},(_,i)=>i).filter(i=>pop(i)%2===0&&i!==c&&!XA.includes(i));
    if(!us.length)continue;const u=us[Math.floor(rng()*us.length)];
    const rem=Array.from({length:32},(_,i)=>i).filter(i=>i!==u&&i!==w&&!XA.includes(i));
    const ev=rem.filter(x=>pop(x)%2===0),od=shuffle(rem.filter(x=>pop(x)%2===1));
    const MA=ev.map((e,i)=>[e,od[i]]),am=new Map(MA.flatMap(([a,b])=>[[a,b],[b,a]]));
    const MB=LB.filter(e=>!ds.has(ek(...e))),C=XB.map(x=>[x,x^32]);
    const segments=[];let chunk=[kb[0]];
    for(let i=1;i<kb.length;i++){if(ds.has(ek(kb[i-1],kb[i]))){segments.push(chunk);chunk=[];}chunk.push(kb[i]);}segments.push(chunk);
    const trans=segments.map(p=>[p[0]^32,...p,p.at(-1)^32]);
    const R=trans.map(p=>[p[0],p.at(-1)]),cs=R.find(e=>e.includes(c)),s=cs.find(x=>x!==c),r=am.get(c);
    const P=[...MA.filter(e=>!e.includes(c)),...R.filter(e=>!e.includes(c)),[r,s],[c,u]];
    insist(P.length===16&&new Set(P.flat()).size===32,'P_A not perfect');
    const targetKind=['r','s','port','general'][Math.floor(sample/6)%4];
    let vs=targetKind==='r'?[r]:targetKind==='s'?[s]:targetKind==='port'?XA:Array.from({length:32},(_,i)=>i);
    vs=vs.filter(v=>v!==w&&v!==u&&pop(v)%2===1&&new Set(MA.flat().concat(XA)).has(v));
    const v=shuffle(vs).find(v=>new Set(MA.filter(e=>!e.includes(c)&&!e.includes(v)&&pop(e[0]^e[1])===1).map(e=>e[0]^e[1])).size>=2);
    if(v===undefined)continue;
    const ka=localPath(P,c,v);insist(ka!==null,'local endpoint theorem counterexample');
    insist(ka[1]===u,'first forced edge wrong');
    const findTrans=(q,h)=>{const p=trans.find(p=>ek(p[0],p.at(-1))===ek(q,h));return p[0]===q?p:p.slice().reverse();};
    const base=ka.slice(1),out=[base[0]];
    for(let i=1;i<base.length;i++){
      const q=base[i-1],h=base[i];let replacement;
      if(ek(q,h)===ek(r,s)){
        const p=[r,...findTrans(c,s)];replacement=q===r?p:p.slice().reverse();
      }else if(R.some(e=>ek(...e)===ek(q,h))){replacement=findTrans(q,h);}else replacement=[q,h];
      out.push(...replacement.slice(1));
    }
    const M=[...MA,...MB,...C],me=new Set(M.map(e=>ek(...e))),oe=new Set(edges(out).map(e=>ek(...e)));
    insist(out.length===64&&new Set(out).size===64&&out[0]===u&&out.at(-1)===v,'not Hamilton with endpoints');
    insist([...me].every(e=>oe.has(e)),'lost original matching edge');
    insist(edges(out).every(e=>me.has(ek(...e))||pop(e[0]^e[1])===1),'new long edge leaked');
    records.push({sample,seed,k:D.length,targetKind,u,v,r,s,c,longOriginal:M.filter(e=>pop(e[0]^e[1])>1).length,inputMatching:M,BPath:kb,APath:ka,finalPath:out});accepted=true;
  }
  // s=w whenever D is empty, so covered target v=s is impossible then.
  if(!accepted)records.push({sample,skipped:true,reason:'requested boundary not realized within 2000 attempts'});
}
const result={coordinate,nearPerfect:{verified:nearPerfect.length,records:nearPerfect},construction:{trials,verified:records.filter(r=>!r.skipped).length,skipped:records.filter(r=>r.skipped),records}};
fs.writeFileSync(new URL('audit_N6_Z5_checks.json',import.meta.url),JSON.stringify(result,null,2));
console.log(JSON.stringify({coordinate,nearPerfect:{verified:nearPerfect.length,allInputEdgesLong:true},construction:{trials,verified:result.construction.verified,skipped:result.construction.skipped,byTarget:records.filter(r=>!r.skipped).reduce((a,r)=>(a[r.targetKind]=(a[r.targetKind]??0)+1,a),{}),withOriginalLongEdges:records.filter(r=>!r.skipped&&r.longOriginal>0).length}},null,2));
