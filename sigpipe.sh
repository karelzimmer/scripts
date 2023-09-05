#!/usr/bin/bash

# Test SIGPIPE i.c.m. set -o pipefail ==> SIGPIPE overbodig als pipefail
# http://www.pixelbeat.org/programming/sigpipe_handling.html

#set -o pipefail
trap 'signal ERR      $?' ERR
trap 'signal EXIT     $?' EXIT
trap 'signal SIGINT   $?' SIGINT
trap 'signal SIGPIPE  $?' SIGPIPE
trap 'signal SIGTERM  $?' SIGTERM
trap 'signal SIGHUP   $?' SIGHUP

function signal {
    local signal=${1:-signal?}
    local -i rc=${2:-1}

    echo "signal=$signal, rc=$rc"

    case $signal in
        ERROR)
            # Systeemvariabele $- bevat alle huidige shell-opties.
            # Als shell-optie errexit is aangezet, bevat $- een e.
            # Als uitgezet, geef dan alleen de afsluitwaarde terug.
            if [[ $- == *e* ]]; then
                exit "$rc"
            else
                return "$rc"
            fi
            ;;
        EXIT)
            trap - ERR EXIT SIGINT SIGPIPE SIGTERM SIGHUP
            exit "$rc"
            ;;
        SIG*)
            exit $rc
            ;;
    esac
}

#set +o errexit
#dr # rc=127, notfnd
#yes | head -n1 # rc=141,brokepipe
#yes 1234 | xargs -n1 | head -n1 # signal=13 SIGPIPE, rc=125
yes 1234 | head -n1

exit 1
