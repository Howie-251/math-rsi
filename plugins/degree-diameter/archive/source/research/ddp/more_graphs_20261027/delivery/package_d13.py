"""Refresh the expert archive after root's live HTML and review disposition are ready."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,json,shutil,subprocess,zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--review-disposition',type=Path,required=True)
    args=parser.parse_args()
    review=args.review_disposition.resolve()
    assert review.exists()
    data=json.loads((HERE/'families.json').read_text())
    assert data['parameter_cells']==3 and data['reviewed_example_count']==38
    subprocess.run(['python',str(HERE/'write_d13_docs.py'),'--review-disposition',str(review)],check=True)
    expert=ROOT/'expert_review_current'
    live=ROOT/'research/progress.html'
    html=live.read_text()
    assert str(data['families']['13']['strongest_n'])in html and str(data['distinct_explicit_examples'])in html
    shutil.copy2(live,expert/'MORE_GRAPHS_20261027.html')
    shutil.copy2(live,expert/'MORE_GRAPHS_20261027.html.txt')
    archive=expert/'MORE_GRAPHS_20261027.zip'
    with zipfile.ZipFile(archive) as previous:
        paths={ROOT/name for name in previous.namelist()if not name.endswith('/')}
    study=HERE.parent/'d13_D5_h9_transfer'
    probe=study/'singlefault_star_probe'
    essential=[review,HERE/'README.md',HERE/'families.json',HERE/'family_generator.py',
               HERE/'dry_run_d13_51418.json',HERE.parent/'FINAL_RESULTS_PROOF.md',
               probe/'first_hit.json',probe/'independent_newroot51418.json',
               probe/'accepted_family40.json',probe/'graph_d13_D5_n51418.edges',
               probe/'continuation/accepted_sequence.json',probe/'continuation/terminal.json',
               ROOT/data['families']['13']['steps'][-1]['graph_file'],
               expert/'MORE_GRAPHS_20261027.html',expert/'MORE_GRAPHS_20261027.html.txt']
    for family in data['families'].values():
        essential.append(ROOT/family['base']['project_file'])
    for step in data['families']['13']['steps']:
        essential.append(ROOT/step['native_R4_evidence'])
    ledger_path=ROOT/'research-wiki/DDP_METHOD_LEDGER.json'
    ledger=json.loads(ledger_path.read_text())
    essential.extend([
        ROOT/'research/progress.html',
        ROOT/'research-wiki/DDP_METHOD_LEDGER.md',
        ledger_path,
        ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',
        ROOT/'context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md',
        ROOT/'RESEARCH_BRIEF.md',
    ])
    assert len(ledger['rows'])==ledger['record_count']
    for row in ledger['rows']:
        node=ROOT/row['wiki_path']
        assert node.suffix=='.md'
        essential.append(node)
    assert all(path.exists()for path in essential)
    paths.update(essential)
    review_stem=review.name.removesuffix('.disposition.json')
    for suffix in ['.raw.json','.meta.json','.response.md','.prompt.txt','.request.json','.DISPOSITION.md']:
        sibling=review.with_name(review_stem+suffix)
        if sibling.exists():paths.add(sibling)
    for path in [study/'SOURCE_FACTS.json',study/'source51417.edges',study/'degree13.u8.bin']:
        if path.exists():paths.add(path)
    for directory in [HERE,probe,probe/'continuation']:
        for path in directory.iterdir():
            if path.is_file()and path.suffix in ['.py','.cpp','.md','.json']:
                paths.add(path)
    # Keep the three strongest complete graphs in addition to the portable generator.
    paths.update([HERE.parent/'h9_d11_followups/graph_d11_D5_n37631.edges',
                  HERE.parent/'h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges'])
    paths.discard(HERE/'D13_DELIVERY_STATUS.json')
    temporary=expert/'MORE_GRAPHS_20261027.next.zip'
    count=0
    with zipfile.ZipFile(temporary,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as output:
        for path in sorted(paths):
            if path.is_file():
                output.write(path,str(path.relative_to(ROOT)));count+=1
    temporary.replace(archive)
    downloads=Path('/mnt/data');downloads.mkdir(exist_ok=True)
    for suffix in ['html','html.txt','zip']:
        shutil.copy2(expert/f'MORE_GRAPHS_20261027.{suffix}',downloads/f'AR4MATH_MORE_GRAPHS.{suffix}')
    status=json.loads((HERE/'D13_DELIVERY_STATUS.json').read_text())
    status.update(status='D13_FAMILY_EXPERT_ARCHIVE_UPDATED',ZIP_rebuilt=True,
                  archive=str(archive.relative_to(ROOT)),archive_bytes=archive.stat().st_size,
                  files_in_archive=count,review_disposition=str(review.relative_to(ROOT)),
                  updated_UTC=datetime.now(timezone.utc).isoformat(),BFS_performed=False)
    (HERE/'D13_DELIVERY_STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
    print(json.dumps(status,indent=2))

if __name__=='__main__':
    main()
