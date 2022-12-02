#!/bin/bash

if [ $# -gt 0 ]
then
	for file in $@
	do
		chmod +x $file
	done
else
	echo "No Args passed"
fi
