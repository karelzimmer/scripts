#!/bin/bash
#
# Elapsed time.  Usage:
#
#   t=$(timer)
#   ... # do something
#   printf 'Elapsed time: %s\n' $(timer $t)
#      ===> Elapsed time: 0:01:12
#
#
#####################################################################
# If called with no arguments a new timer is returned.
# If called with arguments the first is used as a timer
# value and the elapsed time is returned in the form HH:MM:SS.
#
function timer()
{
    if [[ $# -eq 0 ]]
    then
#        echo $(($(date '+%s') - 139342)) #dd uu mm ss
#        echo $(($(date '+%s') - 29342)) #uu mm ss
#        echo $(($(date '+%s') - 193)) #mm ss
#        echo $(($(date '+%s') - 13)) # ss
        echo $(date '+%s') #normaal
    else
        local stime=$1
        etime=$(date '+%s')

        if [[ -z "$stime" ]]
        then
            stime=$etime
        fi

        dt=$((etime - stime))       # Verschil ("elaps").
        dd=$((dt / 86400))          # Dagen.
        dh=$((dt % 86400 / 3600))   # Uren.
        dm=$((dt % 3600 / 60))      # Minuten
        ds=$((dt % 60))             # Seconden.
#        echo $(date --date "1970-01-01 00:00:00 $dt sec" "+d %T")
#        echo $(date --date "1970-01-01 $dt sec utc" "+%d-%T")
        printf '%d-%02d:%02d:%02d' $dd $dh $dm $ds
    fi
}
function timer1()
{
    if [[ $# -eq 0 ]]
    then
        echo $(date '+%s')
    else
        local stime=$1
        etime=$(date '+%s')

        if [[ -z "$stime" ]]
        then
            stime=$etime
        fi

        dt=$((etime - stime))       # Verschil ("elaps").
        dd=$((dt / 86400))          # Dagen.
        dh=$((dt % 86400 / 3600))   # Uren.
        dm=$((dt % 3600 / 60))      # Minuten
        ds=$((dt % 60))             # Seconden.
        if [ $dd -eq 0 ]
        then
            printf '%02d:%02d:%02d' $dh $dm $ds
        else
            printf '%d-%02d:%02d:%02d' $dd $dh $dm $ds
        fi
    fi
}

function timer2()
{
    if [[ $# -eq 0 ]]
    then
        echo $(date '+%s')
    else
        local stime=$1
        etime=$(date '+%s')

        if [[ -z "$stime" ]]
        then
            stime=$etime
        fi

        dt=$((etime - stime))       # Verschil ("elaps").
        dd=$((dt / 86400))          # Dagen.
        dh=$((dt % 86400 / 3600))   # Uren.
        dm=$((dt % 3600 / 60))      # Minuten
        ds=$((dt % 60))             # Seconden.
        if [ $dd -eq 0 -a $dh -eq 0 -a $dm -eq 0 ]
        then
            printf '%ds' $ds
        elif [ $dd -eq 0 -a $dh -eq 0 ]
        then
            printf '%dm %ds' $dm $ds
        elif [ $dd -eq 0 ]
        then
            printf '%du %dm %ds' $dh $dm $ds
        else
            printf '%dd %du %dm %ds' $dd $dh $dm $ds
        fi
    fi
}

# If invoked directly run test code.
p=$(basename $0 .sh)
if [[ $p == 'timer' ]]
then
    t=$(timer)
    read -p 'Enter when ready...'
    clear
    echo
    echo "De $p duurde $(timer $(($t - 139342)))."
    echo "De $p duurde $(timer1 $(($t - 139342)))."
    echo
    echo "De $p duurde $(timer2 $(($t - 139342)))."
    echo
    echo
    echo "De $p duurde $(timer $(($t - 29342)))."
    echo "De $p duurde $(timer1 $(($t - 29342)))."
    echo
    echo "De $p duurde $(timer2 $(($t - 29342)))."
    echo
    echo
    echo "De $p duurde $(timer $(($t - 193)))."
    echo "De $p duurde $(timer1 $(($t - 193)))."
    echo
    echo "De $p duurde $(timer2 $(($t - 193)))."
    echo
    echo
    echo "De $p duurde $(timer $(($t - 13)))."
    echo "De $p duurde $(timer1 $(($t - 13)))."
    echo
    echo "De $p duurde $(timer2 $(($t - 13)))."
    echo
    echo
    echo "De $p duurde $(timer $t)."
    echo "De $p duurde $(timer1 $t)."
    echo
    echo "De $p duurde $(timer2 $t)."
    echo
fi
exit

: <<COMMENTBLOCK
        # $..c = counter/teller
        # $..t = tekst
        # $dc  = som counters/tellers

        if [ $dd -eq 0 ]
        then
            ddc=0
        elif [ $dd -eq 1 ]
        then
            ddt='dag'
            ddc=1
        else
            ddt='dagen'
            ddc=1   
        fi
        if [ $dh -eq 0 ]
        then
            dhc=0
        elif [ $dh -eq 1 ]
        then
            dht='uur'
            dhc=1
        else
            dht='uren'
            dhc=1   
        fi
        if [ $dm -eq 0 ]
        then
            dmc=0
        elif [ $dd -eq 1 ]
        then
            dmt='minuut'
            dmc=1
        else
            dmt='minuten'
            dmc=1   
        fi
        if [ $ds -eq 0 ]
        then
            dsc=0
        elif [ $ds -eq 1 ]
        then
            dst='seconde'
            dsc=1
        else
            dst='seconden'
            dsc=1   
        fi
        dc=$(($ddc + $dhc + $dmc + $dsc))
        echo 'dc='$dc
        if [ $dc -eq 4 ]
        then
            echo "duurde $dd $ddt, $dh $dht, $dm $dmt, en $ds $dst."
        fi
COMMENTBLOCK
