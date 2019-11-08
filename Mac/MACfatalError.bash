#!/bin/bash

errorCode=$(( $RANDOM % 32767 + 1 ))
fiftyFifty=$(( $RANDOM % 2 + 1 ))
fiftyFifty=`expr $fiftyFifty \* 2`
fiftyFifty=`expr $fiftyFifty - 3`
errorCode=`expr $fiftyFifty \* $errorCode`

echo FATAL ERROR HAS OCCURRED, ERROR CODE $errorCode
say 'FATAL ERROR. SHUTDOWN AND DESTRUCTION OF COMPUTER IMMINENT. DELETING ALL FILES...'
sleep 8
say 'sudo rm -rf /* activated'
sleep 4
say 'SUCCESS! ALL FILES DELETED. DESTROYING COMPUTER'
sleep 6
say 'SUCCESS!'
sleep 2
osascript -e 'tell app "System Events" to shut down'
