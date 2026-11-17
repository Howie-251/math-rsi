from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path
from hashlib import sha256
from time import process_time
from functools import lru_cache
import json
import re

START = process_time()
AXES = tuple(range(6))
PERMS = tuple(permutations(AXES))
EVEN = tuple(v for v in range(64) if v.bit_count() % 2 == 0)
ODD = tuple(v for v in range(64) if v.bit_count() % 2 == 1)
BASE = "R7_CENTRAL_NO_D35_MU2_"
FULL = "R7_E16_MU2_FULL_CLOSURE_"
BINDINGS = {}


def budget():
    assert process_time() - START < 30


def raw(path):
    data = Path(path).read_bytes()
    BINDINGS[path] = sha256(data).hexdigest()
    return data


def read(path):
    return json.loads(raw(path))


def permute(v, perm):
    return sum(((v >> i) & 1) << j for i, j in enumerate(perm))


def image(values, p, x):
    assert sorted(p) == list(range(len(p))) and 0 <= x < 1 << len(p)
    return tuple(sorted(permute(v, p) ^ x for v in values))


def bit(v, i):
    return (v >> i) & 1


def loads(points):
    return tuple(sum(bit(v, i) for v in points) for i in AXES)


def physical(s, t, y, u):
    return tuple(sorted((*s, *(v ^ 64 for v in y)))), tuple(sorted((*t, *(v ^ 64 for v in u))))


def aff(record, prefix):
    return tuple(record[prefix + "_permutation"]), record[prefix + "_xor"]


@lru_cache(maxsize=None)
def disjoint_supports(k, count):
    def visit(left, available, lower):
        if left == 0:
            yield ()
        elif available.bit_count() >= left:
            for support in range(lower, 1 << k):
                if support & available == support:
                    for tail in visit(left - 1, available ^ support, support + 1):
                        yield (support, *tail)
    return tuple(visit(count, (1 << k) - 1, 1))


def sparse_sets(axes, exceptional):
    fibers = defaultdict(list)
    for v in ODD:
        support = sum((bit(v, i) == b) << n for n, (i, b) in enumerate(zip(axes, exceptional)))
        fibers[support].append(v)
    for zero_count in range(min(5, len(fibers[0])) + 1):
        for shapes in disjoint_supports(len(axes), 5 - zero_count):
            for zeros, tail in product(combinations(fibers[0], zero_count),
                                       product(*(fibers[support] for support in shapes))):
                yield tuple(sorted((*zeros, *tail)))


@lru_cache(maxsize=None)
def stabilizer(s):
    assert 0 in s
    return tuple((p, x) for p in PERMS for x in s if image(s, p, x) == s)


@lru_cache(maxsize=None)
def canonical(points):
    # Use all anchored ordered difference rows, preserving repeated columns.
    return min(tuple(sorted(sum(bit(v ^ anchor, i) << r for r, v in enumerate(tail))
                            for i in AXES))
               for anchor, *tail in permutations(points))


def canonical_points(key):
    return tuple(sorted((0, *(sum(bit(c, r) << i for i, c in enumerate(key)) for r in range(4)))))


def independent(colors):
    return all((v ^ w).bit_count() != 1 for v in colors[0] for w in colors[1])


def gaps(colors):
    return tuple(sum(bit(v, i) for v in colors[0]) - sum(bit(v, i) for v in colors[1]) for i in range(7))


def has_d35(colors):
    for j, b in product(range(7), (0, 1)):
        side = sorted((tuple(v for v in g if bit(v, j) == b) for g in colors), key=len)
        if list(map(len, side)) != [3, 5]:
            continue
        s, t = side
        for i, c in product(range(7), (0, 1)):
            if i != j and sum(bit(v, i) == c for v in s) == 2 and all(bit(v, i) == c for v in t):
                return True
    return False


def check_reduction():
    prior = read("R7_CENTRAL_D35_COUNT_DELTA.json")
    unrestricted = read("R7_E16_D35_UNRESTRICTED_COUNT_DELTA.json")
    assert unrestricted["previous_input"]["sha256"] == BINDINGS["R7_CENTRAL_D35_COUNT_DELTA.json"]
    raw("R7_CENTRAL_CROSS_CUT_COUNT_GATE_REVIEW.md")
    raw("R7_E16_D35_FULL_CLOSURE_REVIEW.md")
    d35_pairs = {(2, 5), (1, 0)}
    cols124 = {tuple(v) for v in prior["conditional_remainder"]}
    cols94 = {(s,t,y,u) for s,t,y,u in cols124 if (s,t) not in d35_pairs and (u,y) not in d35_pairs}
    assert len(cols124) == 124 and len(cols94) == 94
    assert cols94 == set(map(tuple, unrestricted["conditional_remainder"]))
    cols = {(s,t,y,u) for s,t,y,u in cols94 if abs(s + y - t - u) >= 2}
    assert len(cols) == 78
    for s,t,y,u in cols:
        assert (3-s,5-t,5-y,3-u) in cols and (u,y,t,s) in cols
    projected = {(s,t) for s,t,_,_ in cols}
    assert all(t in (0,1,4,5) for s,t in projected if s in (1,2))
    by_receiver = defaultdict(set)
    for s,t,y,u in cols:
        by_receiver[s,t].add(y)
    source_data = read(BASE+"SOURCE_BASIS.json")
    shapes = read(BASE+"SOURCE_SHAPES.json")
    templates = {(r["distance_type"], r["zero_based_local_index"]): (tuple(r["S"]),tuple(r["T"]))
                 for rows in shapes["rows_by_number_of_sparse_columns"].values() for r in rows}
    assert len(templates) == 32
    raw_T = Counter()
    receivers = Counter()
    for kind, s in (("222",(0,3,5)),("224",(0,3,12)),("244",(0,3,29))):
        axes = tuple(i for i in AXES if loads(s)[i] in (1,2))
        reconstructed = set()
        for side in product((0,1), repeat=len(axes)):
            for t in sparse_sets(axes, side):
                raw_T[kind] += 1
                if independent((s,t)) and set(zip(loads(s),loads(t))) <= projected:
                    assert t not in reconstructed
                    reconstructed.add(t)
        for key,(actual,t) in templates.items():
            if key[0] != kind:
                continue
            assert s == actual
            orbit = {image(t,*f) for f in stabilizer(s)}
            assert orbit <= reconstructed
            reconstructed -= orbit
            receivers[kind] += len(orbit)
        assert not reconstructed
    assert raw_T == {"222":6368,"224":1792,"244":512}
    assert receivers == {"222":234,"224":54,"244":21}
    sources, groups = {}, {}
    Y_reps = set()
    count = Counter()
    for frame in source_data["rows"]:
        budget()
        label = frame["distance_type"],frame["local_index"]
        s,t = templates[label]
        assert (s,t) == (tuple(frame["S"]),tuple(frame["T"]))
        group = groups[label] = tuple(f for f in stabilizer(s) if image(t,*f) == t)
        st = tuple(zip(loads(s),loads(t)))
        choices = [by_receiver[v] for v in st]
        sparse = [(i,int(a <= {0,1})) for i,a in enumerate(choices) if a <= {0,1} or a <= {4,5}]
        assert sparse == [tuple(v) for v in frame["sparse_sides"]]
        eligible = set()
        for y in sparse_sets(*zip(*sparse)):
            count["raw_Y"] += 1
            if set(y)&set(t):
                continue
            count["avoid_T"] += 1
            if all(v in a for v,a in zip(loads(y),choices)):
                assert y not in eligible
                eligible.add(y)
        for r in frame["Y_rows"]:
            y = tuple(r["Y"])
            eligible.remove(y)
            options = [sorted(u for u in range(4) if (a,b,c,u) in cols)
                       for (a,b),c in zip(st,loads(y))]
            assert options == r["allowed_u"]
            rep = min(image(y,*f) for f in group)
            f = aff(r,"to_representative")
            assert f in group and image(y,*f) == rep == tuple(r["representative_Y"])
            sources[label,y] = rep
            if y == rep:
                Y_reps.add((label,y))
        assert not eligible
    assert (count["raw_Y"],count["avoid_T"]) == (2286,2174) and len(sources) == 578 and len(Y_reps) == 299

    pre = read(BASE+"BIDIRECTIONAL_JOIN.json")
    post = read(BASE+"BIDIRECTIONAL_JOIN_COMPLETION_V2.json")
    buckets = defaultdict(set)
    mappings = 0
    for record in pre["template_records"]:
        label = tuple(record["template"])
        s,t = templates[label]
        key = canonical(t)
        canon = canonical_points(key)
        assert key == tuple(record["signature_key"]) and canon == tuple(record["canonical_T"])
        # A direct coordinate-permutation scan plus every possible preimage of zero.
        actions = set()
        for p in PERMS:
            pt = tuple(permute(v,p) for v in t)
            for x in pt:
                if tuple(sorted(v^x for v in pt)) == canon:
                    actions.add((p,x))
        assert actions == {(tuple(p),x) for p,x in record["transformations"]}
        mappings += len(actions)
        buckets[key].update(image(s,*f) for f in actions)
    assert len(pre["template_records"]) == len({tuple(r["template"]) for r in pre["template_records"]}) == 32
    assert mappings == 1726
    directed = {}
    source_seen = set()
    stats = [Counter(),Counter()]
    for phase, rows in enumerate((pre["source_rows"],post["new_source_rows"])):
        assert len(rows) == (197,102)[phase]
        for frame in rows:
            budget()
            label,y = tuple(frame["receiver"]),tuple(frame["Y"])
            assert (label,y) in Y_reps and (label,y) not in source_seen
            source_seen.add((label,y))
            s,t = templates[label]
            assert (s,t) == (tuple(frame["S"]),tuple(frame["T"]))
            key = canonical(y)
            p,x = aff(frame,"Y_to_canonical")
            assert key == tuple(frame["Y_signature_key"]) and image(y,p,x) == canonical_points(key)
            inv = tuple(p.index(i) for i in AXES)
            st_y = tuple(zip(loads(s),loads(t),loads(y)))
            expected = set()
            for shape in buckets[key]:
                # Push the six allowed counts to canonical coordinates before inverse transport.
                if phase and any((*prefix, 3-c if bit(x,p[i]) else c) not in cols
                                 for i,prefix in enumerate(st_y) for c in [loads(shape)[p[i]]]):
                    continue
                expected.add(image(shape,inv,permute(x,inv)))
            group = tuple(f for f in groups[label] if image(y,*f) == y)
            good = {}
            for item in frame["candidates"]:
                u = tuple(item["U"])
                expected.remove(u)
                r_s,r_t = templates[tuple(item["reverse_template"])]
                f = aff(item,"reverse_to_actual")
                assert image(r_s,*f) == u and image(r_t,*f) == y
                colors = physical(s,t,y,u)
                assert independent(colors)
                actual_cols = tuple((*prefix,z) for prefix,z in zip(st_y,loads(u)))
                verdict = ("column78" if not set(actual_cols) <= cols else
                           "D35" if has_d35(colors) else "survives")
                assert verdict == item["verdict"]
                stats[phase][verdict] += 1
                if verdict == "survives":
                    assert min(map(abs,gaps(colors))) == 2
                    good[u] = item
            assert not expected
            for u,item in good.items():
                rep = min(image(u,*f) for f in group)
                f = aff(item,"to_representative")
                assert rep in good and f in group and image(u,*f) == rep == tuple(item["representative_U"])
                if rep == u:
                    directed[*label,y,u] = (s,t,y,u)
    assert source_seen == Y_reps and len(directed) == 4767
    assert stats == [Counter(column78=15327,D35=37,survives=4595),Counter(D35=2,survives=3863)]
    assert Counter(k[0] for k in directed) == {"222":1832,"224":2198,"244":737}
    quotient = read(FULL+"QUOTIENT.json")
    reversal, kept = {}, {}
    def flatten(key):
        a,b,y,u = key
        return a,b,tuple(y),tuple(u)
    for row in quotient["transports"]:
        key,rev = map(flatten,(row["key"],row["reverse_key"]))
        assert key not in reversal and rev in directed
        reversal[key] = rev
        s,t,y,u = directed[key]
        sr,tr,yr,ur = directed[rev]
        p,x = tuple(row["seven_axis_permutation"]),row["seven_xor"]
        for a,b in zip((u,y,t,s),(sr,tr,yr,ur)):
            stages = (row[k] for k in ("inverse_reverse_template","source_transport","U_transport"))
            for per,shift in stages:
                a = image(a,per,shift)
            assert a == b
        assert p[6] == 6 and bit(x,6) == 1 and x.bit_count() % 2 == 1
        old,new = physical(s,t,y,u),physical(sr,tr,yr,ur)
        assert tuple(image(g,p,x) for g in old) == new[::-1]
        assert min(key,rev) == flatten(row["kept_key"])
        if key <= rev:
            kept[key] = directed[key]
    assert reversal.keys() == directed.keys() and all(reversal[v] == k for k,v in reversal.items())
    assert sum(k == v for k,v in reversal.items()) == 85 and len(kept) == 2426
    assert len(quotient["representatives"]) == 2426
    for row in quotient["representatives"]:
        key = flatten(row["key"])
        s,t,y,u = kept[key]
        assert (s,t,y,u) == tuple(tuple(row[k]) for k in ("S","T","Y","U"))
        assert physical(s,t,y,u) == tuple(tuple(row[k]) for k in ("even_holes","odd_holes"))
    assert {flatten(row["key"]) for row in quotient["representatives"]} == kept.keys()
    return kept, flatten



def check_plans(kept, flatten, physical_holes=physical):
    d=read(FULL+"CHECK.json")
    assert d["status"]=="complete" and not d["unvisited"] and d["first_unsupported"] is None
    assert d["visited"]==len(d["positive"])==len(kept)==2426
    core="E:/\u65b0\u95ee\u9898/research/seven_directions/"
    profile=read(core+"Q6_T15_ACTUAL_PROFILE.json")
    targets={row["index"]:(set(row["included"]),set(row["omitted"])) for row in profile["orbits"]}
    registry=read(core+"Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json")
    assert registry["verdict"]=="PASS"
    union=set(registry["union_closed_core_indices"])
    assert len(union)==1017 and union=={x["core_index"] for x in read(core+"Q6_T15_GOOD_ROOT_ALL_CLOSED.json")["cores"]}
    extra={
        85: ("Q6_T15_CORE85_MARKED", "core85_universal_proved", ({31,47,55},{1,2})),
        1007: ("Q6_T15_TWO_CORES_FORCED_PORT", "core1007_closed", ({28,44,61},{7,11})),
        1054: ("Q6_T15_CORE1054_MARKED", "core1054_universal_proved", ({28,61,62},{7,11})),
    }
    for index,(stem,claim,exact) in extra.items():
        receipt=read(core+stem+"_REVIEW.json")
        assert receipt["verdict"]=="PASS" and receipt[claim]
        raw(core+stem+"_REVIEW.md")
        for name in (stem+"_CLOSURE.md","Q6_T15_ACTUAL_PROFILE.json"):
            raw(core+name)
            assert BINDINGS[core+name]==receipt["audited_input_hashes"][name].removeprefix("sha256:")
        assert index not in union and targets[index]==exact
    core_ids=union|extra.keys()
    newp=raw("R7_MU3_T63_NEW_RANK.md").decode("utf8")
    t63={int(k):tuple(set(map(int,s.split(","))) for s in (h,m))
         for k,h,m in re.findall(r"^\| (\d+) \| ([\d,]+) \| ([\d,]+) \| [\d,]+ \|",newp,re.M)}
    assert set(t63)==set(range(1,7))
    assert read("R7_MU3_CONTROLLED_AND_T63_REVIEW.json")["verdict"]=="PASS"
    forward_counts=Counter()
    forward_tools=Counter()
    registered_tools=Counter()
    def bit(v,i):
        return (v >> i) & 1
    def side(values,i,b):
        assert 0<=i<7 and b in (0,1)
        return {v for v in values if bit(v,i)==b}
    def groups(g,i,b):
        return tuple(side(points,i,b) for points in g)
    def size(g):
        return tuple(map(len,g))
    def counts(g,i,order=(0,1)):
        return [list(size(groups(g,i,b))) for b in order]
    def proj(v,axes):
        return sum(bit(v,axis)<<j for j,axis in enumerate(axes))
    def projection(g,axes):
        return {proj(v,axes) for v in g}
    def arrays(g):
        return [sorted(s) for s in g]
    def twins(src,i):
        return {v^(1<<i) for v in src}
    def dual_input(a,b,k,nA,nB,H):
        assert a!=b
        x,ret = set(nA),set(nB)
        assert len(x)==len(nA)==k-2 and len(ret)==len(nB)==2
        assert x<=a[1] and ret<=b[1], (a,b,x,ret)
        return x,ret

    gates=Counter()
    supplier=Counter()
    receiver=Counter()
    broad=Counter()
    kusage=Counter()
    q5=Counter()

    def whole(g,marks,axis,mark_side,claim,kind):
        assert len(marks)==2 and marks<=side(g[1],axis,mark_side)
        actual=counts(g,axis,(mark_side,1-mark_side))
        assert actual==claim
        (a,b),(c,e)=actual
        if kind in ("majority_root","Q6_same_side_majority_root"):
            assert a in (0,1) and b==a+5 and 1<=c<=16 and e==c-1
            return "majority"
        if kind=="Q6_balanced_complement_avoid_two":
            assert (a,b,c,e) in ((1,5,1,1),(0,4,2,2))
            return "balanced_avoid_two"
        assert kind in ("two_minority_roots","Q6_same_side_two_minority_roots")
        assert (a,b)==(2,5) and 0<=c<=15 and e==c+1
        return "two_minority"

    def qfive(g,m,kind):
        a,b=size(g); q=len(m)
        assert m<=g[1] and q>=1 and b-a==2*q and max(a,b)<=16
        if kind in ("Q5_A_ALL","avoid_one"):
            assert q==1 and 0<=a<=14
            return "avoid_one"
        if kind in ("Q5_T15_FULL","T15"):
            assert q==2 and (a,b)==(1,5)
            return "T15"
        assert kind in ("T44","Q5_T44") and q==2 and (a,b)==(0,4)
        return "T44"



    six="E:/\u65b0\u95ee\u9898/research/six_directions/"
    old_text=raw(six+"Q5_T63_RANK_PROOF.md").decode("utf8")
    old_t63={int(rank):tuple(set(map(int,st.split(","))) for st in (holes,marks))
             for rank,holes,marks in re.findall(r"^\|(\d+)\|([\d,]+)\|([\d,]+)\|$",old_text,re.M)}
    assert set(old_t63)==set(range(7))
    batch=raw(six+"Q5_T26_RANK_BATCH_PROOF.md").decode("utf8")
    t26={int(k):tuple(set(map(int,g.split(","))) for g in (a,b,m))
         for k,a,b,m in re.findall(r"^\| (\d+) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \|",batch,re.M)}
    assert set(t26)==set(range(55))
    t26_transports=[]
    central=Counter()
    broad_k=Counter()
    def check_core(a_group,r_group,marks,j,target,root,axes,claimed,per):
        assert target in core_ids
        assert a_group=={root} and len(r_group)==3 and len(marks)==2 and r_group.isdisjoint(marks)
        assert axes==[a for a in range(7) if a!=j] and sorted(per)==list(range(6))
        norm=tuple(projection({root^v for v in group},axes) for group in (r_group,marks))
        assert arrays(norm)==claimed
        assert tuple({permute(v,per) for v in group} for group in norm)==targets[target]

    def check_edge_fields(record):
        if isinstance(record,dict):
            for key,value in record.items():
                if "edge" in key:
                    assert key=="required_forced_edge" and value is None
                check_edge_fields(value)
        elif isinstance(record,list):
            for value in record:
                check_edge_fields(value)

    for row in d["positive"]:
        budget()
        key=flatten(row["key"])
        s,t,y,u=kept.pop(key)
        assert (s,t,y,u)==tuple(tuple(row[k]) for k in ("S","T","Y","U"))
        colors=physical_holes(s,t,y,u)
        assert all(len(set(g))==8 and all(v.bit_count()%2==i for v in g) for i,g in enumerate(colors))
        assert independent(colors) and min(map(abs,gaps(colors)))==2
        assert [list(g) for g in colors]==[row["even_holes"],row["odd_holes"]]
        assert list(gaps(colors))==row["bit_one_even_minus_odd"]
        physical=tuple(map(set,colors))
        H=physical[0]|physical[1]
        p=row["plan"];g=p["gate"]
        check_edge_fields(p)
        gates[g]+=1
        if g=="other_central_cut":
            axis=p["physical_outer"]; swap=p["normalize_swap_axes"]; xor=p["normalize_xor"]
            assert 0<=axis<6 and swap==[axis,6] and xor in (0,1)
            perm=list(range(7));perm[axis],perm[6]=perm[6],perm[axis]
            tr=lambda v:permute(v,perm)^xor
            norm=tuple({tr(v) for v in physical[i^xor]} for i in range(2))
            assert counts(norm,6)==[[3,5],[5,3]]
            pp=p["normalized_plan"]; gg=pp["gate"]; central[gg]+=1
            assert pp["outer"]==6
            two=gg in ("two_majority_roots","controlled_three_majority_roots")
            sb=pp["receiver_side"] if two else pp["B_side"]
            B=groups((norm[sb],norm[1-sb]),6,sb)
            A=groups((norm[1-sb],norm[sb]),6,1-sb)
            assert size(A)==size(B)==(3,5)
            i=pp["inner"]; s=pp["marked_side"] if two else pp["side"]
            xx=set(pp["sources"] if two else pp["X"])
            yy=set(pp["marks"] if two else pp["Y"])
            assert i!=6 and len(xx)==len(yy)==2 and xx<=A[1] and yy==twins(xx,6)
            assert yy.isdisjoint(norm[0]|norm[1])
            inverse=lambda v:permute(v^xor,perm)
            assert {inverse(v) for v in yy}==twins({inverse(v) for v in xx},axis)
            act=counts(B,i,(s,1-s)); (a,b),(c,e)=act
            mm=[len(side(yy,i,t)) for t in (s,1-s)]
            after=(B[0],B[1]|yy)
            if two:
                assert a in (0,1)
                assert arrays(B)==[pp["receiver_minority"],pp["receiver_majority"]]
                if gg=="two_majority_roots":
                    assert b==a+4 and c>=2 and e==c-2 and mm==[2,0]
                else:
                    assert (a,b,c,e)==(0,5,3,0) and mm==[2,0]
                    W=side(B[0],i,1-s)
                    Z=twins(side(B[1],i,s),i)
                    assert W.isdisjoint(Z) and len(Z)==5
                    assert sorted((x^y).bit_count() for x,y in combinations(W,2)) in ([2,2,2],[2,2,4],[2,4,4])
                continue
            assert pp["donor_minority_count"]==3 and counts(B,i)==pp["original_counts"]
            if gg=="central_source_net1_split":
                assert b==a+1 and e==c+1 and mm==[1,1]
                assert pp["root"] is None and pp["mirror"] is None
            elif gg=="central_source_net1_same_side_root":
                root,w=pp["root"],pp["mirror"]
                assert a in (1,2) and b==a+1 and e==c+1 and mm==[2,0]
                assert root in side(B[0],i,s) and w==root^(1<<i) and w not in norm[0]|norm[1]|yy
                assert twins(A[1],6)<=side(twins(A[1],6),i,s)
            elif gg=="central_source_net2_separated_root":
                root,w=pp["root"],pp["mirror"]
                assert a in (0,1) and b==a+2 and c==e and c>=2 and mm==[1,1]
                assert root in side(B[0],i,1-s) and w==root^(1<<i) and w not in norm[0]|norm[1]|yy
            else:
                assert a in (0,1) and pp["root"] is None and pp["mirror"] is None and mm==[2,0]
                if gg=="central_source_net2_balanced_two_marks":
                    assert b==a+2 and c==e and c>=2
                else:
                    assert gg=="central_source_net3_majority_roots" and b==a+3 and e==c-1 and c>=1
            assert counts(after,i)==pp["modified_counts"]
            continue
        j=p["outer"]
        if g=="universal_delta3":
            a=p["alpha_parity"]; s=p["donor_side"]; i=p["inner"]
            A=groups((physical[a],physical[1-a]),j,s)
            B=groups((physical[1-a],physical[a]),j,1-s)
            assert i!=j and size(A)==(4,7) and (p["r"],p["k"])==(4,3) and size(B)==(1,4)
            assert arrays(B)==[p["receiver_minority"],p["receiver_majority"]]
            X=set(p["sources"]); marks=twins(X,j)
            assert len(X)==3 and X<=A[1] and sorted(marks)==p["marks"] and marks.isdisjoint(H)
            root=p["root"]; w=p["mirror"]; z=bit(root,i)
            assert B[0]=={root} and w==root^(1<<i) and w not in H|marks
            assert counts(B,i,(z,1-z))==[[1,2],[0,2]]
            assert [len(side(marks,i,t)) for t in (z,1-z)]==[2,1]
            continue
        if g in ("controlled_cycle_count","controlled_cycle_registered_split"):
            regular=g=="controlled_cycle_count"
            assert "forced_edge" not in p and "required_forced_edge" not in p
            alpha=p["alpha_parity"]; s=p["A_side"] if regular else p["donor_side"]
            A=groups((physical[alpha],physical[1-alpha]),j,s)
            B=groups((physical[1-alpha],physical[alpha]),j,1-s)
            r,k=p["r"],p["k"]; assert 0<=r<=4 and k in (3,4,5) and size(A)==(r,r+k) and size(B)[1]-size(B)[0]==k
            x=p["X"] if regular else p["sources"]
            marks=p["Y"] if regular else p["marks"]
            X=set(x); Z=twins(X,j)
            assert len(X)==len(x)==k and X<=A[1] and sorted(Z)==marks and Z.isdisjoint(H)
            forward_counts[g,k]+=1
            if regular:
                i=p["inner"]; assert i!=j and [f["side"] for f in p["receiver_sides"]]==[0,1]
                assert arrays(A)==[p["donor_original_minority"],p["donor_original_majority"]]
                for b,f in enumerate(p["receiver_sides"]):
                    old=groups(B,i,b); m=side(Z,i,b)
                    assert arrays((*old,m))==[f["original_minority"],f["original_majority"],f["marks"]]
                    assert len(old[1])-len(old[0])==len(m)
                    forward_tools[qfive((old[0],old[1]|m),m,f["interface"])]+=1
            else:
                rr=p["receiver"];i=rr["inner"]
                assert i!=j and arrays(B)==[p["receiver_minority"],p["receiver_majority"]]
                axes=[a for a in range(7) if a not in (i,j)]
                assert axes==rr["projected_axes"] and len(rr["faces"])==2
                local=Counter()
                for b_face,f in enumerate(rr["faces"]):
                    old=groups(B,i,b_face); m=side(Z,i,b_face); new=(old[0],old[1]|m)
                    q=len(m); assert q>0 and len(new[1])-len(new[0])==2*q
                    small,large,omits=map(set,(f["minority"],f["majority"],f["marks"]))
                    assert arrays(tuple(projection(g,axes) for g in (*new,m)))==arrays((small,large,omits))
                    iface=f["interface"]
                    if iface["kind"]=="T63_new":
                        assert size(new)==(0,6) and q==3 and iface["rank"] in t63
                        shift=iface["local_to_rank_xor"]; perm=iface["local_to_rank_permutation"]
                        assert sorted(perm)==list(range(5)) and 0<=shift<32
                        tr=lambda v:sum(bit(v^shift,i)<<p for i,p in enumerate(perm))
                        assert tuple({tr(v) for v in g} for g in (large,omits))==t63[iface["rank"]]
                        local[f"T63_new_{iface['rank']}"]+=1
                    elif iface["kind"]=="Q5_T26_RANK":
                        rank=iface["rank"]
                        target=t26[rank]
                        assert size(new)==(2,6) and q==2 and omits<=large and iface["canonical"]==arrays(target)
                        # Choose the image of one minority point, then derive the common translation.
                        anchor=min(small)
                        witness=next(((p,a^permute(anchor,p)) for p in permutations(range(5)) for a in target[0]
                                      if tuple(set(image(g,p,a^permute(anchor,p))) for g in (small,large,omits))==target),None)
                        assert witness is not None
                        t26_transports.append(dict(key=key,side=b_face,rank=rank,
                                                   permutation=list(witness[0]),xor=witness[1]))
                        local[f"T26_old_{rank}"]+=1
                    else:
                        local[qfive(new,m,iface["kind"])]+=1
                assert sum(n for key,n in local.items() if key.startswith(("T63_new_","T26_old_")))==1
                registered_tools.update(local)
            continue
        assert g in ("k4_two_return","registry_two_return")
        generic=g=="registry_two_return"
        if generic:
            sa=p["donor_side"]; alpha=1-p["donor_majority_parity"]; k=p["k"]
            assert p["required_forced_edge"] is None and k in (4,5,6,7,8)
            broad_k[k]+=1
        else:
            sa=p["A_side"]; alpha=p["alpha_parity"]; k=4
            assert p["B_side"]==1-sa and p["beta_parity"]==1-alpha
        A=groups((physical[alpha],physical[1-alpha]),j,sa)
        B=groups((physical[1-alpha],physical[alpha]),j,1-sa)
        r,t=size(A)[0],size(B)[0]
        assert size(A)==(r,r+k) and size(B)==(t,t+k)
        x,ret=dual_input(A,B,k,p["X"],p["U"],H)
        Ystar,V=twins(x,j),twins(ret,j)
        assert (Ystar|V).isdisjoint(H) and Ystar.isdisjoint(V)
        AA=(A[0],(A[1]-x)|V); BB=(B[0],(B[1]-ret)|Ystar)
        kusage[("two_return",k)]+=1
        if not generic:
            assert sorted(Ystar)==p["Y"] and sorted(V)==p["V"]
            assert sorted(AA[0]|AA[1])==p["H_prime_A"] and arrays(AA)==p["H_prime_A_by_alpha_beta"]
            assert sorted(BB[0]|BB[1])==p["H_prime_B"] and arrays(BB[::-1])==p["H_prime_B_by_alpha_beta"]
            sa1,rb=p["supplier"],p["receiver"]
            assert rb["inner"]!=j
            if sa1["kind"]=="core117":
                assert size(AA)==(1,5)
                check_core(A[0],A[1]-x,V,j,117,sa1["root"],sa1["projected_axes"],
                           [sa1["normalized_retained"],sa1["normalized_marks"]],sa1["coordinate_transport"])
                sk="core117"
            else:
                assert sa1["inner"]!=j
                sk=whole(AA,V,sa1["inner"],sa1["mark_side"],sa1["hole_counts"],sa1["kind"])
            if rb["mode"]=="whole_face":
                assert whole(BB,Ystar,rb["inner"],rb["mark_side"],rb["hole_counts"],rb["kind"]) in ("majority","two_minority")
            elif rb["mode"]=="positive_split":
                i=rb["inner"]
                assert [f["side"] for f in rb["sides"]]==[0,1]
                for s,f in enumerate(rb["sides"]):
                    actual=groups(BB,i,s)
                    m=side(Ystar,i,s)
                    assert arrays((*actual,m))==[f["minority"],f["majority"],f["marks"]]
                    assert list(size(actual))==f["hole_counts"]
                    assert qfive(actual,m,f["interface"])=="avoid_one"
            else:
                assert rb["mode"]=="controlled_single_root"
                i=rb["inner"]; z=rb["Z_side"]; tside=rb["T_side"]
                assert tside==1-z
                [pmin,pmax],[qmin,qmax]=ct=counts(BB,i,(z,tside))
                marks=[len(side(Ystar,i,s)) for s in (z,tside)]
                assert ct==rb["hole_counts"] and marks==rb["mark_counts"]
                assert (pmin,qmin)==(rb["p"],rb["q"])
                if rb["kind"]=="same_side":
                    assert pmin in (1,2) and pmax==pmin+3 and qmax==qmin+1 and marks==[2,0]
                else:
                    assert rb["kind"]=="separated" and pmin>=1 and qmin in (0,1)
                    assert pmax==pmin+1 and qmax==qmin+3 and marks==[1,1]
                root,w=rb["a"],rb["w"]
                assert root in side(B[0],i,z) and w==root^(1<<i)
                assert w not in H|Ystar and bit(w,j)==1-sa and bit(w,i)==tside

            supplier[sk]+=1
            receiver[rb["kind"] if rb["mode"]=="controlled_single_root" else rb["mode"]]+=1
            continue
        assert arrays((A[0],A[1]-x,V))==[p["donor_minority"],p["donor_retained"],p["donor_marks"]]
        assert arrays((B[0],B[1]-ret,Ystar))==[p["receiver_minority"],p["receiver_retained"],p["receiver_marks"]]
        dp=p["donor"]
        if dp["kind"]=="T15_exact_core":
            check_core(A[0],A[1]-x,V,j,dp["index"],dp["normalization_root"],[a for a in range(7) if a!=j],
                       dp["normalized_groups"],dp["coordinate_transport"])
            broad[f"core_{dp['index']}"]+=1
        elif dp["kind"]=="Q6_T15_D4":
            i,s=dp["inner"],dp["side"]
            assert i!=j and V<=side(AA[1],i,s)
            assert counts(AA,i,(s,1-s))==dp["face_counts"]==[[0,4],[1,1]]
            broad["D4"]+=1
        elif dp["kind"]=="Q6_T26_paired_S1":
            assert size(AA)==(2,6)
            root=dp["root"]
            face_specs=dp["inner_sides"]
            assert len(face_specs)==2 and j not in [f[0] for f in face_specs] and face_specs[0][0]!=face_specs[1][0]
            off=[]
            for i,s in face_specs:
                Z=groups(AA,i,s)
                E=groups(AA,i,1-s)
                assert Z[0]=={root} and size(Z)==(1,4) and size(E)==(1,2) and V<=Z[1]
                off.append(E[1])
            assert len(off[0]&off[1]) in (0,2)
            broad["paired_S1"]+=1
        elif dp["kind"] in ("T15_isolated_mark","T44_isolated_mark"):
            i,s=dp["inner"],dp["inner_side"]
            assert i!=j and size(AA)==((1,5) if dp["kind"]=="T15_isolated_mark" else (0,4))
            assert groups(AA,i,s)==(set(),{dp["isolated_mark"]}) and dp["isolated_mark"] in V
            broad[dp["kind"]]+=1
        else:
            assert dp["inner"]!=j
            broad[whole(AA,V,dp["inner"],dp["side"],dp["face_counts"],dp["kind"])]+=1
        rp=p["receiver"]; i=rp["inner"]; assert i!=j and rp["kind"]=="positive_split_Q5"
        axes=[a for a in range(7) if a not in (i,j)]
        assert axes==rp["projected_axes"] and len(rp["faces"])==2
        for s,f in enumerate(rp["faces"]):
            actual=groups(BB,i,s); m=side(Ystar,i,s)
            local=tuple(projection(v,axes) for v in (*actual,m))
            assert arrays(local)==[f["minority"],f["majority"],f["marks"]]
            iface=f["interface"]; kind=iface["kind"]
            if kind in ("T63_old","T63_split","T63_new"):
                assert size(actual)==(0,6) and len(m)==3 and m<=actual[1]
                if kind=="T63_old":
                    rank=iface["rank"]; per=iface["rank_to_local_permutation"]; xor=iface["rank_to_local_xor"]
                    assert sorted(per)==list(range(5)) and 0<=xor<32
                    assert tuple({permute(v,per)^xor for v in group} for group in old_t63[rank])==local[1:]
                    q5[f"T63_old_{rank}"]+=1
                elif kind=="T63_new":
                    rank=iface["rank"]; per=iface["local_to_rank_permutation"]; xor=iface["local_to_rank_xor"]
                    assert sorted(per)==list(range(5)) and 0<=xor<32
                    assert tuple({permute(v^xor,per) for v in group} for group in local[1:])==t63[rank]
                    q5[f"T63_new_{rank}"]+=1
                else:
                    a=iface["local_inner"]; assert 0<=a<5
                    assert tuple(sum(bit(v,a) for v in group) for group in local[1:]) in ((2,1),(4,2))
                    q5["T63_split"]+=1
            else:
                q5[qfive(actual,m,kind)]+=1

    assert not kept
    assert gates==d["plan_counts"]=={
        "other_central_cut":615,"universal_delta3":26,"controlled_cycle_count":568,
        "controlled_cycle_registered_split":266,"k4_two_return":640,"registry_two_return":311}
    assert {i:broad[f"core_{i}"] for i in extra}=={85:1,1007:6,1054:2}
    return dict(plan_counts=gates, central=central, forward_q5=forward_tools, registered_q5=registered_tools,
                k4_supplier=supplier, k4_receiver=receiver, broad_k=broad_k,
                broad_supplier=broad, broad_q5=q5, T26_transports=t26_transports)


if __name__ == "__main__":
    assert __debug__
    manifest = read(FULL+"INPUTS.json")
    assert BINDINGS[FULL+"INPUTS.json"] == "b3153b6e3ef274e61d61dbcb802e7e6d483e24a5cf7c878371b4c3b5b11cf9fd"
    for category in ("author_artifacts","proof_inputs"):
        for file,expected in manifest[category].items():
            raw(file)
            assert BINDINGS[file] == expected, file
    for name in ("QUOTIENT.json","CHECK.json"):
        for file,expected in read(FULL+name)["input_sha256"].items():
            raw(file)
            assert BINDINGS[file] == expected, file
    kept, flatten = check_reduction()
    receipt = check_plans(kept, flatten)
    budget()
    receipt.update(reduction=dict(columns=78,receiver_candidates=8672,receiver_templates=32,
        source_candidates=2286,source_labelled=578,source_representatives=299,template_maps=1726,
        prefix_candidates=19959,suffix_candidates=3865,surviving=8458,directed=4767,
        reversal_fixed=85,reversal_pairs=2341,representatives=2426),
        cpu_seconds=process_time()-START, bindings=BINDINGS)
    print(json.dumps(receipt, ensure_ascii=True))
