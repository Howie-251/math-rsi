"""Sequential-unary at-most-three; no imports or execution side effects."""


def atmost_three(inputs,first_aux):
    n=len(inputs)
    assert n>=1 and len(set(inputs))==n and first_aux>max(inputs)
    def s(i,j):
        return first_aux+(i-1)*3+j-1
    clauses=[]
    for i,x in enumerate(inputs,1):
        clauses.append([-x,s(i,1)])
        for j in range(1,4):
            if j>i:
                clauses.append([-s(i,j)])
        if i>=2:
            for j in range(1,4):
                clauses.append([-s(i-1,j),s(i,j)])
            for j in (2,3):
                clauses.append([-x,-s(i-1,j-1),s(i,j)])
            clauses.append([-x,-s(i-1,3)])
    return clauses,dict(input_count=n,bound=3,first_aux=first_aux,
                        last_aux=first_aux+3*n-1,aux_count=3*n,
                        clause_count=len(clauses),
                        unary_index='s[i,j]=first_aux+3*(i-1)+(j-1), i=1..n,j=1..3')
