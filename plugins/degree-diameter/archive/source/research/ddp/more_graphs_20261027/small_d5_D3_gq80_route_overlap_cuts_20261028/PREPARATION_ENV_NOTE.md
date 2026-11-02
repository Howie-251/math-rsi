# Preparation environment chronology

The executed preparation had no explicit BLAS thread-environment cap. It measured 17.278269307 CPU seconds and 1.1793683469295502 wall seconds; these actual measurements remain unchanged in MODEL_STATS.json. The worker subtracts that preparation CPU from the 55-second aggregate budget, leaving a configured 37-second hard worker CPU limit and a configured 45-second solver time limit.

While the sole worker was already running, prepare_model.py was amended only to set OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS, and NUMEXPR_NUM_THREADS to 1 before importing NumPy/SciPy. This is a future-use environment correction. No preparation, model construction, matrix generation, or numerical call was repeated after the change. The already prepared matrix and this batch's actual CPU accounting are unchanged.
