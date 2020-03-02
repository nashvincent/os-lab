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
Enter size n
2
10
20
The sum of given number is 30

Enter size n
2
Enter number to add
10
10
The sum of given number is 20
'
