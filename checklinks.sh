#!/bin/bash

# Check all html w/the checklink command, a.k.a. the W3C® Link Checker.

LINEH=$(printf '%.0s=' {1..90})

for html in /home/karel/uploads/karelzimmer.nl/httpdocs/html/*.html; do
    echo "
$LINEH"
    checklink   --broken    \
                --summary   \
                "$html"
done
echo "
$LINEH"
