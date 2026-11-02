"""Small deterministic CNF builders used by the n=59 encodings.

The module has no graph-specific constants.  Variables can be allocated by a
semantic key, which makes a regenerated variable map stable as long as the
encoder visits the same mathematical objects in the same order.  Clauses may
be counted, retained in memory, or streamed to DIMACS through the same API.
"""

from __future__ import annotations

import json
import os
import shutil
from collections import Counter
from pathlib import Path
from typing import Hashable, Iterable


Clause = tuple[int, ...]


def _freeze_key(value):
    """Convert ordinary structured keys to deterministic hashable values."""

    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Path):
        return ("path", str(value))
    if isinstance(value, tuple):
        return ("tuple", tuple(_freeze_key(item) for item in value))
    if isinstance(value, list):
        return ("list", tuple(_freeze_key(item) for item in value))
    if isinstance(value, (set, frozenset)):
        frozen = [_freeze_key(item) for item in value]
        return ("set", tuple(sorted(frozen, key=repr)))
    if isinstance(value, dict):
        items = [(_freeze_key(key), _freeze_key(item)) for key, item in value.items()]
        return ("dict", tuple(sorted(items, key=repr)))
    if not isinstance(value, Hashable):
        raise TypeError(f"semantic variable key is not hashable: {value!r}")
    return ("object", type(value).__qualname__, repr(value))


def _json_key(value):
    """Return a JSON-safe rendering of a semantic key without hashing it."""

    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (tuple, list)):
        return [_json_key(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return sorted((_json_key(item) for item in value), key=repr)
    if isinstance(value, dict):
        return {
            str(key): _json_key(item)
            for key, item in sorted(value.items(), key=lambda row: repr(row[0]))
        }
    return repr(value)


class SemanticVariablePool:
    """Allocate DIMACS variables deterministically by semantic key."""

    def __init__(self, first_free: int = 1) -> None:
        if first_free < 1:
            raise ValueError("first_free must be positive")
        self.first_free = int(first_free)
        self._by_key: dict[object, int] = {}
        self._records: list[dict] = []
        self._kind_counts: Counter[str] = Counter()
        self._anonymous_count = 0

    def var(self, key, kind: str = "aux") -> int:
        if not isinstance(kind, str) or not kind:
            raise ValueError("variable kind must be a nonempty string")
        frozen = _freeze_key(key)
        previous = self._by_key.get(frozen)
        if previous is not None:
            record = self._records[previous - self.first_free]
            if record["kind"] != kind:
                raise ValueError(
                    f"semantic key {key!r} was already allocated as "
                    f"{record['kind']!r}, not {kind!r}"
                )
            return previous
        variable = self.first_free + len(self._records)
        self._by_key[frozen] = variable
        self._records.append(
            {
                "variable": variable,
                "kind": kind,
                "semantic_key": _json_key(key),
            }
        )
        self._kind_counts[kind] += 1
        return variable

    def new_var(self, kind: str = "aux") -> int:
        index = self._anonymous_count
        self._anonymous_count += 1
        key = ("__anonymous_variable__", index)
        variable = self.var(key, kind)
        self._records[variable - self.first_free]["anonymous_index"] = index
        return variable

    @property
    def top(self) -> int:
        return self.first_free + len(self._records) - 1

    @property
    def allocated(self) -> int:
        return len(self._records)

    @property
    def kind_counts(self) -> dict[str, int]:
        return dict(sorted(self._kind_counts.items()))

    def records(self) -> list[dict]:
        return [dict(record) for record in self._records]


class CNFBuilder:
    """Common allocation and clause-validation interface."""

    storage_kind = "abstract"

    def __init__(self, pool: SemanticVariablePool | None = None) -> None:
        self.pool = pool or SemanticVariablePool()
        self.clause_count = 0
        self._finished = False

    def var(self, key, kind: str = "aux") -> int:
        return self.pool.var(key, kind)

    def new_var(self, kind: str = "aux") -> int:
        return self.pool.new_var(kind)

    @property
    def variable_count(self) -> int:
        return self.pool.top

    def add_clause(self, *literals: int | Iterable[int]) -> None:
        if self._finished:
            raise RuntimeError("cannot add a clause after finish()")
        if len(literals) == 1 and not isinstance(literals[0], int):
            literals = tuple(literals[0])
        clause = tuple(int(literal) for literal in literals)
        if any(isinstance(literal, bool) for literal in literals):
            raise TypeError("Boolean constants must be simplified before add_clause")
        if any(literal == 0 for literal in clause):
            raise ValueError("zero may not occur inside a DIMACS clause")
        if clause and max(map(abs, clause)) > self.variable_count:
            raise ValueError("clause refers to a variable that has not been allocated")
        self._record_clause(clause)
        self.clause_count += 1

    def _record_clause(self, clause: Clause) -> None:
        raise NotImplementedError

    def finish(self) -> None:
        self._finished = True

    def abort(self) -> None:
        self._finished = True

    def stats(self) -> dict:
        return {
            "storage_kind": self.storage_kind,
            "variables": self.variable_count,
            "allocated_variables": self.pool.allocated,
            "clauses": self.clause_count,
            "variable_kinds": self.pool.kind_counts,
        }

    def variable_map(self, *, include_variables: bool = False, **metadata) -> dict:
        result = {
            "schema_version": "sat59-semantic-variable-map-v1",
            **metadata,
            "top_variable": self.variable_count,
            "allocated_variables": self.pool.allocated,
            "variable_kinds": self.pool.kind_counts,
        }
        if include_variables:
            result["variables"] = self.pool.records()
        return result


class CountingCNFBuilder(CNFBuilder):
    """Count clauses without retaining or writing them."""

    storage_kind = "counting"

    def _record_clause(self, clause: Clause) -> None:
        del clause


class MemoryCNFBuilder(CNFBuilder):
    """Retain clauses for tests and bounded encodings."""

    storage_kind = "memory"

    def __init__(self, pool: SemanticVariablePool | None = None) -> None:
        super().__init__(pool)
        self.clauses: list[Clause] = []

    def _record_clause(self, clause: Clause) -> None:
        self.clauses.append(clause)

    def write_dimacs(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="ascii") as handle:
            handle.write(f"p cnf {self.variable_count} {self.clause_count}\n")
            for clause in self.clauses:
                handle.write(" ".join(map(str, clause)) + " 0\n")


class StreamingCNFBuilder(CNFBuilder):
    """Stream a DIMACS body and prepend its exact header at finish()."""

    storage_kind = "streaming"

    def __init__(
        self,
        output: Path,
        pool: SemanticVariablePool | None = None,
    ) -> None:
        super().__init__(pool)
        self.output = Path(output)
        self.output.parent.mkdir(parents=True, exist_ok=True)
        self.body_path = self.output.with_name(
            f".{self.output.name}.body-{os.getpid()}-{id(self)}"
        )
        self._body = self.body_path.open("w", encoding="ascii")

    def _record_clause(self, clause: Clause) -> None:
        self._body.write(" ".join(map(str, clause)) + " 0\n")

    def finish(self) -> None:
        if self._finished:
            return
        self._body.close()
        with self.output.open("w", encoding="ascii") as target:
            target.write(f"p cnf {self.variable_count} {self.clause_count}\n")
            with self.body_path.open("r", encoding="ascii") as source:
                shutil.copyfileobj(source, target, length=1024 * 1024)
        self.body_path.unlink()
        super().finish()

    def abort(self) -> None:
        if not self._body.closed:
            self._body.close()
        self.body_path.unlink(missing_ok=True)
        super().abort()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, _exc, _traceback):
        if exc_type is None:
            self.finish()
        else:
            self.abort()
        return False


def write_json(path: Path, value) -> None:
    """Write deterministic, human-readable JSON metadata."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

