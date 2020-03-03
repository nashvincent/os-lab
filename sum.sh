#!/bin/bash

echo "Enter the number of inputs: "
read n
sum=0
echo "Enter the numbers: "

for ((i=1;i<=n;i++))
do
  read num
  sum=$(expr "$sum" + "$num" )
done

echo "The sum of given number is $sum"

: ' 			OUTPUT
Enter the number of inputs: 
3
Enter the numbers: 
10
20
30
The sum of given number is 60
-
Enter the number of inputs: 
2
Enter the numbers: 
99
1
The sum of given number is 100

'
