#!/bin/bash
# Removes old revisions of snaps
# CLOSE ALL SNAPS BEFORE RUNNING THIS
set -eu
snap list --all | awk '/uitgeschakeld/{print $1, $3}' |
    while read -r snapname revision; do
        snap remove "$snapname" --revision="$revision"
    done
