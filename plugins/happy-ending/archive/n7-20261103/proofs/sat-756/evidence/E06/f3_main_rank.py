"""Exact occupied-state rank pruning, preserving the measured F3-main CNF.

An occupied proper subset of H_v precedes v, and a proper superset follows v.
Their type counts are bounded by v-1 and N-v. Exact prefix thresholds provide
one canonical auxiliary lift of every old assignment; no research imports or
C_r theorem assumption are used here.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from lib.downset_state import STATE_756_SPEC
from lib.downset_state_cnf import DownsetStateEncoding
from state_charging.obligations import stable_sha256

F3_MAIN_SCHEMA = "state_charging_f3_main_rank_v1"


def _integer(value: Any, label: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{label} must be a plain integer >= {minimum}")
    return value


def _input(value: Any, top: int) -> int:
    if type(value) is not int or value == 0 or abs(value) > top:
        raise ValueError("F3 input must be an existing nonzero literal")
    return value


@dataclass(frozen=True)
class RankInequality:
    inputs: tuple[int, ...]
    bound: int
    guards: tuple[int, ...]
    component: str

    def to_dict(self) -> dict[str, Any]:
        return dict(inputs=list(self.inputs), bound=self.bound,
                    guards=list(self.guards), component=self.component, sense="atmost")


@dataclass(frozen=True)
class PrefixCounter:
    inputs: tuple[int, ...]
    ledger: tuple[tuple[int, int, int], ...]

    def to_dict(self) -> dict[str, Any]:
        return dict(inputs=list(self.inputs), ledger=[list(x) for x in self.ledger])


@dataclass(frozen=True)
class F3MainEncoding:
    base_num_vars: int
    num_vars: int
    clauses: tuple[tuple[int, ...], ...]
    components: tuple[tuple[str, int], ...]
    counters: tuple[PrefixCounter, ...]
    inequalities: tuple[RankInequality, ...]

    def auxiliary_variables(self) -> tuple[dict[str, Any], ...]:
        return tuple(dict(literal=z, role="f3_exact_prefix_threshold",
                          name=f"f3_prefix({index},{i},{k})", counter=index,
                          prefix_length=i, threshold=k)
                     for index, counter in enumerate(self.counters)
                     for z, i, k in counter.ledger)

    def lift(self, old_values: Mapping[int, bool]) -> dict[int, bool]:
        values = dict(old_values)
        for counter in self.counters:
            counts = [0]
            for literal in counter.inputs:
                value = values[abs(literal)]
                if type(value) is not bool:
                    raise ValueError("F3 lift requires Boolean old values")
                counts.append(counts[-1] + int(value == (literal > 0)))
            for z, i, k in counter.ledger:
                values[z] = counts[i] >= k
        return values

    def to_dict(self, *, include_clauses: bool = False) -> dict[str, Any]:
        auxiliary = list(self.auxiliary_variables())
        counters = [x.to_dict() for x in self.counters]
        inequalities = [x.to_dict() for x in self.inequalities]
        result = dict(schema=F3_MAIN_SCHEMA,
                      predicate="guarded_occupied_proper_subset_superset_ranks",
                      canonical_extension="exact_prefix_threshold_iff_v1",
                      base_num_vars=self.base_num_vars, num_vars=self.num_vars,
                      auxiliary_variable_count=self.num_vars - self.base_num_vars,
                      auxiliary_variables=auxiliary,
                      auxiliary_variables_sha256=stable_sha256(auxiliary),
                      counter_count=len(counters), counters=counters,
                      inequality_count=len(inequalities), inequalities=inequalities,
                      components=dict(self.components), clause_count=len(self.clauses),
                      clauses_sha256=stable_sha256([list(c) for c in self.clauses]))
        if include_clauses:
            result["clauses"] = [list(c) for c in self.clauses]
        return result


@dataclass
class _RankBuilder:
    base_num_vars: int
    top: int = field(init=False)
    clauses: list[tuple[int, ...]] = field(default_factory=list)
    components: dict[str, int] = field(default_factory=dict)
    counters: list[PrefixCounter] = field(default_factory=list)
    inequalities: list[RankInequality] = field(default_factory=list)
    cache: dict[tuple[int, ...], tuple[Any, ...]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.top = _integer(self.base_num_vars, "F3 base_num_vars")

    def add(self, terms: Sequence[Any], component: str) -> None:
        # Identical constant/tautology handling and first-occurrence order to
        # the frozen measured template. Constants never enter DIMACS.
        if any(x is True for x in terms):
            return
        xs = tuple(dict.fromkeys(x for x in terms if x is not False))
        if any(-x in xs for x in xs):
            return
        if any(type(x) is not int or x == 0 or abs(x) > self.top for x in xs):
            raise ValueError("invalid F3 clause")
        self.clauses.append(xs)
        self.components[component] = self.components.get(component, 0) + 1

    def threshold(self, inputs: Sequence[int]) -> tuple[Any, ...]:
        inputs = tuple(_input(x, self.base_num_vars) for x in inputs)
        if len({abs(x) for x in inputs}) != len(inputs):
            raise ValueError("F3 counter inputs must be distinct old atoms")
        if inputs in self.cache:
            return self.cache[inputs]
        previous: list[Any] = [True]
        ledger = []
        for i, x in enumerate(inputs, 1):
            row: list[Any] = [True]
            for k in range(1, i + 1):
                a = previous[k] if k < len(previous) else False
                b = previous[k - 1]
                self.top += 1
                z = self.top
                neg = lambda term: not term if type(term) is bool else -term
                for clause in ((-z, a, x), (-z, a, b),
                               (z, neg(a)), (z, -x, neg(b))):
                    self.add(clause, "threshold_definitions")
                row.append(z)
                ledger.append((z, i, k))
            previous = row
        self.counters.append(PrefixCounter(inputs, tuple(ledger)))
        self.cache[inputs] = tuple(previous)
        return tuple(previous)

    def inequality(self, inputs: Sequence[int], bound: int,
                   guards: Sequence[int], component: str) -> None:
        inputs = tuple(_input(x, self.base_num_vars) for x in inputs)
        guards = tuple(_input(x, self.base_num_vars) for x in guards)
        if len({abs(x) for x in inputs}) != len(inputs):
            raise ValueError("F3 inequality inputs must be distinct old atoms")
        if type(bound) is not int or component not in ("rank_subset", "rank_superset"):
            raise ValueError("invalid F3 rank bound/component")
        self.inequalities.append(RankInequality(inputs, bound, guards, component))
        if bound >= len(inputs):
            return
        threshold = False if bound < 0 else -self.threshold(inputs)[bound + 1]
        self.add(tuple(-g for g in guards) + (threshold,), component)

    def finish(self) -> F3MainEncoding:
        allocated = tuple(z for counter in self.counters for z, _, _ in counter.ledger)
        if allocated != tuple(range(self.base_num_vars + 1, self.top + 1)):
            raise AssertionError("F3 auxiliaries are not one fresh canonical chain")
        return F3MainEncoding(self.base_num_vars, self.top, tuple(self.clauses),
                              tuple(self.components.items()), tuple(self.counters),
                              tuple(self.inequalities))


def build_f3_main_rank(encoding: DownsetStateEncoding, *, top_id: int) -> F3MainEncoding:
    """Append only the tested F3-main ranks, in the original measured order."""
    if not isinstance(encoding, DownsetStateEncoding) or encoding.spec != STATE_756_SPEC:
        raise ValueError("F3 requires the exact (7,5,6) state encoding")
    order = _integer(encoding.order, "F3 order", 1)
    if order > 35:
        raise ValueError("F3 order exceeds the canonical domain")
    out = _RankBuilder(top_id)
    subset = lambda a, b: all(x <= y for x, y in zip(a, b))
    for h in encoding.catalog:
        for direction, states in (
            ("subset", [g for g in encoding.catalog if g != h and subset(g, h)]),
            ("superset", [g for g in encoding.catalog if g != h and subset(h, g)]),
        ):
            inputs = [encoding.occupancy_vars[g]._lit for g in states]
            for v in range(1, order + 1):
                bound = v - 1 if direction == "subset" else order - v
                if bound < len(inputs):
                    out.inequality(inputs, bound, (encoding.state_vars[v, h]._lit,),
                                   "rank_" + direction)
    return out.finish()


def replay_f3_main_metadata(raw: Mapping[str, Any]) -> F3MainEncoding:
    """Reconstruct exact counter allocation/clauses from the rank ledger.

    This lightweight check validates canonical syntax, IDs, hashes and layer
    boundaries. Formula/state semantic agreement still uses fresh cell replay.
    """
    if not isinstance(raw, Mapping) or raw.get("schema") != F3_MAIN_SCHEMA:
        raise ValueError("unknown F3 metadata schema")
    out = _RankBuilder(_integer(raw.get("base_num_vars"), "F3 base_num_vars"))
    rows = raw.get("inequalities")
    if not isinstance(rows, list):
        raise ValueError("missing F3 inequality ledger")
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != {
            "inputs", "bound", "guards", "component", "sense"
        } or row.get("sense") != "atmost":
            raise ValueError("invalid F3 inequality metadata")
        if not isinstance(row["inputs"], list) or not isinstance(row["guards"], list):
            raise ValueError("F3 inputs/guards must be lists")
        out.inequality(row["inputs"], row["bound"], row["guards"], row["component"])
    result = out.finish()
    if stable_sha256(dict(raw)) != stable_sha256(result.to_dict()):
        raise ValueError("F3 metadata is not a canonical exact replay")
    return result
