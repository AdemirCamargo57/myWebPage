# Content migration and review status

Updated: October 31, 2026.

## Website

Implemented: all seven agreed sections, responsive layouts, publication search and filters, downloadable BibTeX, separate teaching pages, MathJax, lesson contents navigation, print styles, GitHub Pages deployment workflow, and maintenance instructions.

The site has not been pushed to GitHub or published. No domain or DNS changes have been made. The website repository name remains your choice; the workflow derives its deployed base path from GitHub Pages.

## Biography

The biography combines the supplied Lattes CV, ORCID biography, and existing website. As instructed, the Lattes dates take precedence: Chemistry 1987; Pure Mathematics 2000; UEG employment beginning in 2003, with Anápolis from 2004. The original curriculum PDF remains local and is excluded from Git and published files. Residential address, birth details, and personal contact information have not been included.

## Publications

The curated snapshot contains **98 journal articles, three preprints, and one undated conference contribution**. All 98 numbered journal entries in the supplied CV have been accounted for. Original published titles are retained, including Portuguese titles. Preprints are listed separately from journal articles even when a related final article exists.

The first extraction missed four inline-numbered CV entries; the corrected parser asserts a complete 1–98 sequence. The four recovered entries are the Clinoptilolite study (2015), Computational Quantum Chemistry Applied to Drug Modeling (2005), Validation of Polymorphic Drugs (2005), and Ab Initio and Chemometric Studies of Quinone Compounds (2003). Bibliographic details follow the supplied CV where no matching ORCID record exists; missing DOIs are not invented.

Five name-match records in ORCID are excluded **as confirmed by the author**: Pectin-based Polymer Electrolytes with Ir(III) Complexes; Reply to Stokic and Curt; Stem Cells in the Treatment of Chronic Spinal Cord Injury; On-line Mass Spectrometry Investigation of CO₂ Reduction on Platinum; and H-reflex in Spastic Patients. A second ORCID entry for the H1N1 chalcone study is also excluded as an apparent duplicate. Detailed reconciliation is retained locally in `working/bibliography-reconciliation.json`.

This is a complete reconciliation of the **journal-article list supplied**, not a claim that all lifetime conference presentations, books, chapters, or other outputs have been recovered. The CV's summary mentions additional output categories without full itemized records in this export. Add those if a complete all-output bibliography is desired.

## Completed teaching pages

These are English web editions rewritten from the Site handouts, with mathematical corrections noted below. They preserve the principal derivations, examples, and exercises, but are edited teaching editions rather than line-for-line documentary translations. Hand-drawn or redundant source illustrations have been replaced by mathematical explanations where appropriate.

| Source | Web edition |
| --- | --- |
| `Site/grupo.docx` | Groups and Abelian Groups |
| `Site/grupo_corpo_espaco_vetorial_norma.docx` | Fields, Vector Spaces, Inner Products, and Norms |
| `Site/Espaco_Hilbert.docx` | Hilbert Spaces |
| `Site/Operador_linear.docx` | Linear Operators and Matrix Representations |
| `Site/Metodo_diferencas_finitas.docx` | The Finite Difference Method |
| `Site/CÁLCULO VARIACIONAL.docx` | Variational Calculus |
| `Site/funcoes_base.docx` | Basis Functions in Quantum Chemistry |
| `Site/calculo_numerico_focas.docx` | Numerical Calculation of Atomic Forces |
| `Site/verlet_velocity_verlet_leap_frog.docx` | Verlet, Velocity Verlet, and Leapfrog Integration |
| `01_MDEE_Chapters/CAP-II_v10.docx` | Postulates of Quantum Mechanics |
| `01_MDEE_Chapters/CAP-VI_v2.docx` | Reduced Density Gradient and Noncovalent Interactions; Hole–Electron Analysis and Transition Properties; Natural Transition Orbitals |

Chapter VI already contains English sections. Those were converted with their equations and all four embedded PNG figures. The repeated Portuguese hole–electron section was omitted because the same material appears in English. Source title and cover/contents boilerplate were removed. A long inline RMSD equation was changed to display format to prevent mobile overflow.

## Textbook chapters still requiring translation and scientific review

The complete textbook migration is **not finished**. These sources have been inventoried and converted locally as preparation, but are not published as finished English lessons:

- `01_MDEE_Chapters/CAP-I_v12.docx`: mathematical review.
- `01_MDEE_Chapters/CAP-III_v11.docx`: advanced molecular dynamics.
- `01_MDEE_Chapters/CAP-IV_v12.docx`: electronic structure methods.
- `01_MDEE_Chapters/CAP-V_v13.docx`: molecular property calculations.
- `02_QQ_Chapters/QQ_CAP-I_Rev1.docx` through `QQ_CAP-VII_Rev1.docx`: quantum chemistry textbook collection. **The file labeled chapter VI contains approximately the entire compiled textbook**, so it must be separated and checked against the other chapter files before translation to avoid repeating the book as one chapter.

The root-level compiled textbooks, older chapter revisions, and source PDFs have not been duplicated as separate lessons. Supplementary drafts, including XC_ChatGPT and Veritasium, are excluded as instructed.

Source conversions and extracted text are kept under `working/`, which is excluded from Git and the built website. Never treat the conversion outputs as verified translations. Equations inside tables need checking as well as equations in ordinary paragraphs.

## Scientific editorial changes for author review

- **Groups:** subtraction on the real numbers is not a group operation; retained the example as a counterexample. Commutativity is presented as the additional condition for an abelian group.
- **Vector spaces:** linear independence means the coefficient equation has only the trivial coefficient solution. Corrected malformed coordinate examples and distinguished a dual bra from its ket representation.
- **Hilbert spaces:** separability is not required by the general definition. The Cauchy condition involves every pair of sufficiently late terms, not only consecutive terms. Square-integrability statements are qualified by the function domain.
- **Operators:** taking the adjoint of `O|a⟩=|b⟩` produces `⟨a|O†=⟨b|`. Eigenvectors for distinct Hermitian eigenvalues are orthogonal; degeneracy requires a separate choice of basis. Boundary conditions and domains qualify differential-operator statements. The Pauli y matrix follows the standard sign convention.
- **Finite differences:** forward/backward first derivatives have first-order errors; central first and second derivatives have second-order errors. Corrected Taylor factorial indices, powers, and the distinction between a numerator remainder and the derivative's error.
- **Forces:** finite differences are applied to individual Cartesian coordinates. The full potential energy depends on all coordinates, not on an isolated atom's energy. Corrected the Taylor second-order coefficient.
- **Verlet:** distinguished local Taylor remainders from second-order global accuracy. Corrected the force-gradient signs. Clarified velocity-dependent forces, half-step velocities, and kinetic-temperature degrees of freedom.
- **Basis sets:** distinguished molecular orbitals from many-electron wavefunctions, primitives from contractions, and five spherical versus six Cartesian d functions. Corrected carbon counts: 6-311G has 13 contracted functions; 6-31+G(d) has 19 with six Cartesian d functions and 18 with five spherical d functions.
- **Variational calculus:** zero integral does not by itself imply zero integrand; the fundamental lemma requires arbitrary admissible variations. Stationarity does not establish a minimum. Pointwise constraints generally require multiplier functions. Equal numbers of equations and unknowns do not guarantee a unique solution. Distinguished the directional derivative from the functional derivative.
- **Quantum postulates:** the Dirac delta is a distribution; continuum eigenkets are generalized states. Corrected Fourier normalization to include ħ. Symmetric operator ordering and Poisson-bracket correspondence are qualified rather than asserted as universal quantization theorems. Ehrenfest's classical correspondence is qualified for nonlinear potentials.

These notes are intended to make the mathematical editing reviewable. The English editions should receive the author's scientific review before being used as official course texts.

## Verification

- Real Jekyll 4.4.1 static build completed locally.
- Local link, image, fragment, heading, and bibliography checks passed for 21 HTML pages, 13 lessons, and 102 publication records.
- All 13 lessons checked in the browser at a 390-pixel mobile width; MathJax reports no formula-rendering errors after corrections. No page-level horizontal overflow remained in these checks; long display equations can scroll within their own region.
- Desktop homepage and lesson layouts inspected visually; mobile homepage inspected visually. Publication keyword search and combined year filtering verified. Remaining changes should be checked again after publication.
- The first standard GitHub Actions build and deployment remain to be run in the selected repository. The portable local check bypasses optional Windows live-reload extensions, not the Jekyll template or Markdown renderer.
