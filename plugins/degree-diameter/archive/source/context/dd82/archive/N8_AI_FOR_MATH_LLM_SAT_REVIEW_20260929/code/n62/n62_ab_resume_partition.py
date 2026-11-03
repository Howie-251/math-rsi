#!/usr/bin/env python3
"""Generate the canonical n=62 A+B resume tasks."""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path

SCHEMA="n62-ab-canonical-resume-partition-v1"
S_A=(10,16,34,41,48,55)
S_REPS=((10,16),(10,34),(34,41),(11,22),(11,35),(22,35),
        (11,12),(22,23),(35,36),(11,17),(22,28),(35,42))
S_ORDERED=frozenset(((10,34),(11,22),(11,35),(22,35)))
D_CASES={
 "D0_MATCH":{"a":(29,35,41,48,55),"reps":(10,11,30,42),"count":14},
 "D1_MATCH":{"a":(28,34,41,48,55),"reps":(10,11,16,29,35),"count":18},
 "D2_MATCH":{"a":(27,34,41,48,55),"reps":(10,11,21,28),"count":14}}

def read(path): return json.loads(Path(path).read_text(encoding="utf-8"))
def pair(u,v): return (u,v) if u<v else (v,u)

def triple_index(rows):
    out={}
    for u,v,var in rows:
        key=pair(int(u),int(v))
        if key in out: raise ValueError(f"duplicate map key {key}")
        out[key]=int(var)
    return out

def contexts(manifest):
    path=Path(manifest).resolve(); root=path.parent; out={}
    for case in read(path)["cases"]:
        case={**case,"cnf":str((root/case["cnf"]).resolve()),
              "map":str((root/case["map"]).resolve())}
        m=read(case["map"])
        out[case["template_id"]]={"case":case,"a":triple_index(m["edge_variables"]),
          "b1":triple_index(m["b1_variables"]),"b2":triple_index(m["b2_variables"]),
          "tau":{int(u):int(v) for u,v in m["tau_variables"]},
          "base":{int(v):int(x) for v,x,_ in m["unit_assignments"]}}
    return out

def templates(path): return {x["id"]:x for x in read(Path(path).resolve())["templates"]}

def classes(template):
    cs={int(k):tuple(map(int,v)) for k,v in template["singleton_classes"].items()}; owner={}
    for label,vertices in cs.items():
        for vertex in vertices:
            if vertex in owner: raise ValueError("duplicate singleton vertex")
            owner[vertex]=label
    return cs,owner

def put(assign,reasons,var,value,reason):
    if var in assign and assign[var]!=value: raise ValueError(f"variable conflict {var}")
    assign[var]=int(value); reasons.setdefault(var,reason)

def row(assign,reasons,index,vertex,trues,reason):
    mapped={v if u==vertex else u:var for (u,v),var in index.items() if vertex in (u,v)}
    if not set(trues)<=mapped.keys(): raise ValueError(f"missing {reason} variable")
    for neighbor,var in mapped.items(): put(assign,reasons,var,neighbor in trues,reason)

def occurrence_order(context):
    candidates=set(context["a"].values()); counts=Counter()
    with Path(context["case"]["cnf"]).open(encoding="ascii") as handle:
        for line in handle:
            if not line or line[0] in "cp": continue
            for token in line.split():
                lit=int(token)
                if lit and abs(lit) in candidates: counts[abs(lit)]+=1
    return sorted(candidates,key=lambda v:(-counts[v],v))

def finish(task_id,family,c,assign,reasons,semantic,order):
    for var,value in assign.items():
        if var in c["base"] and c["base"][var]!=value: raise ValueError(f"{task_id}: base conflict")
    lits=[v if assign[v] else -v for v in sorted(assign)]
    if len(lits)!=len({abs(v) for v in lits}): raise ValueError(f"{task_id}: literal conflict")
    case=c["case"]
    return {"task_id":task_id,"family":family,"base_instance":case["template_id"],
      "cnf":case["cnf"],"map":case["map"],
      "base_variables":case["variables"],"base_clauses":case["clauses"],
      "initial_literals":lits,"initial_literal_reasons":{str(v):reasons[v] for v in sorted(reasons)},
      "adaptive_split_variables":[v for v in order if v not in assign],"semantics":semantic}

def audit_s(template):
    cs,owner=classes(template)
    if {tuple(x) for x in template["H_edges"]}!={(1,2)}: raise ValueError("S H audit")
    if set(template["exceptional"][0]["parents"])!={3,4}: raise ValueError("S parent audit")
    group={1:"H",2:"H",3:"P9",4:"P9",5:"free",6:"free",7:"free",8:"free"}; sigs=[]
    for b,c in S_REPS:
        if (b in S_A)!=(c in S_A): raise ValueError("S A-status audit")
        gb,gc=group[owner[b]],group[owner[c]]
        sigs.append(("A" if b in S_A else "nonA",*sorted((gb,gc)),owner[b]==owner[c]))
    if len(set(sigs))!=12: raise ValueError("S orbit signature audit")
    ordered={r for r,s in zip(S_REPS,sigs) if s[1]!=s[2]}
    if ordered!=set(S_ORDERED): raise ValueError("S endpoint-swap audit")
    if tuple(sorted(map(len,cs.values())))!=(6,6,6,6,7,7,7,7): raise ValueError("S size audit")
    return {"representatives":[list(x) for x in S_REPS],"signature_count":12,
      "ordered_endpoint_representatives":[list(x) for x in sorted(S_ORDERED)],
      "swappable_endpoint_representatives":[list(x) for x in S_REPS if x not in S_ORDERED]}

def audit_d(template,a_row,reps):
    cs,owner=classes(template); exc={x["vertex"]:set(x["parents"]) for x in template["exceptional"]}
    def sig(v):
        if v==10: return ("exceptional10",)
        label=owner[v]; return ("singleton",int(label in exc[9]),int(label in exc[10]))
    universe=[10]+[v for vs in cs.values() for v in vs if v not in a_row]
    all_sigs={sig(v) for v in universe}; rep_sigs=[sig(v) for v in reps]
    if len(set(rep_sigs))!=len(reps) or set(rep_sigs)!=all_sigs: raise ValueError(f"{template['id']} orbit audit")
    return {"representatives":list(reps),"orbit_signature_count":len(all_sigs),
            "orbit_signatures":[list(x) for x in sorted(all_sigs,key=str)]}

def build_s(c,template):
    audit=audit_s(template); order=occurrence_order(c); tasks=[]
    for b,cend in S_REPS:
        taus=((0,0),(0,1),(1,0),(1,1)) if (b,cend) in S_ORDERED else ((0,0),(0,1),(1,1))
        for tb,tc in taus:
            for abc in (0,1):
                a={}; why={}; row(a,why,c["a"],9,set(S_A),"canonical_A_row_9")
                row(a,why,c["b1"],9,{b,cend},"canonical_B1_row_9")
                if any(9 in e for e in c["b2"]): raise ValueError("S has dynamic B2 row")
                put(a,why,c["a"][pair(b,cend)],abc,"split_A_between_B1_endpoints")
                put(a,why,c["tau"][b],tb,"split_tau_endpoint")
                put(a,why,c["tau"][cend],tc,"split_tau_endpoint")
                tid=f"S_DISJOINT__b{b:02d}_{cend:02d}__a{abc}__tau{tb}{tc}"
                tasks.append(finish(tid,"S_DISJOINT",c,a,why,{"canonical_A_neighbors_of_9":list(S_A),
                  "canonical_dynamic_B1_neighbors_of_9":[b,cend],"A_between_B1_endpoints":abc,
                  "tau_at_B1_endpoints":{str(b):tb,str(cend):tc},
                  "endpoint_state_rule":"ordered" if (b,cend) in S_ORDERED else "swappable_01_canonical"},order))
    if len(tasks)!=80: raise ValueError("S task count")
    return tasks,audit

def build_d(c,template,config):
    audit=audit_d(template,config["a"],config["reps"]); order=occurrence_order(c); tasks=[]
    for y in config["reps"]:
        states=[(None,t) for t in (0,1)] if y==10 else [(av,t) for av in (0,1) for t in (0,1)]
        for ay10,ty in states:
            a={}; why={}; row(a,why,c["a"],9,set(config["a"]),"canonical_A_row_9")
            row(a,why,c["b1"],9,{y},"canonical_B1_row_9")
            row(a,why,c["b2"],9,set(),"canonical_B2_row_9")
            if ay10 is not None: put(a,why,c["a"][pair(y,10)],ay10,"split_A_y_10")
            put(a,why,c["tau"][y],ty,"split_tau_y")
            middle=f"a{ay10}__" if ay10 is not None else ""
            tid=f"{c['case']['template_id']}__y{y:02d}__{middle}tau{ty}"
            tasks.append(finish(tid,c["case"]["template_id"],c,a,why,
              {"canonical_A_neighbors_of_9":list(config["a"]),"canonical_dynamic_B1_neighbors_of_9":[y],
               "canonical_dynamic_B2_neighbors_of_9":[],"A_y_10":ay10,"tau_y":ty},order))
    if len(tasks)!=config["count"]: raise ValueError("D task count")
    return tasks,audit

def main():
    p=argparse.ArgumentParser(); p.add_argument("--instances-manifest",required=True,type=Path)
    p.add_argument("--templates",required=True,type=Path); p.add_argument("--output",required=True,type=Path)
    p.add_argument("--scope",choices=("s_disjoint","all"),default="s_disjoint"); args=p.parse_args()
    cs=contexts(args.instances_manifest); ts=templates(args.templates); tasks,audit_s_result=build_s(cs["S_DISJOINT"],ts["S_DISJOINT"])
    audits={"S_DISJOINT":audit_s_result}
    if args.scope=="all":
        for name,config in D_CASES.items():
            more,audit=build_d(cs[name],ts[name],config); tasks+=more; audits[name]=audit
    expected=80 if args.scope=="s_disjoint" else 126
    keys=[(x["base_instance"],tuple(x["initial_literals"])) for x in tasks]
    if len(tasks)!=expected or len({x["task_id"] for x in tasks})!=expected or len(set(keys))!=expected:
        raise ValueError("global count/uniqueness audit")
    counts=Counter(x["family"] for x in tasks)
    doc={"schema":SCHEMA,"scope":args.scope,"source_instances_manifest":str(args.instances_manifest.resolve()),
      "source_template_manifest":str(args.templates.resolve()),"task_count":len(tasks),"family_counts":dict(sorted(counts.items())),
      "partition_semantics":"exhaustive canonical orbit representatives; one solver run per task; no portfolio duplication",
      "orbit_audit":audits,"audits":{"expected_task_count":expected,"actual_task_count":len(tasks),
      "unique_task_ids":True,"unique_base_literal_sets":True,"no_variable_or_base_unit_conflicts":True},"tasks":tasks}
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(doc,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"output":str(args.output),"tasks":len(tasks),"family_counts":dict(counts)},sort_keys=True))

if __name__=="__main__": main()
