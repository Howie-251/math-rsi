export MATHRSI_ROOT="$PWD"
export ARIS_REPO="$MATHRSI_ROOT/base"
export TASK_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/mathrsi-proof-repair.XXXXXX")"
cp "$MATHRSI_ROOT/examples/proof-repair/starter/REQUEST.md" "$TASK_ROOT/REQUEST.md"
cp "$MATHRSI_ROOT/examples/proof-repair/starter/PROOF.tex" "$TASK_ROOT/PROOF.tex"
python3 -c 'import json,os; print(json.dumps({"TASK_ROOT":os.environ["TASK_ROOT"],"MATHRSI_ROOT":os.environ["MATHRSI_ROOT"],"ARIS_REPO":os.environ["ARIS_REPO"]}))'
