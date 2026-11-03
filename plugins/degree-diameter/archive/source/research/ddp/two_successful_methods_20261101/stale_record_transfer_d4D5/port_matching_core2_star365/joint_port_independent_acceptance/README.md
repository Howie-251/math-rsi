# Conditional independent acceptance — no current data run

This draft is only for a real root-produced365/730 candidate with fixedcuts(43,58),(151,314),14portmatchingedges and star364to{43,58,151,314}. Do not run on the oldfailedsample or acceptedsource for testing. Execution needs root's actualcandidate and separatefreshbudget.

It reads source364literal once and candidate once; compares exactedge delta, all4degrees/simple/header, actual28portperfectmatching and fixedstar. It then runs ordinaryBFS on the actualcandidate: root364 followed by all364oldlabels. A completepass covers all133225orderedpairs and saves an actualdistance5witness. It uses no producer masks/allowedgraph/model, and performs0sourceD5/BFS or geometryvalidation.

From repositoryroot, only after authorization:

    python research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365/joint_port_independent_acceptance/verify_candidate.py --source research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/source364.edges --candidate ACTUAL365.edges --out FRESH_OUT --cpu-budget BUDGET

Current state: syntaxAST parsed only; source/candidate parses0, BFS0, no candidatePASS. Result/terminal files will be created only by a later actualrun, not by this preparation.

Root actual fixedP result is HallNO (24hard owners, neighborunion1); no candidate exists. This draft is unused and must not be exercised on oldfailedsample/source.
