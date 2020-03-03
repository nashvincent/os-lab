#!/bin/bash

n=1
while read line
do
	n=$((n+1))
	
done < demo.txt

echo "The number of lines are: "$n