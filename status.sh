#!/bin/bash

# Toon status-informatie

function status {
    {
        echo -e "\n--distribution:"
        lsb_release --all
        echo -e "\n--system:"
        uname --all
        echo -e "\n--uptime:"
        uptime
        echo -e "\n--disk:"
        df --human-readable 2> /dev/null
        echo -e "\n--block devices:"
        blkid
        echo -e "\n--memory:"
        free --human
        echo -e "\n--temperature:"
        sensors
        echo -e "\n--last backup:"
        if ! ls -1 /var/scripts/backup/*.tar 2> /dev/null; then
            echo "No backups."
        fi    
        echo -e "\n--syslog:"
        tail /var/log/syslog
    } | less
}

status
