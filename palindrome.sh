#!/bin/bash

echo "Enter the string: "
read string

len=${#string}

for ((i=$len-1;i>=0;i--))
do
	reverse="$reverse${string:$i:1}"
done

if [ "$string" == "$reverse" ]
then
	echo "It is a palindrome"
else
	echo "It is not a palindrome"
fi

: '				OUTPUT
Enter the string: 
malayalam
It is a palindrome
Enter the string: 
cat
It is not a palindrome
'
