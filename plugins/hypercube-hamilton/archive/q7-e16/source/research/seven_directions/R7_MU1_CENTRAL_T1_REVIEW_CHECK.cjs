const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { createHash } = require("node:crypto");
const { join } = require("node:path");

const source = "R7_MU1_CENTRAL_T1_MINIMUM_CHECK.json";
const read = f => JSON.parse(readFileSync(f, "utf8"));
const sha = f => createHash("sha256").update(readFileSync(f)).digest("hex");
const data = read(source);
assert.equal(data.geometry_status, "complete");
assert.equal(data.gate_status, "complete");
assert.equal(data.geometry_frontier, null);
assert.equal(data.gate_frontier, null);
assert.deepEqual(data.unresolved, []);
assert.equal(data.checker_sha256, sha("R7_MU1_CENTRAL_T1_MINIMUM_CHECK.py"));
assert.equal(data.planner_sha256, sha("R7_MU1_EDGE_GEOMETRY_CHECK.py"));
const range = n => Array.from({ length: n }, (_, i) => i);
const axes = range(7);
const bit = (v, i) => (v >> i) & 1;
const wt = range(128).map(v => axes.reduce((n, i) => n + bit(v, i), 0));
const face = (pts, i, b) => pts.filter(v => bit(v, i) === b);
const flip = (v, i) => v ^ (1 << i);
const sorted = pts => [...pts].sort((a, b) => a - b);
const same = (a, b) => assert.deepEqual(sorted(a), sorted(b));
const permute = (v, p) => p.reduce((w, i, j) => w + (bit(v, j) << i), 0);
const project = (v, cols) => cols.reduce((w, i, j) => w + (bit(v, i) << j), 0);
const subset = (a, b, n) => a.length === n && new Set(a).size === n && a.every(x => b.includes(x));
const count = (table, key) => { table[key] = (table[key] ?? 0) + 1; };

const seven = process.argv[2];
const reviewPath = join(seven, "Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json");
const profilePath = join(seven, "Q6_T15_ACTUAL_PROFILE.json");
const accepted = read(reviewPath);
assert.equal(accepted.verdict, "PASS");
assert.equal(accepted.audited_input_hashes["Q6_T15_ACTUAL_PROFILE.json"].replace(/^sha256:/, ""), sha(profilePath));
const review1054 = join(seven, "Q6_T15_CORE1054_MARKED_REVIEW.json");
const proof1054 = "Q6_T15_CORE1054_MARKED_CLOSURE.md";
const accepted1054 = read(review1054);
assert.equal(accepted1054.verdict, "PASS");
assert.equal(accepted1054.core1054_universal_proved, true);
assert.equal(accepted1054.audited_input_hashes[proof1054].replace(/^sha256:/, ""), sha(join(seven, proof1054)));
assert.equal(accepted1054.audited_input_hashes["Q6_T15_ACTUAL_PROFILE.json"].replace(/^sha256:/, ""), sha(profilePath));
const profile = new Map(read(profilePath).orbits.map(r => [r.index, r]));
const cores = {};
const donorKinds = {}, receivers = {}, gateReasons = {}, oldKinds = {};

function verifyBridge(p, colors, old) {
  const j = old ? p.outer_direction : p.outer, b = p.donor_side;
  const k = old ? p.inner_direction : p.receiver.direction;
  const z = old ? p.inner_side : p.receiver.side;
  assert(axes.includes(j) && axes.includes(k) && j !== k && [0, 1].includes(b) && [0, 1].includes(z));
  const A = colors.map(xs => face(xs, j, b));
  const B = colors.map(xs => face(xs, j, 1 - b));
  const beta = Number(A[1].length > A[0].length), alpha = 1 - beta;
  const bridges = A[beta].length - A[alpha].length;
  assert([4, 5].includes(bridges));
  assert.equal(A[alpha].length, 1);
  const [a] = A[alpha];
  const X = old ? p.x : p.source_x, U = old ? p.u : p.source_u;
  assert(subset(X, A[beta], bridges - 2) && subset(U, B[alpha], 2));
  const I = A[beta].filter(v => !X.includes(v));
  const J = B[alpha].filter(v => !U.includes(v));
  const V = U.map(v => flip(v, j)), Y = X.map(v => flip(v, j));
  assert(V.concat(Y).every(v => !colors.flat().includes(v)));
  const d = old ? null : p.donor;
  const f = old ? null : p.receiver;
  const cols = axes.filter(i => i !== j);
  const norm = v => project(v ^ a, cols);
  if (old) {
    assert.equal(p.gate, bridges === 4 ? "four117" : "five117");
    count(oldKinds, p.gate);
    assert.equal(p.donor_minority_parity, alpha);
    same(p.v, V); same(p.y, Y); same(p.B_minor, B[beta]); same(p.B_retained_major, J);
    const loc = v => project(v, cols);
    const groups = p.core117_Q6_groups;
    assert.equal(groups[0], loc(a));
    same(groups[1], I.map(loc)); same(groups[2], V.map(loc));
    const isom = p.core117_isomorphism;
    assert.equal(isom.tool, "core117");
    assert.equal(isom.xor_before_permutation, loc(a));
    const p6 = isom.permutation_source_to_target;
    same(p6, range(6));
    same(I.map(norm).map(v => permute(v, p6)), [31, 61, 62]);
    same(V.map(norm).map(v => permute(v, p6)), [1, 2]);
  } else {
    assert.equal(p.bridges, bridges);
    assert.equal(p.donor_minority, a);
    same(p.donor_markers, V); same(p.receiver_markers, Y);
    count(donorKinds, d.kind);
    if (d.kind === "audited_exact_core") {
      assert(d.index === 1054 || accepted.union_closed_core_indices.includes(d.index));
      count(cores, d.index);
      same(d.coordinate_transport, range(6));
      const target = profile.get(d.index);
      for (const [i, xs, group] of [[0, I, "included"], [1, V, "omitted"]]) {
        same(xs.map(norm), d.normalized_groups[i]);
        same(xs.map(norm).map(v => permute(v, d.coordinate_transport)), target[group]);
      }
    } else {
      const ell = d.direction;
      assert(axes.includes(ell) && ell !== j);
      if (d.kind === "forced_split") {
        assert.equal(d.forced_positive_crossing, true);
        assert(subset(d.prescribed_pair, X, 2));
        assert.notEqual(bit(d.prescribed_pair[0], ell), bit(d.prescribed_pair[1], ell));
        const split = [0, 1].map(side => [[a], I.concat(V), V].map(xs => face(xs, ell, side).length));
        assert.deepEqual(split, d.counts);
        assert(split.every(([l, m, q]) => m - l === 2 * q));
      } else if (d.kind === "audited_easy_same_face") {
        assert([a, ...I, ...V].every(v => bit(v, ell) === bit(a, ell)));
      } else {
        assert.equal(d.kind, "audited_easy_isolated_mark");
        assert(V.includes(d.isolated_mark));
        assert.deepEqual(face([a, ...I, ...V], ell, bit(d.isolated_mark, ell)), [d.isolated_mark]);
      }
    }
  }
  const majority = J.concat(Y);
  const [l, m, q] = [B[beta], majority, Y].map(xs => face(xs, k, z).length);
  const mode = old ? ({ same_side: "same", separated: "separated", split_2_plus_1: "T17" })[p.inner_mode] : f.kind;
  const root = old ? p.a : f.minority;
  assert(face(B[beta], k, z).includes(root));
  const w = flip(root, k), edge = sorted([w, flip(w, j)]);
  assert(!Y.includes(w));
  assert.equal(w, old ? p.w : f.w);
  same(edge, old ? p.necessary_edge : f.necessary_edge);
  if (bridges === 5) {
    assert.equal(mode, "T17");
    assert.deepEqual([l, m, q], [1, 4, 2]);
  } else if (mode === "same") {
    assert([1, 2].includes(l));
    assert.deepEqual([m, q], [l + 3, 2]);
  } else {
    assert.equal(mode, "separated");
    assert([1, 2].includes(l));
    assert.deepEqual([m, q], [l + 1, 1]);
  }
  const universal = mode === "same" && l === 2;
  const opposite = face(majority, k, 1 - z);
  if (old) assert.deepEqual(p.inner_shape, [l, m]);
  else {
    assert.equal(f.universal, universal);
    if (bridges === 4) {
      assert.deepEqual(f.counts, [l, m, q]);
      same(f.opposite_majority, opposite);
    }
  }
  count(receivers, mode);
  return { universal, l, mode, root, k, opposite, edge };
}

function verifyPlan(plan, colors) {
  const old = plan.gate === "old_high_gap";
  assert(old || plan.gate === "broad_high_gap");
  const reason = old ? plan.reason : plan.kind;
  count(gateReasons, plan.gate + "/" + reason);
  const proofs = plan.plans.map(p => verifyBridge(p, colors, old));
  const edges = proofs.map(p => p.edge);
  const occupied = new Set(edges.flat());
  const holes = new Set(colors.flat());
  if (plan.edges) assert.deepEqual(plan.edges.map(e => sorted(e).join(",")).sort(), edges.map(e => e.join(",")).sort());
  if (reason === "same_side_s2" || reason === "unconditional_four117_same_side_s2") {
    assert(proofs.length === 1 && proofs[0].universal);
  } else if (reason === "same_side_double_cut") {
    assert(!old && proofs.length === 2);
    const [p, q] = proofs;
    for (const r of proofs) assert(r.mode === "same" && r.l === 1 && r.opposite.length === 2);
    assert(p.root === q.root && p.k !== q.k);
    assert([0, 2].includes(p.opposite.filter(v => q.opposite.includes(v)).length));
    const strip = ({ receiver, ...rest }) => rest;
    assert.deepEqual(strip(plan.plans[0]), strip(plan.plans[1]));
  } else if (reason === "necessary_edge_touches_hole") {
    assert(edges.length === 1 && edges[0].some(v => holes.has(v)));
  } else if (reason === "necessary_edges_share_endpoint" || reason === "two_necessary_edges_share_endpoint") {
    assert.equal(edges.length, 2);
    assert.equal(occupied.size, 3);
  } else {
    assert.equal(reason, "necessary_edges_leave_isolate");
    assert(old && Number.isInteger(plan.isolate) && plan.isolate >= 0 && plan.isolate < 128);
    assert.equal(occupied.size, 2 * edges.length);
    assert([...occupied].every(v => !holes.has(v)));
    assert(!holes.has(plan.isolate) && !occupied.has(plan.isolate));
    assert(axes.map(i => flip(plan.isolate, i)).every(v => holes.has(v) || occupied.has(v)));
  }
}

function* permutations(xs) {
  if (!xs.length) yield [];
  for (const x of xs) for (const tail of permutations(xs.filter(v => v !== x))) yield [x, ...tail];
}
function* subsets(xs, n, i = 0, part = []) {
  if (!n) {
    yield part;
    return;
  }
  for (let j = i; j <= xs.length - n; j++) yield* subsets(xs, n - 1, j + 1, part.concat(xs[j]));
}

assert.equal(data.column_checker_sha256, sha("R7_MU1_COLUMN_COUNT_INTERFACES.py"));
const columnCap = [4, 3, 4, 3];
function* countVectors(total, i = 0, a = []) {
  if (i === 4) {
    if (total === 0) yield a;
    return;
  }
  for (let n = 0; n <= Math.min(total, columnCap[i]); n++) yield* countVectors(total - n, i + 1, a.concat(n));
}

function columnGates(column, total) {
  const points = columnCap.flatMap((m, k) => {
    const color = Number(k >= 2);
    return range(m).map(t => ({ color, low: (k % 2) ^ color, high: Number(t < column[k]) ^ color }));
  });
  const single = [];
  for (const low of [1, 0]) {
    for (const high of [0, 1]) {
      const box = points.filter(p => p.low === low && p.high === high);
      if (box.filter(p => p.color === 0).length * 2 !== box.length) continue;
      if (points.some(p => p.low !== low && p.high !== high && p.color === 1 - low)) {
        single.push({ low_axis: 0, donor_low_bit: low, donor_balanced_high_bit: high });
      }
    }
  }
  if (single.length) return { central_single_side: single };
  if (total !== 4) return {};
  const C = [], P = [];
  for (const donor_high_bit of [0, 1]) {
    const A = points.filter(p => p.high === donor_high_bit), B = points.filter(p => p.high !== donor_high_bit);
    const source_color = Number(A.filter(p => p.color === 1).length * 2 > A.length);
    const r = A.filter(p => p.color !== source_color).length;
    const s = B.filter(p => p.color === source_color).length;
    const counts = (side, c) => [0, 1].map(z => side.filter(p => p.color === c && p.low === z).length);
    const sources = counts(A, source_color), minor = counts(B, source_color);
    const major = counts(B, 1 - source_color), gaps = major.map((n, i) => n - minor[i]);
    if (Math.min(...gaps) !== 1 || Math.max(...gaps) !== 2) continue;
    const two = gaps.indexOf(2);
    const witness = { low_axis: 0, donor_high_bit, source_color, donor_minor: r, receiver_minor: s,
      raw_receiver_gap: gaps, donor_major_by_low_bit: sources, receiver_minor_by_low_bit: minor };
    if (sources.every((n, i) => n >= gaps[i]) && minor[two] <= 1) C.push(witness);
    if (r === 2 && s === 2 && sources.every(n => n >= 1)) P.push({ ...witness, consumed_receiver_low_bit: two });
  }
  return Object.fromEntries([["delta3_controlled_circle", C], ["delta3_path", P]].filter(([, x]) => x.length));
}

const loadFour = [];
const loadFourFirst = {};
let columnsChecked = 0;
assert.deepEqual(data.single_column_table.map(x => x.weight), range(5));
for (const { weight, rows } of data.single_column_table) {
  const index = new Map(rows.map(x => [x.column.join(","), x.interfaces]));
  assert.equal(index.size, rows.length);
  for (const column of countVectors(weight)) {
    const hits = columnGates(column, weight);
    const key = column.join(",");
    assert.deepEqual(index.get(key), hits);
    assert(index.delete(key));
    if (weight === 4) {
      const [first] = Object.keys(hits);
      if (first) count(loadFourFirst, first);
      else loadFour.push(column);
    }
    columnsChecked++;
  }
  assert.equal(index.size, 0);
}
assert.equal(columnsChecked, 68);
assert.deepEqual(loadFour, [[0, 1, 0, 3], [0, 3, 0, 1]]);
assert.deepEqual(loadFourFirst, { central_single_side: 16, delta3_controlled_circle: 14, delta3_path: 1 });

function verifyTwoReturn(p, colors) {
  const j = p.outer, b = p.donor_side, k = p.inner, beta = p.donor_majority_parity, alpha = 1 - beta;
  assert(axes.includes(j) && axes.includes(k) && j !== k && [0, 1].includes(b) && [0, 1].includes(beta));
  const A = colors.map(xs => face(xs, j, b));
  const B = colors.map(xs => face(xs, j, 1 - b));
  assert.deepEqual([p.k, A[alpha].length, A[beta].length], [4, 0, 4]);
  const X = p.source_x, U = p.source_u;
  assert(subset(X, A[beta], 2) && subset(U, B[alpha], 2));
  const V = U.map(v => flip(v, j)), Y = X.map(v => flip(v, j));
  assert(V.concat(Y).every(v => !colors.flat().includes(v)));
  const I = A[beta].filter(v => !X.includes(v));
  assert.deepEqual(p.donor_minority, []);
  same(I, p.donor_retained); same(V, p.donor_marks); same(Y, p.receiver_marks);
  const d = p.donor_interface;
  assert.equal(d.kind, "T44_same_face");
  assert(axes.includes(d.inner) && d.inner !== j && [0, 1].includes(d.inner_side));
  assert(I.concat(V).every(v => bit(v, d.inner) === d.inner_side));
  const cols = axes.filter(i => i !== j && i !== k);
  assert.deepEqual(cols, p.receiver_axes);
  assert.equal(p.receiver_faces.length, 2);
  for (const [z, f] of p.receiver_faces.entries()) {
    const [l, m, y] = [B[beta], B[alpha].filter(v => !U.includes(v)).concat(Y), Y]
      .map(xs => face(xs, k, z).map(v => project(v, cols)));
    assert.equal(f.inner_side, z);
    same(l, f.minority); same(m, f.majority); same(y, f.marks);
    assert.deepEqual([m.length - l.length, y.length], [2, 1]);
    assert.equal(f.interface.kind, "avoid_one");
  }
}

const units = range(6).map(i => 1 << i);
const edges = [...subsets(units, 2)].map(xs => xs[0] | xs[1]);
const triples = [...subsets(units, 3)].map(xs => xs.reduce((a, b) => a | b));
const quads = [...subsets(units, 4)].map(xs => xs.reduce((a, b) => a | b));
const choices = (pool, n) => [...subsets(pool, n)];
const evenBase = choices(edges, 2).map(xs => [0, ...xs]);
const oddBase = choices(units, 4);
const maps = fixed => [...permutations(range(6).slice(fixed))]
  .map(p => range(64).map(h => permute(h, range(fixed).concat(p))));
const loads = hs => range(6).map(i => face(hs, i, 1).length);
const asGroups = (L, V) => [L, V].flatMap(xs => [0, 1].map(p => xs.filter(v => (v & 1) === p).map(v => v >> 1)));
const mask = hs => hs.reduce((n, h) => n | (1n << BigInt(h)), 0n);
const groupKey = groups => groups.map(xs => mask(xs).toString(16)).join("/");

function* aCompletions() {
  const edgeTriples = choices(edges, 3);
  const degrees = edgeTriples.map(edges => loads(edges));
  const byDegree = new Map();
  for (const [i, xs] of edgeTriples.entries()) {
    const k = degrees[i].join(",");
    if (!byDegree.has(k)) byDegree.set(k, []);
    byDegree.get(k).push(xs);
  }
  const unitTriples = choices(units, 3);
  for (const U of unitTriples) for (const W of unitTriples) {
    const cap = loads(U.concat(W)).map(n => 3 - n);
    for (const [i, G] of edgeTriples.entries()) {
      const complement = cap.map((n, j) => n - degrees[i][j]).join(",");
      for (const H of byDegree.get(complement) ?? []) yield [[0, ...G], U, [0, ...H], W];
    }
  }
}

function* bCompletions(name) {
  const odd = name === "Bodd" ? choices(units, 3).flatMap(xs => triples.map(v => xs.concat(v))) : oddBase;
  const even = name === "Beven" ? choices(edges, 3) :
    name === "Bquad" ? edges.flatMap(e => quads.map(q => [0, e, q])) : evenBase;
  yield* byGroups([odd, even, oddBase, evenBase], [3, 3, 3, 3, 3, 3]);
}

function* cCompletions() {
  const tail = units.slice(1);
  const units4 = choices(tail, 4);
  const lightSide = tail.flatMap(h => choices(tail, 2).map(xs => [0, xs[0] | xs[1], h | 1]));
  const heavySide = choices(tail.map(v => v | 1), 3);
  yield* byGroups([units4, lightSide, units4, heavySide], [4, 3, 3, 3, 3, 3]);
}

function* dCompletions() {
  const tail = units.slice(2);
  for (const left of choices(tail, 2)) {
    const right = tail.filter(h => !left.includes(h));
    yield [tail, [3, ...left.map(h => h | 2)], tail, [3, ...right.map(h => h | 1)]];
  }
}

function* byGroups(options, cap) {
  const prepared = options.map(rows => rows.map(hs => ({ hs, load: loads(hs) })));
  const groups = [];
  function* visit(i, load) {
    if (i === options.length) {
      yield [...groups];
      return;
    }
    for (const item of prepared[i]) {
      const next = load.map((v, j) => v + item.load[j]);
      if (next.some((v, j) => v > cap[j])) continue;
      if (i >= 2 && [0, 1].some(j => groups[j].some(h =>
        item.hs.some(t => wt[h ^ t] + Number((i % 2) !== j) === 6)))) continue;
      groups[i] = item.hs;
      yield* visit(i + 1, next);
    }
  }
  yield* visit(0, [0, 0, 0, 0, 0, 0]);
}

const full = maps(0), oneFixed = maps(1), twoFixed = maps(2);
const counts = {}, templates = {};
let totalLabeled = 0, totalReps = 0;
const names = ["A", "Bbase", "Bodd", "Beven", "Bquad", "C", "D"];
assert.deepEqual(Object.keys(data.stats), names);
for (const name of names) {
  const stat = data.stats[name];
  assert.equal(stat.status, "complete");
  const rows = data.rows.filter(r => r.template === name);
  assert.equal(rows.length, stat.representatives);
  assert.equal(rows.length, stat.gates_checked);
  const group = name === "C" ? oneFixed : name === "D" ? twoFixed : full;
  const expected = new Set();
  for (const row of rows) {
    const { L, V } = row;
    const e = Number(name !== "A");
    assert([L, V].every(xs => new Set(xs).size === 7 && xs.every(v => wt[v] % 2 === e)));
    assert(L.every(x => V.every(y => wt[x ^ y] !== 6)));
    const groups = asGroups(L, V);
    assert.deepEqual(groups.map(xs => xs.length), columnCap);
    const orbit = new Set(group.map(f => groupKey(groups.map(xs => xs.map(h => f[h])))));
    assert.equal(orbit.size, row.orbit_size);
    for (const k of orbit) {
      assert(!expected.has(k), "overlapping high-coordinate orbits");
      expected.add(k);
    }
    const physical = V.map(v => v ^ 127);
    const colors = e === 0 ? [L, physical] : [physical, L];
    same(colors[0], row.even); same(colors[1], row.odd);
    const gaps = axes.map(j => face(colors[0], j, 1).length - face(colors[1], j, 1).length);
    assert.deepEqual(gaps, row.gaps);
    assert.equal(gaps[0], 2 * e - 1);
    assert(gaps.slice(1).every(g => (1 - 2 * e) * g <= -3));
    if (row.plan.gate === "controlled_two_return") verifyTwoReturn(row.plan, colors);
    else verifyPlan(row.plan, colors);
    count(counts, row.plan.gate);
  }
  assert.equal(expected.size, stat.labeled);
  const generated = name === "A" ? aCompletions() : name === "C" ? cCompletions() :
    name === "D" ? dCompletions() : bCompletions(name);
  let labeled = 0;
  for (const groups of generated) {
    assert(expected.delete(groupKey(groups)), "missing labeled completion for " + name);
    labeled++;
  }
  assert.equal(expected.size, 0, "extra labeled completions for " + name);
  assert.equal(labeled, stat.labeled);
  totalLabeled += labeled;
  totalReps += rows.length;
  templates[name] = { labeled, representatives: rows.length };
}
assert.equal(totalLabeled, data.labeled);
assert.equal(totalReps, data.rows.length);
assert.equal(totalReps, data.gates_checked);
assert.equal(totalReps, data.representatives);
assert.deepEqual(counts, data.plans);

console.log(JSON.stringify({
  sourceSha256: sha(source), checkerSha256: sha("R7_MU1_CENTRAL_T1_REVIEW_CHECK.cjs"),
  columnsChecked, loadFour, loadFourFirst, templates, labeled: totalLabeled, representatives: totalReps,
  planCounts: counts, gateReasons, donorKinds, oldKinds, receivers, exactCores: Object.keys(cores).map(Number),
  core1054Uses: cores[1054], core1054ReviewSha256: sha(review1054),
  matchingCalls: 0, hamiltonCalls: 0, rankRuns: 0,
}, null, 2));


