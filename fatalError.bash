#!/bin/bash

errorCode=$(( $RANDOM % 32767 + 1 ))
fiftyFifty=$(( $RANDOM % 2 + 1 ))
fiftyFifty=`expr $fiftyFifty \* 2`
fiftyFifty=`expr $fiftyFifty - 3`
errorCode=`expr $fiftyFifty \* $errorCode`

echo FATAL ERROR HAS OCCURRED, ERROR CODE $errorCode
spd-say 'FATAL ERROR. SHUTDOWN AND DESTRUCTION OF COMPUTER IMMINENT. DELETING ALL FILES...'
sleep 8
spd-say 'sudo rm -rf /* activated'
sleep 4
spd-say 'SUCCESS! ALL FILES DELETED. DESTROYING COMPUTER'
sleep 6
spd-say 'SUCCESS!'
sleep 2
poweroff
