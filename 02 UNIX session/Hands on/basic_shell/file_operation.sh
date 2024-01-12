#!/bin/bash
filename="sample.txt"
touch $filename
echo "Hello, Unix!" > $filename
cat $filename
rm $filename
