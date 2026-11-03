# Fixed v12312 residual: one direct SAT at-most-five decision

Both preceding HiGHS windows returned node0/timecap, so the new algorithmic question is direct feasibility on the SAME frozen v12312/seed11/1744-hole residual: can atmost5 of3771 distinct residual columns cover everyhole? No newv, seed, MIP, balls or sourceD4 work.

Existing executable CaDiCaL is actually present at `.tools/lean-4.24.0-linux/bin/cadical`. Invoke once with separate argv `-t`, `19`, CNF. No install/help/probe/secondrun. Native hardCPU20, parenthard24; sameC prior71.065033579+newprep0.5+allactualparent/child remainsunder120.

Realvariables x1..3771 map to actualavailablepin representatives. Eachactualhole supplies the positiveOR ofALL coveringcolumns, including anemptyclause ifeverempty. Auxiliarys(i,j)=3771+(i-1)*5+j means prefix>=j. Include x_i=>s_i1, prevs_j=>s_ij, x_i&prevs_(j-1)=>s_ij, overflow not(x_i&prevs5), and firstprefixj>1=false. This existential encoding isexactatmost5, notanMIPwarmassignmentconstraint.

SAT is only a rawdecision until allrealvariables aredecoded, actualselected<=5, allpins eligible, seed+extras<=16 and cachedcurrent-R3 wholeunion=16416. Onlythen generatepreserved129240-oldedge16417graph, degrees/PIN_SET/newrootroutes and stopforfreshacceptance. RawUNSATwithoutlogged/checkedproof isnotstrict mathematicalfamilyNO. Timeout/parsefailureisUNKNOWN, no secondSAT/solver/refreeze. Goal/countersnotcompletedbythismodel.
