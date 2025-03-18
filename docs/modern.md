# latex-lint-modern

Hooks that check that modern $\LaTeX$ practices are followed.

To ignore an error, add `% tex: ignore` to end of the line.

## `avoid-let`

Use `\NewCommandCopy` instead of `\let` to create copies of existing commands.

## `avoid-newcommand`

Use `\NewDocumentCommand` instead of `\newcommand` to define commands.

## `avoid-def`

Use `\NewDocumentCommand` instead of `\def` to define commands.
Contrary to `\newcommand`, this hooks ignores cases where (1) the command contains `@`, marking it as internal, or (2) is of the form `\d` for some single digit `d`. This can be useful to temporarily assign a command to a different meaning.

## `avoid-double-dollar`

Use `\[ ... \]` instead of `$$ ... $$` for display math[^$$][^l2tabu].

## `avoid-legacy-options`

Use modern key-value system provided by `\DeclareKeys`, `\SetKeys` and `\ProcessKeys` instead of the legacy `\DeclareOption` and `\ProcessOptions`.

See `texdoc clsguide` for more information.

## `avoid-legacy-commands`

Avoid using legacy commands that are considered deprecated. This includes:

- Font selection commands like `\rm`, `\it`, `\bf`, `\sf`, `\tt`, or `\sc`:
  Use `\textbf{}`, `\textit{}`, etc. instead[^fonts][^l2tabu].
- `\centerline`: Use `\centering` instead[^l2tabu].
- `\over`: Use `\frac{}{}` instead[^l2tabu].
- `\sloppy`[^l2tabu].
- `\graphicspath`: Use environment variable instead[^l2tabu].

## `avoid-legacy-environments`

Avoid using legacy environments that are considered deprecated. This includes:

- `begin{appendix}`: Use `\appendix` instead[^l2tabu].

## `avoid-obsolete-packages`

Checks that certain obsolete packages are not used. List from Stefan Kottwitz[^26200] and updated[^l2tabu].

| Outdated Package | Alternative      | Description                        |
|------------------|------------------|------------------------------------|
| a4               | geometry         | Page layouts.                      |
| a4wide           | geometry         | Page layouts.                      |
| ae               | fontenc+lmodern  | Font encoding.                     |
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
| eqnarray         | amsmath          | Equation Arrays.                   |
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
| pdfsync          | pdftex           | PDF synchronization.               |
| picinpar         | wrapfig          | Inline figures.                    |
| prosper          | beamer           | Presentations.                     |
| ps4pdf           | pst-pdf          | PDF conversion.                    |
| pslatex          | mathptmx         | Times math.                        |
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
| SIunits          | siunitx          | SI units.                          |
| subfig           | subcaption       | Sub-figures.                       |
| subfigure        | subcaption       | Sub-figures.                       |
| t1enc            | fontenc          | Font encoding.                     |
| times            | newtx            | Times fonts.                       |
| tocstyle         | tocbasic         | Table of contents.                 |
| twoside          | geometry         | Page layouts.                      |
| txdonts          | newtx            | Times fonts.                       |
| ucs              | None             | UTF8 is default.                   |
| umlaut           | inputenc         | Font encoding.                     |
| utopia           | fourier          | Utopia fonts.                      |
| vmargin          | geometry         | Margins.                           |
| xparse           | None             | Use built-in `\NewDocumentCommand` |
| zefonts          | fontenc+lmodern  | Fonts.                             |

[//]: # (footnotes)
[^fonts]: <https://tex.stackexchange.com/q/15361>
[^$$]: <https://tex.stackexchange.com/q/503>
[^l2tabu]: <https://ctan.org/pkg/l2tabu>
[^26200]: <https://tex.stackexchange.com/a/26200>
