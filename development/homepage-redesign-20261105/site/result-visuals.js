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
        { label: 'Full figure ↗', href: 'assets/result-figures/property-b-delta.svg', sourceLanguage: 'EN' }
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
        { label: 'Full figure ↗', href: 'assets/result-figures/ecc-five-parameters.png', sourceLanguage: '中文' },
        { label: 'Method ↗', href: 'assets/result-figures/ecc-method-results.png', sourceLanguage: '中文', sub: true }
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
      resultLabel: 'Our best constructions by setting: (10,4) 2,567; (11,5) 37,632; (12,5) 42,433; (16,4) 16,416 vertices.',
      resultCap: 'Results · our best constructions by setting',
      links: [
        { label: 'Results by setting ↗', href: 'dd-latest.html', sourceLanguage: 'EN + 中文' },
        { label: '(10,4) construction ↗', href: 'dd-10-4.html', sourceLanguage: 'EN', sub: true }
      ],
      render() {
        const rows = [['(10, 4)','2,567'],['(11, 5)','37,632'],['(12, 5)','42,433'],['(16, 4)','16,416']];
        let body = `<text class="rv-h" x="18" y="22">Four showcased settings</text>`;
        rows.forEach(([parameter, vertices], i) => {
          const y = 34 + i * 46;
          body += `<rect class="rv-panel" x="14" y="${y}" width="352" height="41" rx="9"/>
            <text x="26" y="${y + 26}" font-size="14" font-weight="550" fill="var(--ink-2)">${parameter}</text>
            <text x="352" y="${y + 27}" text-anchor="end" font-size="21" font-weight="680" class="rv-accent">${vertices}</text>`;
        });
        body += `<text class="rv-sub" x="18" y="242">Vertices in our constructions</text>`;
        return svgWrap(this.resultLabel, body);
      }
    },

    e86: {
      resultLabel:
        'Erdős Problem 86 results by setting: Q7 construction 304 verified (304 upper bound source-reported), Q8 narrowed to 682–683, and asymptotic C4-free density lowered from 0.60318 to at most 0.5912405943 (T3) and 0.5912405942 (T4).',
      resultCap:
        'Results · Q₇ 304 (≤ source), Q₈ 682–683 and asymptotic Q∞ ≤ 0.5912405943',
      links: [
        { label: 'Results by setting ↗', href: 'erdos-86-latest.html', sourceLanguage: 'EN + 中文' },
        { label: 'Historical Q₄ ↗', href: '../../../plugins/hypercube-extremal/archive/source/START_HERE.html', sourceLanguage: '中文', sub: true }
      ],
      render() {
        const X = v => 44 + ((v - 0.49) / 0.125) * 292;
        const xHalf = f2(X(0.5));
        const xNew = f2(X(0.5912405943));
        const xRef = f2(X(0.60318));

        return svgWrap(this.resultLabel, `
          <defs>
            <marker id="rv-e86-arr" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M1 1L7 4L1 7" fill="none" stroke="var(--e86)" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
            </marker>
          </defs>

          <!-- Top summary: three settings side-by-side -->
          <rect class="rv-panel" x="14" y="10" width="352" height="104" rx="10"/>
          <text class="rv-h" x="24" y="28">Three C₄-free cube settings</text>
          <text class="rv-meta" x="356" y="28" text-anchor="end">finite &amp; limit</text>

          <rect x="22" y="36" width="102" height="68" rx="7" fill="#F8F9FB" stroke="var(--hair)"/>
          <text class="rv-sub" x="73" y="52" text-anchor="middle">Q₇ (n = 7)</text>
          <text x="73" y="75" text-anchor="middle" font-size="17.5" font-weight="680" class="rv-accent">≥ 304</text>
          <text class="rv-sub" x="73" y="94" text-anchor="middle">≤304 in source</text>

          <rect x="130" y="36" width="108" height="68" rx="7" fill="#F8F9FB" stroke="var(--hair)"/>
          <text class="rv-sub" x="184" y="52" text-anchor="middle">Q₈ (n = 8)</text>
          <text x="184" y="75" text-anchor="middle" font-size="17" font-weight="680" class="rv-accent">682–683</text>
          <text class="rv-sub" x="184" y="94" text-anchor="middle">≤682 open</text>

          <rect x="244" y="36" width="114" height="68" rx="7" fill="#F8F9FB" stroke="var(--hair)"/>
          <text class="rv-sub" x="301" y="52" text-anchor="middle">Q∞ density</text>
          <text x="301" y="74" text-anchor="middle" font-size="11.2" font-weight="680" class="rv-accent">≤ 0.5912405943</text>
          <text class="rv-sub" x="301" y="94" text-anchor="middle">T3/T4 proved</text>

          <!-- Bottom density scale (Q_infty only) -->
          <rect class="rv-panel" x="14" y="122" width="352" height="122" rx="10"/>
          <text class="rv-h" x="24" y="141">Asymptotic Q∞ scale</text>
          <text class="rv-meta" x="356" y="141" text-anchor="end">T4 ≤ 0.5912405942</text>

          <rect x="${xHalf}" y="186" width="${f2(xNew - xHalf)}" height="8" rx="4" fill="#EEF1F6"/>
          <rect x="${xNew}" y="185" width="${f2(xRef - xNew)}" height="10" rx="4" fill="var(--e86)" fill-opacity="0.26"/>
          <line class="rv-axis" x1="36" y1="190" x2="344" y2="190"/>

          <path d="M${xRef} 168H${f2(xNew + 4)}" fill="none" stroke="var(--e86)" stroke-width="1.8" marker-end="url(#rv-e86-arr)"/>

          <circle cx="${xHalf}" cy="190" r="5.5" fill="#fff" stroke="var(--muted)" stroke-width="1.6" stroke-dasharray="2 2"/>
          <circle cx="${xRef}" cy="190" r="5" fill="#fff" stroke="#98A2B3" stroke-width="1.8"/>
          <circle cx="${xNew}" cy="190" r="6.5" fill="var(--e86)" stroke="#fff" stroke-width="1.8"/>

          <text x="${xHalf}" y="166" text-anchor="middle" font-size="12" font-weight="620" fill="var(--ink-2)">1/2 (0.5)</text>
          <text x="${xHalf}" y="216" text-anchor="middle" class="rv-sub">Conjecture (open)</text>

          <text x="${f2(xNew - 8)}" y="164" text-anchor="end" font-size="12.5" font-weight="680" class="rv-accent">≤ 0.5912405943</text>
          <text x="${f2(xNew - 6)}" y="216" text-anchor="end" font-size="11" font-weight="640" class="rv-accent">T3 bound</text>

          <text x="${f2(xRef + 8)}" y="164" text-anchor="start" font-size="12" font-weight="540" fill="var(--muted)">0.60318</text>
          <text x="${f2(xRef + 6)}" y="216" text-anchor="start" class="rv-sub">Reference</text>
        `);
      }
    },

    q6: {
      resultLabel: "Ruskey–Savage: full Q7 author working proof for every matching, all 128 vertices, preserving every edge; Q6 universal theorem retained; the at-most-six-direction corollary uses prescribed-endpoint P6 and published lifting results.",
      resultCap: "Results · Q₇ full author working proof; Q₆ theorem retained",
      links: [
        { label: 'Q7 result & methods ↗', href: 'q7.html', sourceLanguage: 'EN + 中文' },
        { label: 'Q6 report ↗', href: '../../../plugins/hypercube-hamilton/archive/source/Ruskey-Savage_Q6_研究报告.html', sourceLanguage: '中文', sub: true }
      ],
      render(problemSvg) {
        const inset = problemSvg ? problemSvg.innerHTML : '';
        return svgWrap(this.resultLabel, `
          <defs><marker id="rv-q6-arr" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M1 1L7 4L1 7" fill="none" stroke="var(--q6)" stroke-width="1.6"/></marker></defs>
          <rect class="rv-panel" x="14" y="12" width="226" height="132" rx="10"/>
          <text class="rv-kicker" x="26" y="29">Q₇ · author working proof</text>
          <rect x="24" y="36" width="206" height="32" rx="7" fill="#F3F5F8" stroke="var(--hair)"/>
          <text x="127" y="56" text-anchor="middle" font-size="12.5" font-weight="650" fill="var(--ink)">Every matching in Q₇</text>
          <line x1="127" y1="69" x2="127" y2="90" stroke="var(--q6)" stroke-width="1.7" marker-end="url(#rv-q6-arr)"/>
          <text x="135" y="83" font-size="10.5" class="rv-accent">all edges kept</text>
          <rect class="rv-panel-tint" x="24" y="93" width="206" height="39" rx="7"/>
          <text x="127" y="110" text-anchor="middle" font-size="12.5" font-weight="650" fill="var(--ink)">Hamilton cycle in Q₇</text>
          <text class="rv-sub" x="127" y="125" text-anchor="middle">all 128 vertices</text>
          <rect class="rv-panel" x="248" y="12" width="118" height="132" rx="10"/>
          <text class="rv-meta" x="307" y="29" text-anchor="middle">Q₆ example</text>
          <g transform="translate(247 24) scale(0.375)">${inset}</g>
          <text class="rv-sub" x="307" y="133" text-anchor="middle">matching ⊂ cycle</text>
          <rect class="rv-panel" x="14" y="154" width="352" height="90" rx="10"/>
          <text class="rv-kicker" x="26" y="174">Q₆ theorem retained</text>
          <text x="26" y="196" font-size="12.5" font-weight="620" fill="var(--ink)">Every Q₆ matching → all-64-vertex cycle</text>
          <text class="rv-sub" x="26" y="216">≤6 directions via prescribed-endpoint P₆</text>
          <text class="rv-meta" x="26" y="234">Q₇ external peer review pending · no Lean</text>
        `);
      }
    },

    he: {
      resultLabel:
        'Happy Ending and ordered rank-3 signotope capacities across m = 7, 8, 9: working ES(7) <= 77, replayed N(8,6,6) <= 61 CNF+DRAT and signotope N(8,8,8) <= 318, and replayed native-trace duals C9 <= 688, D9 <= 458 assembling to working ES(9) <= 1148.',
      resultCap:
        'Results · m = 7, 8, 9 capacities & planar thresholds (replayed duals/DRAT + working assembly)',
      links: [
        { label: 'm = 7–9 overview ↗', href: 'happy-ending-latest.html', sourceLanguage: 'EN + 中文' },
        { label: 'm = 7 figure ↗', href: 'assets/result-figures/happy-ending-bounds.svg', sourceLanguage: '中文', sub: true }
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

          <!-- Top panel: three m = 7, 8, 9 settings side-by-side -->
          <rect class="rv-panel" x="14" y="10" width="352" height="104" rx="10"/>
          <text class="rv-h" x="24" y="28">Signotope &amp; planar bounds</text>
          <text class="rv-meta" x="356" y="28" text-anchor="end">m = 7, 8, 9</text>

          <rect x="22" y="36" width="102" height="68" rx="7" fill="#F8F9FB" stroke="var(--hair)"/>
          <text class="rv-sub" x="73" y="52" text-anchor="middle">m = 7 (7-gons)</text>
          <text x="73" y="75" text-anchor="middle" font-size="14.5" font-weight="680" class="rv-accent">ES(7) ≤ 77</text>
          <text class="rv-sub" x="73" y="94" text-anchor="middle">78 → 77 working</text>

          <rect x="130" y="36" width="112" height="68" rx="7" fill="#F8F9FB" stroke="var(--hair)"/>
          <text class="rv-sub" x="186" y="52" text-anchor="middle">m = 8 (8-gons)</text>
          <text x="186" y="75" text-anchor="middle" font-size="13.5" font-weight="680" class="rv-accent">N(8,6,6) ≤ 61</text>
          <text x="186" y="94" text-anchor="middle" font-size="8.8" fill="var(--muted)">signotope · N(8,8,8) ≤ 318</text>

          <rect x="248" y="36" width="110" height="68" rx="7" fill="#F8F9FB" stroke="var(--hair)"/>
          <text class="rv-sub" x="303" y="52" text-anchor="middle">m = 9 (9-gons)</text>
          <text x="303" y="75" text-anchor="middle" font-size="13.5" font-weight="680" class="rv-accent">ES(9) ≤ 1148</text>
          <text class="rv-sub" x="303" y="94" text-anchor="middle">working · vs 1508</text>

          <!-- Bottom panel: m = 9 native-trace dual assembly -->
          <rect class="rv-panel" x="14" y="122" width="352" height="122" rx="10"/>
          <text class="rv-h" x="24" y="141">m = 9 native-trace assembly</text>
          <text class="rv-meta" x="356" y="141" text-anchor="end">replayed duals · Λ = 10⁶</text>

          <rect x="22" y="152" width="116" height="80" rx="8" fill="#FAF6EE" stroke="#E5D5B5"/>
          <text class="rv-sub" x="80" y="170" text-anchor="middle">Replayed duals</text>
          <text x="80" y="191" text-anchor="middle" font-size="11.5" font-weight="650" fill="var(--ink)">C₉ ≤ 688 · D₉ ≤ 458</text>
          <text class="rv-sub" x="80" y="213" text-anchor="middle" fill="#8C581C">236 &amp; 124 holes</text>

          <line x1="141" y1="192" x2="167" y2="192" stroke="#667085" stroke-width="1.5" marker-end="url(#rv-he-chain)"/>
          <text x="154" y="182" text-anchor="middle" font-size="8.8" font-weight="650" fill="var(--ink-2)">R7+R20</text>

          <rect x="170" y="152" width="82" height="80" rx="8" fill="#FAF6EE" stroke="#E5D5B5"/>
          <text class="rv-sub" x="211" y="170" text-anchor="middle">Signotope</text>
          <text x="211" y="192" text-anchor="middle" font-size="10.2" font-weight="650" fill="var(--ink)">N(9,9,9) ≤ 1147</text>
          <text class="rv-sub" x="211" y="213" text-anchor="middle" fill="#8C581C">Q₉ ≤ 1146</text>

          <line x1="255" y1="192" x2="273" y2="192" stroke="var(--he)" stroke-width="1.6" marker-end="url(#rv-he-arr)"/>
          <text x="264" y="182" text-anchor="middle" font-size="10" font-weight="650" fill="var(--ink-2)">+1</text>

          <rect class="rv-panel-dash" x="276" y="152" width="82" height="80" rx="8"/>
          <text x="317" y="170" text-anchor="middle" font-size="10" font-weight="640" class="rv-accent">Convex 9-gon</text>
          <text x="317" y="192" text-anchor="middle" font-size="12" font-weight="700" class="rv-accent">ES(9) ≤ 1148</text>
          <text class="rv-sub" x="317" y="213" text-anchor="middle">1508 / 1501*</text>
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
          `<a class="rv-link${l.sub ? ' rv-link-sub' : ''}" href="${l.href}" target="_blank" rel="noopener">${l.label}<span class="source-language" data-no-i18n>${l.sourceLanguage}</span></a>`
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
