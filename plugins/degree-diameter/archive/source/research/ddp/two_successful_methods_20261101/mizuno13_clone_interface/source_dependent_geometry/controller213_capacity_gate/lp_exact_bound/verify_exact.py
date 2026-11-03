"""Pure-integer check of the saved LP dual combination; no solver imports."""
from pathlib import Path
from fractions import Fraction
import json,time
D=Path(__file__).resolve().parent;T=time.process_time()
I=json.loads((D/'LP_INPUT.json').read_text());C=json.loads((D/'SIMPLIFIED_DUAL_CERTIFICATE.json').read_text())
Q=C['common_denominator'];Y=C['controller_and_cost_row_numerators'];Z=C['upper_bound_row_numerators'];A=I['rows'];B=I['rhs']
assert Q>0 and len(A)==len(B)==len(Y)==365 and len(Z)==364
assert all(isinstance(v,int) and v>=0 for v in Y+Z)
columns=[sum(A[b][a]*Y[b] for b in range(365))+Z[a] for a in range(364)]
rhs=sum(b*y for b,y in zip(B,Y))+sum(Z)
assert columns==C['column_coefficient_numerators'] and min(columns)>=Q
assert rhs==C['RHS_numerator'] and rhs<207*Q
assert Fraction(rhs,Q)==Fraction(C['exact_upper_bound'])
out={'status':'PASS_EXACT_INTEGER_ARITHMETIC','solver_imports':0,'solver_calls':0,'nonnegative_multipliers':True,'checked_columns':364,'min_column_coefficient_numerator':min(columns),'common_denominator':Q,'RHS_numerator':rhs,'exact_upper_bound':str(Fraction(rhs,Q)),'strictly_less_than207':True,'integer_block_upper':206,'CPU_seconds':time.process_time()-T}
(D/'EXACT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
