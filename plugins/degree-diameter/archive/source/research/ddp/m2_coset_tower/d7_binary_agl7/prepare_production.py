"""Preserve the exact O7-H-anchor scope; do not quotient remaining stabilizers."""
from pathlib import Path
from itertools import combinations
import json
import resource
import subprocess
HERE=Path(__file__).resolve().parent
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
source=json.loads((HERE/'STRUCTURE_CHECK.json').read_text())
st=json.loads((HERE/'profile_structure.json').read_text())
lists=json.loads((HERE/'profile_generator_lists.json').read_text())
A=st['K_action'];P=st['K_multiplication_table'];I=st['K_inverse'];H=st['H_K_codes']
def gp(g,h):return ((g%64)^A[g//64][h%64])+64*P[g//64][h//64]
def inv(g):return A[I[g//64]][g%64]+64*I[g//64]
scope=source['O7_anchor_H_conjugation']
anchors={}
for name,source_key,list_key in [('involutions','involution_orbits','involutions_by_colour'),('pairs','inverse_pair_orbits','inverse_pairs_by_colour')]:
    actual=[];covered=set();reps=[]
    for row in scope[source_key]:
        rep=tuple(row['representative_G_codes']);reps.append(rep)
        orbit={tuple(sorted(gp(gp(64*h,g),inv(64*h)) for g in rep)) for h in H}
        expected={tuple(z) for z in row['orbit_members_G_codes']}
        assert orbit==expected and len(orbit)==row['orbit_size'] and not (covered&orbit)
        covered|=orbit
    original=lists[list_key]['product1_7']
    wanted={tuple([g]) if isinstance(g,int) else tuple(g) for g in original}
    assert covered==wanted
    anchors[name]=reps
assert len(anchors['involutions'])==4 and len(anchors['pairs'])==26
names=['product1_7','axes14','product124_21','product356_21']
branches=[];global_anchors=[];total=0
with (HERE/'production.scope.txt').open('w') as f:
    f.write('6\n')
    for branch,ic in enumerate(combinations(names,2)):
        pc=[c for c in names if c not in ic];components=[]
        for c in ic:components.append(anchors['involutions'] if c=='product1_7' else [(g,) for g in lists['involutions_by_colour'][c]])
        for c in pc:components.append(anchors['pairs'] if c=='product1_7' else list(map(tuple,lists['inverse_pairs_by_colour'][c])))
        apos=0 if 'product1_7' in ic else 2
        count=1
        for z in components:count*=len(z)
        expected=scope['two_pair_two_involution_branches'][branch]
        assert list(ic)==expected['involution_colors'] and count==expected['choices_after_only_O7_H_orbit_anchor']
        f.write(str(apos)+'\n')
        for cc in components:
            f.write(str(len(cc))+'\n')
            for z in cc:f.write(str(z[0])+' '+str(z[1] if len(z)==2 else -1)+'\n')
        per=count//len(components[apos])
        for ai,ac in enumerate(components[apos]):
            global_anchors.append({'anchor_id':len(global_anchors),'branch':branch,'anchor_index':ai,'O7_component':ac,
                                   'cursor_start':total+ai*per,'cursor_end':total+(ai+1)*per,'raw_count':per})
        branches.append({'branch':branch,'involution_colours':ic,'pair_colours':pc,'anchor_component_position':apos,
                         'component_sizes':list(map(len,components)),'raw':count,'cursor_start':total,'cursor_end':total+count})
        total+=count
assert total==76384728 and len(global_anchors)==90
meta={'scope_total':total,'branches':branches,'anchors':global_anchors,
 'source':'STRUCTURE_CHECK.json: O7_anchor_H_conjugation',
 'all_4_involution_and_26_pair_anchor_orbits_match_member_by_member':True,
 'no_remaining_stabilizer_quotient':True,'no_division_by_six':True,
 'order':'branch, O7 anchor, then the three non-anchor component indices in original component-position order; each index ascending',
 'production_start_cursor':0,'random_profile_is_not_an_enumeration_prefix':True,
 'random_profile_cache_reused_in_production':False,
 'only_generator_composition':'two noninvolution inverse pairs and two nonidentity involutions',
 'other_generator_compositions':'not included',
 'filters':['four actual horizontal colours (HH)','exact nonnormal-H two-mask BB condition','actual three-root BFS for every BB survivor'],
 'stop_on_D5':True,'worker_count':1,'cumulative_CPU_limit_seconds':360}
(HERE/'production.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
# Reuse the already calibrated graph and output routines without changing the profile record.
engine=(HERE/'profile.cpp').read_text().split('int main(int argc,char**argv)')[0]
(HERE/'production_engine.hpp').write_text(engine)
before=cpu()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'production.cpp'),'-o',str(HERE/'production')],check=True)
compile_cpu=cpu()-before
# The optimized necessary filter is calibrated against the same 1200 saved inputs,
# without rebuilding any graph or running any further BFS.
subprocess.run([str(HERE/'production'),'calibrate','1',str(HERE)],check=True)
out={'status':'PRODUCTION_PREPARED','cpu_seconds':cpu()-start,'compile_cpu_seconds':compile_cpu,
 'scope_total':total,'anchor_count':90,'optimized_BB_saved_input_calibration':1200,'additional_BFS':0}
(HERE/'production.prepare.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
