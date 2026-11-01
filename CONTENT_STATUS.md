# Content migration and review status

Updated: November 1, 2026.

## Website

Implemented: all seven agreed sections, responsive layouts, publication search and filters, downloadable BibTeX, a weekly PDF teaching catalog, print styles, GitHub Pages deployment workflow, and maintenance instructions.

The site is published at https://ademircamargo57.github.io/myWebPage/. This PDF catalog update is local until committed and pushed to the repository. No domain or DNS changes are part of this update.

## Biography

The biography combines the supplied Lattes CV, ORCID biography, and existing website. As instructed, the Lattes dates take precedence: Chemistry 1987; Pure Mathematics 2000; UEG employment beginning in 2003, with Anápolis from 2004. The original curriculum PDF remains local and is excluded from Git and published files. Residential address, birth details, and personal contact information have not been included.

## Publications

The curated snapshot contains **98 journal articles, three preprints, and one undated conference contribution**. All 98 numbered journal entries in the supplied CV have been accounted for. Original published titles are retained, including Portuguese titles. Preprints are listed separately from journal articles even when a related final article exists.

The first extraction missed four inline-numbered CV entries; the corrected parser asserts a complete 1–98 sequence. The four recovered entries are the Clinoptilolite study (2015), Computational Quantum Chemistry Applied to Drug Modeling (2005), Validation of Polymorphic Drugs (2005), and Ab Initio and Chemometric Studies of Quinone Compounds (2003). Bibliographic details follow the supplied CV where no matching ORCID record exists; missing DOIs are not invented.

Five name-match records in ORCID are excluded **as confirmed by the author**: Pectin-based Polymer Electrolytes with Ir(III) Complexes; Reply to Stokic and Curt; Stem Cells in the Treatment of Chronic Spinal Cord Injury; On-line Mass Spectrometry Investigation of CO₂ Reduction on Platinum; and H-reflex in Spastic Patients. A second ORCID entry for the H1N1 chalcone study is also excluded as an apparent duplicate. Detailed reconciliation is retained locally in `working/bibliography-reconciliation.json`.

This is a complete reconciliation of the **journal-article list supplied**, not a claim that all lifetime conference presentations, books, chapters, or other outputs have been recovered. The CV's summary mentions additional output categories without full itemized records in this export. Add those if a complete all-output bibliography is desired.

## Teaching Materials — PDF catalog

The teaching section now publishes author-supplied PDFs. All 13 former Markdown and HTML lesson sources and their dedicated lesson layout were removed. Main site pages and unrelated biography, research, contact, publication, and navigation behavior are preserved. The lesson collection, lesson-only JavaScript, and external MathJax loader are no longer used.

The public page remains at `/teaching/`, with the navigation label **Teaching Materials**. Entries are sorted by numeric week in ascending order. Each entry displays its week, publication date, title, optional page count, and a short description. PDF links explicitly indicate that they open in a new tab and use `target="_blank"` with `rel="noopener noreferrer"`.

### First material

- Week: 01
- Date: November 1, 2026
- Title: Calculus of Variations
- File: `assets/teaching/CAP_I_A_EN.pdf`
- Length: 18 pages
- Description: variational methods, the Euler–Lagrange equations, Fermat's principle and least action, conservation laws, multiple dependent variables, and holonomic constraints.

The PDF supplied in `_lessons/CAP_I_A_EN.pdf` was moved intact to `assets/teaching/CAP_I_A_EN.pdf`; its contents were not edited. Its title, contents, and length were read to prepare the catalog entry. The original curriculum PDF remains excluded from Git and the published website.

### Weekly updates

Upload each new PDF to `assets/teaching/` and add one entry to `_data/teaching_materials.yml`. The catalog and homepage teaching links update automatically during the Jekyll build. See the weekly PDF instructions in `README.md`. There is no need to create a lesson page, edit navigation, or convert the PDF to HTML.

Old lesson URLs no longer publish content. The current catalog remains at the existing `/teaching/` address. No replacement PDF is invented for a removed lesson.

## Verification

Build and verification results for this update are recorded locally in `working/validation.json`. Checks cover the main HTML pages, local links and fragments, PDF new-tab attributes, matching source/build PDF bytes, bibliography files, and removal of generated HTML lesson pages. The existing deployment workflow remains unchanged.

The catalog PDF was opened by clicking its link in the browser: it loaded in a separate tab while the catalog stayed open. The built-in viewer showed 18 pages. The catalog had no page-level horizontal overflow in the observed narrow preview, and publication search returned 8 of 102 records for “solvation.”
