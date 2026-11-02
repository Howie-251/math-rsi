"""Select one exhaustive graph-semantic split for an n=62 cube."""

from n62_semantic_decisions import (
    assignments,
    exact_one_decision,
    signature_decision,
    touched_vertices,
)


def coverage_decision(model, values, touched):
    candidates = []
    for vertex in range(model.l_size):
        for parent, fiber in enumerate(model.fibers):
            if parent in model.parents[vertex]:
                continue
            variables = [
                model.instance.edge_var(vertex, other)
                for other in fiber if other != vertex
            ]
            if any(values.get(var) is True for var in variables):
                continue
            open_vars = [var for var in variables if var not in values]
            if open_vars:
                candidates.append((len(open_vars), vertex not in touched,
                                   vertex, parent, open_vars))
    if not candidates:
        return None
    _, _, vertex, parent, variables = min(candidates)
    cases = [
        [-value for value in variables[:index]] + [variable]
        for index, variable in enumerate(variables)
    ]
    return {"kind": "coverage_first_witness", "vertex": vertex,
            "fiber": parent, "variables": variables, "cases": cases}


def choose_decision(model, literals):
    values = assignments(literals)
    touched = touched_vertices(model, values)
    return (exact_one_decision(model, values, touched)
            or signature_decision(model, values, touched)
            or coverage_decision(model, values, touched))


def validate_decision(decision):
    variables = decision["variables"]
    cases = decision["cases"]
    matched = []
    for bits in range(1 << len(variables)):
        values = {var: bool(bits & (1 << index)) for index, var in enumerate(variables)}
        allowed = True
        if decision["kind"] == "matching_exact_one":
            allowed = sum(values.values()) == 1
        elif decision["kind"] == "coverage_first_witness":
            allowed = any(values.values())
        count = sum(all(values[abs(lit)] == (lit > 0) for lit in case) for case in cases)
        if count != (1 if allowed else 0):
            raise AssertionError("semantic cases are not an exact partition")
        matched.append(count)
    return len(matched)
