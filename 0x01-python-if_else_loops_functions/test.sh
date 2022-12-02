#!/bin/bash
i=1

while [ $i -le 10 ] ; do
	echo "$i"
	(( i += 1 ))
done

line=1

while read -r CURRENT_LINE
do
	echo "$LINE: $CURRENT_LINE"
	(( LINE++ ))
done < "bash_exe"



read -p "Enter a number " num
echo
case $num in
	1) echo "You enter bash";;
	2) echo "You select perl";;
	3) echo "You select python";;
	4) exit;;
	*) echo "You don't select anything: number is between 1 and 4"
esac
