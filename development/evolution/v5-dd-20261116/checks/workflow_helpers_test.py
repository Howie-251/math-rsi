"""Software-only regression; optional --archive tests original receipt JSON shape."""
import argparse, copy, importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'base/tools'))
import current_context as context

def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'plugins/degree-diameter/tools'/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
batch=load('d5_blocking_batch');receipts=load('extension_receipts');ARCHIVE=None

def fixture():
    f=dict(degree=12,diameter=5,phase_start_order=10,accepted_orders=[],latest_graph=dict(n=10,m=20,edge_file='source.edges',evidence={'accepted':'proof'}))
    c=dict(families={'12,5':f},route_stops={'old':'retain'},concrete_Lean_count=0)
    a=dict(running=False,source_n=10,accepted_new_graphs=1,final_n=11,final_m=21,final_edgefile='final.edges',status='BATCH_LIMIT_REACHED')
    i=dict(status='PASS',construction_inputs={'source_raw_edge_file':'source.edges'},source=dict(n=10,m=20,previously_independently_accepted_diameter_upper_bound=5),prefixes=[dict(status='PASS',n=11,m=21,simple=True,maximum_degree=12,all_vertex_degrees_checked=11,retained_previous_edge_count=20,removed_edge_count=0,other_added_edge_count=0,new_vertex=10,added_edge_count=1,prior_prefix_diameter_upper_bound=5,diameter_upper_bound=5,bfs_in_this_prefix=dict(root=10,graph_order_at_bfs=11,visited_count=11,unreachable_count=0,maximum_distance=5))],independently_accepted_prefix_count=1,final_graph=dict(n=11,m=21,simple=True,maximum_degree=12,diameter_upper_bound=5),author_final_graph_comparison=dict(status='MATCH',path='final.edges',author_n=11,author_m=21,missing_edge_count=0,extra_edge_count=0))
    return c,a,i

class Helpers(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='mathrsi-software-');self.addCleanup(self.tmp.cleanup);self.work=Path(self.tmp.name)
    def consume(self,c,a,i,evidence=None):
        return receipts.consume(c,a,i,family_key='12,5',evidence=evidence or {'author':'a','independent':'i'},acceptance_basis='Parent accepted original source and independent receipt',state_dir=self.work)
    def test_generic_state_and_relative_review(self):
        s={'status':'PAUSED','current_context':{'obligation':'arbitrary mathematics'}}
        (self.work/'review.txt').write_text('original review')
        req=dict(review_mode='reuse',prior_reviews=[{'path':'review.txt','scope':'lemma'}],reuse_scope='unchanged')
        text=context.request_text(s,req,state_dir=self.work)
        self.assertIn('arbitrary mathematics',text)
        self.assertIn(f'the STATE directory: {self.work.resolve()}',text)
        (self.work/'STATE.json').write_text(json.dumps({**s,'current_context_view':'CURRENT.txt'}))
        context.write_current(self.work/'STATE.json',s['current_context'])
        self.assertIn('PAUSED',(self.work/'CURRENT.txt').read_text());self.assertNotIn('families',context.snapshot(s))
    def test_source_counts_path_and_evidence(self):
        for field,value in [('m',1),('n',9)]:
            c,a,i=fixture();i['source'][field]=value
            with self.assertRaises(ValueError):self.consume(c,a,i)
        c,a,i=fixture();i['construction_inputs']['source_raw_edge_file']='other.edges'
        with self.assertRaisesRegex(ValueError,'source edge file'):self.consume(c,a,i)
        c,a,i=fixture();del c['families']['12,5']['latest_graph']['evidence']
        with self.assertRaisesRegex(ValueError,'needs evidence'):self.consume(c,a,i)
    def test_replay_preserves_later_stop(self):
        c,a,i=fixture();result=self.consume(c,a,i)
        self.assertEqual(set(result['families']['12,5']['accepted_checkpoints']),{'10','11'})
        za=copy.deepcopy(a);za.update(source_n=11,accepted_new_graphs=0,status='UNKNOWN_WHOLE_CPU_LIMIT')
        zi=copy.deepcopy(i);zi.update(source=dict(n=11,m=21,previously_independently_accepted_diameter_upper_bound=5),prefixes=[],independently_accepted_prefix_count=0)
        zi['construction_inputs']['source_raw_edge_file']='final.edges'
        result=self.consume(result,za,zi,{'author':'later','independent':'later-i'})
        stop=copy.deepcopy(result['families']['12,5']['last_batch']);replay=self.consume(result,a,i)
        self.assertEqual(replay['families']['12,5']['last_batch'],stop)
        self.assertEqual(replay['families']['12,5']['accepted_orders'],[11]);self.assertEqual(replay['route_stops'],{'old':'retain'})
    def test_relative_source_paused_terminal_and_stale_guards(self):
        c,_,_=fixture();f=c['families']['12,5'];f.update(generator_domain='d12_754_planes_core41356',accepted_orders=[10])
        state={'status':'PAUSED','current_context':c};p=self.work/'STATE.json'
        (self.work/'source.edges').write_text('10 20\n');(self.work/'planes.txt').write_text('754\n');p.write_text(json.dumps(state))
        plan=batch.build_plan(p,self.work/'planes.txt',self.work/'out',1,2,3)
        self.assertEqual(plan['source'],str((self.work/'source.edges').resolve()))
        with self.assertRaisesRegex(ValueError,'not ACTIVE'):batch.execute(plan)
        state['status']='ACTIVE';c['current_work']={'in_flight':{'job':{'terminal_result':'RESULT.json'}}}
        (self.work/'RESULT.json').write_text('{}');p.write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError,'must be consumed'):batch.execute(plan)
        with self.assertRaisesRegex(ValueError,'must be consumed'):context.request_text(state,{'review_mode':'task'},state_dir=self.work)
        c['current_work']['in_flight']={};f['latest_graph']['n']=11;p.write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError,'no longer the latest'):batch.execute(plan)
        self.assertFalse((self.work/'out').exists())
    def test_optional_dd_summary(self):
        c,a,i=fixture();c['phase_start_counts']={'versions':163,'parameters':44};c['families']['12,5']['parameter_previously_known']=True
        self.assertEqual(self.consume(c,a,i)['result_counts'],dict(new_versions=1,new_parameters=0,total_versions=164,total_parameters=44,concrete_Lean=0))
    def test_actual_receipt_shape(self):
        if ARCHIVE is None:self.skipTest('supply --archive for original receipt compatibility')
        parent=ARCHIVE/'originals/ar4math/research/ddp/expert15_20261114/d5_resume_20261115/resume_workflow_20261115/d12_batch01'
        for name,path in [('a',parent/'RESULT.json'),('i',parent/'independent/RESULT.json')]:
            (self.work/(name+'.json')).write_text(path.read_text())
        a=json.loads((self.work/'a.json').read_text());i=json.loads((self.work/'i.json').read_text());c,_,_=fixture();s=i['source']
        c['families']['12,5'].update(phase_start_order=s['n'],accepted_orders=[],latest_graph=dict(n=s['n'],m=s['m'],edge_file=i['construction_inputs']['source_raw_edge_file'],evidence={'original':'accepted source'}))
        self.assertEqual(self.consume(c,a,i)['families']['12,5']['accepted_orders'],list(range(42412,42420)))
    def test_cpp_compile_and_toy_control(self):
        binary=self.work/'control'
        subprocess.run(['g++','-O2','-std=c++17',str(ROOT/'plugins/degree-diameter/tools/d5_blocking_batch.cpp'),'-o',str(binary)],check=True,capture_output=True,text=True)
        r=subprocess.run([str(binary),'--control'],check=True,capture_output=True,text=True)
        self.assertIn('STOP_REASON_CONTROL_PASS',r.stdout);self.assertIn('CONTROL_PASS',r.stdout)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--archive',type=Path);p.add_argument('--result',type=Path);args=p.parse_args();ARCHIVE=args.archive
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Helpers))
    if args.result:args.result.write_text(json.dumps(dict(tests_run=result.testsRun,failures=len(result.failures),errors=len(result.errors),skipped=len(result.skipped),success=result.wasSuccessful(),actual_archive_receipt_test=ARCHIVE is not None,scope='software mocks, original receipt JSON compatibility, C++ compile and toy control; no graph search/BFS/Lean or live state writes'),indent=2)+'\n')
    raise SystemExit(not result.wasSuccessful())
