#!/usr/bin/env python3
"""One fixed16-source static fluid-routing pilot; never a sourceD3 verifier."""
import json,math,pathlib,time
D=pathlib.Path(__file__).resolve().parent
PROJECT=D.parents[4]
START=time.process_time()
SOURCES=[(17+233*i)%3750 for i in range(16)]
def save(name,x):(D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

def read_graph(path):
    with path.open() as f:
        n,m=map(int,f.readline().split());edges=[tuple(map(int,line.split())) for line in f if line.strip()]
    assert len(edges)==m
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(edges):adj[u].append((v,2*i));adj[v].append((u,2*i+1))
    return n,m,edges,adj

def bfs(adj,s):
    d=[-1]*len(adj);sigma=[0]*len(adj);order=[s];d[s]=0;sigma[s]=1
    for v in order:
        for w,_ in adj[v]:
            if d[w]<0:d[w]=d[v]+1;order.append(w)
            if d[w]==d[v]+1:sigma[w]+=sigma[v]
    return d,sigma,order

def model(name,path,baseline):
    start=time.process_time();n,m,edges,adj=read_graph(path);loads=[0.0]*(2*m)
    hopvolume=0.0;using_new=0.0;demands=[];base_out={}
    for s in SOURCES:
        assert time.process_time()-START<9
        d,sigma,order=bfs(adj,s)
        mass=[0.0]*n
        for t in SOURCES:
            if t==s:continue
            assert d[t]>=0 and sigma[t]>0
            mass[t]=1.0/15;hopvolume+=d[t]/15
            base_out[s,t]=(d[t],sigma[t])
            if baseline is None:pnew=0.0
            else:
                old_d,old_sigma=baseline[s,t]
                assert d[t]==old_d and sigma[t]>=old_sigma
                pnew=1.0-old_sigma/sigma[t]
            using_new+=pnew/15
            demands.append({'source':s,'target':t,'hops':d[t],'shortest_paths':sigma[t],
                            'probability_path_uses_new_edge':pnew})
        for v in reversed(order):
            if v==s or not mass[v]:continue
            for u,reverse_index in adj[v]:
                if d[u]==d[v]-1:
                    flow=mass[v]*sigma[u]/sigma[v]
                    loads[reverse_index^1]+=flow;mass[u]+=flow
        assert abs(mass[s]-1.0)<1e-10
    total_volume=sum(loads);assert abs(total_volume-hopvolume)<1e-8
    newvolume=sum(loads[2*i]+loads[2*i+1] for i,(u,v) in enumerate(edges) if u>=3750 or v>=3750)
    # For old-old demands of length<=3, a new-vertex route has exactly two new edges.
    assert abs(newvolume-2*using_new)<1e-8
    peak_i=max(range(2*m),key=lambda i:loads[i]);edge=edges[peak_i//2]
    directed=[edge[0],edge[1]] if peak_i%2==0 else [edge[1],edge[0]]
    meansquare=sum(x*x for x in loads)/(2*m)
    slots={str(r):{'physical_ports_total':r*n,'network_endpoints_used':2*m,'remaining_endpoint_slots':r*n-2*m}
           for r in [24,32,48]}
    result={'name':name,'graph_file':str(path.relative_to(PROJECT)),
            'n':n,'m':m,'physical_port_counts':slots,
            'device_increment_vs_source':n-3750,'network_edge_increment_vs_source':m-37500,
            'device_increment_fraction_vs_source':(n-3750)/3750,
            'network_edge_increment_fraction_vs_source':(m-37500)/37500,
            'routing_BFS_sources':16,'diameter_validation_performed':False,
            'ordered_demands':len(demands),'total_offered_traffic':16,
            'directed_link_capacity':1,'maximum_directed_load':loads[peak_i],
            'maximum_directed_load_over_capacity':loads[peak_i],
            'one_maximum_load_directed_link':directed,
            'mean_squared_directed_load_including_zero_arcs':meansquare,
            'root_mean_square_directed_load_including_zero_arcs':math.sqrt(meansquare),
            'average_hops':hopvolume/16,'total_directed_hop_volume':total_volume,
            'traffic_fraction_path_uses_any_new_edge':using_new/16,
            'new_edge_hop_volume':newvolume,'new_edge_fraction_of_hop_volume':newvolume/total_volume,
            'demand_details':demands,'CPU_seconds':time.process_time()-start}
    return result,base_out

def main():
    if (D/'RESULT.json').exists():raise SystemExit('fixed pilot already complete')
    source=PROJECT/'research/ddp/refresh_20261029/f5_full_d20_D3/graph_d20_D3_n3750.edges'
    items=[('source3750',source),('cap21_n3900',D.parent/'graph_d21_D3_n3900.edges'),
           ('cap22_n4125',D.parent/'graph_d22_D3_n4125.edges')]
    results=[];baseline=None
    for name,path in items:
        result,b= model(name,path,baseline);results.append(result)
        if baseline is None:baseline=b
    base=results[0]
    for r in results:
        for physical in [24,32,48]:
            z=r['physical_port_counts'][str(physical)]
            z['slot_increment_vs_source']=z['remaining_endpoint_slots']-base['physical_port_counts'][str(physical)]['remaining_endpoint_slots']
        r['maximum_directed_load_change_fraction_vs_source']=r['maximum_directed_load']/base['maximum_directed_load']-1
    elapsed=time.process_time()-START;assert elapsed<10
    out={'status':'FIXED_WORKLOAD_STATIC_ENGINEERING_PILOT_COMPLETE','source_labels':SOURCES,
         'per_ordered_demand_offered_traffic':'1/15','graphs':results,'whole_CPU_seconds':elapsed,
         'CPU_budget_seconds':10,'workers':1,'routing_BFS_total':48,'source_D3_reverification':False,
         'mean_hops_unchanged_prediction':all(abs(r['average_hops']-base['average_hops'])<1e-12 for r in results),
         'peak_nonincrease_prediction':all(r['maximum_directed_load']<=base['maximum_directed_load']+1e-12 for r in results),
         'new_edges_positive_usage_prediction':all(r['traffic_fraction_path_uses_any_new_edge']>0 for r in results[1:]),
         'faults_tested':False,'wiring_tested':False,'measured_throughput_claimed':False,'followup_started':False}
    save('RESULT.json',out);save('TERMINAL.json',{'running':False,'status':'COMPLETE','CPU_seconds':elapsed,'routing_BFS_total':48,'no_further_pilot':True})
    print(json.dumps({**{k:v for k,v in out.items() if k!='graphs'},'graphs':[{k:v for k,v in r.items() if k!='demand_details'} for r in results]}))
if __name__=='__main__':main()
