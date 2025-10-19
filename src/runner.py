#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "identify"
# ]
# ///

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Sequence

from identify import identify

type FilePath = str | Path


@dataclass(frozen=True, slots=True)
class Check:
    ID: str
    name: str
    message: str
    description: str
    entry: str

def parse_checks(file_path: Path) -> list[Check]:
    r"""Parse check definitions from a YAML file."""
    return []


def parse_check_definition(yaml_content: str) -> Check:
    r"""Parse a check definition from its YAML content."""
    return Check(
        ID="",
        name="",
        message="",
        description="",
        entry="",
    )


def load_checks() -> dict[str, Check]:
    r"""Load available checks.

    These are stored as .yaml files in the `checks/` directory.
    """
    return {}


def run_checks(target: FilePath, checks: Sequence[Check]) -> int:
    r"""Run the selected checks on the given file paths."""
    return 0


def get_files_of_kind(
    files_or_pattern: Iterable[str],
    /,
    *,
    kind: str,
    root: Optional[Path] = None,
    raise_notfound: bool = True,
    relative_to_root: bool = False,
    ignore_hidden: bool = True,
) -> list[Path]:
    r"""Get all python files from the given list of files or patterns."""
    paths: list[Path] = [Path(item).absolute() for item in files_or_pattern]

    # determine the root directory
    if root is None:
        root = (
            paths[0] if len(paths) == 1 and paths[0].is_dir() else Path.cwd().absolute()
        )

    files: list[Path] = []
    for path in paths:
        if path.exists():
            if path.is_file():
                assert kind in identify.tags_from_path(str(path))
                # check that if ignore_hidden is set, the file is not hidden
                assert not (
                    ignore_hidden and any(part.startswith(".") for part in path.parts)
                )
                files.append(path)
            if path.is_dir():
                for file in path.rglob("*"):
                    if (
                        file.is_file()
                        and kind in identify.tags_from_path(str(file))
                        and (
                            not any(part.startswith(".") for part in file.parts)
                            or not ignore_hidden
                        )
                    ):
                        files.append(file)
        # else: path does not exist
        matches = list(root.glob(path.name))
        if not matches and raise_notfound:
            raise FileNotFoundError(f"Pattern {path!r} did not match any files.")
        files.extend(matches)

    if relative_to_root:
        files = [file.relative_to(root) for file in files]

    return files



def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the application with specified options."
    )
    parser.add_argument(
        "--select",
        type=str,
        default=["ALL"],
        help="Which checks to run (use 'ALL' to select all checks).",
    )
    parser.add_argument(
        "--ignore",
        type=str,
        default="",
        help="Which checks to ignore (comma-separated list).",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=str,
        help="Paths to the files to check.",
    )

    args = parser.parse_args()
    known_checks = load_checks()

    selected_check_ids: list[str] = args.select.split(",")
    assert selected_check_ids, "No checks selected to run."

    ignored_check_ids: list[str] = args.ignore.split(",")
    chosen_checks: list[Check] = [
        known_checks[check_id]
        for check_id in selected_check_ids
        if check_id not in ignored_check_ids
    ]
    assert chosen_checks, "All selected checks were ignored."

    if "ALL" in chosen_checks:
        chosen_checks = list(known_checks)

    unknown_checks = set(chosen_checks) - set(known_checks)
    unknown_ignores = set(ignored_check_ids) - set(known_checks)
    assert not unknown_checks, f"Unknown checks selected: {unknown_checks}"
    assert not unknown_ignores, f"Unknown checks ignored: {unknown_ignores}"

    # run checks for all files
    file_paths: list[Path] = get_files_of_kind(args.paths, kind="tex")

    violations = 0
    exceptions = []

    for file_path in file_paths:
        try:
            violations += run_checks(file_path, checks=chosen_checks)
        except Exception as e:
            exceptions.append((file_path, e))

    if exceptions:
        exc = ExceptionGroup(exceptions)
        exc.add_note("Some files could not be processed due to errors.")
        for file_path, exception in exceptions:
            exc.add_note(f"Error processing {file_path}: {exception}")
        raise exc

    if violations:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
