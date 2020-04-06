#!/bin/bash
PID=`pidof matchbox-keyboard`
if [ ! -e $PID ]; then
  kill $PID
else
 matchbox-keyboard -s 100 extended  &
fi

