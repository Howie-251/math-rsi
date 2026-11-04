"""Producer geometry/reduction evidence only; no A10 extension claim."""
from pathlib import Path
from itertools import permutations
import hashlib,json,math
R=Path(__file__).resolve().parent
V=set(range(32));H={0,1,2,4,8,15,23,27,29,30};covered=V-H
major={x for x in H if x.bit_count()%2==0};minor=H-major
N={x:{x^(1<<d) for d in range(5)} for x in V}
assert len(major)==6 and len(minor)==4
assert not any(N[z]&minor for z in major-{0})
assert N[31]<=major and N[31]=={15,23,27,29,30}
rows=[]
for d in range(5):
 bit=1<<d;A={x for x in V if not x&bit};B=V-A
 sources=minor&A;Y={x^bit for x in sources}
 assert Y<=covered&B
 assert len(major&A)==2
 assert len(major&A)-len((minor&A)-sources)==2
 if d<4:
  singleton=next(iter(minor&B));available=(N[singleton]&B)-Y
  assert len(available)==1 and singleton in H
  reason='included original hole has only one available short neighbor'
  blocker=singleton
 else:
  blocker=16;available=(N[blocker]&B)-Y
  assert blocker in covered and not available
  reason='covered vertex has no available new short neighbor beyond its one required edge'
 rows.append({'bit':bit,'A_majority_holes':sorted(major&A),'A_minority_holes':sorted(minor&A),
              'all_minority_bridge_mirrors':sorted(Y),'B_original_holes':sorted(H&B),
              'blocked_vertex':blocker,'available_B_short_neighbors':sorted(available),'obstruction':reason})
maps=[];images=set()
for p in permutations(range(5)):
 image=lambda x:sum(1<<p[d] for d in range(5) if x&(1<<d))
 images.add(tuple(sorted(image(x) for x in H)))
 if {image(x) for x in H}==H:maps.append([image(x) for x in range(32)])
assert len(images)==5 and len(maps)==24
partner_orbits=[];remaining=covered-{31}
while remaining:
 h=min(remaining);orb={tr[h] for tr in maps}
 assert orb<=remaining;remaining-=orb
 partner_orbits.append({'representative':h,'partners':sorted(orb),'orbit_size':len(orb),
                         'stabilizer_order':24//len(orb)})
assert sorted(g['orbit_size'] for g in partner_orbits)==[1,4,4,6,6]
total=math.prod(range(1,22,2));fixed=math.prod(range(1,20,2))
assert total==13749310575 and fixed==654729075
def fixed_matching_count(tr,support):
 remaining=set(support);cycles={}
 while remaining:
  x=min(remaining);cycle=[];y=x
  while y not in cycle:cycle.append(y);y=tr[y]
  assert y==x and set(cycle)<=remaining
  remaining-=set(cycle);cycles[len(cycle)]=cycles.get(len(cycle),0)+1
 value=1
 for length,m in cycles.items():
  if length%2:
   if m%2:return 0
   value*=math.factorial(m)//(2**(m//2)*math.factorial(m//2))*length**(m//2)
  else:
   value*=sum(math.factorial(m)//(math.factorial(m-2*p)*2**p*math.factorial(p))*length**p for p in range(m//2+1))
 return value
burnside=sum(fixed_matching_count(tr,covered) for tr in maps)
assert burnside%24==0
for g in partner_orbits:
 h=g['representative'];stab=[tr for tr in maps if tr[h]==h]
 numerator=sum(fixed_matching_count(tr,covered-{31,h}) for tr in stab)
 assert numerator%len(stab)==0
 g['matching_orbits_under_partner_stabilizer']=numerator//len(stab)
assert sum(g['matching_orbits_under_partner_stabilizer'] for g in partner_orbits)==burnside//24
out={'status':'GEOMETRY_PASS_NO_CLOSURE','H':sorted(H),'covered':sorted(covered),
     'covered_even_vertices':sorted(covered&{x for x in V if x.bit_count()%2==0}),
     'covered_odd_vertices':sorted(x for x in covered if x.bit_count()%2),
     'direct_coordinate_bridge_obstructions':rows,'marked_hole_orbit_size':len(images),
     'marked_stabilizer_order':len(maps),'partner31_orbits':partner_orbits,
     'arbitrary_matching_count':total,'matchings_per_fixed_partner':fixed,
     'exact_arbitrary_matching_orbits_under_marked_stabilizer':burnside//24,
     'normalized_fixed_partner_families':len(partner_orbits),'matching_instances_enumerated':0,
     'full_A10_orbit3_proved':False,'full_A10_proved':False,'full_P6_proved':False,
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'A10_ORBIT3_geometry_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
