# Reproduce only this frozen I32 graph

From the repository root:

    python research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/produce.py

Inputs:controller_pack32_gate/SELECTED_BLOCKS.json andtheoriginalmore_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt. The scriptparses thesourceonce andcopiesactualoldfullN;itdoesnotruntheMIP,sourcegenerator,fieldchecks orBFS.

Output:graph_d16_D4_n16416.edges hasan n/m header andstrictlexsorteda<b pairs;PARAMETERS.json recordsactualn,m,I32,targetsets,offsets/centers/labels. ALL864_ROLE_BINDINGS.tsv givesoneorderedj/sourcecenter/newlabel/source-degree/frozen-full-N rowperclone. RESULT/TERMINAL recordactualdegrees,oldpinloads andcounts. No extra prefixgraphs aregenerated. Existingcompletefiles/receipts should beinspectedwithoutre-runningproduction.
