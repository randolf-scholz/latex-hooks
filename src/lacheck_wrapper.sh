#!/bin/env bash
# shellcheck disable=SC2016
# NOTE: lacheck only takes a single file at a time, so we need to use xargs
# NOTE: lacheck always returns 0, so we need to grep for output
# NOTE: grep has exit code 1 if no matches are found, so we need to invert with `!`
# NOTE: We add a `--` to the end of the command to ensure that no filenames are interpreted as arguments

CYAN='\033[0;36m'
RESET='\033[0m'

# the pattern to match the error message (returns 3 groups)
PATTERN='^"(.*?)",\s*line\s*(\d+):\s*(.*?)$'
line='$1'
col='$2'
error='$3'

check_file() {
    path=$(dirname "$1")
    fname=$(basename "$1")
    cd "$path" || exit 1
    lacheck "$fname" | perl -ne "
      if (/$PATTERN/){
        if ($error !~ /Do not use @ in LaTeX macro names/) {
          print \"${CYAN}${path}/${line}:${col}:${RESET} ${error}\n\"
        }
      }"
}

exit_status=0

# Iterate over each file passed as an argument
for file in "$@"; do
    # NOTE: skip warning a la 'Style file `...' omitted.
    check_file "$file" | grep -v ".sty' omitted" && exit_status=1
done

exit $exit_status
