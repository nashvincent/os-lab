#!/bin/bash

echo "Enter the string: "
read string

len=${#string}

for ((i=$len-1;i>=0;i--))
do
	reverse="$reverse${string:$i:1}"
done

if [ "$string" == "$rev" ]
then
	echo "$string is palindrome"
else
	echo "$string is not palindrome"
fi

: '				OUTPUT
Enter the string : 
lol
lol is palindrome
Enter the string : 
afsan
afsan is not palindrome
'