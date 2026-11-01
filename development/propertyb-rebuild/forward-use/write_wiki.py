from pathlib import Path
import subprocess,json,os,sys
ROOT=Path(__file__).resolve().parents[3]; OWNED=Path(__file__).resolve().parent
ARIS=ROOT/'base'; WIKI=OWNED/'research-wiki'
env=dict(os.environ,ARIS_REPO=str(ARIS))
notes={
 'm7': 'For finite simple 7-uniform hypergraphs with at most 130 edges, the supplied mathematical reduction and actual-profile selection connect every original putative counterexample to one of 424 exact probability profiles, whose strict values imply an original proper coloring. Author and independent runs exit 0; all 424 fractions agree. Independent probability representation uses falling-factorial injections and enumerates 2115296 common integer vectors. Maximum is 2257893910847/2257897608351. This is same-family provisional development validation of a computer-assisted candidate; no new Lean, cross-family final audit or public-record novelty check. It does not establish colorability with 131 edges: the new degree budget is 917; the two-lock domain becomes 350 rather than 337; the old 71-vertex selection guarantees only two unit locks; the tested old worst profile in both old layouts is nonstrict. See REPORT.md and SCOPE_RESULTS.json.',
 'five26': 'A pair-covering finite simple 5-uniform hypergraph with at most 33 edges has at most 25 vertices. For v>=26, every vertex has degree at least ceil((v-1)/4)>=7, so total degree is at least 182 but at most 165, contradiction. The coarse v(v-1)<=660 alone permits v=26 since 650<=660. This is a complete conditional incidence proof, also checked by exact integer arithmetic. Applying it to arbitrary original hypergraphs requires the minimum-vertex noncolorable quotient reduction; the short lemma alone is not the entire 33-edge Property B theorem. No Lean or cross-family audit is performed here. See PROOF_PACKAGE_26.md and SCOPE_RESULTS.json.'}
records=[]
def run(label,argv):
    out=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True,text=True)
    (OWNED/(label+'.stdout.log')).write_text(out.stdout)
    (OWNED/(label+'.stderr.log')).write_text(out.stderr)
    records.append(dict(label=label,argv=argv,cwd='.',ARIS_REPO=str(ARIS),exit_code=out.returncode))
    (OWNED/'WIKI_COMMANDS.json').write_text(json.dumps(records,indent=2)+'\n')
    if out.returncode:print(label,out.stderr,out.stdout);sys.exit(out.returncode)
for key,note in notes.items():
    path=OWNED/(key+'.capture-note.txt');path.write_text(note+'\n')
    run('capture-'+key,['python3','-B',str(ARIS/'tools/capture_filter.py'),str(path)])
helper=['python3','-B',str(ARIS/'tools/research_wiki.py')]
run('wiki-init',helper+['init',str(WIKI)])
run('wiki-m7-idea',helper+['upsert_idea',str(WIKI),'--slug','m7-certificate-scope','--title','Scope of the seven-uniform 130-edge certificate','--stage','piloted','--outcome','positive','--description','424-profile complete replay with an explicit original-object connection; budget 130 only.','--thesis',notes['m7'],'--risks','131-edge original theorem remains unproved here. No Lean or cross-family final audit was performed.','--tags','propertyb,scope,certificate'])
run('wiki-m7-replay',helper+['add_experiment',str(WIKI),'--slug','m7-424-replay','--title','Author and falling-factorial complete replay','--idea','m7-certificate-scope','--verdict','yes','--confidence','high','--metrics','M=130; profiles=424; groups=17+337+64+6; integer vectors=2115296; maximum=2257893910847/2257897608351; both exit0.','--reasoning',notes['m7'],'--provenance','development/propertyb-rebuild/forward-use/COMMANDS.json'])
run('wiki-m7-next-budget',helper+['add_experiment',str(WIKI),'--slug','m7-131-budget-transfer','--title','Same successful record does not establish 131-edge colorability','--idea','m7-certificate-scope','--verdict','partial','--confidence','high','--metrics','M=131; degree budget917; two profiles350 versus337; at v71 unit-lock guarantee2; old worst profile has U=2611935984095/2580454409544 and 4064403701937/4014040192624 in the two tested layouts.','--reasoning','The reusable formulas remain available, but input coverage and strictness are not preserved. This diagnostic tests only the two old layouts of one necessary local profile; it does not prove a noncolorable hypergraph or rule out all other layouts.','--provenance','development/propertyb-rebuild/forward-use/SCOPE_RESULTS.json'])
run('wiki-five-idea',helper+['upsert_idea',str(WIKI),'--slug','five26-integer-incidences','--title','Integer degrees exclude 26 vertices under pair coverage','--stage','piloted','--outcome','positive','--description','Pair-covering 5-uniform graphs with at most33 edges have v<=25 by total degree.','--thesis',notes['five26'],'--risks','The pair-covering hypothesis must come from a valid caller; this is not the full 33-edge coloring theorem.','--tags','propertyb,incidence,integer'])
run('wiki-five-proof',helper+['add_experiment',str(WIKI),'--slug','five26-incidence-proof','--title','Complete short proof and exact arithmetic','--idea','five26-integer-incidences','--verdict','yes','--confidence','high','--metrics','v26; coarse650<=660; min degree7; lower182>upper165.','--reasoning',notes['five26'],'--provenance','development/propertyb-rebuild/forward-use/PROOF_PACKAGE_26.md'])
run('wiki-stats',helper+['stats',str(WIKI)])
print('All capture and wiki helper calls exit0; records:',len(records))
