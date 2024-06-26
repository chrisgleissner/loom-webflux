#!/bin/bash
# Measures the system load and creates a CSV file.

if [[ $# -ne 2 ]] ; then
    echo 'Syntax: system-measure.sh <outputCsvFilename> <durationInSeconds>'
    exit 0
fi

outputCsvFilename=$1
durationInSeconds=$2
sarOptions="-ur -n TCP,SOCK,DEV --iface=lo"

function log() {
  echo "$( date +"%H:%M:%S" )" "$1"
}

log "Measuring system for ${durationInSeconds}s..."
rm -f bin/sar.bin
# Columns: # hostname;interval;timestamp;CPU;%user;%nice;%system;%iowait;%steal;%idle[...];kbmemfree;kbavail;kbmemused;%memused;kbbuffers;kbcached;kbcommit;%commit;kbactive;kbinact;kbdirty;IFACE;rxpck/s;txpck/s;rxkB/s;txkB/s;rxcmp/s;txcmp/s;rxmcst/s;%ifutil[...];totsck;tcpsck;udpsck;rawsck;ip-frag;tcp-tw;active/s;passive/s;iseg/s;oseg/s
sar $sarOptions -o bin/sar.bin 1 "$durationInSeconds" >/dev/null
sadf -Udh bin/sar.bin -- $sarOptions | cut -d ";" -f3,5,7,8,14,23-26,32,37-40 > "$outputCsvFilename"
log "Saved $outputCsvFilename"

