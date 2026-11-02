#!/usr/bin/env python3
"""Integrated exact audit for the theorem Q2 <= 8 in active N59 c1 branches.

The script imports two local, standard-library-only finite audits.  It does
not call a SAT/SMT/MILP solver and does not generate a 59-vertex graph.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

BASE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, BASE / filename)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def m0_high_macros(hq):
    out = []
    for part in hq.M0_PARTS:
        for (q, key), (adj, sigma) in hq.enumerate_m0_support(part).items():
            if q >= 9 and hq.parent_assignment_exists_m0(part, adj, sigma):
                out.append((part, q, key))
    return out


def m1_high_macros(hq):
    out = []
    for part in hq.M1_PARTS:
        for (q, key), (adj, sigma) in hq.enumerate_m1_support(part).items():
            if q >= 9 and hq.parent_assignment_exists_m1(part, adj, sigma):
                out.append((part, q, key, adj))
    return out


def fibre_charge_rejects(part, adj):
    k = len(part)
    for i, e in enumerate(part):
        f_neighbours = [j for j in range(k) if j + 2 in adj[i + 2]]
        if len(f_neighbours) == k - 1:
            weighted_degree = sum(part[j] for j in f_neighbours)
            if 2 * e + weighted_degree > 5:
                return True
    return False


def clean_endpoint_has_survivor(ce):
    for K in ce.k_matrices():
        for N in ce.n_matrices(K):
            # Every enumerated pair is rejected by one branch of the exact
            # endpoint proof.  A missing reason would be a proof-interface bug.
            reason = ce.rejection_reason(K, N)
            if not reason:
                return True
    return False


def main():
    hq = load("n59_hq", "n59_high_q_support_audit_20260903.py")
    ce = load("n59_ce", "n59_m0_q9_clean_endpoint_audit_20260903.py")

    m0 = m0_high_macros(hq)
    m1 = m1_high_macros(hq)

    assert {q for _, q, _ in m0} == {9}
    assert len(m0) == 3
    assert all(part[0] == 3 for part, _, _ in m0)

    assert m1
    assert all(q in {9, 10} for _, q, _, _ in m1)
    assert all(fibre_charge_rejects(part, adj) for part, _, _, adj in m1)

    assert not clean_endpoint_has_survivor(ce)

    print("N59 Q2<=8 INTEGRATED THEOREM AUDIT")
    print(f"m=1 high macros rejected by fibre charge: {len(m1)}")
    print(f"m=0 Q2=9 macros reduced to the common heavy-pair transport: {len(m0)}")
    print("m=0 final 4x4 clean-endpoint transport survivors: 0")
    print("THEOREM INTERFACE AUDIT PASS")
    print("Conclusion audited: active c1 m=0/m=1 candidates satisfy Q2<=8.")


if __name__ == "__main__":
    main()
