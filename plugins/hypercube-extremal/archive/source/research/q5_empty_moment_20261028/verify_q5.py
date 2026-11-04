"""Independent exact verifier: six Gram blocks plus Q5 cubic-identity cuts.

No NumPy, SciPy, model.py or optimizer coefficient tables are imported.
The local C++ checker rebuilds geometry, group averaging and full Q4 coverage.
The non-PSD empty-root additions are justified here by an exact cubic identity.
"""
from fractions import Fraction
from itertools import product,combinations
from pathlib import Path
import json,subprocess,shutil,sys
P=Path(__file__).resolve().parent

def prepare(c,path,target):
    assert c['proof_type']=='Q5_EMPTY_CUBIC_PARTITION_IDENTITY_V1'
    D=c['gram_denominator'];assert isinstance(D,int) and D>0
    dims=[240,212,190,187,170,9]
    assert c['dimensions']==dims and len(c['gram_factors'])==6
    matrices=[]
    for n,L in zip(dims,c['gram_factors']):
        assert len(L)==n and len(set(map(len,L)))==1 and len(L[0])>0
        assert all(isinstance(z,int) for row in L for z in row)
        matrices.append([[sum(a*b for a,b in zip(L[i],L[j])) for j in range(n)] for i in range(n)])
    H=[[1 if i==j or (i-j)%5 not in (1,4) else -1 for j in range(5)] for i in range(5)]
    positive={abc for abc in combinations(range(5),3)
              if sum(H[a][b]==-1 for a,b in combinations(abc,2))==1}
    for a,b,d in product(range(5),repeat=3):
        left=H[a][b]+H[a][d]+H[b][d]
        right=H[a][b]*H[a][d]+H[b][a]*H[b][d]+H[d][a]*H[d][b]
        if tuple(sorted((a,b,d))) in positive:right+=2
        assert left==right
    cuts=c['q5_cuts'];assert isinstance(cuts,list)
    for cut in cuts:
        labels=cut['labels'];w=cut['weight_numerator']
        assert len(labels)==240 and all(isinstance(z,int) and 0<=z<5 for z in labels)
        assert isinstance(w,int) and w>=0
        for i in range(240):
            for j in range(240):matrices[0][i][j]+=w*H[labels[i]][labels[j]]
    ab=192*(D*D+sum(max(abs(z) for row in Q for z in row) for Q in matrices))
    assert ab<2**63
    den=192*D*D
    with path.open('w',encoding='ascii') as f:
        f.write(f'{D} {target} {den}\n')
        for Q in matrices:
            f.write(str(len(Q))+'\n')
            f.write('\n'.join(' '.join(map(str,row)) for row in Q)+'\n')
    print(f'PASS: six integer Gram blocks and {len(cuts)} nonnegative Q5 cubic-identity cuts.',flush=True)
    print('PASS: all 125 polarized identity cases and exact 64-bit safety bound.',flush=True)
    return matrices

if __name__=='__main__':
    c=json.loads((P/(sys.argv[1] if len(sys.argv)>1 else 'certificate.json')).read_text(encoding='utf-8'))
    bound=Fraction(c['upper_numerator'],c['upper_denominator'])
    assert bound<=Fraction(c['upper_decimal_ceil_8'])<bound+Fraction(1,10**8)
    target=bound*(192*c['gram_denominator']**2);assert target.denominator==1
    prepare(c,P/'verification_matrices.txt',target.numerator)
    compiler=shutil.which('g++') or shutil.which('clang++');assert compiler
    subprocess.run([compiler,'-O3','-std=c++17',str(P/'verify_local.cpp'),'-o',str(P/'verify_local')],check=True)
    subprocess.run([str(P/'verify_local'),'verification_matrices.txt'],cwd=P,check=True)
    print('CERTIFIED ASYMPTOTIC UPPER BOUND:',bound,flush=True)
    print('OUTWARD DECIMAL:',c['upper_decimal_ceil_8'],flush=True)
    print('Compressed Q5 moment cuts eliminated into Q4 coefficients; not a full Q5 enumeration.')
