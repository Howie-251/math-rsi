/* Local presentation only: the small example data and figures are precomputed. */
(() => {
  document.documentElement.classList.add('js');
  const methodButtons = [...document.querySelectorAll('[data-method]')];
  const panels = [...document.querySelectorAll('.method-panel')];
  function selectMethod(id) {
    for (const button of methodButtons) {
      button.setAttribute('aria-pressed', String(button.dataset.method === id));
    }
    for (const panel of panels) panel.hidden = panel.id !== id;
  }
  for (const button of methodButtons) {
    button.addEventListener('click', () => selectMethod(button.dataset.method));
  }
  selectMethod('method-filling');

  // TOC links also reveal a construction when its tab is currently hidden.
  function revealAnchor(hash) {
    if (!hash) return;
    const target = document.getElementById(decodeURIComponent(hash.slice(1)));
    const panel = target && target.closest('.method-panel');
    if (panel) selectMethod(panel.id);
    return target;
  }
  for (const link of document.querySelectorAll('a[href^="#"]')) {
    link.addEventListener('click', () => revealAnchor(link.getAttribute('href')));
  }
  revealAnchor(window.location.hash);
  window.addEventListener('hashchange', () => {
    const target = revealAnchor(window.location.hash);
    if (target) target.scrollIntoView({block: 'start'});
  });

  const steps = [...document.querySelectorAll('[data-step]')];
  const figures = [...document.querySelectorAll('.demo-state')];
  const description = document.getElementById('demo-description');
  const data = JSON.parse(document.getElementById('demo-data').textContent);
  function selectStep(id) {
    for (const button of steps) {
      button.setAttribute('aria-pressed', String(button.dataset.step === id));
    }
    for (const figure of figures) figure.hidden = figure.dataset.state !== id;
    description.textContent = data.states.find(state => state.id === id).explanation;
  }
  for (const button of steps) {
    button.addEventListener('click', () => selectStep(button.dataset.step));
  }
  selectStep('cover');
})();
