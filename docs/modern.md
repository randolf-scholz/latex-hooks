# latex-lint-modern

Hooks that check that modern $\LaTeX$ practices are followed.

To ignore an error, add `% tex: ignore` to end of the line.

## `avoid-let`

Use `\NewCommandCopy` instead of `\let` to create copies of existing commands.

## `avoid-newcommand`

Use `\NewDocumentCommand` instead of `\newcommand` to define commands.

## `avoid-def`

Use `\NewDocumentCommand` instead of `\def` to define commands.
Contrary to `\newcommand`, this hooks ignores cases where (1) the command contains `@`, marking it as internal, or (2) is of the form `\d` for some single digit `d`.
This can be useful to temporarily assign a command to a different meaning.

## `avoid-double-dollar`

Use `\[ ... \]` instead of `$$ ... $$` for display math[^$$][^l2tabu].

## `avoid-legacy-options`

Use modern key-value system provided by `\DeclareKeys`, `\SetKeys` and `\ProcessKeys` instead of the legacy `\DeclareOption` and `\ProcessOptions`.

See `texdoc clsguide` for more information.

## `avoid-legacy-commands`

Avoid using legacy commands that are considered deprecated. This includes:

- Use the new built-in hook management system instead of `\AtEndPreamble`, `\AfterEndPreamble`, and `\AfterEndDocument`.
  The new hooks are clearer in their timing and do not require the `etoolbox` package. Check `texdoc lthooks` for more information.
- Outdated methods to define commands and environments, such as `\newcommand` and `\newenvironment`,
  should be replaced with the more powerful and flexible `\NewDocumentCommand` and `\NewDocumentEnvironment` interfaces.
- Outdated font commands such as `\rm`, `\bf`, etc. should be replaced with their modern equivalents like `\textrm`, `\textbf`, etc.
  for better font handling and compatibility with packages.[^fonts][^3][^l2tabu].

| outdated              | built-in alternative                    | Source            | description                                                                                                                        |
|-----------------------|-----------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------|
| `\@ifpackageloaded`   | `\IfPackageLoadedTF`                    | clsguide §4.6[^1] | test whether a package is loaded                                                                                                   |
| `\AtEndPreamble`      | `\AddToHook{begindocument/before}{...}` | lthooks §3.1[^2]  | before `aux` file gets parsed                                                                                                      |
| `\AtBeginDocument`    | `\AddToHook{begindocument}{...}`        | lthooks §3.1[^2]  | after `aux` file has been parsed                                                                                                   |
| `\AfterEndPreamble`   | `\AddToHook{begindocument/end}{...}`    | lthooks §3.1[^2]  | immediately after `\begin{document}`                                                                                               |
| `\AtEndDocument`      | `\AddToHook{enddocument}{...}`          | lthooks §3.1[^2]  | at start of end{document}                                                                                                          |
| `\AfterEndDocument`   | `\AddToHook{enddocument/end}{...}`      | lthooks §3.1[^2]  | after the new `aux` has been written and re-read                                                                                   |
| `\uppercase`          | `\MakeUppercase`, `\MakeTitlecase`      | clsguide §5.2[^1] | case changing for text (locale-aware; primitives suggested only for programmatic material)                                         |
| `\lowercase`          | `\MakeLowercase`                        | clsguide §5.2[^1] | case changing for text (locale-aware; primitives suggested only for programmatic material)                                         |
| `\@ifnextchar`        | `\NewDocumentCommand`                   | usrguide §2.4[^0] | replace manual lookahead-based optional-argument parsing with declarative argument signatures (incl. safe nesting of optionals)    |
| `\@ifstar`            | `\IfBooleanTF`                          | usrguide §2.8[^0] | structured star/flag branching (typically used with an `s` argument in `\NewDocumentCommand`)                                      |
| `\newcommand`         | `\NewDocumentCommand`                   | usrguide §2.4[^0] | Command definition                                                                                                                 |
| `\renewcommand`       | `\RenewDocumentCommand`                 | usrguide §2.4[^0] | Command redefinition                                                                                                               |
| `\providecommand`     | `\ProvideDocumentCommand`               | usrguide §2.4[^0] | Command definition if not exists                                                                                                   |
| `\declarecommand`     | `\DeclareDocumentCommand`               | usrguide §2.4[^0] | Command declaration                                                                                                                |
| `\newenvironment`     | `\NewDocumentEnvironment`               | usrguide §2.4[^0] | Environment definition                                                                                                             |
| `\renewenvironment`   | `\RenewDocumentEnvironment`             | usrguide §2.4[^0] | Environment redefinition                                                                                                           |
| `\declareenvironment` | `\DeclareDocumentEnvironment`           | usrguide §2.4[^0] | Environment declaration                                                                                                            |
| `\let`                | `\NewCommandCopy`                       | usrguide §3[^0]   | create a copy of an existing command (robust, with error checking)                                                                 |
| `\let`                | `\RenewCommandCopy`                     | usrguide §3[^0]   | redefine a copy of an existing command (robust, with error checking)                                                               |
| `\let`                | `\DeclareCommandCopy`                   | usrguide §3[^0]   | declare a copy of an existing command (robust, with error checking)                                                                |
| `\let`                | `\NewEnvironmentCopy`                   | usrguide §3[^0]   | create a copy of an existing environment (robust, with error checking)                                                             |
| `\let`                | `\RenewEnvironmentCopy`                 | usrguide §3[^0]   | redefine a copy of an existing environment (robust, with error checking)                                                           |
| `\let`                | `\DeclareEnvironmentCopy`               | usrguide §3[^0]   | declare a copy of an existing environment (robust, with error checking)                                                            |
| `\show`               | `\ShowCommand`                          | usrguide §3[^0]   | show the *real* meaning of robust / `\NewDocumentCommand`-style commands (incl. argument signature), not just a wrapper            |
| `\show`               | `\ShowEnvironment`                      | usrguide §3[^0]   | show begin/end code meaning for environments in a more informative way                                                             |
| `\setbox`             | `\sbox`                                 | clsguide §2.6[^1] | box manipulation using LaTeX box commands (color-safe; modern options comparable to primitives)                                    |
| `\hbox`               | `\mbox`                                 | clsguide §2.6[^1] | box manipulation using LaTeX box commands (color-safe; modern options comparable to primitives)                                    |
| `\vbox`               | `\parbox`                               | clsguide §2.6[^1] | vertical boxing using LaTeX constructs (color-safe; robust scoping)                                                                |
| none                  | `\fpeval`                               | usrguide §5[^0]   | expandable floating-point (and more) evaluation in the kernel (incl. trig, exponentials, rounding, randoms, tuples, etc.)          |
| `\numexpr`            | `\inteval`                              | usrguide §5[^0]   | expandable integer arithmetic wrapper (usable where TeX needs a number; documents the syntax restrictions clearly)                 |
| `\dimexpr`            | `\dimeval`                              | usrguide §5[^0]   | expandable dimension arithmetic wrapper (fast, primitive-backed; usable in assignments/expansion contexts)                         |
| `\glueexpr`           | `\skipeval`                             | usrguide §5[^0]   | expandable skip (“rubber length”) arithmetic wrapper (primitive-backed)                                                            |
| `\@nameuse`           | `\UseName`                              | usrguide §4[^0]   | execute a control sequence constructed from a string (document-level interface to `\csname...\endcsname` usage patterns)           |
| `\edef`               | `\ExpandArgs`                           | usrguide §4[^0]   | expand selected arguments (using an expansion “spec”) before calling a command—cleaner than ad-hoc `\edef`/temporary-csname tricks |
| `\DeclareOption`      | `\DeclareKeys`                          | clsguide §4.5[^1] | declare options using the key–value option system (more flexible and robust than classic option system)                            |
| none                  | `\SetKeys`                              | clsguide §4.5[^1] | set default values for keys (key–value option system)                                                                              |
| `\DeclareOption*`     | `\DeclareUnknownKeyHandler`             | clsguide §4.5[^1] | default handler for unknown *key* options (key–value option system)                                                                |
| `\ProcessOptions`     | `\ProcessKeyOptions`                    | clsguide §4.5[^1] | process options using the key–value option system                                                                                  |
| `\@latexerr`          | `\PackageError`, `\ClassError`          | clsguide §4.8[^1] | report errors with package/class context and consistent formatting                                                                 |
| `\@warning`           | `\PackageWarning`, `\ClassWarning`,     | clsguide §4.8[^1] | emit warnings with package/class context (optionally with/without line numbers)                                                    |
| `\wlog`               | `\PackageInfo`, `\ClassInfo`            | clsguide §4.8[^1] | write informational messages to the log with package/class context                                                                 |
| `\rm`                 | `\textrm{…}`, `\rmfamily`               | fntguide §2[^3]   | roman/serif family: use `\textrm` for an argument, `\rmfamily` as a declaration                                                    |
| `\sf`                 | `\textsf{…}`, `\sffamily`               | fntguide §2[^3]   | sans-serif family                                                                                                                  |
| `\tt`                 | `\texttt{…}`, `\ttfamily`               | fntguide §2[^3]   | typewriter/monospace family                                                                                                        |
| `\bf`                 | `\textbf{…}`, `\bfseries`               | fntguide §2[^3]   | bold series                                                                                                                        |
| `\it`                 | `\textit{…}`, `\itshape`                | fntguide §2[^3]   | italic shape                                                                                                                       |
| `\sl`                 | `\textsl{…}`, `\slshape`                | fntguide §2[^3]   | slanted/oblique shape                                                                                                              |
| `\sc`                 | `\textsc{…}`, `\scshape`                | fntguide §2[^3]   | small caps shape                                                                                                                   |
| `\em`                 | `\emph{…}`                              | fntguide §2[^3]   | emphasis (semantic; typically italic or slanted)                                                                                   |
| `\over`               | `\frac{...}{...}`                       | l2tabu[^l2tabu]   | `\over` is TeX syntax, hard to parse and interacts badly with `amsmath`; `\frac` is clearer and package-friendly                   |
| `\centerline`         | `\centering`                            | l2tabu[^l2tabu]   | `\centerline` is plain TeX, can be incompatible with LaTeX packages and cause weird list/layout effects                            |
| `\parindent=...`      | `\setlength{\parindent}{...}`           | l2tabu[^l2tabu]   | prefer LaTeX length setting (more robust, interacts better with packages like `calc`)                                              |
| `\eqnarray`           | `align`, `align*`, etc.                 | l2tabu[^l2tabu]   | `eqnarray` has spacing and numbering issues; `amsmath` alignments are more consistent and capable                                  |

## `avoid-legacy-environments`

Avoid using legacy environments that are considered deprecated. This includes:

| Legacy Environment    | Built-in alternative          | Source               | Description                                                                                      |
|-----------------------|-------------------------------|----------------------|--------------------------------------------------------------------------------------------------|
| `\begin{appendix}`    | `\appendix`                   | l2tabu §3.2[^l2tabu] | appendix is a switch, not an environment                                                         |
| `\begin{eqnarray}`    | `\begin{align}...\end{align}` | l2tabu §3.3[^l2tabu] | `eqnarray` has spacing/numbering issues; `amsmath` alignments are consistent and more capable    |
| `\begin{displaymath}` | `\[...\]`                     | l2tabu §3.3[^l2tabu] | with `amsmath`, `displaymath` is explicitly discouraged; `\[...\]` is the supported display form |

## `avoid-obsolete-packages`

Checks that certain obsolete packages are not used. Orighinal list from Stefan Kottwitz[^26200],
updated by `l2tabu`[^l2tabu] and custom additions:

- `\CurrentFile` makes `currfile` obsolete.[^currfile]
- `\TrimSpaces` makes `trimspaces` obsolete.

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
| currfile         | None             | Use `\CurrentFile` built-in.       |
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
| trimspaces       | None             | Use `\TrimSpaces`                  |
| twoside          | geometry         | Page layouts.                      |
| txfonts          | newtx            | Times fonts.                       |
| ucs              | None             | UTF8 is default.                   |
| umlaut           | inputenc         | Font encoding.                     |
| utopia           | fourier          | Utopia fonts.                      |
| vmargin          | geometry         | Margins.                           |
| xparse           | None             | Use built-in `\NewDocumentCommand` |
| zefonts          | fontenc+lmodern  | Fonts.                             |

[//]: # (footnotes)
[^0]: <https://www.latex-project.org/help/documentation/usrguide.pdf>
[^1]: <https://www.latex-project.org/help/documentation/clsguide.pdf>
[^2]: <https://www.latex-project.org/help/documentation/lthooks-doc.pdf>
[^3]: <https://www.latex-project.org/help/documentation/fntguide.pdf>
[^l2tabu]: <https://ctan.org/pkg/l2tabu>
[^currfile]: <https://ctan.org/pkg/currfile>
[^fonts]: <https://tex.stackexchange.com/q/15361>
[^$$]: <https://tex.stackexchange.com/q/503>
[^26200]: <https://tex.stackexchange.com/a/26200>
