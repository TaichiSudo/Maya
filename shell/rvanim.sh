#!/bin/bash

ep=ZERO$1
sq=$2
sh=$3
user=$4

qt=$ep"_"$sq"_"$sh"_ANM_AP.mjpeg.mov"

dirs="/ppi/Wdrv/shots/"$ep"/"$sq"/"$sh"/ANM/AP/c/*"
dirary=()
for dirpath in $dirs; do
	dirary+=("$dirpath")
done

i="${#dirary[@]}"-1
path="${dirary[$i]}/QT/$qt"
echo "$path"


if [ -e $path ]; then
	/opt/rv-Linux-x86-64-7.2.0/bin/rv $path &
else
	echo "$path not found."
fi
