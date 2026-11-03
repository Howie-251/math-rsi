"""First q5 root/partner endpoint test, with no matching search or graph BFS."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,time
OUT=Path(__file__).resolve().parent
def ball2(x,q):
    a,b,c=x;ans={x}
    for u in range(q):
        ans.add((u,(a*u-b)%q,(a*a*u+a*u*u-c)%q))
        for d in range(q):
            ans.add((d,(b+u*(d-a))%q,(c+(d-a)*(u*u+(a+d)*u))%q))
    return ans
def main():
    started=time.process_time();q=5;root=(0,0,0)
    A=set()
    for u in range(q):
        for v in range(q):
            for d in range(q):
                e=v*(d-u)%q;A.add((d,e,e*(v+d+u)%q))
    forbidden={(u,0,0) for u in range(q)};rows=[];allhist=Counter();allowedhist=Counter()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                x=(a,b,c);B=ball2(x,q);outside=B-A;inter=B&A;allowed=x not in forbidden
                row={"partner":list(x),"eligible_complement_partner":allowed,"B2_size":len(B),"B2_outside_A_size":len(outside),"B2_intersect_A_size":len(inter)};rows.append(row);allhist[len(outside)]+=1
                if allowed:allowedhist[len(outside)]+=1
    eligible=[x for x in rows if x["eligible_complement_partner"]];mx=max(x["B2_outside_A_size"] for x in eligible)
    bound=len(A)+mx+45;unmatched=len(A)+len(ball2(root,q))+4*5
    result={"timestamp_UTC":datetime.now(timezone.utc).isoformat(),"status":"STRICT_ALL_MATCHING_OVERLAP_EXCLUSION" if bound<125 else "OVERLAP_PREDICTION_REFUTED_BOUND_NOT_STRICT","q":q,"n_derived":125,"target_Delta":6,"target_D":3,"saved_public_lower_bound":120,"formal_root_B3_exact_size":len(A),"root_B2_exact_size":len(ball2(root,q)),"potential_partners_total":len(rows),"eligible_complement_partners":len(eligible),"B2_outside_A_max_over_eligible":mx,"max_witness_partners":[x["partner"] for x in eligible if x["B2_outside_A_size"]==mx],"eligible_outside_histogram":dict(sorted(allowedhist.items())),"all_outside_histogram":dict(sorted(allhist.items())),"matched_root_R3_upper":bound,"unmatched_root_R3_upper":unmatched,"uniform_missing_from_root_lower_bound":max(0,125-max(bound,unmatched)),"prediction_max_outside_le24_supported":mx<=24,"actual_source_graph_generated":False,"augmented_graph_generated":False,"actual_n":None,"actual_D":None,"ordinary_bad_unordered_pairs":None,"matching_assignments_tested":0,"BFS":0,"solver_calls":0,"symbolic_CPU_seconds":time.process_time()-started}
    (OUT/"PARTNER_BALL_MARGINALS.json").write_text(json.dumps({"root":list(root),"root_B3_targets":[list(x) for x in sorted(A)],"rows":rows},indent=2)+"\n")
    (OUT/"RESULT.json").write_text(json.dumps(result,indent=2)+"\n");print(json.dumps(result))
if __name__=="__main__":main()
