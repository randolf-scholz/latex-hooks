# latex-lint-modern

Hooks that check that modern $\LaTeX$ practices are followed.

## `avoid-obsolete-packages`

Checks that certain obsolete packages are not used. List taken from
<https://tex.stackexchange.com/a/26200/119955> and updated.

| Outdated Package | Alternative      | Description                        |
|------------------|------------------|------------------------------------|
| a4               | geometry         | Page layouts.                      |
| a4wide           | geometry         | Page layouts.                      |
| algorithmic      | algpseudocode    | Algorithms.                        |
| anysize          | geometry         | Page layouts.                      |
| backrefx         | backref          | Back references.                   |
| bitfield         | bytefield        | Bit fields.                        |
| caption2         | caption          | Captions.                          |
| color            | xcolor           | Enhanced color support.            |
| csvtools         | datatool         | CSV data.                          |
| datetime         | datetime2        | Date/time.                         |
| dinat            | natdin           | DIN citations.                     |
| doublespace      | setspace         | Double spacing.                    |
| dropping         | lettrine         | Dropped capitals.                  |
| eledmac          | reledmac         | Critical editions.                 |
| eps              | graphicx         | Graphics inclusion.                |
| epsfig           | graphicx         | Graphics inclusion.                |
| euler            | eulervm          | Euler fonts.                       |
| eurotex          | inputenx         | Euro symbols.                      |
| fancyheadings    | fancyhdr         | Headers/footers.                   |
| filecontents     | None             | Now in the kernel.                 |
| fixltx2e         | Remove           | Kernel fixes now built-in.         |
| floatfig         | floatflt         | Floating figures.                  |
| german           | babel            | German language.                   |
| glossary         | glossaries       | Glossaries.                        |
| graphics         | graphicx         | Graphics inclusion.                |
| HA-prosper       | beamer           | Presentations.                     |
| here             | float            | Float placement.                   |
| hyper            | hyperref         | Hyperlinks.                        |
| ifthen           | etoolbox         | Conditionals.                      |
| isolatin         | inputenc         | Input encoding.                    |
| isolatin1        | inputenc         | Input encoding.                    |
| letltxmacro      | None             | Use built-in `\NewCommandCopy`     |
| mathpple         | mathpazo         | Palatino math.                     |
| mathptm          | mathptmx         | Times math.                        |
| ngerman          | babel            | German language.                   |
| nthm             | ntheorem         | Theorems.                          |
| palatino         | mathpazo         | Palatino fonts.                    |
| picinpar         | wrapfig          | Inline figures.                    |
| prosper          | beamer           | Presentations.                     |
| ps4pdf           | pst-pdf          | PDF conversion.                    |
| psfig            | graphicx         | Graphics inclusion.                |
| psfrag           | pstool           | Text overlays.                     |
| raggedr          | ragged2e         | Ragged text.                       |
| scrjura          | contract         | Contracts.                         |
| scrlettr         | scrlttr2         | Letters.                           |
| scrpage          | scrlayer-scrpage | Page headers.                      |
| scrpage2         | scrlayer-scrpage | Page headers.                      |
| seminar          | beamer           | Presentations.                     |
| sistyle          | siunitx          | SI units.                          |
| siunit           | siunitx          | SI units.                          |
| subfig           | subcaption       | Sub-figures.                       |
| subfigure        | subcaption       | Sub-figures.                       |
| t1enc            | fontenc          | Font encoding.                     |
| times            | mathptmx         | Times fonts.                       |
| tocstyle         | tocbasic         | Table of contents.                 |
| ucs              | None             | UTF8 is default.                   |
| utopia           | fourier          | Utopia fonts.                      |
| vmargin          | geometry         | Margins.                           |
| xparse           | None             | Use built-in `\NewDocumentCommand` |

## `avoid-let`

Use `\NewCommandCopy` instead of `\let` to create copies of existing commands.

## `avoid-newcommand`

Use `\NewDocumentCommand` instead of `\newcommand` to define commands.

## `avoid-def`

Use `\NewDocumentCommand` instead of `\def` to define commands.
Contrary to `\newcommand`, this hooks ignores cases where (1) the command contains `@`, marking it as internal, or (2) is of the form `\d` for some single digit `d`. This can be useful to temporarily assign a command to a different meaning.

## `avoid-legacy-options`

Use modern key-value system provided by `\DeclareKeys`, `\SetKeys` and `\ProcessKeys` instead of the legacy `\DeclareOption` and `\ProcessOptions`.

See `texdoc clsguide` for more information.

## `avoid-double-dollar`

Use `\[ ... \]` instead of `$$ ... $$` for display math.
