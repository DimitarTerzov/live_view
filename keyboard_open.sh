#!/bin/bash
PID=`pidof matchbox-keyboard`
if [ ! -e $PID ]; then
  kill $PID
fi
matchbox-keyboard -s 100 extended  &
