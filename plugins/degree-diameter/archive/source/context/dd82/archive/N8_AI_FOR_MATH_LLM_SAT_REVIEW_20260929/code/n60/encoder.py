"""Append feedback propagation to the unchanged full r01 encoder."""
from __future__ import annotations
import json
from pathlib import Path
import time
from sat60.round11.encoder import TrackedCNF
from sat60.round13.encoder import N60Round13Encoder
from .contract import VERSION, REVISION, COMMON_IDS, Q038_IDS, MODULES
from .constraints import add_feedback


class N60Round13R02Encoder(N60Round13Encoder):
    def __init__(self, job, builder, *, families=None, feedback_modules=None):
        allowed = COMMON_IDS + (Q038_IDS if job["job_id"] == "Q_C02_038" else ())
        chosen = allowed if feedback_modules is None else tuple(feedback_modules)
        if len(set(chosen)) != len(chosen) or not set(chosen) <= set(allowed):
            raise ValueError("unknown, duplicated, or out-of-scope feedback module")
        self.feedback_modules = tuple(k for k in allowed if k in chosen)
        self.feedback_mapping = None
        super().__init__(job, builder, families=families)
        self.enabled_ids += list(self.feedback_modules)

    def encode(self):
        super().encode()
        self._r13f_before = self.builder.clause_count
        if self.feedback_modules:
            self.feedback_mapping = add_feedback(self, self.feedback_modules)
        return self.stats()

    def stats(self):
        data = super().stats()
        data.update(encoding=VERSION, package_revision=REVISION,
                    feedback_modules={k: MODULES[k] for k in self.feedback_modules},
                    specialized_status="ROUND13_R02_IMPLEMENTED_NOT_A_SOLVER_RESULT")
        return data

    def mapping(self):
        data = super().mapping()
        data.update(version="n60-round13-r02-map-v1", encoding_version=VERSION, package_revision=REVISION,
                    round13_feedback=self.feedback_mapping,
                    feedback_modules={k: MODULES[k] for k in self.feedback_modules},
                    specialized_status="ROUND13_R02_IMPLEMENTED_NOT_A_SOLVER_RESULT")
        return data


def generate_instance(job, directory, families):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    builder = TrackedCNF(directory / "base.cnf")
    try:
        encoder = N60Round13R02Encoder(job, builder, families=families)
        stats = encoder.encode()
        mapping = encoder.mapping()
        builder.finish()
    except BaseException:
        builder.abort()
        raise
    stats.update(generation_wall_seconds=round(time.monotonic() - started, 3),
                 cnf_bytes=(directory / "base.cnf").stat().st_size)
    (directory / "base.map.json").write_text(json.dumps(mapping, indent=2) + "\n")
    (directory / "base.stats.json").write_text(json.dumps(stats, indent=2) + "\n")
    return stats, mapping
