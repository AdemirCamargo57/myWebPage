# Site design and maintenance guide

These instructions apply throughout this repository. Preserve the established
design for routine additions; change the visual direction only when requested.
Use the existing source files as the reference for exact implementation details.

## Purpose and voice

- This is Ademir Camargo's academic website at the State University of Goiás
  (UEG), focused on physical chemistry, computational chemistry, research,
  publications, and teaching.
- Write interface text and explanatory copy in American English (`en-US`). Keep
  names, diacritics, and original publication titles intact for accurate citation.
- Use clear, factual academic prose. Personal biography and research introductions
  use the first person; resource descriptions explain what the reader will find.
- Use descriptive text links and brief introductions. Do not introduce marketing
  copy, invented credentials, group members, publication details, or course content.
- Consult `README.md` for maintenance procedures and `CONTENT_STATUS.md` for
  provenance and editorial decisions. Keep the original Lattes CV and private
  working material out of published output.

## Visual character

The site resembles a quiet academic publication: a light page, generous whitespace,
serif headings, readable sans-serif body text, and restrained blue accents. Thin
rules organize content instead of raised cards. Preserve the text-led presentation;
avoid adding gradients, shadows, large rounded panels, decorative icons, or animation
as part of routine updates. The current theme is light only.

### Color and typography

Reuse the variables in `assets/site.css` rather than introducing near-duplicates.

| Token | Value | Role |
| --- | --- | --- |
| `--ink` | `#243039` | Main text |
| `--muted` | `#596671` | Supporting text and metadata |
| `--blue` | `#244e6b` | Links, eyebrows, and header accent |
| `--line` | `#dbe1e4` | Dividers and light borders |
| `--paper` | `#fff` | Page background |
| `--wash` | `#f3f6f7` | Subtle notice, code, and tag backgrounds |
| `--serif` | `Georgia, 'Times New Roman', serif` | Identity and headings |

- Body text uses the system sans-serif stack at 17px with 1.75 line height;
  it becomes 16px at the small-screen breakpoint. Do not add remote font dependencies.
- Headings use regular-weight serif type, 1.25 line height, and slightly tight
  letter spacing. The main heading scales fluidly; secondary headings are about
  1.8rem and tertiary headings about 1.3rem.
- `.eyebrow` is a small blue uppercase label with wide letter spacing, not a heading.
  `.deck` is a larger muted introduction. Metadata is smaller and muted.
- Links are blue, generally underlined, with an offset underline and a heavier
  underline on hover. Navigation uses its existing hover and current-page treatment.
- Corners are nearly square: the portrait has a 2px radius and controls/tags 3px.

### Layout and reusable patterns

- `.wrap` centers content at a maximum width of 1100px with 32px side gutters;
  small screens use 18px side gutters. Prose is limited to 780px, page headings
  to 800px, and deck text to 720px.
- `_layouts/default.html` owns the shared masthead, navigation, main landmark,
  footer, metadata, stylesheet, and deferred script. Do not duplicate this shell.
- The masthead pairs the serif name and role with a right-aligned affiliation.
  A 5px blue top border and thin navigation rules establish the page frame.
- Interior pages begin with `.page-heading`, an eyebrow, one `h1`, and a `.deck`.
  Long-form content uses `.prose.page-body`; Markdown inside HTML needs `markdown="1"`.
- The homepage uses `.hero` with a text column and portrait, then `.home-columns`
  for research and teaching. Preserve the existing portrait crop and useful alt text.
- Reuse `.resource-list` for resources, `.timeline` for appointments, `.publication`
  for bibliography entries, `.meta` for small supporting text, and `.notice` for
  contextual notes. These patterns use spacing and thin rules to separate entries.
- Keep actions as plain text links where the current design does so. Reuse shared
  classes before adding styles; put shared CSS in `assets/site.css`.

## Responsive behavior and accessibility

- Preserve the existing 800px and 600px breakpoints. At 800px, homepage columns
  and filters tighten; at 600px, the masthead and homepage columns stack, the
  portrait follows the introduction, and the footer becomes vertical.
- Navigation wraps visibly on narrow screens. Publication search spans a full
  row above the two selectors on small screens. Avoid page-level horizontal overflow;
  wide tables and code blocks may scroll within their own containers.
- Keep semantic landmarks, one `h1` per page, ordered heading levels, descriptive
  links, meaningful image alternatives, explicit form labels, and `aria-current`
  for the active navigation item.
- Preserve the skip link, focusable main target, visible amber keyboard focus
  outlines (`#a66818`), and the publication count's polite live announcement.
- Content and resource links must work without JavaScript. `assets/site.js` only
  enhances publication filtering; retain its IDs and data attributes when editing
  that page. Preserve accent-insensitive search and the no-results message.
- Respect reduced-motion preferences. Keep print rules that hide site chrome and
  filters, use black serif text, and reduce awkward heading/publication breaks.

## Sources, URLs, and content conventions

- This is a Jekyll site using Liquid templates and Kramdown, deployed through
  `.github/workflows/pages.yml`. Keep the existing static architecture for routine work.
- Edit source files, never `_site/`: Jekyll regenerates that directory. If supplied
  assets arrive there, copy them into the corresponding source `assets/` directory
  before building so they survive subsequent builds.
- Use YAML front matter with a title and preserve existing permalinks. Keep the
  current navigation order in `_data/navigation.yml`: Home, About, Research,
  Publications, Teaching Materials, Research Group, Contact.
- Route local links and assets through Liquid's `relative_url` filter so the
  `/myWebPage` base path works. Use `absolute_url` for canonical URLs. Escape
  data-derived text and attributes, and preserve filename case.
- Teaching PDFs live in `assets/teaching/`; catalog entries live in
  `_data/teaching_materials.yml`. Use unique increasing integer weeks, an ISO posting
  date, the exact PDF path, the document title, a verified optional page count, and
  a short description based on the document. Preserve supplied PDF bytes.
- The teaching catalog sorts weeks ascending and displays two-digit week labels,
  a posting date, title, page count, and description. Reuse `.resource-list` and
  `.teaching-materials`. Every PDF link opens in a new tab with
  `target="_blank"`, `rel="noopener noreferrer"`, and a visible new-tab notice.
- The homepage shows the first three teaching entries in week order and links
  to the catalog. Preserve `/teaching/` and `#weekly-materials`; do not create
  separate HTML lessons or restore the removed lesson collection/MathJax loader.
- Publications come from `_data/publications.json`, sorted newest first and grouped
  by year. Preserve distinctions among journal articles, preprints, and conference
  papers, original titles, DOI links, and downloadable BibTeX. Use
  `python tools/sync_bibliography.py` after publication data edits; consult the
  README before using its replacement option. Do not scrape profiles at page load.

## Verification and delivery

- For site changes, run `bundle exec jekyll build`, then
  `python tools/validate_site.py`. The repository's portable Windows alternative is
  `& './tools/rubyinstaller-3.3.13-1-x64/bin/ruby.exe' tools/build-local.rb` when those
  local tools and gems are available. Do not commit portable runtimes or caches.
- For teaching updates, check all catalog links, page counts, new-tab attributes,
  and source/build PDF byte equality. Commit the source PDFs with the catalog data.
- For layout or interaction changes, inspect affected pages at desktop and narrow
  mobile widths, keyboard navigation, and relevant print styles. Report any
  verification that could not be completed.
- Keep maintenance instructions, private source material, `working/`, tools, and
  output archives out of `_site/`. Include this guide in source packages only.
- Run `git diff --check` and review the changed files. Preserve unrelated work.
  Distinguish local build success from public deployment: the GitHub Pages workflow
  publishes after a push to `main`; do not claim publication without confirming it.
