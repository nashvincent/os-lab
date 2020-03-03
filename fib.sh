#!/bin/bash

echo "Enter the limit: "
read n
a=0
b=1
i=2

echo ""
echo $a
echo $b

while [ $i -lt $n ]
do
	i=$((i+1))
	temp=$((a+b))
	echo "$temp"
	a=$b
	b=$temp
done


: '				OUTPUT
Enter the limit: 
3

0
1
1

Enter the limit: 
8

0
1
1
2
3
5
8
13
'
