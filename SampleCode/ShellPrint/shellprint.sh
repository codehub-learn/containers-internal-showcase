#!/bin/bash
echo "Starting our script"
MAXTIMES=${1:-1}
i=0
while [ $i -lt $MAXTIMES ]; do
    echo "Hello from Jenkins"
    i=$(( i + 1 ))
done
