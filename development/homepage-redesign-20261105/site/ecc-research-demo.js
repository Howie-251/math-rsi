/* A research organization example, not a solver or a computation replay. */
(() => {
  'use strict';

  function mount() {
    const host = document.getElementById('ecc-research-demo');
    if (!host || host.querySelector('.ecd-demo')) return;
    host.innerHTML = `
      <details class="ecd-demo">
        <summary class="ecd-summary">
          <span class="ecd-summary-title">How we organize research</span>
          <span class="ecd-example">Research organization example · [72,36,≥16]</span>
        </summary>
        <div class="ecd-content">
          <p class="ecd-intro">An open existence question, organized into exact domains and shared work.</p>
          <div class="ecd-steps" role="group" aria-label="Research organization steps">
            <button class="ecd-step" type="button" data-ecd-step="0" aria-pressed="true">
              <span class="ecd-number" aria-hidden="true">1</span><span><b>Partition the problem</b><small>Keep every code in view.</small></span>
            </button>
            <button class="ecd-step" type="button" data-ecd-step="1" aria-pressed="false">
              <span class="ecd-number" aria-hidden="true">2</span><span><b>Reuse shared computation</b><small>One task can serve several domains.</small></span>
            </button>
            <button class="ecd-step" type="button" data-ecd-step="2" aria-pressed="false">
              <span class="ecd-number" aria-hidden="true">3</span><span><b>Check coverage &amp; return</b><small>Local evidence keeps its exact scope.</small></span>
            </button>
          </div>

          <div class="ecd-tree" data-ecd-tree-step="0" data-ecd-tree-branch="A">
            <div class="ecd-root"><span>Original existence question</span><b>[72,36,≥16]</b></div>
            <svg class="ecd-fork" viewBox="0 0 300 28" preserveAspectRatio="none" aria-hidden="true">
              <path class="ecd-trunk" d="M150 0V13H50V28 M150 13H250V28 M150 13V28"/>
              <path class="ecd-fork-a" d="M150 0V13H50V28"/>
              <path class="ecd-fork-b" d="M150 0V28"/>
              <path class="ecd-fork-c" d="M150 0V13H250V28"/>
            </svg>
          </div>
              <div class="ecd-branches" role="group" aria-label="Inspect a code class">
                <button type="button" class="ecd-branch" data-ecd-branch="A" aria-pressed="true" aria-label="Inspect class A: self-dual"><b>A</b><span>Self-dual</span></button>
                <button type="button" class="ecd-branch" data-ecd-branch="B" aria-pressed="false" aria-label="Inspect class B: even, not self-dual"><b>B</b><span>Even, not self-dual</span></button>
                <button type="button" class="ecd-branch" data-ecd-branch="C" aria-pressed="false" aria-label="Inspect class C: contains an odd word"><b>C</b><span>Contains an odd word</span></button>
              </div>

          <div class="ecd-scene" data-ecd-current="0">
            <section class="ecd-layer ecd-classify" aria-label="Mutually exclusive code classes">
              <div class="ecd-layer-heading"><span class="ecd-dot" aria-hidden="true"></span><b>Three exhaustive, disjoint classes</b></div>
              <div class="ecd-class-detail" aria-live="polite" aria-atomic="true">
                <div data-ecd-detail="A"><span class="ecd-formula">C = C⊥</span><p>All codewords are even. Fixing a self-orthogonal core covers only the codes containing that core; the rest remain in view.</p></div>
                <div data-ecd-detail="B" hidden><span class="ecd-formula">h = dim(C ∩ C⊥) ∈ {0, 2, …, 34}</span><p>There are 18 hull layers. A self-orthogonal 35-dimensional parent reaches only h = 34; the other 17 layers remain.</p></div>
                <div data-ecd-detail="C" hidden><span class="ecd-formula">E = {c ∈ C : wt(c) ≡ 0 (mod 2)}, dim E = 35</span><p>The even subcode E is unique. It may be self-orthogonal or not; a library of self-orthogonal parents does not cover every E.</p></div>
              </div>
            </section>

            <section class="ecd-layer ecd-shared" aria-label="A shared fixed-parent task">
              <div class="ecd-layer-heading"><span class="ecd-dot" aria-hidden="true"></span><b>One shared fixed-parent task</b></div>
              <p>Fix a self-orthogonal parent S of dimension 35.</p>
              <span class="ecd-formula">C = S + 〈v〉, v ∉ S</span>
              <div class="ecd-routes">
                <div class="ecd-route" data-ecd-route="A"><b>A</b><span>v even, v ⟂ S</span><small>Self-dual extensions</small></div>
                <div class="ecd-route" data-ecd-route="B"><b>B</b><span>v even, not orthogonal to S</span><small>Only the h = 34 subdomain</small></div>
                <div class="ecd-route" data-ecd-route="C"><b>C</b><span>v odd</span><small>Only the E = S subdomain</small></div>
              </div>
              <p class="ecd-caption">Compute once for S; route each result to its exact domain.</p>
            </section>

            <section class="ecd-layer ecd-coverage" aria-label="Return to the original existence question">
              <div class="ecd-layer-heading"><span class="ecd-dot" aria-hidden="true"></span><b>Return to the original question</b></div>
              <div class="ecd-endpoint"><b>Existence</b><span>One rank-36 generator matrix, verified against the original specification, is enough.</span></div>
              <div class="ecd-endpoint"><b>Nonexistence</b><span>Every necessary domain and its remaining cases must be covered.</span></div>
              <p class="ecd-caption">A fixed parent leaves other parents and uncovered cases. This example does not solve [72,36,≥16].</p>
            </section>
          </div>

          <div class="ecd-controls" role="group" aria-label="Play the research explanation">
            <button class="ecd-control ecd-play" type="button" aria-label="Play explanation">Play</button>
            <button class="ecd-control ecd-replay" type="button" aria-label="Replay explanation">Replay</button>
            <span class="ecd-position" aria-label="Current explanation step">1 / 3</span>
          </div>
          <p class="ecd-footnote">Illustration only. No search or computation runs here.</p>
        </div>
      </details>`;

    const details = host.querySelector('.ecd-demo');
    const scene = host.querySelector('.ecd-scene');
    const steps = [...host.querySelectorAll('[data-ecd-step]')];
    const branches = [...host.querySelectorAll('[data-ecd-branch]')];
    const play = host.querySelector('.ecd-play');
    const replay = host.querySelector('.ecd-replay');
    const position = host.querySelector('.ecd-position');
    let step = 0;
    let timer = null;
    let playing = false;
    const dwell = 5000;

    function pause() {
      clearTimeout(timer);
      timer = null;
      playing = false;
      play.textContent = 'Play';
      play.setAttribute('aria-label', 'Play explanation');
    }
    function selectStep(next) {
      step = next;
      scene.dataset.ecdCurrent = String(step);
      host.querySelector('.ecd-tree').dataset.ecdTreeStep = String(step);
      host.querySelectorAll('.ecd-layer').forEach((layer, i) => {
        layer.setAttribute('aria-hidden', String(i !== step));
        layer.inert = i !== step;
      });
      steps.forEach((button, i) => button.setAttribute('aria-pressed', String(i === step)));
      position.textContent = `${step + 1} / 3`;
    }
    function schedule() {
      timer = setTimeout(() => {
        if (!playing || !details.open) return pause();
        if (step === 2) return pause();
        selectStep(step + 1);
        schedule();
      }, dwell);
    }
    function start(reset) {
      pause();
      if (!details.open) return;
      if (reset || step === 2) selectStep(0);
      playing = true;
      play.textContent = 'Pause';
      play.setAttribute('aria-label', 'Pause explanation');
      schedule();
    }
    steps.forEach((button, i) => button.addEventListener('click', () => {
      pause();
      selectStep(i);
    }));
    branches.forEach(button => button.addEventListener('click', () => {
      const selected = button.dataset.ecdBranch;
      host.querySelector('.ecd-tree').dataset.ecdTreeBranch = selected;
      branches.forEach(branch => branch.setAttribute('aria-pressed', String(branch === button)));
      host.querySelectorAll('[data-ecd-detail]').forEach(detail => {
        detail.hidden = detail.dataset.ecdDetail !== selected;
      });
      host.querySelectorAll('[data-ecd-route]').forEach(route => {
        route.classList.toggle('ecd-route-selected', route.dataset.ecdRoute === selected);
      });
    }));
    selectStep(0);
    branches[0].click();
    play.addEventListener('click', () => playing ? pause() : start(false));
    replay.addEventListener('click', () => start(true));
    details.addEventListener('toggle', () => { if (!details.open) pause(); });
    document.addEventListener('visibilitychange', () => { if (document.hidden) pause(); });
    // Never autoplay. Reduced-motion users retain all text and manual controls.
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount, { once: true });
  else mount();
})();

/* ECC_DEMO_ZH_START
{
  "Original existence question": "原存在性问题",
  "How we organize research": "我们如何组织研究",
  "Research organization example · [72,36,≥16]": "研究组织示例 · [72,36,≥16]",
  "An open existence question, organized into exact domains and shared work.": "将尚未解决的存在性问题，按准确子域与共用任务组织起来。",
  "Research organization steps": "研究组织步骤",
  "Partition the problem": "划分原问题",
  "Keep every code in view.": "保留全部码的覆盖范围。",
  "Reuse shared computation": "复用共同计算",
  "One task can serve several domains.": "一个任务可以服务多个子域。",
  "Check coverage & return": "核对覆盖并返回原题",
  "Local evidence keeps its exact scope.": "局部证据保留其准确适用范围。",
  "Mutually exclusive code classes": "互斥的码分类",
  "Three exhaustive, disjoint classes": "互斥且穷尽的三类",
  "Inspect a code class": "查看码的分类",
  "Inspect class A: self-dual": "查看A类：自对偶",
  "Inspect class B: even, not self-dual": "查看B类：偶且非自对偶",
  "Inspect class C: contains an odd word": "查看C类：含奇字",
  "Self-dual": "自对偶",
  "Even, not self-dual": "偶且非自对偶",
  "Contains an odd word": "含奇字",
  "All codewords are even. Fixing a self-orthogonal core covers only the codes containing that core; the rest remain in view.": "所有码字均为偶重。固定一个自正交核心，只覆盖包含该核心的码；其余情况仍须保留。",
  "There are 18 hull layers. A self-orthogonal 35-dimensional parent reaches only h = 34; the other 17 layers remain.": "共有18个hull层。自正交的35维母码只到达h = 34子域，其余17层仍须处理。",
  "The even subcode E is unique. It may be self-orthogonal or not; a library of self-orthogonal parents does not cover every E.": "偶子码E唯一。它可能自正交，也可能非自正交；自正交母码库不能覆盖所有E。",
  "A shared fixed-parent task": "共用的固定母码任务",
  "One shared fixed-parent task": "一个共用的固定母码任务",
  "Fix a self-orthogonal parent S of dimension 35.": "固定一个35维自正交母码S。",
  "v even, v ⟂ S": "v为偶重且v ⟂ S",
  "v even, not orthogonal to S": "v为偶重且不正交于S",
  "v odd": "v为奇重",
  "Self-dual extensions": "自对偶扩张",
  "Only the h = 34 subdomain": "仅h = 34子域",
  "Only the E = S subdomain": "仅E = S子域",
  "Compute once for S; route each result to its exact domain.": "对S只计算一次，再将结果接回其准确子域。",
  "Return to the original existence question": "返回原存在性问题",
  "Return to the original question": "返回原问题",
  "Existence": "存在性",
  "One rank-36 generator matrix, verified against the original specification, is enough.": "一份秩为36、按原规格核验通过的生成矩阵，即已足够。",
  "Nonexistence": "不存在性",
  "Every necessary domain and its remaining cases must be covered.": "必须覆盖全部必要子域及其余类。",
  "A fixed parent leaves other parents and uncovered cases. This example does not solve [72,36,≥16].": "固定母码之外还有其他母码和未覆盖余类。本示例未解答[72,36,≥16]。",
  "Play the research explanation": "播放研究组织说明",
  "Play explanation": "播放说明",
  "Pause explanation": "暂停说明",
  "Replay explanation": "重播说明",
  "Current explanation step": "当前说明步骤",
  "Play": "播放",
  "Pause": "暂停",
  "Replay": "重播",
  "Illustration only. No search or computation runs here.": "仅作方法示意，此处不运行搜索或计算。"
}
ECC_DEMO_ZH_END */
