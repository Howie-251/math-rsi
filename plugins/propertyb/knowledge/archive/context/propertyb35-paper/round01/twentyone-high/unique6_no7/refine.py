"""Exact repaired all-avoided-quota joint refinements for bounded actual unit8-star domains."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time,argparse
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math'),str(BASE/'two_low_high_star')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from unpaired_three import serial

def main():
 parser=argparse.ArgumentParser();parser.add_argument('tag');parser.add_argument('s',type=int);args=parser.parse_args();st=time.time();src=json.loads((HERE/f'{args.tag}_DP.json').read_text())['cases'];eng=Engine(21,args.s);out=[]
 for r in src:
  if r['strict']:continue
  z=solve_profile(eng,dict(r,counts={m:n for m,n in r['counts'].items() if n},graph=args.tag,group=r['id']),permutation_limit=120);z['source_id']=r['id'];out.append(z)
 print(args.tag,'joint',len(out),'strict',sum(Q(z.get('bound','2'))<1 for z in out),'seconds',time.time()-st,flush=True)
 (HERE/f'{args.tag}_JOINT.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,results=out,elapsed_seconds=time.time()-st)),indent=2)+'\n')
if __name__=='__main__':main()
