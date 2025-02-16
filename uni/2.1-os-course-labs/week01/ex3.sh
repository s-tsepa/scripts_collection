#!/bin/sh

date
sleep 3

mkdir 3a

date
sleep 3

mkdir 3b

date
sleep 3

/bin/ls ~ -tr > 3a/home.txt

date
sleep 3

/bin/ls / -tr > 3b/root.txt

cat 3a/home.txt
cat 3b/root.txt

ls 3a
ls 3b
