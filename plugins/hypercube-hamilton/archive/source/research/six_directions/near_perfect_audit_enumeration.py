"""Reproduce the reviewer's exact all-perfect-matching enumeration.

The original code ran in the functions.exec V8 JavaScript runtime. Its source is
preserved verbatim in EXACT_EXECUTED_JS below. This Python launcher provides the
original `text` output helper and runs that source with Node.js. It requires
Python 3 and Node.js on PATH; neither third-party packages nor input data.

Usage: python near_perfect_audit_enumeration.py

The adjacent JSON records the existing original output, not a fresh run made
when saving this launcher. Cases n=3 and n=4 enumerate ALL perfect matchings of
B(Q_n), all even-odd nonpartner endpoint pairs, and every coordinate half-layer.
These finite tests do not prove the arbitrary-dimensional rigidity lemma.
"""

import json
import shutil
import subprocess


EXACT_EXECUTED_JS = r"""function pc(v){let c=0;for(;v;v&=v-1)c++;return c;}
for(const n of [3,4]){
 const N=1<<n, A=Array.from({length:N},(_,i)=>i).filter(v=>pc(v)%2===0), B=Array.from({length:N},(_,i)=>i).filter(v=>pc(v)%2), enc=(a,b)=>Math.min(a,b)*N+Math.max(a,b), halves=[];
 for(let i=0;i<n;i++)for(let eps=0;eps<2;eps++)halves.push([...new Set(Array.from({length:N},(_,v)=>v).filter(v=>pc(v&~(1<<i))%2===eps).map(v=>enc(v,v^(1<<i))))]);
 const counts={P:0,endpairs:0,obstructed:0},byLong={};const perm=B.slice();
 function rec(k){
  if(k<perm.length){for(let j=k;j<perm.length;j++){[perm[k],perm[j]]=[perm[j],perm[k]];rec(k+1);[perm[k],perm[j]]=[perm[j],perm[k]];}return;}
  counts.P++;const partner=new Map(),P=new Set(),dirs=new Set();let longs=0;
  for(let j=0;j<A.length;j++){let a=A[j],b=perm[j];partner.set(a,b);partner.set(b,a);P.add(enc(a,b));if(pc(a^b)===1)dirs.add(Math.log2(a^b));else longs++;}
  for(const x of A)for(const y of B){
   if(partner.get(x)===y)continue;counts.endpairs++;
   const a=partner.get(x),b=partner.get(y),e1=enc(x,a),e2=enc(y,b),add=enc(a,b);
   if(!halves.some(H=>H.every(e=>e===add||(e!==e1&&e!==e2&&P.has(e)))))continue;
   counts.obstructed++;byLong[longs]=(byLong[longs]||0)+1;if(dirs.size>3)throw new Error(JSON.stringify({n,perm,x,y,dirs:[...dirs]}));
  }
 }
 rec(0);text({general_rigidity:true,n,counts,obstructed_by_number_long_edges:byLong,failures:0});
}
"""


def main():
    node = shutil.which("node")
    if node is None:
        raise SystemExit("Node.js is required to execute the preserved original JavaScript.")
    source = "const text = value => console.log(JSON.stringify(value));\n" + EXACT_EXECUTED_JS
    result = subprocess.run([node, "-e", source], check=True, capture_output=True, text=True)
    outputs = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    print(json.dumps(outputs, indent=2))


if __name__ == "__main__":
    main()
