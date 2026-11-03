"""One symbolic root image and a route budget; no source graph or matching search."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,time
OUT=Path(__file__).resolve().parent
def main():
    start=time.process_time();q=7;images=set();multiplicities=Counter();cases=[]
    for u in range(q):
        for v in range(q):
            for d in range(q):
                e=(v*(d-u))%q;f=e*(v+d+u)%q;t=(d,e,f)
                images.add(t);multiplicities[t]+=1;cases.append({"u":u,"v":v,"d":d,"target":list(t)})
    by_d=Counter(x[0] for x in images);hist=Counter(multiplicities.values())
    limit=len(images)+50+48+43+7
    result={"timestamp_UTC":datetime.now(timezone.utc).isoformat(),"status":"STRICT_ALL_SINGLE_MATCHING_EXCLUSION" if limit<343 else "PREDICTED_BUDGET_NOT_STRICT", "field":7,"target_n":343,"root":[0,0,0],"formal_triples":len(cases),"formal_threewalk_image_size":len(images),"formal_image_by_target_first_coordinate":dict(sorted(by_d.items())),"endpoint_multiplicity_histogram":dict(sorted(hist.items())),"zero_M_upper":len(images),"one_M_first_upper":50,"one_M_middle_upper":48,"one_M_last_upper":43,"two_M_upper":7,"augmented_R3_upper":limit,"uniform_missing_from_root_lower_bound":max(0,343-limit),"count_type":"symbolic upperbound for all arbitrary matchings, not measured graph badpairs", "prediction_threshold_supported":len(images)<=194,"actual_source_graph_generated":False,"augmented_graph_generated":False,"actual_D":None,"actual_n":None,"ordinary_bad_unordered_pairs":None,"SAT_calls":0,"BFS":0,"matching_assignments_tested":0,"symbolic_body_CPU_seconds":time.process_time()-start}
    (OUT/"FORMAL_ENDPOINT_IMAGE.json").write_text(json.dumps({"field":q,"formula":["d","v*(d-u)","v*(d-u)*(v+d+u)"],"targets":[list(x) for x in sorted(images)],"formal_triple_cases":cases},indent=2)+"\n")
    (OUT/"RESULT.json").write_text(json.dumps(result,indent=2)+"\n");print(json.dumps(result))
if __name__=="__main__":main()
