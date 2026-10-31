# Ademir Camargo — academic website

A lightweight Jekyll website for GitHub Pages. The interface and available teaching lessons use American English. Original publication titles are retained for accurate citation.

## Current content

The site includes Home, About, Research, Publications, Teaching, Research Group, and Contact pages; 98 journal articles reconciled against the supplied Lattes CV; three separately labeled preprints; one undated conference contribution; and 13 English teaching pages.

**The full textbook migration is not finished.** Read `CONTENT_STATUS.md` for the source inventory, completed lessons, remaining chapters, and editorial corrections. The group page describes confirmed research areas; it does not invent a current membership list.

## Publish on GitHub Pages

1. Create a new public repository in `AdemirCamargo57`, for example `myWebPage`. Keep the existing `gqteaWinToga` repository separate.
2. Upload this website's source files, including the hidden `.github` folder. If using the provided source ZIP, extract it first and upload its contents, not the ZIP itself.
3. Use `main` as the default branch. The workflow in `.github/workflows/pages.yml` runs on pushes to `main`.
4. In the repository, open **Settings → Pages** and choose **GitHub Actions** as the build and deployment source.
5. Open **Actions → Build and deploy academic website**. Run it manually if the initial push occurred before Pages was enabled. Wait for both the build and deployment jobs to finish successfully.
6. Open the URL returned by the deployment. For a repository named `myWebPage`, the expected address is `https://ademircamargo57.github.io/myWebPage/`.

The workflow reads the correct path prefix from GitHub Pages, so a different repository name works without editing every link. For local builds, update `baseurl` in `_config.yml` to match the repository name. If using the account-root repository `AdemirCamargo57.github.io`, set `baseurl: ""`.

Do not upload the original Lattes PDF, `working/`, portable tools, or build caches. They are excluded by `.gitignore`; they are also excluded from Jekyll's published output. The original CV contains personal details that are not used on the website. The supplied source ZIP contains only the website and its maintenance files.

## Edit text

Open a file in GitHub, select the pencil icon, make your changes, and commit to `main`. GitHub Actions rebuilds and deploys the site automatically.

| Change | File |
| --- | --- |
| Homepage introduction | `index.html` |
| Biography and education | `about.md` |
| Research and software links | `research.md` |
| Research group | `group.md` |
| Contact details | `contact.md` |
| Navigation | `_data/navigation.yml` |
| Publications | `_data/publications.json` |
| Teaching lessons | `_lessons/` |
| Colors, typography, and responsive layouts | `assets/site.css` |
| Site address and page defaults | `_config.yml` |

## Add a teaching lesson

Create `_lessons/descriptive-topic-name.md`. Start with this metadata, then write the lesson in Markdown:

```yaml
---
title: A Descriptive Lesson Title
subject: Quantum chemistry
order: 30
description: A short explanation of what the reader will learn.
---
```

Use one of the existing subject names exactly: `Mathematical foundations`, `Quantum chemistry`, or `Molecular dynamics`. Lessons appear automatically on the teaching index, sorted by `order`. A lesson named `descriptive-topic-name.md` appears at `/teaching/descriptive-topic-name/`.

Use `##` for main sections and `###` for subsections. The lesson navigation is generated from these headings. The page title comes from the metadata; do not repeat it as a `#` heading.

Kramdown uses **double dollar signs** for both inline and display math:

```text
The energy is $$E=mc^2$$.

$$
F_{\alpha x}=-\frac{\partial E}{\partial x_\alpha}.
$$
```

Keep display delimiters on their own lines, separated from surrounding paragraphs by blank lines. Kramdown protects TeX from Markdown processing and produces MathJax delimiters in the generated HTML. Avoid ordinary single-dollar inline notation and raw `\(...\)` in Markdown source. In `.html` lessons, use `\(...\)` and `\[...\]` directly.

Put figures in `assets/lessons/`, use descriptive alternative text, and build their URLs with Jekyll's `relative_url` filter. Keep equations as text rather than screenshots. Students can use **Print / Save as PDF** on any lesson page. Printing requires no account or server-side conversion.

## Add a publication

Add an object to `_data/publications.json`, using an existing entry as a model. Required fields are `id`, `title`, `authors`, `journal`, `year`, `date`, `doi`, `url`, `type`, `source`, and `bib_path`. Use a unique ID, `YYYY-MM-DD` for `date`, and one of `journal-article`, `preprint`, or `conference-paper` for `type`. Use `0000-01-01` for sorting an undated record and `Undated` for its displayed year. Use empty strings for unknown fields rather than inventing values.

For a DOI link, put the bare identifier in `doi` and the complete `https://doi.org/...` URL in `url`. Keep publisher links and manuscript links distinct. Retain the original published title even when it is in Portuguese.

After editing, run `python tools/sync_bibliography.py` to regenerate the individual and combined downloadable BibTeX files from the same data. This requires only Python's standard library. Existing imported BibTeX entries contain more metadata; the helper preserves them unless the `--replace` option is explicitly supplied. Use `--replace` after editing citation fields, then review the generated result.

The site reads a local bibliography snapshot. It does **not** scrape ORCID or Scholar when a visitor opens the page. This keeps loading fast and gives you control over attribution. Do not import every name match without review.

## Local build

With Ruby and Bundler installed:

```text
bundle install
bundle exec jekyll serve --baseurl /myWebPage
```

Open the local URL printed by Jekyll. For a one-time static build, use `bundle exec jekyll build`. Windows users can use RubyInstaller with its development toolchain, or run the build in a suitable Linux environment. The deployed site is ordinary HTML, CSS, images, and a small JavaScript file; Ruby is only a build dependency.

After a build, run:

```text
python tools/validate_site.py
```

This checks local links and fragment targets, one main heading per page, image alternative text, bibliography consistency, unresolved templates, and exclusion of local source material from `_site`. It does not replace browser and scientific review.

## Custom domain later

When the domain is chosen, configure it under **Settings → Pages → Custom domain**, follow GitHub's DNS instructions for your domain provider, and enable HTTPS once the certificate is available. Set `url` in `_config.yml` to the final origin and `baseurl: ""` for a domain serving this site at its root. Keep only one canonical domain and update inbound links or redirects from the old website where possible. No custom domain or DNS changes have been made.

## Design and accessibility

The site uses system fonts and Georgia, semantic landmarks, keyboard focus styles, a skip link, responsive navigation, readable contrast, and print layouts. Publication search runs entirely in the browser; the full list remains readable without JavaScript. Lesson contents navigation and the print button are enhancements; the lesson text remains available without them.

MathJax 3.2.2 is pinned and loaded only on lesson pages from jsDelivr. Readers need internet access to render equations; if the CDN is unavailable, the underlying TeX remains in the HTML. For fully offline equation rendering, vendor MathJax and its fonts and update the script path.

## Verification and deployment status

The site was built locally using Jekyll 4.4.1. Local static builds used the real Jekyll renderer with its dependencies loaded directly, avoiding optional Windows live-reload extensions. The normal Bundler workflow still needs its first successful GitHub Actions run. Browser checks cover the homepage, publication filters, and representative lessons at desktop and mobile widths. See `CONTENT_STATUS.md` for remaining content work. No repository, public deployment, or DNS configuration has been changed by this work.
