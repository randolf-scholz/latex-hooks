# latex-lint-extra

Additional hooks for opinionated $\LaTeX$ style.

## `avoid-makeatletter`

Use `\makeatletter` and `\makeatother` only when necessary.

## `avoid-manual-spacing`

Do no use difficult to read manual spacing commands like `\!`, `\,`, `\:` and `\;`.

## `use-label-convention`

Checks that `\label{..}` commands follow the schema `\label{<tag>:<name>}`, 
matching the regex `[a-z]+:[a-z0-9_]+`. That is, the tag should consist only
of lowercase letters and the name should consist only of digits, underscores and lowercase letters.
Dashes are not allowed to ensure the name can be selected with a simple double click in most editors.

Examples: `\label{sec:intro}` or `\label{fig:example_a}`.

## `use-textoids`

Checks that super- and subscripts do not use the `\text` command.

Instead of writing `x^\text{missing}`, define a macro `\miss` and write `x^\miss`.
