# Public MathRSI Pages

**[Open the public homepage](https://lisresearchgroup.github.io/math-rsi/)** · [Local clone viewing](HOMEPAGE.md)

The public site serves the interactive bilingual homepage and selected six-topic readers without requiring access to the private repository. GitHub source/evidence links require repository permission. The repository stays private.

## What is published

[`site/public-files.json`](../site/public-files.json) is the complete source-to-public-path allowlist. The build copies only these 77 named files: homepage HTML/CSS/JS, local fonts/KaTeX and licenses, presentation images/logo, and the selected Property B, ECC, Degree–Diameter, Erdős 86, Ruskey–Savage and Happy Ending readers. Individual rendered reports/PDFs stored under source archives are promoted into `readers/`; archive trees, evidence directories, raw reviews, research logs, source trees and build caches are not copied.

The curated bilingual Q7 page presents the ≥57-edge theorem, the exact open scope and v3-local-adaptation → v5 provenance. It adds no raw Q7 research logs or certificate archive. Mathematical text and its stated assurance remain those of the selected readers.

The old offline packager is broader and recursively follows small linked files. It is not used for public publication. [`tools/build_public_site.py`](../tools/build_public_site.py) reuses its URL-adaptation approach with this explicit list. It rewrites local HTML/CSS/JS references, including the dynamic six-topic Read links. Selected materials resolve locally; other available sources link to GitHub with an access notice. Unavailable references retain their labels with disabled links. No linked file is automatically added.

## Build and preview

Python standard library only, from the clone root:

```sh
python3 tools/build_public_site.py --output _site
python3 -m http.server 8000 --bind 127.0.0.1 --directory _site
```

Open `http://127.0.0.1:8000/`. The build output uses relative references and also works under the project prefix `/math-rsi/`; the local browser check exercises that exact prefix. Original source pages stay at their existing locations and retain file/full-clone-server use. Generated `_site/` is ignored by Git.

## Workflow and deployment

[`.github/workflows/pages.yml`](../.github/workflows/pages.yml) builds on PRs, main pushes and manual dispatch. PR runs only build/check: they do not upload a Pages artifact or deploy. Only main can upload the dedicated `_site` output and deploy through the `github-pages` environment. The deployment needs the build job, `pages: write` and `id-token: write`; other work uses `contents: read`.

The workflow follows [GitHub's custom Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages): checkout v6, configure-pages v5, upload-pages-artifact v4 and deploy-pages v4. It never uploads the checkout root. No npm or site-generation framework is required.

Maintainers review the actual PR head and public file map before merging. After merge, check the Pages Actions run and the anonymous public URL. This implementation does not change organization settings or repository visibility.
