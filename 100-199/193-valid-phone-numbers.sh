#!/bin/bash

# while read line
# do
#     echo $line | grep -E "^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$"
# done < file.txt

cat file.txt | grep -E "^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$"