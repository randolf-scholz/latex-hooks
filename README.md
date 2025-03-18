# latex-hooks

A collection of pre-commit hooks for $\LaTeX$.

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) | [HOOKS](HOOKS) | [CHANGELOG](CHANGELOG.md) | [LICENSE](LICENSE)

## Hooks

- [`chktex`](docs/chktex.md): Wrapper for the [`chktex`](https://ctan.org/pkg/chktex) $\LaTeX$ linter with opinionated defaults.
- [`lacheck`](docs/lacheck.md): Wrapper for the [`lacheck`](https://ctan.org/pkg/lacheck) $\LaTeX$ linter with opinionated defaults.

- [`latex-lint-modern`](docs/modern.md): Hooks that check that modern $\LaTeX$ practices are followed.
  - [`latex-avoid-obsolete-packages`](docs/modern.md#avoid-obsolete-packages)
  - [`latex-avoid-def`](docs/modern.md#avoid-def)
  - [`latex-avoid-let`](docs/modern.md#avoid-let)
  - [`latex-avoid-newcommand`](docs/modern.md#avoid-newcommand)
  - [`latex-avoid-legacy-options`](docs/modern.md#avoid-legacy-options)
  - [`latex-avoid-double-dollar`](docs/modern.md#avoid-double-dollar)
- [`latex-lint-extra`](docs/extra.md): Additional hooks for opinionated $\LaTeX$ style.
  - [`latex-avoid-makeatletter`](docs/extra.md#avoid-makeatletter)
  - [`latex-avoid-manual-spacing`](docs/extra.md#avoid-manual-spacing)
  - [`latex-use-label-convention`](docs/extra.md#use-label-convention)
  - [`latex-use-textoids`](docs/extra.md#use-textoids)
- [`check-seperator-length-XXX`](docs/misc.md#check-seperator-length-xxx): Check that "line separator comments" have a certain length.
