# Manuscript and style provenance

Official ICML 2026 style archive: https://media.icml.cc/Conferences/ICML2026/Styles/icml2026.zip (retrieved by the manuscript preparation task on 2026-11-03). Style files are unchanged and retain their own notices. This is a writing draft, not evidence of submission or acceptance. Author fields remain anonymous placeholders.

This release preserves the existing PDF and TeX manuscript verbatim. The manuscript describes the smaller manuscript-source bundle and its local evidence map. In this larger release, all witness streams are supplied in `../evidence/`; runnable commands are in `../REPRODUCE.md`. Thus the manuscript's statement that large streams are not embedded in its compact source archive does not describe this full release folder. Historical model-review records remain in the research archive; they are not necessary computational inputs and are not republished. No fresh external-review verdict is claimed for this release.

Build with a standard TeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

A ready-to-read PDF is included. The release packaging does not change mathematical claims in the manuscript.
