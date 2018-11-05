#!/bin/bash
#
# sudo web script allowing user www-data to run commands with root privilegs
# https://github.com/achilikin/RdSpi
# shell_exec('sudo /var/sudowebscript.sh PARAMETER')

case "$1" in
    radiostart)
        rdspi reset
        rdspi volume 5
        rdspi tune 93.20
    ;;
    radiostartstop) # $2 = up OR down | power up/down - powers Si4703 up/down
        rdspi power $2
    ;;
    radioreset) # resets and powers up Si4703, dumps register map while resetting
        rdspi reset
    ;;
    radioseek) # $2 = next OR prev | seeks to the next/prev station
        rdspi seek $2
    ;;
    radiocmd) # run in interactive command mode
        rdspi cmd
    ;;
    radiodump) # dumps Si4703 register
        rdspi dump
    ;;
    radiospacingkhz) # $2 = kHz | sets 200, 100, or 50 kHz spacing
        rdspi spacing $2
    ;;
    radioscan) # $2 = (mode) | scans for radio stations, mode can be specified 1-5, see AN230, Table 23. Summary of Seek Settings (default, recommended, more stations, good quality stations only, most stations)
        rdspi scan $2
    ;;
    radiospectrum) # scans full FM band and prints RSSI
        rdspi spectrum
    ;;
    radiotunefreq) # $2 = freq | tunes to specified FM frequency, for example rdspi tune 9500 or rdspi tune 95.00 or rdspi tune 95. to tune to 95.00 MHz
        rdspi tune $2
    ;;
    radiordsonoff) # $2 = on OR off OR verbose | sets RDS mode, on for RDSPRF
        rdspi rds $2
    ;;
    radiords) # scan for complete RDS PS and Radiotext messages with default 15 seconds timeout
        rdspi rds
    ;;
    radiordsscan) # $2 = [gt G] $3 = [time T] $4 = [log] | scan for RDS messages. Use to gt specify RDS Group Type to scan for, for example 0 for basic tuning and switching information. Use time to specify timeout T in seconds. T = 0 turns off timeout. Use log to scroll output instead on using one-liners.
        rdspi rds $2 $3 $4
    ;;
    radiovolume) # $2 = volume | set audio volume, 0 to mute
        rdspi volume $2
    ;;
    
    radioset) #  $2 = register $3 = value | set specified register
        rdspi set $2=$3
    ;;  
    *) echo "ERROR: invalid parameter: $1 (for $0)"; exit 1 #Fehlerbehandlung
    ;;
esac

exit 0
