#!/bin/sh

echo "Some text dddddddd" > _ex1.txt
ln _ex1.txt _ex1_1.txt
ln _ex1.txt _ex1_2.txt

cat _ex1.txt
cat _ex1_1.txt
cat _ex1_2.txt

/bin/ls -i
/bin/ls -i > ex1.txt
