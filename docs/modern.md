# latex-lint-modern

Hooks that check that modern $\LaTeX$ practices are followed.

## `avoid-xparse`

Using the `xparse` package is redundant when using a recent version of $\LaTeX$.

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
