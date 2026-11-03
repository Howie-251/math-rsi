"""Deterministic target generator; no search/BFS, optional hit edge export."""
import argparse,json,pathlib
HERE=pathlib.Path(__file__).resolve().parent
PH=[38,3,58];Z=[824,625,1089]
def generators(actor,b,degree):
 out=[(z,t,j) for z,t,j in zip(Z,b,PH)]
 out += [((-pow(317,80-j,1361)*z)%1361,(-pow(actor,80-j,13)*t)%13,(-j)%80) for z,t,j in out[:3]]
 if degree==7:out.append((1109,0,40))
 return out
def main():
 p=argparse.ArgumentParser();p.add_argument('--hit',type=pathlib.Path,default=HERE/'HIT.json');p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args();h=json.loads(a.hit.read_text());actor=h['actor13'];gs=generators(actor,h['positive_small_normals'],h['degree'])
 with a.output.open('w') as out:
  out.write(f"1415440 {1415440*h['degree']//2}\n")
  for j in range(80):
   rz=pow(317,j,1361);rt=pow(actor,j,13)
   for z in range(1361):
    for t in range(13):
     u=13*(z+1361*j)+t
     for w,s,k in gs:
      v=13*((z+rz*w)%1361+1361*((j+k)%80))+(t+rt*s)%13
      if u<v:out.write(f'{u} {v}\n')
if __name__=='__main__':main()
