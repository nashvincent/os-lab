#!/bin/bash

echo "Input a number: "
read n
fact=1
if [ $n -lt 2 ]
then
	echo $fact
else
	for ((i=1;i<=n;i++))
	do
		fact=$((fact*i))
	done
	echo "The factorial of $n is $fact"
fi

: '				OUTPUT
Input a number: 
3
The factorial of 3 is 6
Input a number: 
5
The factorial of 5 is 120
'
