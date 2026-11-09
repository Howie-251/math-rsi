/* Translate existing nodes in place: listeners, visual playback and open UI stay intact. */
(() => {
  'use strict';
  const KEY = 'mathrsi-language';
  const ATTRS = ['aria-label', 'title', 'alt', 'aria-valuetext', 'content'];
  const SKIP = 'script,style,code,pre,math,.katex,.katex-display,[data-no-i18n]';
  const texts = new WeakMap();
  const attributes = new WeakMap();
  let language = 'en';
  let observer;
  let started = false;
  try {
    if (localStorage.getItem(KEY) === 'zh-CN') language = 'zh-CN';
  } catch (_) { /* Storage may be unavailable in private or local-file contexts. */ }

  const normalize = value => value.replace(/\s+/g, ' ').trim();
  function translate(source) {
    const key = normalize(source);
    if (!key || language === 'en') return source;
    const dictionary = window.MATHRSI_ZH || {};
    let result = Object.prototype.hasOwnProperty.call(dictionary, key) ? dictionary[key] : undefined;
    if (typeof result !== 'string') {
      for (const rule of window.MATHRSI_ZH_RULES || []) {
        if (!Array.isArray(rule) || rule.length !== 2) continue;
        try {
          const pattern = new RegExp(rule[0]);
          if (pattern.test(key)) { result = key.replace(pattern, rule[1]); break; }
        } catch (_) { /* Ignore a malformed optional catalog rule. */ }
      }
    }
    if (typeof result !== 'string') return source;
    return (source.match(/^\s*/)[0]) + result + (source.match(/\s*$/)[0]);
  }
  function excluded(element) {
    return !element || Boolean(element.closest(SKIP));
  }
  function textNode(node) {
    if (excluded(node.parentElement)) return;
    const value = node.nodeValue;
    let entry = texts.get(node);
    // A value different from our last rendering is fresh application-owned English.
    if (!entry || value !== entry.rendered) entry = { source: value, rendered: value };
    const rendered = translate(entry.source);
    if (value !== rendered) node.nodeValue = rendered;
    entry.rendered = rendered;
    texts.set(node, entry);
  }
  function elementAttributes(element) {
    if (excluded(element)) return;
    let entries = attributes.get(element);
    if (!entries) { entries = new Map(); attributes.set(element, entries); }
    for (const name of ATTRS) {
      if (name === 'content' && !element.matches('meta[name="description"]')) continue;
      if (!element.hasAttribute(name)) { entries.delete(name); continue; }
      const value = element.getAttribute(name);
      let entry = entries.get(name);
      if (!entry || value !== entry.rendered) entry = { source: value, rendered: value };
      const rendered = translate(entry.source);
      if (value !== rendered) element.setAttribute(name, rendered);
      entry.rendered = rendered;
      entries.set(name, entry);
    }
  }
  function walk(root) {
    if (root.nodeType === Node.TEXT_NODE) { textNode(root); return; }
    if (root.nodeType !== Node.ELEMENT_NODE && root.nodeType !== Node.DOCUMENT_NODE) return;
    if (root.nodeType === Node.ELEMENT_NODE) {
      if (excluded(root)) return;
      elementAttributes(root);
    }
    for (const child of root.childNodes) walk(child);
  }
  const options = { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ATTRS };
  function observe() { observer.observe(document.documentElement, options); }
  function process(records) {
    // Disconnect only during synchronous writes so our own rendering never loops.
    observer.disconnect();
    try {
      for (const record of records) {
        if (record.type === 'childList') record.addedNodes.forEach(walk);
        else if (record.type === 'characterData') textNode(record.target);
        else elementAttributes(record.target);
      }
    } finally { observe(); }
  }
  function buttons() {
    document.documentElement.lang = language;
    document.querySelectorAll('[data-lang]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.lang === language));
    });
  }
  function refresh() {
    if (!started) return;
    observer.disconnect();
    try { walk(document); buttons(); } finally { observe(); }
  }
  function setLanguage(next) {
    if (next !== 'en' && next !== 'zh-CN') return;
    const changed = next !== language;
    language = next;
    try { localStorage.setItem(KEY, next); } catch (_) { /* Still switch for this visit. */ }
    refresh();
    if (changed) window.dispatchEvent(new CustomEvent('languagechange', { detail: { language } }));
  }
  observer = new MutationObserver(process);
  document.addEventListener('click', event => {
    const button = event.target.closest && event.target.closest('[data-lang]');
    if (button) setLanguage(button.dataset.lang);
  });
  window.MathRSII18n = Object.freeze({ setLanguage, get lang() { return language; }, refresh });
  // Let application closures capture their original English captions/labels first.
  // Observing earlier would also translate parser-added nodes before startup ends.
  function start() { started = true; refresh(); }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start, { once: true });
  } else {
    start();
  }
})();
