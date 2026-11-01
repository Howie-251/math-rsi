"""M35/v23 actual six-degree unit-star: mixed double and triple necessary domains."""
from pathlib import Path
import sys,time,json,itertools
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import *
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
def main():
 st=time.time();out=[]
 for b in range(6,31):
  ns=double(23,6,b,1);z=best(23,ns,True)
  out.append(dict(degrees=[6,b],codegree=1,**z));print('pair',b,z['bound'],z['positions'],flush=True)
 (HERE/'PAIR_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-st,profiles=out)),indent=2)+'\n')
if __name__=='__main__':main()
