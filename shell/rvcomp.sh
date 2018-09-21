#!/bin/bash

ep=ZERO$1
sq=$2
sh=$3
user=$4

dirs="/ppi/Ydrv/shots/"$ep"/"$sq"/"$sh"/work/"$user"/compout/*"
dirary=()
for dirpath in $dirs; do
	dirary+=("$dirpath")
done

i="${#dirary[@]}"-1
echo "${dirary[$i]}"

#path="/ppi/Ydrv/shots/"$ep"/"$sq"/"$sh"/work/"$user"/compout/"$r
if [ -e ${dirary[$i]} ]; then
	/opt/rv-Linux-x86-64-7.2.0/bin/rv ${dirary[$i]} &
else
	echo "${dirary[$i]} not found."
fi
