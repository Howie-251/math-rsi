(() => {
  'use strict';

  const root = document.getElementById('results');
  if (!root) return;

  const f2 = n => Number(n.toFixed(2));
  const svgWrap = (ariaLabel, body) =>
    `<svg class="rv-svg" viewBox="0 0 380 256" role="img" aria-label="${ariaLabel}">${body}</svg>`;

  const CONFIG = {
    pb: {
      resultLabel:
        'Property B results: pointwise lower-bound gains +3 to +31 for k = 5 to 12 on a linear scale, and certified uniform-theorem lower-bound gains from at least 2 at k = 12 to at least 152,837,269 at k = 64 on an independent log10 scale.',
      resultCap:
        'Lower-bound gains over the stated references. Uniform samples: guaranteed gain over the combined RS baseline, on a separate log scale.',
      links: [
        { label: 'Full figure ↗', href: 'assets/result-figures/property-b-delta.svg' }
      ],
      render() {
        // Panel A: True continuous linear scale for k = 5..12, gain in [0, 31]
        const gains = [
          [5, 3], [6, 3], [7, 3], [8, 4],
          [9, 5], [10, 27], [11, 30], [12, 31]
        ];
        const baseA = 98, maxH = 45, maxG = 31;
        const y30 = f2(baseA - (30 / maxG) * maxH);
        let bars = '';
        gains.forEach(([k, g]) => {
          const cx = 62 + (k - 5) * 40;
          const bh = f2((g / maxG) * maxH);
          const by = f2(baseA - bh);
          bars += `
            <rect x="${cx - 10}" y="${by}" width="20" height="${bh}" rx="3" fill="var(--pb)" fill-opacity="0.24" stroke="var(--pb)" stroke-width="1.2"/>
            <text x="${cx}" y="${f2(by - 5)}" text-anchor="middle" font-size="11" font-weight="650" class="rv-accent">+${g}</text>
            <text x="${cx}" y="${baseA + 14}" text-anchor="middle" class="rv-sub">${k === 5 ? 'k=5' : k}</text>`;
        });

        // Panel B: True linear k in [12, 64] and true log10(gain) in [0, 8.2]
        const xK = k => f2(72 + ((k - 12) / (64 - 12)) * 268);
        const yLog = e => f2(220 - (e / 8) * 52);
        const y0 = yLog(0), y4 = yLog(4), y8 = yLog(8);

        const samples = [
          { k: 12, val: 2, label: '≥2', anchor: 'start', dx: 7, dy: -6 },
          { k: 32, val: 2346, label: '≥2,346', anchor: 'middle', dx: 0, dy: -9 },
          { k: 64, val: 152837269, label: '≥152,837,269', anchor: 'end', dx: -10, dy: -2 }
        ].map(s => ({
          ...s,
          x: xK(s.k),
          y: yLog(Math.log10(s.val))
        }));

        const poly = samples.map(p => `${p.x},${p.y}`).join(' ');
        let nodes = '';
        samples.forEach(p => {
          nodes += `
            <line x1="${p.x}" y1="${p.y}" x2="${p.x}" y2="${y0}" class="rv-grid"/>
            <circle cx="${p.x}" cy="${p.y}" r="4.2" fill="#1D4ED8" stroke="#fff" stroke-width="1.5"/>
            <text x="${f2(p.x + p.dx)}" y="${f2(p.y + p.dy)}" text-anchor="${p.anchor}" font-size="11.5" font-weight="650" fill="#1E40AF">${p.label}</text>
            <text x="${p.x}" y="236" text-anchor="middle" class="rv-sub">k=${p.k}</text>`;
        });

        return svgWrap(this.resultLabel, `
          <!-- Panel A: Pointwise bounds (linear scale) -->
          <rect class="rv-panel" x="14" y="10" width="352" height="108" rx="10"/>
          <text class="rv-h" x="24" y="28">Pointwise gain</text>
          <text class="rv-meta" x="354" y="28" text-anchor="end">k = 5–12 · linear scale</text>
          <line class="rv-grid" x1="44" y1="${y30}" x2="354" y2="${y30}"/>
          <text class="rv-sub" x="38" y="${f2(y30 + 3.5)}" text-anchor="end">30</text>
          <line class="rv-axis" x1="44" y1="${baseA}" x2="354" y2="${baseA}"/>
          <text class="rv-sub" x="38" y="${baseA + 3.5}" text-anchor="end">0</text>
          ${bars}

          <!-- Panel B: Uniform theorem (true log10 scale) -->
          <rect class="rv-panel" x="14" y="126" width="352" height="120" rx="10" style="fill:#F4F7FB;stroke:#C9D8EE"/>
          <text class="rv-h" x="24" y="145" fill="#1E3A8A">Uniform gain</text>
          <text class="rv-meta" x="354" y="145" text-anchor="end" fill="#1E40AF">all k ≥ 12 · log₁₀ scale</text>
          <line class="rv-grid" x1="52" y1="${y8}" x2="354" y2="${y8}"/>
          <text class="rv-sub" x="46" y="${f2(y8 + 3.5)}" text-anchor="end">10⁸</text>
          <line class="rv-grid" x1="52" y1="${y4}" x2="354" y2="${y4}"/>
          <text class="rv-sub" x="46" y="${f2(y4 + 3.5)}" text-anchor="end">10⁴</text>
          <line class="rv-axis" x1="52" y1="${y0}" x2="354" y2="${y0}"/>
          <text class="rv-sub" x="46" y="${f2(y0 + 3.5)}" text-anchor="end">10⁰</text>
          <polyline points="${poly}" fill="none" stroke="#1D4ED8" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
          ${nodes}
        `);
      }
    },

    ecc: {
      resultLabel:
        'Binary linear code minimum distance improvements across five parameters: d2(43,10) from 16–17 to 16, d2(44,10) from 17–18 to 17, d2(44,11) from 16–17 to 16, d2(42,16) from 12–13 to 12, and d2(45,11) narrowed from 16–18 to 16–17 (open).',
      resultCap:
        'Results · five code parameters (prior range → settled optimal d₂ or narrowed interval)',
      links: [
        { label: 'Full figure ↗', href: 'assets/result-figures/ecc-five-parameters.png' },
        { label: 'Method ↗', href: 'assets/result-figures/ecc-method-results.png', sub: true }
      ],
      render() {
        const rows = [
          { p: '[43, 10]', prev: '16–17', cur: '16', kind: 'exact', status: 'Exact' },
          { p: '[44, 10]', prev: '17–18', cur: '17', kind: 'exact', status: 'Exact' },
          { p: '[44, 11]', prev: '16–17', cur: '16', kind: 'exact', status: 'Exact' },
          { p: '[42, 16]', prev: '12–13', cur: '12*', kind: 'lit', status: 'Exact*' },
          { p: '[45, 11]', prev: '16–18', cur: '16–17', kind: 'open', status: 'Open' }
        ];
        let body = `
          <defs>
            <pattern id="rv-ecc-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
              <rect width="6" height="6" fill="#fff"/>
              <line x1="0" y1="0" x2="0" y2="6" stroke="var(--ecc)" stroke-opacity="0.32" stroke-width="2"/>
            </pattern>
            <marker id="rv-ecc-arr" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M1 1L7 4L1 7" fill="none" stroke="var(--ecc)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
            </marker>
          </defs>
          <text class="rv-h" x="18" y="23">Optimal distance d₂(n, k)</text>
          <text class="rv-meta" x="362" y="23" text-anchor="end">prior range → result</text>`;

        rows.forEach((r, i) => {
          const y = 34 + i * 38;
          const cy = y + 17;
          let badge = '';
          if (r.kind === 'exact') {
            badge = `<rect x="210" y="${y + 5}" width="62" height="24" rx="6" fill="var(--ecc)"/>
                     <text x="241" y="${cy + 4}" text-anchor="middle" font-size="13.5" font-weight="650" fill="#fff">${r.cur}</text>`;
          } else if (r.kind === 'lit') {
            badge = `<rect x="210" y="${y + 5}" width="62" height="24" rx="6" fill="var(--ecc)" fill-opacity="0.14" stroke="var(--ecc)" stroke-width="1.4"/>
                     <text x="241" y="${cy + 4}" text-anchor="middle" font-size="13.5" font-weight="650" class="rv-accent">${r.cur}</text>`;
          } else {
            badge = `<rect x="210" y="${y + 5}" width="62" height="24" rx="6" fill="url(#rv-ecc-hatch)" stroke="var(--ecc)" stroke-width="1.4" stroke-dasharray="3 2"/>
                     <text x="241" y="${cy + 4}" text-anchor="middle" font-size="12.5" font-weight="650" fill="var(--ink)">${r.cur}</text>`;
          }
          body += `
            <rect class="rv-panel" x="14" y="${y}" width="352" height="34" rx="8"/>
            <text x="28" y="${cy + 4}" font-size="13" font-weight="640" fill="var(--ink)">${r.p}</text>
            <rect x="112" y="${y + 6}" width="58" height="22" rx="5" fill="#F1F3F7"/>
            <text x="141" y="${cy + 4}" text-anchor="middle" font-size="12" font-weight="540" fill="var(--muted)">${r.prev}</text>
            <line x1="178" y1="${cy}" x2="202" y2="${cy}" stroke="var(--ecc)" stroke-width="1.5" marker-end="url(#rv-ecc-arr)"/>
            ${badge}
            <text x="352" y="${cy + 4}" text-anchor="end" font-size="11.5" font-weight="${r.kind === 'open' ? '500' : '620'}" fill="${r.kind === 'open' ? 'var(--muted)' : 'color-mix(in srgb,var(--ecc) 82%,#000)'}">${r.status}</text>`;
        });

        body += `<text class="rv-meta" x="190" y="241" text-anchor="middle">4 exact values · 1 narrowed interval</text>`;
        return svgWrap(this.resultLabel, body);
      }
    },

    dd: {
      resultLabel: 'Vertex gains over dated Comellas entries on one linear scale: (10,4) 2,566 to 2,567 (+1); (11,5) 37,628 to 37,631 (+3); (12,5) 42,342 to 42,402 (+60); (16,4) 16,384 to 16,416 (+32).',
      resultCap: 'Results · vertex gains over dated Comellas entries · one linear scale',
      links: [
        { label: '(10,4) details ↗', href: 'dd-10-4.html' },
        { label: 'Earlier figure ↗', href: 'assets/result-figures/degree-diameter-results.svg', sub: true }
      ],
      render() {
        const items = [
          { p:'(10, 4)', sub:'deg 10 · diam 4', prev:'2,566', cur:'2,567', gain:1, isNew:true },
          { p:'(11, 5)', sub:'deg 11 · diam 5', prev:'37,628', cur:'37,631', gain:3 },
          { p:'(12, 5)', sub:'deg 12 · diam 5', prev:'42,342', cur:'42,402', gain:60 },
          { p:'(16, 4)', sub:'deg 16 · diam 4', prev:'16,384', cur:'16,416', gain:32 }
        ];
        const barX = 122, maxW = 178;
        let body = `<text class="rv-h" x="18" y="22">Vertex gains at fixed (d, D)</text>
          <text class="rv-meta" x="362" y="22" text-anchor="end">previous → new order</text>`;
        items.forEach((it, i) => {
          const y = 32 + i * 53, w = f2((it.gain / 60) * maxW);
          body += `<rect class="rv-panel" x="14" y="${y}" width="352" height="47" rx="9" ${it.isNew ? 'style="fill:#fff3e8"' : ''}/>
            <text x="26" y="${y + 20}" font-size="13.5" font-weight="650" fill="var(--ink)">${it.p}</text>
            ${it.isNew ? `<text x="81" y="${y + 20}" font-size="8" fill="var(--dd)">NEW</text>` : ''}
            <text x="26" y="${y + 36}" class="rv-sub">${it.sub}</text>
            <text x="${barX}" y="${y + 19}" font-size="12.5" fill="var(--muted)">${it.prev} <tspan fill="var(--ink-2)">→</tspan> <tspan font-weight="650" fill="var(--ink)">${it.cur}</tspan></text>
            <rect x="${barX}" y="${y + 28}" width="${maxW}" height="10" rx="3.5" fill="#EEF1F6"/>
            <rect x="${barX}" y="${y + 28}" width="${w}" height="10" rx="${f2(Math.min(3.5, w / 2))}" fill="var(--dd)"/>
            <text x="352" y="${y + 27}" text-anchor="end" font-size="16" font-weight="680" class="rv-accent">+${it.gain}</text>`;
        });
        return svgWrap(this.resultLabel, body);
      }
    },

    e86: {
      resultLabel:
        'Erdős Problem 86 asymptotic C4-free edge density upper bound in Qn lowered from the 0.60318 reference to at most 0.59155154, narrowing the gap toward the open 1/2 conjecture.',
      resultCap:
        'Results · asymptotic C₄-free density ceiling lowered from 0.60318 to ≤ 0.59155154',
      links: [
        { label: 'Source report ↗', href: '../../../plugins/hypercube-extremal/archive/source/START_HERE.html' }
      ],
      render() {
        const e = [[15, 0], [0, 15], [7, -6], [34, 4]];
        const o = [288, 39];
        const P = Array.from({ length: 16 }, (_, v) => {
          let x = o[0], y = o[1];
          for (let j = 0; j < 4; j++) if ((v >> j) & 1) { x += e[j][0]; y += e[j][1]; }
          return [x, y];
        });
        let q4 = '';
        for (let v = 0; v < 16; v++) {
          for (let j = 0; j < 4; j++) {
            if (!((v >> j) & 1)) {
              const w = v | (1 << j);
              q4 += `<line x1="${P[v][0]}" y1="${P[v][1]}" x2="${P[w][0]}" y2="${P[w][1]}" stroke="#C5CCD6" stroke-width="0.9"/>`;
            }
          }
        }
        q4 += `<polygon points="${[0, 1, 3, 2].map(i => P[i].join(',')).join(' ')}" fill="var(--e86)" fill-opacity="0.16" stroke="var(--e86)" stroke-width="1.6"/>`;

        const X = v => 44 + ((v - 0.49) / 0.125) * 292;
        const xHalf = f2(X(0.5));
        const xNew = f2(X(0.59155154));
        const xRef = f2(X(0.60318));

        return svgWrap(this.resultLabel, `
          <defs>
            <marker id="rv-e86-arr" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M1 1L7 4L1 7" fill="none" stroke="var(--e86)" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
            </marker>
          </defs>

          <!-- Top summary card with separated mini Q4 inset -->
          <rect class="rv-panel" x="14" y="12" width="352" height="84" rx="10"/>
          <text class="rv-kicker" x="26" y="32">Asymptotic C₄-free density</text>
          <text x="26" y="60" font-size="14" font-weight="540" fill="var(--muted)">0.60318 <tspan fill="var(--ink-2)">→</tspan> <tspan font-size="20" font-weight="680" class="rv-accent">≤ 0.59155154</tspan></text>
          <text class="rv-sub" x="26" y="80">Lower ceiling is tighter</text>
          <line x1="266" y1="20" x2="266" y2="88" stroke="var(--hair)"/>
          ${q4}
          <text class="rv-sub" x="316" y="82" text-anchor="middle">C₄ in Q₄</text>

          <!-- Bottom density scale -->
          <rect class="rv-panel" x="14" y="106" width="352" height="138" rx="10"/>
          <text class="rv-h" x="26" y="127">Upper-bound scale</text>

          <!-- Open gap vs closed reduction on axis y=180 -->
          <rect x="${xHalf}" y="176" width="${f2(xNew - xHalf)}" height="8" rx="4" fill="#EEF1F6"/>
          <rect x="${xNew}" y="175" width="${f2(xRef - xNew)}" height="10" rx="4" fill="var(--e86)" fill-opacity="0.26"/>
          <line class="rv-axis" x1="36" y1="180" x2="344" y2="180"/>

          <!-- Arrow showing reduction from 0.60318 down to 0.59155154 -->
          <path d="M${xRef} 158H${f2(xNew + 4)}" fill="none" stroke="var(--e86)" stroke-width="1.8" marker-end="url(#rv-e86-arr)"/>

          <!-- Markers -->
          <circle cx="${xHalf}" cy="180" r="5.5" fill="#fff" stroke="var(--muted)" stroke-width="1.6" stroke-dasharray="2 2"/>
          <circle cx="${xRef}" cy="180" r="5" fill="#fff" stroke="#98A2B3" stroke-width="1.8"/>
          <circle cx="${xNew}" cy="180" r="6.5" fill="var(--e86)" stroke="#fff" stroke-width="1.8"/>

          <!-- Labels with wide horizontal clearance -->
          <text x="${xHalf}" y="154" text-anchor="middle" font-size="12.5" font-weight="620" fill="var(--ink-2)">1/2 (0.5)</text>
          <text x="${xHalf}" y="206" text-anchor="middle" class="rv-sub">Conjecture (open)</text>

          <text x="${f2(xNew - 8)}" y="152" text-anchor="end" font-size="13.5" font-weight="680" class="rv-accent">≤ 0.59155154</text>
          <text x="${f2(xNew - 6)}" y="206" text-anchor="end" font-size="11" font-weight="640" class="rv-accent">New bound</text>

          <text x="${f2(xRef + 8)}" y="152" text-anchor="start" font-size="12" font-weight="540" fill="var(--muted)">0.60318</text>
          <text x="${f2(xRef + 6)}" y="206" text-anchor="start" class="rv-sub">Reference</text>
        `);
      }
    },

    q6: {
      resultLabel:
        'Ruskey–Savage Q6 theorem diagram: every matching in Q6 is contained in a Hamilton cycle visiting all 64 vertices; with imported results, every matching in Qn using at most six directions also extends to a Hamilton cycle.',
      resultCap:
        'Results · universal Q₆ theorem and six-direction extension in Qₙ (with example instance)',
      links: [
        { label: 'Source report ↗', href: '../../../plugins/hypercube-hamilton/archive/source/Ruskey-Savage_Q6_研究报告.html' }
      ],
      render(problemSvg) {
        const inset = problemSvg ? problemSvg.innerHTML : '';
        return svgWrap(this.resultLabel, `
          <defs>
            <marker id="rv-q6-arr" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M1 1L7 4L1 7" fill="none" stroke="var(--q6)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
            </marker>
          </defs>

          <!-- Primary Q6 universal theorem flow -->
          <rect class="rv-panel" x="14" y="12" width="226" height="138" rx="10"/>
          <text class="rv-kicker" x="26" y="30">Q₆ theorem</text>

          <rect x="24" y="38" width="206" height="34" rx="7" fill="#F3F5F8" stroke="var(--hair)"/>
          <text x="127" y="59" text-anchor="middle" font-size="12.5" font-weight="650" fill="var(--ink)">Every matching in Q₆</text>

          <line x1="127" y1="73" x2="127" y2="95" stroke="var(--q6)" stroke-width="1.7" marker-end="url(#rv-q6-arr)"/>
          <text x="135" y="87" font-size="10.5" font-weight="600" class="rv-accent">extends to</text>

          <rect class="rv-panel-tint" x="24" y="98" width="206" height="40" rx="7"/>
          <text x="127" y="115" text-anchor="middle" font-size="12.5" font-weight="650" fill="var(--ink)">Hamilton cycle in Q₆</text>
          <text class="rv-sub" x="127" y="130" text-anchor="middle" fill="var(--ink-2)">all 64 vertices</text>

          <!-- Right inset: single example instance reused from original SVG -->
          <rect class="rv-panel" x="248" y="12" width="118" height="138" rx="10"/>
          <text class="rv-meta" x="307" y="29" text-anchor="middle">1 example</text>
          <g transform="translate(247 26) scale(0.375)">${inset}</g>
          <text class="rv-sub" x="307" y="137" text-anchor="middle">matching ⊂ cycle</text>

          <!-- Secondary node: arbitrary dimension Qn corollary -->
          <rect class="rv-panel" x="14" y="160" width="352" height="84" rx="10" stroke-dasharray="4 3"/>
          <text class="rv-kicker" x="26" y="180">Qₙ extension</text>
          <text class="rv-meta" x="354" y="180" text-anchor="end">with imported results</text>
          <text x="26" y="204" font-size="12.5" font-weight="620" fill="var(--ink)">Every matching in Qₙ using ≤ 6 directions</text>
          <text x="26" y="225" font-size="12.5" font-weight="650" class="rv-accent">→ contained in a Hamilton cycle</text>
        `);
      }
    },

    he: {
      resultLabel:
        'Happy Ending working proof results: ES(7) geometric upper bound lowered from 78 to 77, derived via the cross-parameter proof chain N(7,6,7) <= 75 to N(7,7,7) <= 76 to ES(7) <= 77.',
      resultCap:
        'Results · ES(7) upper bound 78 → 77 and cross-parameter proof chain (working proof)',
      links: [
        { label: 'Full figure ↗', href: 'assets/result-figures/happy-ending-bounds.svg' }
      ],
      render() {
        return svgWrap(this.resultLabel, `
          <defs>
            <marker id="rv-he-arr" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M1 1L7 4L1 7" fill="none" stroke="var(--he)" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
            </marker>
            <marker id="rv-he-chain" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M1 1L7 4L1 7" fill="none" stroke="#667085" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </marker>
          </defs>

          <!-- Top banner: same-metric upper bound improvement 78 -> 77 -->
          <rect class="rv-panel-dash" x="14" y="12" width="352" height="80" rx="10"/>
          <text class="rv-h" x="26" y="32">ES(7) upper bound</text>
          <text x="354" y="32" text-anchor="end" font-size="11" font-weight="650" class="rv-accent">Working proof</text>
          <text x="26" y="68" font-size="21" font-weight="600" fill="var(--muted)">78</text>
          <line x1="60" y1="60" x2="90" y2="60" stroke="var(--he)" stroke-width="2" marker-end="url(#rv-he-arr)"/>
          <text x="100" y="69" font-size="25" font-weight="700" class="rv-accent">≤ 77</text>
          <text class="rv-meta" x="176" y="65">planar points for a convex 7-gon</text>

          <!-- Bottom panel: cross-parameter proof chain (75 -> 76 -> 77) -->
          <rect class="rv-panel" x="14" y="102" width="352" height="142" rx="10"/>
          <text class="rv-h" x="26" y="122">Proof chain</text>
          <text class="rv-meta" x="354" y="122" text-anchor="end">from N(7,4,7) = 16, N(7,5,6) = 25</text>

          <!-- Node 1: N(7,6,7) <= 75 -->
          <rect x="24" y="136" width="94" height="92" rx="8" fill="#FAF6EE" stroke="#E5D5B5"/>
          <text class="rv-sub" x="71" y="156" text-anchor="middle">Restricted bound</text>
          <text x="71" y="184" text-anchor="middle" font-size="12.5" font-weight="650" fill="var(--ink)">N(7,6,7) ≤ 75</text>
          <text class="rv-sub" x="71" y="210" text-anchor="middle" fill="#8C581C">3 · N(7,5,6)</text>

          <line x1="121" y1="180" x2="140" y2="180" stroke="#667085" stroke-width="1.5" marker-end="url(#rv-he-chain)"/>
          <text x="130" y="170" text-anchor="middle" font-size="10.5" font-weight="650" fill="var(--ink-2)">+1</text>

          <!-- Node 2: N(7,7,7) <= 76 -->
          <rect x="143" y="136" width="94" height="92" rx="8" fill="#FAF6EE" stroke="#E5D5B5"/>
          <text class="rv-sub" x="190" y="156" text-anchor="middle">Avoiding capacity</text>
          <text x="190" y="184" text-anchor="middle" font-size="12.5" font-weight="650" fill="var(--ink)">N(7,7,7) ≤ 76</text>
          <text class="rv-sub" x="190" y="210" text-anchor="middle" fill="#8C581C">N(7,6,7) + 1</text>

          <line x1="240" y1="180" x2="259" y2="180" stroke="#667085" stroke-width="1.5" marker-end="url(#rv-he-chain)"/>
          <text x="249" y="170" text-anchor="middle" font-size="10.5" font-weight="650" fill="var(--ink-2)">+1</text>

          <!-- Node 3: ES(7) <= 77 -->
          <rect class="rv-panel-dash" x="262" y="136" width="94" height="92" rx="8"/>
          <text x="309" y="156" text-anchor="middle" font-size="10" font-weight="640" class="rv-accent">Convex 7-gon</text>
          <text x="309" y="184" text-anchor="middle" font-size="13.5" font-weight="680" class="rv-accent">ES(7) ≤ 77</text>
          <text class="rv-sub" x="309" y="210" text-anchor="middle">N(7,7,7) + 1</text>
        `);
      }
    }
  };

  root.querySelectorAll('.viz[data-viz]').forEach(viz => {
    const id = viz.dataset.viz;
    const cfg = CONFIG[id];
    const problemSvg = viz.querySelector('svg');
    if (!cfg || !problemSvg) return;

    const card = viz.closest('.card');
    const vcap = card ? card.querySelector('.vcap') : null;
    const problemLabel = viz.getAttribute('aria-label') || `${id} problem illustration`;
    const problemCap = vcap ? vcap.textContent : '';

    viz.removeAttribute('role');
    viz.removeAttribute('aria-label');
    viz.classList.add('rv-ready');

    problemSvg.classList.add('rv-problem-svg');
    problemSvg.setAttribute('aria-label', problemLabel);

    const bar = document.createElement('div');
    bar.className = 'rv-bar';
    const linksHtml = cfg.links
      .map(
        l =>
          `<a class="rv-link${l.sub ? ' rv-link-sub' : ''}" href="${l.href}" target="_blank" rel="noopener">${l.label}</a>`
      )
      .join('');
    bar.innerHTML = `
      <div class="rv-tabs" role="group" aria-label="Visual mode">
        <button type="button" class="rv-tab is-on" data-rv-mode="result" aria-pressed="true">Results</button>
        <button type="button" class="rv-tab" data-rv-mode="problem" aria-pressed="false">Problem</button>
      </div>
      <div class="rv-links">${linksHtml}</div>
    `;

    const stage = document.createElement('div');
    stage.className = 'rv-stage';
    stage.innerHTML = cfg.render(problemSvg);
    const resultSvg = stage.querySelector('svg');
    stage.appendChild(problemSvg);

    viz.innerHTML = '';
    viz.appendChild(bar);
    viz.appendChild(stage);

    const btns = [...bar.querySelectorAll('.rv-tab')];
    const setMode = mode => {
      const isResult = mode === 'result';
      btns.forEach(b => {
        const on = b.dataset.rvMode === mode;
        b.classList.toggle('is-on', on);
        b.setAttribute('aria-pressed', String(on));
      });
      if (isResult) {
        resultSvg.removeAttribute('hidden');
        resultSvg.removeAttribute('aria-hidden');
        resultSvg.setAttribute('role', 'img');
        problemSvg.setAttribute('hidden', '');
        problemSvg.setAttribute('aria-hidden', 'true');
        problemSvg.removeAttribute('role');
        if (vcap) vcap.textContent = cfg.resultCap;
      } else {
        problemSvg.removeAttribute('hidden');
        problemSvg.removeAttribute('aria-hidden');
        problemSvg.setAttribute('role', 'img');
        resultSvg.setAttribute('hidden', '');
        resultSvg.setAttribute('aria-hidden', 'true');
        resultSvg.removeAttribute('role');
        if (vcap) vcap.textContent = problemCap;
      }
    };

    bar.addEventListener('click', e => {
      const btn = e.target.closest('.rv-tab');
      if (btn) setMode(btn.dataset.rvMode);
    });

    bar.addEventListener('keydown', e => {
      if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
      const cur = btns.findIndex(b => b === document.activeElement);
      if (cur < 0) return;
      e.preventDefault();
      const next = btns[(cur + 1) % btns.length];
      next.focus();
      setMode(next.dataset.rvMode);
    });

    setMode('result');
  });
})();
