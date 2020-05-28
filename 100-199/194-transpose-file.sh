#!/bin/bash

transpose=`head -n1 file.txt | wc -w`

for i in `seq 1 $transpose`
do
    echo `cut -d' ' -f$i file.txt`
done