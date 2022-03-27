#!/bin/bash

# Generate PDFs w/lowriter (ilo enscript + ps2pfd).

SOURCE=/home/karel/kz-uploads/app/data/linux-archief/scripts
TARGET=/tmp/pdfs
temptextfile=''

echo 'Genereer PDFs:'
rm --force --recursive $TARGET || exit 1
mkdir --parents $TARGET || exit 1
cd $SOURCE || exit 1
for file in *; do
    # Must copy each file with suffix '.txt' added before converting because:
    # 1. desktop-files have XML inside which gets interpreted by Libre Office,
    # 2. 'lowriter convert-to pdf' replaces last suffix (if any) by '.pdf'.
    temptextfile=/tmp/$file.txt
    echo "copy $file -> $temptextfile"
    cp "$file" "$temptextfile" || exit 1
    lowriter    --headless          \
                --convert-to pdf    \
                --outdir $TARGET    \
                "$temptextfile"     || exit 1
    rm "$temptextfile" || exit 1
    echo
done
