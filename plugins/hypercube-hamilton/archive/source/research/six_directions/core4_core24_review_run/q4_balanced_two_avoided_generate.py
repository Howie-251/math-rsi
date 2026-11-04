import itertools,json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
def main():
    perms=[p+(3,) for p in itertools.permutations(range(3))]
    def tr(v,p):return sum(((v>>j)&1)<<p[j] for j in range(4))
    domain={(r,y) for r in range(1,16) if r.bit_count()%2==0 for y in range(16) if y!=7 and y.bit_count()%2}
    rows=[]
    while domain:
        r,y=min(domain);orb={(tr(r,p),tr(y,p)) for p in perms};assert orb<=domain;domain-=orb
        file=R/f'q4_balanced_two_avoided_{r}_{y}.bin'
        result=json.loads(subprocess.check_output([str(R/'q4_balanced_two_avoided_probe.exe'),str(r),str(y),str(file)],text=True))
        result['orbit_size']=len(orb);result['orbit']=[list(t) for t in sorted(orb)];rows.append(result)
        print(result,flush=True)
    (R/'q4_balanced_two_avoided_generation.json').write_text(json.dumps(dict(scope='Complete marked Q4 geometry with retained free pair at distance3',rows=rows,independent_check_pending=True,full_t15_proved=False),indent=2)+'\n')
if __name__=='__main__':main()
