"""Complete geometry orbit preparation for the three-avoid bridge table.

Preserves already audited binary files. New records require independent checks.
"""
import itertools,json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
def main():
    even=[v for v in range(1,16) if v.bit_count()%2==0];odd=[v for v in range(16) if v.bit_count()%2]
    domain={(a,b,y) for a,b in itertools.combinations(even,2) for y in odd};rows=[]
    ps=list(itertools.permutations(range(4)))
    def tr(v,p):return sum(((v>>j)&1)<<p[j] for j in range(4))
    while domain:
        a,b,y=min(domain);orb=set()
        for p in ps:
            aa,bb=sorted((tr(a,p),tr(b,p)));orb.add((aa,bb,tr(y,p)))
        assert orb<=domain;domain-=orb;name=f'q4_three_avoided_{a}_{b}_{y}.bin';path=R/name
        if not path.exists():
            report=json.loads(subprocess.check_output([str(R/'q4_three_avoided_probe.exe'),str(a),str(b),str(y),str(path)],text=True))
        else:
            raw=path.read_bytes();assert len(raw)==10395*29
            negatives=sum(raw[i+16:i+29]==bytes([255])*13 for i in range(0,len(raw),29))
            report=dict(holes=[0,a,b,y],avoided=[a,b,y],positive=10395-negatives,negative=negatives,preserved_existing_file=True)
        report.update(orbit=sorted(orb),orbit_size=len(orb),file=name);rows.append(report)
        print(a,b,y,report['positive'],report['negative'],len(orb),flush=True)
    out=dict(scope='All168 marked Q4 geometries with sole retained free hole0, omitted2even+1odd',
        rows=rows,independent_review_pending=True,full_t15_proved=False)
    (R/'q4_three_avoided_all_generation.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
