#!/bin/bash

if [ $# -gt 0 ]
then
	for file in $@
	do
		touch $file
		chmod +x $file
	done
else
	echo "Format $0 [file1, file2, ...]"
fi
