#!/usr/bin/env python3
"""Draw explanatory figures and four exact, small cube-extension examples."""
from collections import deque
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np

CASE = Path(__file__).resolve().parents[1]
ASSETS = CASE / "assets"
PAPER, INK, MUTED = "#fdfcf7", "#1a1a1a", "#6b6b6b"
BLUE, ORANGE, GREEN, RED = "#1a4a8c", "#b8390e", "#065f46", "#991b1b"
BORDER, LIGHT = "#d6d0c0", "#f4f1ea"
plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 11,
                     "text.color": INK, "svg.fonttype": "none",
                     "mathtext.fontset": "dejavuserif"})


def canvas(width=10, height=5):
    fig, ax = plt.subplots(figsize=(width, height))
    fig.patch.set_facecolor(PAPER)
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    fig.subplots_adjust(left=.02, right=.98, top=.98, bottom=.02)
    return fig, ax


def line(ax, a, b, color=BORDER, width=1.6, bend=0, arrow=False, style="-", z=1):
    patch = FancyArrowPatch(a, b, arrowstyle="-|>" if arrow else "-",
                            mutation_scale=11, color=color, linewidth=width,
                            connectionstyle=f"arc3,rad={bend}", linestyle=style,
                            shrinkA=7, shrinkB=7, zorder=z)
    ax.add_patch(patch)


def node(ax, pos, label, face=PAPER, edge=BLUE, radius=.14, size=10, z=5):
    ax.add_patch(Circle(pos, radius, facecolor=face, edgecolor=edge, lw=1.6, zorder=z))
    ax.text(*pos, label, ha="center", va="center", fontsize=size,
            color="white" if face in [BLUE, ORANGE, RED, GREEN] else INK, zorder=z+1)


def panel(ax, x, y, w, h, face=LIGHT):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=.02,rounding_size=.05",
                               facecolor=face, edgecolor=BORDER, linewidth=.7, zorder=0))


def save(fig, stem):
    fig.savefig(ASSETS / f"{stem}.svg", facecolor=PAPER)
    fig.savefig(ASSETS / f"{stem}.png", facecolor=PAPER, dpi=170)
    plt.close(fig)


def distances(adj, root):
    d, parent = {root: 0}, {root: None}
    q = deque([root])
    while q:
        u = q.popleft()
        for v in sorted(adj[u]):
            if v not in d:
                d[v], parent[v] = d[u] + 1, u
                q.append(v)
    return d, parent


BASE = {i: {i ^ (1 << bit) for bit in range(3)} for i in range(8)}
STATES = [
    {"id": "one", "file": "filling_one_pin", "pins": [[0]],
     "title": "1. A single attachment misses the opposite corner",
     "label": "只接一处", "explanation": "只把 x 接到 0，点 7 仍需走 4 步。度数够用，但距离覆盖不够。"},
    {"id": "cover", "file": "construction_filling", "pins": [[0, 7]],
     "title": "2. Complementary attachments cover the whole source",
     "label": "互补两处", "explanation": "把 x 接到互为对角的 0 和 7：两个半径 2 邻域共同覆盖原来的 8 个点，新点到各点至多 3 步。"},
    {"id": "capacity", "file": "filling_capacity", "pins": [[0, 7], [0, 7]],
     "title": "3. Reusing the same pins exceeds the degree budget",
     "label": "重复占用", "explanation": "再让 y 使用相同的 0、7，覆盖仍然完整，但这两个旧点的度数升到 5，超过上限 4。"},
    {"id": "rebalance", "file": "filling_rebalanced", "pins": [[0, 7], [1, 6]],
     "title": "4. Different pins preserve both coverage and capacity",
     "label": "换组邻域", "explanation": "让 y 改接 1、6，覆盖当前全部 9 个点（也包括先前加入的 x），同时让每个点的度数保持不超过 4。"},
]


def draw_cube_examples():
    positions = {0:(2.0,3.05), 1:(3.9,3.05), 2:(2.0,1.15), 3:(3.9,1.15),
                 4:(2.85,3.95), 5:(4.75,3.95), 6:(2.85,2.05), 7:(4.75,2.05),
                 8:(.55,3.05), 9:(5.95,3.05)}
    def edge_bend(u, v):
        lo, hi = sorted([u, v])
        if (lo, hi) == (6, 9):
            return .55
        return -.32 if hi >= 8 and abs(positions[u][0]-positions[v][0]) > 2 else 0
    output = []
    for state in STATES:
        adj = {u: set(vs) for u, vs in BASE.items()}
        for step, pins in enumerate(state["pins"]):
            root = 8 + step
            before = {u:set(vs) for u,vs in adj.items()}
            adj[root] = set(pins)
            for p in pins:
                adj[p].add(root)
        covered = set().union(*(set(v for v,d in distances(before,p)[0].items() if d<=2)
                                for p in state["pins"][-1]))
        dist, parent = distances(adj, root)
        far = max(dist, key=dist.get)
        path = [far]
        while parent[path[-1]] is not None:
            path.append(parent[path[-1]])
        path.reverse()
        diameter = max(max(distances(adj,u)[0].values()) for u in adj)
        degree = max(map(len, adj.values()))
        entry = dict(state, vertices=len(adj), covered=len(covered), source_vertices=len(before),
                     max_degree=degree, diameter=diameter, root=root, farthest=far,
                     highlighted_path=path, degrees={str(u):len(vs) for u,vs in adj.items()})
        output.append(entry)
        fig, ax = canvas(10, 4.7)
        ax.text(.1,4.65,state["title"],fontsize=14,weight="bold")
        ax.text(.1,4.32,"Cube extension: eight starting vertices; limits Δ ≤ 4 and D ≤ 3.",
                fontsize=10,color=MUTED)
        for u, vs in adj.items():
            for v in sorted(vs):
                if u < v:
                    is_new = v >= 8
                    line(ax,positions[u],positions[v],ORANGE if is_new else "#a3abb5",
                         2 if is_new else 1.5, bend=edge_bend(u, v))
        for u,v in zip(path,path[1:]):
            is_new = max(u,v)>=8
            # Keep the same orientation as the base drawing for curved edges.
            lo,hi=sorted([u,v])
            line(ax,positions[lo],positions[hi], RED if diameter>3 else GREEN, 3,
                 bend=edge_bend(lo, hi), z=3)
        for u in adj:
            overloaded = len(adj[u])>4
            uncovered = u in before and u not in covered
            face = ORANGE if u==root else (RED if uncovered else PAPER)
            edge = RED if overloaded or uncovered else (ORANGE if u>=8 else BLUE)
            if u in state["pins"][-1] and not overloaded:
                face = BLUE
            node(ax,positions[u],str(u) if u<8 else ("x" if u==8 else "y"),face,edge,.19,11)
            if overloaded:
                ax.add_patch(Circle(positions[u],.245,fill=False,edgecolor=RED,lw=1.3,zorder=6))
                ax.text(positions[u][0],positions[u][1]-.38,"degree 5",color=RED,ha="center",fontsize=9)
        metrics = [("CURRENT VERTICES COVERED",f"{len(covered)} / {len(before)}",len(covered)==len(before)),
                   ("MAXIMUM DEGREE",f"{degree} / 4",degree<=4),
                   ("DIAMETER",f"{diameter} / 3",diameter<=3)]
        for i,(label,value,ok) in enumerate(metrics):
            y=3.15-i*.96
            panel(ax,6.6,y,3.05,.8)
            ax.text(6.78,y+.55,label,fontsize=8.5,color=MUTED)
            ax.text(6.78,y+.16,value,fontsize=18,color=GREEN if ok else RED,weight="bold")
            status=("complete" if ok else "incomplete") if i==0 else ("within limit" if ok else "over limit")
            ax.text(9.45,y+.22,status,fontsize=9,color=GREEN if ok else RED,ha="right")
        names=lambda u: str(u) if u<8 else ("x" if u==8 else "y")
        ax.text(.15,.47,"Highlighted shortest path:  " + " → ".join(map(names,path)),fontsize=10,color=GREEN if diameter<=3 else RED)
        ax.text(.15,.13,"Blue nodes: chosen pins.  Orange: new vertex/edges.  Red outline: exceeded degree capacity.",fontsize=9,color=MUTED)
        save(fig,state["file"])
    actual=[(r["vertices"],r["covered"],r["source_vertices"],r["max_degree"],r["diameter"]) for r in output]
    assert actual == [(9,7,8,4,4),(9,8,8,4,3),(10,9,9,5,3),(10,9,9,4,3)],actual
    (CASE/"data/construction_demo.json").write_text(json.dumps({
        "scope":"Exact small cube examples for explanation; not additional research results.",
        "source_edges":[[u,v] for u,vs in BASE.items() for v in sorted(vs) if u<v],
        "states":output},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


def draw_controller():
    fig,ax=canvas(11.6,5.3)
    ax.text(.1,4.7,"A small controller becomes a 3,840-vertex graph",fontsize=17,weight="bold")
    ax.text(.1,4.35,"The F₄ construction: 60 controller states, 64 coordinate points in each layer.",fontsize=10,color=MUTED)
    for x in [2.7,6.3]:
        ax.plot([x,x],[1.35,3.95],color=BORDER,lw=.8)
    ax.text(.1,3.9,"1  Choose the layer connections",fontsize=11,color=BLUE,weight="bold")
    center=(1.3,2.65)
    for i,angle in enumerate(np.linspace(0,2*np.pi,6)[:-1]+np.pi/2):
        pos=(center[0]+.9*np.cos(angle),center[1]+.85*np.sin(angle))
        line(ax,center,pos,BLUE)
        node(ax,pos,f"v{i+1}",radius=.17,size=9)
    node(ax,center,"u",face=BLUE,radius=.2)
    ax.text(1.3,1.42,"5 ports per state",ha="center",fontsize=11)

    ax.text(2.95,3.9,"2  Expand each edge into affine links",fontsize=11,color=BLUE,weight="bold")
    grids=[]
    for start in [3.0,4.95]:
        grid=[(start+c*.14,2.0+r*.16) for r in range(8) for c in range(8)]
        grids.append(grid)
        ax.scatter(*zip(*grid),s=13,color="#b0bdcf",zorder=2)
    source=grids[0][4*8+5]
    targets=[grids[1][r*8+2] for r in [1,3,5,7]]
    for target in targets:
        line(ax,source,target,ORANGE,1.1,arrow=True)
        ax.scatter(*target,s=28,color=ORANGE,zorder=4)
    ax.scatter(*source,s=40,color=BLUE,zorder=4)
    ax.text(source[0]-.14,source[1]+.17,"x",color=BLUE,fontsize=11)
    ax.text(3.5,1.65,"Layer u: 64 points",ha="center",fontsize=9)
    ax.text(5.45,1.65,"Layer v: 64 points",ha="center",fontsize=9)
    ax.text(4.45,1.3,r"$y=A_e x+\lambda b_e,\quad\lambda\in\mathbb{F}_4$",ha="center",fontsize=12)

    ax.text(6.55,3.9,"3  Make short routes cover",fontsize=11,color=BLUE,weight="bold")
    route=[(6.8,2.9),(7.65,2.9),(8.5,2.9),(9.35,2.9)]
    for i in range(3):
        line(ax,route[i],route[i+1],BLUE,1.8,arrow=True)
        ax.text((route[i][0]+route[i+1][0])/2,3.2,f"λ{i+1}",ha="center",fontsize=10,color=BLUE)
    for p,label in zip(route,["x","","","y"]):node(ax,p,label,radius=.12)
    ax.text(8.12,2.3,"3 independent directions",ha="center",fontsize=12)
    ax.text(8.12,1.92,"4 × 4 × 4 = 64 endpoints",ha="center",fontsize=12,color=ORANGE,weight="bold")
    ax.text(8.12,1.47,"Other layer pairs use complementary\nplane covers with compatible edge maps.",ha="center",fontsize=9,color=MUTED)
    panel(ax,.1,.48,9.65,.52,face="#eef1f5")
    ax.text(2.6,.68,"60 × 64 = 3,840 vertices",ha="center",fontsize=13,color=BLUE,weight="bold")
    ax.text(7.3,.68,"5 × 4 = 20 neighbors per vertex",ha="center",fontsize=12,color=ORANGE,weight="bold")
    ax.text(.1,.14,"Local schematic. Affine edge maps are chosen jointly so that the required short routes cover every layer pair.",fontsize=9,color=MUTED)
    save(fig,"construction_controller")


def draw_geometry():
    fig,ax=canvas(11,5.7)
    ax.text(.1,4.7,"One more vertex with the same number of edges",fontsize=17,weight="bold")
    ax.text(.1,4.34,"The (26,3) construction: 7,531 → 7,532 vertices; 97,750 edges in both graphs.",fontsize=10,color=MUTED)
    ax.text(2.35,3.95,"BEFORE: clone–filler links",ha="center",color=BLUE,weight="bold",fontsize=11)
    ax.text(7.45,3.95,"AFTER: 17 fillers share a new hub",ha="center",color=BLUE,weight="bold",fontsize=11)
    ax.plot([4.9,4.9],[1.1,3.7],color=BORDER,lw=.8)
    for row,label in enumerate(["1","2","17"]):
        y=3.25-row*.85
        for offset in [0,5.1]:
            c,a,f=(.7+offset,y),(2.2+offset,y+.3),(3.7+offset,y)
            line(ax,c,a,BLUE,1.6);line(ax,a,f,BLUE,1.6)
            node(ax,c,f"c{label}",radius=.17,size=9)
            node(ax,a,f"a{label}",edge=MUTED,radius=.15,size=9)
            node(ax,f,f"f{label}",face=BLUE,radius=.17,size=9)
            if offset==0:
                line(ax,c,f,RED,1.6,bend=.18,style="--")
        line(ax,(8.8,y),(9.5,2.4),ORANGE,1.8)
    node(ax,(9.5,2.4),"h",face=ORANGE,edge=ORANGE,radius=.23,size=13)
    ax.text(9.5,1.13,"new hub",ha="center",fontsize=10,color=ORANGE)
    ax.text(2.2,1.12,"Delete 17 direct c–f links",ha="center",color=RED,fontsize=11)
    ax.text(7.2,1.12,"Insert 17 f–h links",ha="center",color=ORANGE,fontsize=11)
    panel(ax,.1,.43,9.65,.43,face="#eef1f5")
    ax.text(4.92,.58,"Retain the two-step route c → a → f; keep each filler's degree unchanged.",ha="center",fontsize=11,color=BLUE)
    ax.text(.1,.13,"Three of the 17 groups are shown. Blue edges retain the two-step routes; orange edges connect the new hub.",fontsize=9,color=MUTED)
    save(fig,"construction_geometry")


if __name__=="__main__":
    ASSETS.mkdir(exist_ok=True)
    draw_cube_examples()
    draw_controller()
    draw_geometry()
    print("Rendered 6 construction figures (SVG + PNG); checked the four exact cube examples.")
