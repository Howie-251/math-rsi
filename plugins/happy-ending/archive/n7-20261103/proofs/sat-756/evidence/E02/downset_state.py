"""Independent terminal-pair down-set states for the ``(7, 5, 6)`` target.

The existing SAT encoding stores cap/cup witnesses by their *outer* endpoints.
Those variables are useful for the solver, but they are not the terminal-pair
profiles used by the Baek--Balko state injection.  This module deliberately
depends only on a complete coloring of ordered triples and recomputes every
path fact from scratch.

All public vertices are one-based.  Internally, the two colors use neutral
names tied to their forbidden path lengths:

``path5_color``
    Blue in the current encoding.  A path on five vertices is forbidden, so
    the split-side witness has four vertices and contributes the width-three
    coordinate.

``path6_color``
    Red in the current encoding.  A path on six vertices is forbidden, so the
    split-side witness has five vertices and contributes the height-four
    coordinate.

No solver dependency is required.  In particular, this module must remain an
independent oracle for any future opt-in CNF state encoding.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Sequence


PROFILE_SCHEMA = "downset_state_profile_v1"
SEMANTICS_SCHEMA = "downset_state_semantics_v1"
FIRST_EXCEPTIONAL_EVENT_SCHEMA = "downset_first_exceptional_event_v1"

ORDINARY_KIND = "ordinary"
EXCEPTIONAL_KIND = "exceptional"

ORIENTATION_NONE = "none"
ORIENTATION_OVERLAP = "overlap"
ORIENTATION_PATH5_BEFORE_PATH6 = "path5_before_path6"
ORIENTATION_PATH6_BEFORE_PATH5 = "path6_before_path5"
ORIENTATION_INTERLEAVED = "interleaved"

ENDPOINT_ORIENTATION_SCHEMA = "downset_endpoint_orientation_catalog_v1"
ENDPOINT_ORIENTATIONS = (
    ORIENTATION_NONE,
    ORIENTATION_OVERLAP,
    ORIENTATION_PATH5_BEFORE_PATH6,
    ORIENTATION_PATH6_BEFORE_PATH5,
    ORIENTATION_INTERLEAVED,
)

# Keep this payload JSON-native: corpus and obligation artifacts embed it
# directly and bind it by ENDPOINT_ORIENTATION_CATALOG_SHA256.  The condition
# tokens are deliberately exact rather than relying on an informal meaning of
# "interleaved" (which does not require strict alternation).
ENDPOINT_ORIENTATION_SEMANTICS = {
    ORIENTATION_NONE: {
        "condition": "path5_empty_or_path6_empty",
        "both_nonempty": False,
        "disjoint": None,
    },
    ORIENTATION_OVERLAP: {
        "condition": "path5_intersection_path6_nonempty",
        "both_nonempty": True,
        "disjoint": False,
    },
    ORIENTATION_PATH5_BEFORE_PATH6: {
        "condition": "both_nonempty_disjoint_and_max_path5_lt_min_path6",
        "both_nonempty": True,
        "disjoint": True,
    },
    ORIENTATION_PATH6_BEFORE_PATH5: {
        "condition": "both_nonempty_disjoint_and_max_path6_lt_min_path5",
        "both_nonempty": True,
        "disjoint": True,
    },
    ORIENTATION_INTERLEAVED: {
        "condition": (
            "both_nonempty_disjoint_and_neither_strict_separation_holds"
        ),
        "both_nonempty": True,
        "disjoint": True,
    },
}

ENDPOINT_ORIENTATION_CATALOG = {
    "schema": ENDPOINT_ORIENTATION_SCHEMA,
    "inputs": ["path5_start_endpoints", "path6_start_endpoints"],
    "values": [
        {
            "name": orientation,
            **ENDPOINT_ORIENTATION_SEMANTICS[orientation],
        }
        for orientation in ENDPOINT_ORIENTATIONS
    ],
    "classification_order": list(ENDPOINT_ORIENTATIONS),
    "partition": "exactly_one_for_all_finite_start_endpoint_sets",
    "overlap_precedes_order_relations": True,
}


def endpoint_orientation_catalog_sha256(
    catalog: Mapping[str, Any] = ENDPOINT_ORIENTATION_CATALOG,
) -> str:
    """Return the canonical JSON identity of an orientation catalog."""

    payload = json.dumps(catalog, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


ENDPOINT_ORIENTATION_CATALOG_SHA256 = endpoint_orientation_catalog_sha256()

StateRows = tuple[int, ...]
Triple = tuple[int, int, int]
PathTuple = tuple[int, ...]


class ColoringValidationError(ValueError):
    """Raised when an input is not a complete ordered triple coloring."""


class PathBoundViolation(ValueError):
    """Raised when a coloring lies outside the finite state box."""

    def __init__(self, violations: Sequence[Mapping[str, Any]]):
        self.violations = tuple(dict(item) for item in violations)
        summary = ", ".join(
            f"{item['family']} length {item['length']} at "
            f"{tuple(item['terminal_pair'])}"
            for item in self.violations[:3]
        )
        suffix = "" if len(self.violations) <= 3 else ", ..."
        super().__init__(
            "triple coloring violates the configured path bounds: "
            + summary
            + suffix
        )


@dataclass(frozen=True)
class DownsetSpec:
    """Neutral state-box and target semantics.

    ``path5_forbidden_length`` and ``path6_forbidden_length`` name the two
    monochromatic path bounds.  The split witness lengths are stored
    separately so the state/endpoint equivalence is explicit rather than
    inferred from a project-specific cap/cup name.
    """

    gon_size: int = 7
    path5_color: str = "blue"
    path6_color: str = "red"
    path5_forbidden_length: int = 5
    path6_forbidden_length: int = 6
    path5_split_length: int = 4
    path6_split_length: int = 5

    def __post_init__(self) -> None:
        colors = {self.path5_color, self.path6_color}
        if colors != {"red", "blue"}:
            raise ValueError("path colors must be distinct members of {'red', 'blue'}")
        for name, value in (
            ("gon_size", self.gon_size),
            ("path5_forbidden_length", self.path5_forbidden_length),
            ("path6_forbidden_length", self.path6_forbidden_length),
            ("path5_split_length", self.path5_split_length),
            ("path6_split_length", self.path6_split_length),
        ):
            if isinstance(value, bool) or not isinstance(value, int) or value < 3:
                raise ValueError(f"{name} must be an integer at least 3")
        if self.path5_split_length != self.path5_forbidden_length - 1:
            raise ValueError("path5 split length must be one below its forbidden length")
        if self.path6_split_length != self.path6_forbidden_length - 1:
            raise ValueError("path6 split length must be one below its forbidden length")
        if self.path5_split_length + self.path6_split_length != self.gon_size + 2:
            raise ValueError("split path lengths must sum to gon_size + 2")

    @property
    def width(self) -> int:
        return self.path5_forbidden_length - 2

    @property
    def height(self) -> int:
        return self.path6_forbidden_length - 2

    def semantics_dict(self) -> dict[str, Any]:
        return {
            "schema": SEMANTICS_SCHEMA,
            "path5_color": self.path5_color,
            "path6_color": self.path6_color,
            "path5_forbidden_length": self.path5_forbidden_length,
            "path6_forbidden_length": self.path6_forbidden_length,
            "split_length_pair": [
                self.path5_split_length,
                self.path6_split_length,
            ],
            "split_mapping": {
                "d": "path5_color",
                "e": "path6_color",
                "project_d_name": "cap",
                "project_e_name": "cup",
            },
            "gon_semantics": "weak_shared_outer_endpoints",
            "state_profile_semantics": "terminal_pair",
            "rtq_r_semantics": "first_split_right_endpoint",
            "rtq_q_semantics": "minimum_path6_outer_left_endpoint",
            "box": [self.width, self.height],
            "state_row_order": "nonincreasing_heights_by_path5_coordinate",
        }


STATE_756_SPEC = DownsetSpec()


@dataclass(frozen=True)
class _ColorPathDP:
    longest_length: Mapping[tuple[int, int], int]
    longest_path: Mapping[tuple[int, int], PathTuple]
    target_paths_by_start: Mapping[tuple[int, int], Mapping[int, PathTuple]]


def _normalize_color(value: Any) -> str:
    if isinstance(value, bool):
        return "red" if value else "blue"
    if isinstance(value, int) and value in {0, 1}:
        return "red" if value else "blue"
    token = str(value).strip().lower()
    if token in {"red", "r", "true", "t", "1", "+"}:
        return "red"
    if token in {"blue", "b", "false", "f", "0", "-"}:
        return "blue"
    raise ColoringValidationError(f"unknown triple color {value!r}")


def _normalize_triple(value: Any) -> Triple:
    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned.startswith("(") and cleaned.endswith(")"):
            cleaned = cleaned[1:-1]
        raw = cleaned.replace(",", " ").split()
    else:
        try:
            raw = list(value)
        except TypeError as exc:
            raise ColoringValidationError(
                f"triple key must be a length-three sequence, got {value!r}"
            ) from exc
    if len(raw) != 3:
        raise ColoringValidationError(
            f"triple key must have length three, got {value!r}"
        )
    try:
        triple: Triple = (int(raw[0]), int(raw[1]), int(raw[2]))
    except (TypeError, ValueError) as exc:
        raise ColoringValidationError(f"invalid triple {value!r}") from exc
    if triple[0] < 1 or not triple[0] < triple[1] < triple[2]:
        raise ColoringValidationError(
            f"triple vertices must be one-based and strictly increasing: {triple!r}"
        )
    return triple


def normalize_complete_coloring(
    triple_colors: Mapping[Any, Any],
    order: int | None = None,
) -> tuple[dict[Triple, str], int]:
    """Normalize and validate a complete one-based triple coloring."""

    if not isinstance(triple_colors, Mapping):
        raise TypeError("triple_colors must be a mapping")
    normalized: dict[Triple, str] = {}
    for raw_triple, raw_color in triple_colors.items():
        triple = _normalize_triple(raw_triple)
        if triple in normalized:
            raise ColoringValidationError(f"duplicate normalized triple {triple}")
        normalized[triple] = _normalize_color(raw_color)

    if order is None:
        if not normalized:
            raise ColoringValidationError(
                "order is required when the triple-color mapping is empty"
            )
        order = max(vertex for triple in normalized for vertex in triple)
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")

    expected_count = math.comb(order, 3) if order >= 3 else 0
    if len(normalized) != expected_count:
        first_missing = next(
            (
                triple
                for triple in itertools.combinations(range(1, order + 1), 3)
                if triple not in normalized
            ),
            None,
        )
        raise ColoringValidationError(
            f"incomplete coloring for order {order}: expected {expected_count} "
            f"triples, found {len(normalized)}; first missing={first_missing}"
        )
    extra = next(
        (
            triple
            for triple in normalized
            if triple[2] > order
        ),
        None,
    )
    if extra is not None:
        raise ColoringValidationError(
            f"triple {extra} lies outside the declared order {order}"
        )
    return dict(sorted(normalized.items())), order


def canonical_coloring_sha256(triple_colors: Mapping[Triple, str]) -> str:
    """Hash the repository's canonical one-based ``R|B`` color text."""

    text = "".join(
        f"{i} {j} {k} {'R' if color == 'red' else 'B'}\n"
        for (i, j, k), color in sorted(triple_colors.items())
    )
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def enumerate_states(spec: DownsetSpec = STATE_756_SPEC) -> tuple[StateRows, ...]:
    """Enumerate every down-set row partition in the configured box."""

    states = [
        tuple(rows)
        for rows in itertools.product(range(spec.height + 1), repeat=spec.width)
        if all(rows[index] >= rows[index + 1] for index in range(len(rows) - 1))
    ]
    return tuple(sorted(states))


def state_bounding_box(rows: Sequence[int]) -> tuple[int, int]:
    """Return ``(width, height)`` for a nonincreasing row partition."""

    normalized = tuple(int(value) for value in rows)
    if any(value < 0 for value in normalized):
        raise ValueError("state rows must be nonnegative")
    if any(
        normalized[index] < normalized[index + 1]
        for index in range(len(normalized) - 1)
    ):
        raise ValueError("state rows must be nonincreasing")
    width = max(
        (index + 1 for index, value in enumerate(normalized) if value > 0),
        default=0,
    )
    height = normalized[0] if width else 0
    return width, height


def classify_state(
    rows: Sequence[int],
    spec: DownsetSpec = STATE_756_SPEC,
) -> str:
    """Classify a state by the split bounding-box threshold."""

    normalized = tuple(int(value) for value in rows)
    if len(normalized) != spec.width:
        raise ValueError(f"expected {spec.width} rows, got {len(normalized)}")
    if any(value > spec.height for value in normalized):
        raise ValueError(f"state row exceeds configured height {spec.height}")
    width, height = state_bounding_box(normalized)
    return (
        ORDINARY_KIND
        if width + height <= spec.gon_size - 1
        else EXCEPTIONAL_KIND
    )


def ordinary_states(spec: DownsetSpec = STATE_756_SPEC) -> tuple[StateRows, ...]:
    return tuple(
        state for state in enumerate_states(spec) if classify_state(state, spec) == ORDINARY_KIND
    )


def exceptional_states(spec: DownsetSpec = STATE_756_SPEC) -> tuple[StateRows, ...]:
    return tuple(
        state
        for state in enumerate_states(spec)
        if classify_state(state, spec) == EXCEPTIONAL_KIND
    )


def shadow_x(rows: Sequence[int], spec: DownsetSpec = STATE_756_SPEC) -> StateRows:
    """Delete the first path5-coordinate row and append an empty row."""

    state = tuple(int(value) for value in rows)
    if classify_state(state, spec) != EXCEPTIONAL_KIND:
        raise ValueError(f"X-shadow is defined only for exceptional states, got {state}")
    shadow = (*state[1:], 0)
    if classify_state(shadow, spec) != ORDINARY_KIND:
        raise AssertionError("X-shadow must land in the ordinary state family")
    return shadow


def shadow_y(rows: Sequence[int], spec: DownsetSpec = STATE_756_SPEC) -> StateRows:
    """Lower every row of an exceptional state by one cell."""

    state = tuple(int(value) for value in rows)
    if classify_state(state, spec) != EXCEPTIONAL_KIND:
        raise ValueError(f"Y-shadow is defined only for exceptional states, got {state}")
    if any(value < 1 for value in state):
        raise AssertionError("exceptional state must meet every path5-coordinate row")
    shadow = tuple(value - 1 for value in state)
    if classify_state(shadow, spec) != ORDINARY_KIND:
        raise AssertionError("Y-shadow must land in the ordinary state family")
    return shadow


def _compute_color_paths(
    triple_colors: Mapping[Triple, str],
    order: int,
    *,
    color: str,
    target_length: int,
) -> _ColorPathDP:
    longest_length: dict[tuple[int, int], int] = {}
    longest_path: dict[tuple[int, int], PathTuple] = {}
    exact: dict[tuple[int, int, int], dict[int, PathTuple]] = {}

    for right in range(2, order + 1):
        for left in range(1, right):
            pair = (left, right)
            best_length = 2
            best_path: PathTuple = pair
            exact[(2, left, right)] = {left: pair}

            for predecessor in range(1, left):
                if triple_colors[(predecessor, left, right)] != color:
                    continue
                candidate_path = longest_path[(predecessor, left)] + (right,)
                candidate_length = longest_length[(predecessor, left)] + 1
                if candidate_length > best_length or (
                    candidate_length == best_length and candidate_path < best_path
                ):
                    best_length = candidate_length
                    best_path = candidate_path

            longest_length[pair] = best_length
            longest_path[pair] = best_path

            for length in range(3, target_length + 1):
                by_start: dict[int, PathTuple] = {}
                for predecessor in range(1, left):
                    if triple_colors[(predecessor, left, right)] != color:
                        continue
                    for start, prefix in exact.get(
                        (length - 1, predecessor, left), {}
                    ).items():
                        candidate = prefix + (right,)
                        previous = by_start.get(start)
                        if previous is None or candidate < previous:
                            by_start[start] = candidate
                exact[(length, left, right)] = by_start

    target_paths = {
        pair: exact.get((target_length, pair[0], pair[1]), {})
        for pair in longest_length
    }
    return _ColorPathDP(
        longest_length=longest_length,
        longest_path=longest_path,
        target_paths_by_start=target_paths,
    )


def _aggregate_target_paths(
    path_dp: _ColorPathDP,
    right_endpoint: int,
) -> dict[int, PathTuple]:
    by_start: dict[int, PathTuple] = {}
    for penultimate in range(1, right_endpoint):
        for start, path in path_dp.target_paths_by_start.get(
            (penultimate, right_endpoint), {}
        ).items():
            previous = by_start.get(start)
            if previous is None or path < previous:
                by_start[start] = path
    return dict(sorted(by_start.items()))


def _normalize_endpoint_starts(
    starts: Iterable[int],
    *,
    family: str,
) -> frozenset[int]:
    if isinstance(starts, (str, bytes)):
        raise TypeError(f"{family} starts must be an iterable of positive integers")
    try:
        values = tuple(starts)
    except TypeError as exc:
        raise TypeError(
            f"{family} starts must be an iterable of positive integers"
        ) from exc
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(
                f"{family} starts must contain only positive integers, got {value!r}"
            )
    return frozenset(values)


def classify_endpoint_orientation(
    path5_starts: Iterable[int],
    path6_starts: Iterable[int],
) -> str:
    """Classify the exact order type of two finite outer-start sets.

    Overlap has priority over all order comparisons.  For disjoint nonempty
    sets, ``interleaved`` is precisely the complement of the two strict
    separation cases; it does not mean that the starts strictly alternate.
    """

    path5 = _normalize_endpoint_starts(path5_starts, family="path5")
    path6 = _normalize_endpoint_starts(path6_starts, family="path6")
    if not path5 or not path6:
        return ORIENTATION_NONE
    if path5 & path6:
        return ORIENTATION_OVERLAP
    if max(path5) < min(path6):
        return ORIENTATION_PATH5_BEFORE_PATH6
    if max(path6) < min(path5):
        return ORIENTATION_PATH6_BEFORE_PATH5
    return ORIENTATION_INTERLEAVED


def _endpoint_orientation(path5_starts: set[int], path6_starts: set[int]) -> str:
    """Backward-compatible private alias for the public classifier."""

    return classify_endpoint_orientation(path5_starts, path6_starts)


def extract_downset_profile(
    triple_colors: Mapping[Any, Any],
    order: int | None = None,
    *,
    spec: DownsetSpec = STATE_756_SPEC,
) -> dict[str, Any]:
    """Recompute terminal-pair states and endpoint defects from a full model.

    A :class:`PathBoundViolation` is raised before any state is emitted if the
    model contains a forbidden path.  Clipping a longer path into the finite
    box would fabricate a valid-looking state and is therefore never allowed.
    """

    colors, order = normalize_complete_coloring(triple_colors, order=order)
    path5 = _compute_color_paths(
        colors,
        order,
        color=spec.path5_color,
        target_length=spec.path5_split_length,
    )
    path6 = _compute_color_paths(
        colors,
        order,
        color=spec.path6_color,
        target_length=spec.path6_split_length,
    )

    violations: list[dict[str, Any]] = []
    for family, forbidden_length, path_dp in (
        ("path5_color", spec.path5_forbidden_length, path5),
        ("path6_color", spec.path6_forbidden_length, path6),
    ):
        for pair, length in sorted(path_dp.longest_length.items()):
            if length >= forbidden_length:
                violations.append(
                    {
                        "family": family,
                        "terminal_pair": list(pair),
                        "length": length,
                        "canonical_path": list(path_dp.longest_path[pair]),
                    }
                )
    if violations:
        raise PathBoundViolation(violations)

    terminal_profiles = []
    for right in range(2, order + 1):
        for left in range(1, right):
            pair = (left, right)
            terminal_profiles.append(
                {
                    "terminal_pair": [left, right],
                    "sigma": [
                        path5.longest_length[pair] - 1,
                        path6.longest_length[pair] - 1,
                    ],
                    "path5_color": {
                        "longest_length": path5.longest_length[pair],
                        "canonical_longest_path": list(path5.longest_path[pair]),
                        "split_start_endpoints": sorted(
                            path5.target_paths_by_start[pair]
                        ),
                    },
                    "path6_color": {
                        "longest_length": path6.longest_length[pair],
                        "canonical_longest_path": list(path6.longest_path[pair]),
                        "split_start_endpoints": sorted(
                            path6.target_paths_by_start[pair]
                        ),
                    },
                }
            )

    vertex_states = []
    state_to_vertices: dict[StateRows, list[int]] = {}
    first_exceptional_vertex = None
    first_weak_gon_vertex = None

    for vertex in range(1, order + 1):
        rows = []
        for x in range(1, spec.width + 1):
            height = max(
                (
                    path6.longest_length[(left, vertex)] - 1
                    for left in range(1, vertex)
                    if path5.longest_length[(left, vertex)] - 1 >= x
                ),
                default=0,
            )
            rows.append(height)
        state = tuple(rows)
        kind = classify_state(state, spec)
        bbox = state_bounding_box(state)
        state_to_vertices.setdefault(state, []).append(vertex)

        path5_paths = _aggregate_target_paths(path5, vertex)
        path6_paths = _aggregate_target_paths(path6, vertex)
        path5_starts = set(path5_paths)
        path6_starts = set(path6_paths)
        common_starts = path5_starts & path6_starts
        split_here = bool(path5_starts) and bool(path6_starts)
        weak_here = bool(common_starts)

        if (kind == EXCEPTIONAL_KIND) != split_here:
            raise AssertionError(
                f"state/split equivalence failed at vertex {vertex}: "
                f"state={state}, path5_starts={sorted(path5_starts)}, "
                f"path6_starts={sorted(path6_starts)}"
            )
        if split_here and first_exceptional_vertex is None:
            first_exceptional_vertex = vertex
        if weak_here and first_weak_gon_vertex is None:
            first_weak_gon_vertex = vertex

        witnesses_by_start = []
        for start in sorted(common_starts):
            witnesses_by_start.append(
                {
                    "start": start,
                    "path5_path": list(path5_paths[start]),
                    "path6_path": list(path6_paths[start]),
                }
            )

        vertex_states.append(
            {
                "vertex": vertex,
                "rows": list(state),
                "bbox": list(bbox),
                "kind": kind,
                "split_witness": split_here,
                "weak_gon": weak_here,
                "endpoint_orientation": classify_endpoint_orientation(
                    path5_starts, path6_starts
                ),
                "path5_start_endpoints": sorted(path5_starts),
                "path6_start_endpoints": sorted(path6_starts),
                "common_start_endpoints": sorted(common_starts),
                "path5_canonical_paths": [
                    {"start": start, "path": list(path)}
                    for start, path in path5_paths.items()
                ],
                "path6_canonical_paths": [
                    {"start": start, "path": list(path)}
                    for start, path in path6_paths.items()
                ],
                "weak_witnesses": witnesses_by_start,
            }
        )

    universe = enumerate_states(spec)
    ordinary = tuple(
        state for state in universe if classify_state(state, spec) == ORDINARY_KIND
    )
    exceptional = tuple(
        state for state in universe if classify_state(state, spec) == EXCEPTIONAL_KIND
    )
    occupied = set(state_to_vertices)
    occupied_ordinary = tuple(sorted(occupied & set(ordinary)))
    occupied_exceptional = tuple(sorted(occupied & set(exceptional)))
    missing_ordinary = tuple(sorted(set(ordinary) - occupied))
    collisions = [
        {"rows": list(state), "vertices": vertices}
        for state, vertices in sorted(state_to_vertices.items())
        if len(vertices) > 1
    ]
    defect = len(occupied_exceptional) - len(missing_ordinary)
    injection_holds = not collisions

    return {
        "schema": PROFILE_SCHEMA,
        "order": order,
        "coloring_sha256": canonical_coloring_sha256(colors),
        "semantics": spec.semantics_dict(),
        "state_universe": {
            "all_count": len(universe),
            "ordinary_count": len(ordinary),
            "exceptional_count": len(exceptional),
            "ordinary_states": [list(state) for state in ordinary],
            "exceptional_states": [list(state) for state in exceptional],
        },
        "terminal_profiles": terminal_profiles,
        "vertex_states": vertex_states,
        "occupied_ordinary_states": [list(state) for state in occupied_ordinary],
        "missing_ordinary_states": [list(state) for state in missing_ordinary],
        "occupied_exceptional_states": [
            list(state) for state in occupied_exceptional
        ],
        "occupied_state_count": len(occupied),
        "defect": defect,
        "defect_identity": {
            "lhs_order_minus_ordinary_universe": order - len(ordinary),
            "rhs_occupied_exceptional_minus_missing_ordinary": defect,
            "holds": injection_holds and order - len(ordinary) == defect,
        },
        "first_exceptional_vertex": first_exceptional_vertex,
        "first_weak_gon_vertex": first_weak_gon_vertex,
        "state_injection": {
            "holds": injection_holds,
            "collisions": collisions,
        },
    }


def _validated_profile_start_endpoints(
    item: Mapping[str, Any],
    *,
    vertex: int,
    family: str,
    field: str,
    paths_field: str,
) -> list[int]:
    """Validate one cached endpoint-start set against its witness records."""

    target_length = {
        "path5": STATE_756_SPEC.path5_split_length,
        "path6": STATE_756_SPEC.path6_split_length,
    }.get(family)
    if target_length is None:  # pragma: no cover - private caller guard
        raise ValueError(f"unsupported path family {family!r}")

    raw_starts = item.get(field)
    if not isinstance(raw_starts, list):
        raise ValueError(f"vertex {vertex} has no list-valued {field}")
    starts = sorted(_normalize_endpoint_starts(raw_starts, family=family))
    if raw_starts != starts:
        raise ValueError(f"vertex {vertex} has a noncanonical {field}")

    raw_paths = item.get(paths_field)
    if not isinstance(raw_paths, list):
        raise ValueError(f"vertex {vertex} has no list-valued {paths_field}")
    witness_starts = []
    for index, witness in enumerate(raw_paths):
        if not isinstance(witness, Mapping):
            raise ValueError(
                f"vertex {vertex} {paths_field}[{index}] is not an object"
            )
        start = witness.get("start")
        path = witness.get("path")
        if (
            isinstance(start, bool)
            or not isinstance(start, int)
            or not isinstance(path, list)
            or any(
                isinstance(value, bool) or not isinstance(value, int)
                for value in path
            )
            or not path
            or len(path) != target_length
            or path[0] != start
            or path[-1] != vertex
            or any(left >= right for left, right in zip(path, path[1:]))
        ):
            raise ValueError(
                f"vertex {vertex} has an invalid {paths_field}[{index}] witness"
            )
        witness_starts.append(start)
    if witness_starts != starts:
        raise ValueError(
            f"vertex {vertex} {field} disagrees with {paths_field}"
        )
    return starts


def extract_first_exceptional_event(
    profile: Mapping[str, Any],
) -> dict[str, Any] | None:
    """Derive the first split/full endpoint from an existing state profile.

    The function does not trust ``first_exceptional_vertex`` or the cached
    endpoint labels.  It rescans the exact state rows in vertex order, checks
    every cached split/orientation/start-set field against the profile's own
    witness records, and returns the RTQ coordinates of the first exceptional
    event.  The input profile is never modified.
    """

    if not isinstance(profile, Mapping):
        raise TypeError("profile must be a mapping")
    if profile.get("schema") != PROFILE_SCHEMA:
        raise ValueError(f"expected profile schema {PROFILE_SCHEMA!r}")
    if profile.get("semantics") != STATE_756_SPEC.semantics_dict():
        raise ValueError("profile does not use the canonical (7,5,6) semantics")
    order = profile.get("order")
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("profile order must be a positive integer")
    raw_vertices = profile.get("vertex_states")
    if not isinstance(raw_vertices, list):
        raise ValueError("profile vertex_states must be a list")
    if len(raw_vertices) != order:
        raise ValueError("profile vertex_states length disagrees with order")

    first: tuple[int, StateRows, str, list[int], list[int], list[int]] | None = None
    seen_vertices = []
    for index, item in enumerate(raw_vertices):
        if not isinstance(item, Mapping):
            raise ValueError(f"vertex_states[{index}] is not an object")
        vertex = item.get("vertex")
        if isinstance(vertex, bool) or not isinstance(vertex, int):
            raise ValueError(f"vertex_states[{index}] has an invalid vertex")
        seen_vertices.append(vertex)

        raw_rows = item.get("rows")
        if not isinstance(raw_rows, list) or any(
            isinstance(value, bool) or not isinstance(value, int)
            for value in raw_rows
        ):
            raise ValueError(f"vertex {vertex} has invalid state rows")
        state = tuple(raw_rows)
        kind = classify_state(state)
        if item.get("kind") != kind:
            raise ValueError(f"vertex {vertex} cached state kind is inconsistent")
        if item.get("bbox") != list(state_bounding_box(state)):
            raise ValueError(f"vertex {vertex} cached bounding box is inconsistent")

        path5_starts = _validated_profile_start_endpoints(
            item,
            vertex=vertex,
            family="path5",
            field="path5_start_endpoints",
            paths_field="path5_canonical_paths",
        )
        path6_starts = _validated_profile_start_endpoints(
            item,
            vertex=vertex,
            family="path6",
            field="path6_start_endpoints",
            paths_field="path6_canonical_paths",
        )
        common = sorted(set(path5_starts) & set(path6_starts))
        if item.get("common_start_endpoints") != common:
            raise ValueError(f"vertex {vertex} cached common starts are inconsistent")

        split_here = bool(path5_starts) and bool(path6_starts)
        if item.get("split_witness") is not split_here:
            raise ValueError(f"vertex {vertex} cached split flag is inconsistent")
        if (kind == EXCEPTIONAL_KIND) != split_here:
            raise ValueError(f"vertex {vertex} state/split semantics are inconsistent")
        if item.get("weak_gon") is not bool(common):
            raise ValueError(f"vertex {vertex} cached weak-gon flag is inconsistent")

        orientation = classify_endpoint_orientation(path5_starts, path6_starts)
        if item.get("endpoint_orientation") != orientation:
            raise ValueError(f"vertex {vertex} cached orientation is inconsistent")
        if kind == EXCEPTIONAL_KIND and first is None:
            first = (
                vertex,
                state,
                orientation,
                path5_starts,
                path6_starts,
                common,
            )

    if seen_vertices != list(range(1, order + 1)):
        raise ValueError("profile vertices are not exactly the ordered range 1..order")
    if "first_exceptional_vertex" not in profile:
        raise ValueError("profile has no cached first_exceptional_vertex")
    computed_r = first[0] if first is not None else None
    if profile.get("first_exceptional_vertex") != computed_r:
        raise ValueError("cached first_exceptional_vertex is inconsistent")
    if first is None:
        return None

    vertex, state, orientation, path5_starts, path6_starts, common = first
    if not path6_starts:  # guarded by the state/split equivalence above
        raise AssertionError("an exceptional event must have a path6 start")
    return {
        "schema": FIRST_EXCEPTIONAL_EVENT_SCHEMA,
        "vertex": vertex,
        "rtq_r": vertex,
        "rtq_q": min(path6_starts),
        "exceptional_state": list(state),
        "endpoint_orientation": orientation,
        "path5_start_endpoints": list(path5_starts),
        "path6_start_endpoints": list(path6_starts),
        "common_start_endpoints": list(common),
    }


def audit_cube_semantics(
    profile: Mapping[str, Any],
    cube_metadata: Mapping[str, Any],
) -> dict[str, Any]:
    """Compare extracted state semantics with an R/RT/RTP/RTQ/RTPQ cube."""

    if profile.get("schema") != PROFILE_SCHEMA:
        raise ValueError(f"expected profile schema {PROFILE_SCHEMA!r}")
    cubing = cube_metadata.get("cubing")
    if not isinstance(cubing, Mapping):
        raise ValueError("cube metadata has no object-valued 'cubing' record")
    level = str(cubing.get("level") or "").lower()
    if level not in {"r", "rt", "rtp", "rtq", "rtpq"}:
        raise ValueError(f"unsupported cubing level {level!r}")

    vertices = {
        int(item["vertex"]): item
        for item in profile.get("vertex_states", [])
        if isinstance(item, Mapping) and "vertex" in item
    }
    expected_r = cubing.get("r")
    checks = []
    if expected_r is not None:
        actual_r = profile.get("first_exceptional_vertex")
        checks.append(
            {
                "name": "r_is_first_exceptional_vertex",
                "expected": int(expected_r),
                "actual": actual_r,
                "holds": actual_r == int(expected_r),
            }
        )

    if level in {"rt", "rtp", "rtq", "rtpq"}:
        checks.append(
            {
                "name": "split_type_is_4_5",
                "expected": [4, 5],
                "actual": [cubing.get("d"), cubing.get("e")],
                "holds": [cubing.get("d"), cubing.get("e")] == [4, 5],
            }
        )

    if expected_r is not None and int(expected_r) in vertices:
        endpoint = vertices[int(expected_r)]
        for coordinate, field, label in (
            (cubing.get("p"), "path5_start_endpoints", "p_is_path5_start"),
            (cubing.get("q"), "path6_start_endpoints", "q_is_path6_start"),
        ):
            if coordinate is None:
                continue
            starts = [int(value) for value in endpoint.get(field, [])]
            checks.append(
                {
                    "name": label,
                    "expected": int(coordinate),
                    "actual": starts,
                    "holds": int(coordinate) in starts,
                }
            )
            checks.append(
                {
                    "name": label.replace("_is_", "_is_minimum_"),
                    "expected": int(coordinate),
                    "actual": min(starts) if starts else None,
                    "holds": bool(starts) and min(starts) == int(coordinate),
                }
            )

    return {
        "schema": "downset_cube_semantics_audit_v1",
        "level": level,
        "checks": checks,
        "pass": bool(checks) and all(check["holds"] for check in checks),
    }
