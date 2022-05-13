 opt='--xz'
#opt='--bzip2'
#opt='--gz'
# opt=''
tar --create                        \
    $opt                            \
    "$HOME/Documenten/Checklists"   \
    "$HOME/debs"                    \
    "$HOME/scripts.dev"             \
    "$HOME/Programma's"             \
    "$HOME/scripts"                 \
    "$HOME/scripts.arch"            \
    "$HOME/uploads"                 \
    --file=/tmp/scripts.tar

#xz : 43s/ 98 MB (--xz)
#bz2: 17s/101 MB (--bzip2)
#gz :  4s/103 MB (--gzip)
#NVT:  0s/119 MB ()                 <=== snelheid >>, grootte ~ gz/bz2
