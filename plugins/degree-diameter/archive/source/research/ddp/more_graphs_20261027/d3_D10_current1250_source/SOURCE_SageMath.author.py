# SageMathCell online  https://sagecell.sagemath.org/?q=hsebti
#  (3,10) = 1250; Moore bound=3070;
#  Ord.: 1250 / Size: 1875 / Diam.: 10 / Avg.dist: 7.98959 / Degree histogram: [0, 0, 0, 1250]  / Girth: 16
#  | Aut.group.ord.: 15000 /  Cayley ? False ---  vtx.trans. ? True -- edge.trans. ? True
#  Communicated by Marston Conder ( m.conder@auckland.ac.nz ) on August 17, 2006. 
#  http://www.math.auckland.ac.nz/~conder/symmcubic2048list.txt
#  Marston Conder, Jicheng Ma. Arc-transitive abelian regular covers of cubic graphs. J. Algebra, 387 (2013) 215-242.


import networkx as nx

conder=Graph(r":~?Ra_?_?_?_@_@_A_A_B_B_C_C_D_D_E_E_F_F_G_G_H_H_I_I_J_J_K_K_L_L_M_M_N_N_O_O_P_P_Q_Q_R_R_S_S_T_T_U_U_V_V_W_W_X_X_Y_Y_Z_Z_[_[_\_\_]_]_^_^_____`_`_e_e_f_f_g_g_h_h_a_a_b_b_c_c_d_d_i_i_j_j_k_k_l_l_m_m_n_n_o_o_p_p_u_u_v_v_w_w_x_x_q_q_r_r_s_s_t_t_y_y_z_z_{_{_|_|_}_}_~_~`?`?`@`@`E`E`F`F`G`G`H`H`M`M`N`N`O`O`P`P`U`U`V`V`W`W`X`X`A`A`B`B`C`C`D`D`I`I`J`J`K`K`L`L`Q`Q`R`R`S`S`T`T`Y`Y`Z`Z`[`[`\`\`]`]`^`^`_`_`````e`e`f`f`g`g`h`h`m`m`n`n`o`o`p`p`u`u`v`v`w`w`x`x`a`a`b`b`c`c`d`d`i`i`j`j`k`k`l`l`q`q`r`r`s`s`t`t`y`y`z`z`{`{`|`|`}`}`~`~a?a?a@a@aEaEaFaFaGaGaHaHaMaMaNaNaOaOaPaPaUaUaVaVaWaWaXaXa]a]a^a^a_a_a`a`aeaeafafagagahahamamananaoaoapapauauavavawawaxaxaAaAaBaBaCaCaDaDaIaIaJaJaKaKaLaLaQaQaRaRaSaSaTaTaYaYaZaZa[a[a\a\aaaaababacacadadaiaiajajakakalalaqaqararasasatatayayazaza{a{a|a|a}a}a~a~b?b?Cdb@CTb@bEbEbFDTbFDLbGbGbHbHbMbMDcbNbNbObObPbPCCbUbUDkbVbVbWbWCcbXbXb]b]b^b^b_b_b`CZb`CBbeDrbebfbfDBbgbgbhbhbmDqbmbnbnboCybobpbpbububvDQbvbwCqbwbxbxbAbAbBbBDHbCbCChbDbDbIbIbJbJD@bKbKbLbLCHbQbQbRbRbSCwbSbTbTCGbYDwbYD_bZbZb[b[b\b\bababbDVbbbcbcbdCNbdbiDvbibjbjbkbkblCVblbqbqbrbrbsCmbsCebtbtbybyDebzDUbzb{b{b|b|b}EqFgb}FZb~E{b~c?Fxc?Clc@C\c@cEFVcEcFcFcGcHEbcMEgcMcND\cOcOcPcPFPcUcUcVDDFOcWcWFbcXcXc]EQc]Dkc^c^c_c_F|c`cKC`ceG]cfcfElcgEMcgchcmcncncockCocpcpcucuDcEjcvFocvcwcxcxc}c}c~F{c~d?d?EDcJD@dEFEdEdFdFdGdGGDcRDHF|dMDzdMFSdNGRdJDNdOFmdOEVFDdPdPEPdUdVEEdWdWFqdXdXG\d]Dyd]d^d^d_d`d`dedfdfcqDgD}dgdhdhF\dmFOdmdYDndncyDodoEvdpGGdpduduEzdvdwH`dxE?dxcAcAFzcBcCcDF?cDHNcIcIcJFCcKcLHocLEjcQE]cQcRcScScTcYGucYcZc[c[c\cacacbEHHgcbGXccFtcdHKciFicicjEuFccjELckclEfcrcrcscsGFctctEtczFuczc{c{D~c|c|HWdAdAdBdCdCEJdDdIdIdJdKdKGOdLdQdRGEdRFldSFMdSdTdYdZD}dZInd[IEd[d\FhdaHMdadbEWdbddddIOdiEididjGhdjdldlFRdqFWdrGIdsdsHtdtG~dtEcGedyIQdzEAd{d{E~d|E_d|ERFHd~e?Ele@E\e@eEeFeFeGGueMeNF\eOeOIJePeUeUeWeXGjeXIqe]Fke^e^e_Iue`GmeKE`eeJbefImegIIehemenenH]eoGWekEoepepG_euevI@ewexGsexe}GIe}e~f?eJF@fEfFH`fFIDfGfGJPfMFzfNJZfJFNfPfUI}fWfXfXJaf]Fyf]ISf^Hvf^f_f`I`f`feffffH|fgfhGifmG~fYFnfnICeyFofpJRfpfuGJfvfwKSfxHleAHmeBeCeDJAeIeIeKHSeLITK^eQIfeReSHZeSeTeYJueYGqeZe[e[Hbe\H?eaeaebJ^edGOKCeiekereresHResHwJQeteze{e|e|JBKMfAfAI^fBfCHVfDfIIofIfJIvfKHzfKJXfLfQfRHLfSGbfTfYIcfZGXLMf[Kpf[faG]KDfaIefbfdfdKufifjHKJjfjflfrI\JTfsfsKbftJ{fyKvf{f~g?HJg@Gmg@gFgGHPgHGtgHgKLBgLgLgMG|JVgRgSgSgYgZIVJ_g[LNg[IPg\gagbKHgcJ`ggggghgiGrgngngpgqIkgvJYKOgvgwI{gtGxLYgPGxg}Ltg}gWH?hCMBhDIshEIOhFhQhRJfhIHSgfHThThVHXhXMIgPHYJvhOHYhZh_hahbKXhghhHzglHihihmJlhnKXhogAHshsKchthugVG{KVhyh{h{Ldi?h~I@iAiALhiEJDiFLxh}IFiHiKJJiLL|iCILiNiQiRiRMAhcIwJyiWKeiXiXMFi]JCiYI]JWi^i_Ifi_icJIhpIdidieK\iBIiiiMEijioJ`ipiSIvixLjixM\MbiYI|h}I|K}i~Lni~JtJwgDJGhfJHN?gBgCgNK|L?gNgQIZNRgUgUg^g_LQg`gdI`MtgegfgjK]gkglgrM`gsgygygzKRh@h@hAM?hGhIhMhOhUhUhWh\h\h]HqLmh^hdheNWhfKUhjhkKahlLFhpNWhrhvKahxh|h~LsiBiDLLiUNdiUN^i[Ngi[KhLWiaibibNkigihihNmilLQimKoinirODisJcitiyiyNUizMZj?j?NXj@JqjCNnjEjINqjKjMJojMNFjQNqO?jRKFNRjSJtjSN]jUOOjUMfjZNBNfj[M_j[jaN?jeNgOWjiMPjijjNJjkJrM~jpMojpNejvjYJwN[jzOhjzNpj]J|N[k?MlMpk@KuNPkAkGkBKIjhKJkJLxNikLKNMQkNNvOMkEKOkPOZkTNINLkYMmNkjnKZkZk^LnMzkbO@kfLkkfOZO^kjOCkiKkMiklklNaObkpL]MHkqMYOjkhKqkrL|M}ktN|OnknKtkvLiOAkwkwOOOpk{OHk{M_Osl?L\l@MolALGL{lALtM^lDL`k_LElELmNnkmLJlJOrlKLdOYkxLSMWlTLzOclTPCPEk|LWMWlYOfjPL_MJjNLbLfjOjWj\j\OJjdMDMGjgLhO[jhjmjnMkOUjrNyOPjsNljxNxjxL}j}Luj}j~MPOXkBMYkDNcOIkEN|kKNBkKkMMFkQLekQOVkWMRPjk[NdOTk_Pjk`MqNmkgLekiLwMbkmMtOLkzMhPskzPnk}PulCMylCNlPxlHNXlIlIOAPzlMLjMvlPNbQHlUlUNxPilVMxNalZNrlZLuPkl\NFP{l^MUMgl`N]P~laNHlaMOQQlkMXloNYP^loM\PWlpMjlpORlyMclyP[l}OxP?mANCmLMUOomLOxmMNNmVMsmVNhPBm]QImaQTmeNtmePJQcmhP}mnPSP_mrPJm{OgPCmKM}Q?n@OkQamsNAPSnDO\OgmuNEPNmyNGnUOBnYO\QYn_OEn`NcPFn`OwQmnZNeQvn^NhO~m[NjPvnjN~QgnoORQinoOyQonrOwPXmcNuQknuOKn{OSOan}OVQ[nSO?QJl~OGQ_oGOkQwoJQLQeoNPiQ`oQPtlcQMlgQBQQlrPURLlvPeRDlzOll~QMQfmKPomNP|mTPnPvmfPoPrmjPQRTmuN~P\nHOSOznSPhRQnpPHRSntP|QynwOdQjnzOpQ^oHPhQDoKO]RM~~~~~~")
         
condernx =conder.networkx_graph()

# List of graphs to process
graphs = [('Conder   ', conder )]


def count_k_cycles(G, k):
    count = 0
    visited = set()
    def dfs(path, start, depth):
        nonlocal count
        current = path[-1]
        # Early exit if we?re going too deep
        if depth == k:
            if start in G.neighbors(current):
                # Normalize to avoid duplicates
                cycle = tuple(sorted(path))
                if cycle not in visited:
                    visited.add(cycle)
                    count += 1
            return
        for neighbor in G.neighbors(current):
            if neighbor not in path and neighbor >= start:
                dfs(path + [neighbor], start, depth + 1)
    for v in G.vertices():
        dfs([v], v, 1)
    return count   # each cycle counted twice (once forward, once reverse)

def algebraic_connectivity(G):
    """
    Compute the algebraic connectivity (Fiedler value) of a graph G.
    INPUT:
        - G: a SageMath Graph
    OUTPUT:
        - The second-smallest eigenvalue of the Laplacian matrix of G
    """
    L = G.laplacian_matrix()
    eigenvalues = L.eigenvalues()
    eigenvalues.sort()
    
    if len(eigenvalues) < 2:
        return 0  # Trivial case: empty or isolated vertex graph
    return eigenvalues[1]


def domination_number(G):
    """
    Compute the domination number of a graph G using MILP.
    INPUT:
        - G: a SageMath Graph
    OUTPUT:
        - The domination number (integer)
    """
    p = MixedIntegerLinearProgram(maximization=False)
    x = p.new_variable(binary=True)   
    # Objective: minimize the number of chosen vertices
    p.set_objective(sum(x[v] for v in G.vertices()))
    # Constraint: each vertex is dominated
    for v in G.vertices():
        p.add_constraint(x[v] + sum(x[u] for u in G.neighbors(v)) >= 1)
    return p.solve()


# Print properties for each graph in the list
print("\n Main properties of the graph\n")
for label, graph in graphs:
    print(f"{label} | Ord.: {graph.order()} / Size: {graph.size()}  "
          f" / Diam.: {graph.diameter()} / Avg.dist: {graph.average_distance().n(digits=6)} \n"
          f" / 3-reg.? {graph.is_regular(k=3)} / Degree histogram: {nx.degree_histogram(condernx)}  / Girth: {graph.girth()}\n ")
          #f" /  Alg.conn. {algebraic_connectivity(graph).n(digits=6)}") # /  Domin. number: {domination_number(graph)} ")

print("\n Symmetry properties of the graph\n")
for label, graph in graphs:
    print(f"{label} | Aut.group.ord.: {graph.automorphism_group().order()} /  Cayley ? {graph.is_cayley()} ---  vtx.trans. ? {graph.is_vertex_transitive()} -- edge.trans. ? {graph.is_edge_transitive()}" )


# Compute the distance distribution from a given vertex v in graph G
# Returns a list where the i-th element is the number of vertices at distance i from v
def distance_distribution(G, v):
    from collections import Counter    
    distances = G.shortest_path_lengths(v)
    distribution = Counter(distances.values())
    result = [distribution[d] for d in sorted(distribution)]    
    return result

print("\n")
for label, graph in graphs:
    print(f"{label} distance distrib from vtx. 0: {distance_distribution(graph, 0)}")

    
# Counting k-cycles for each graph
print("\nNumber of k-cycles for k=3 up to 7")
for label, graph in graphs:
    print(f"{label} ", " ".join(str(count_k_cycles(graph, k)) for k in range(3, 8)))

print("\n")
