#!/bin/bash

gcc ex3.c

./a.out 3 &
pstree
sleep 5
pstree
sleep 5
pstree

echo; echo;
echo 5555555555555555555555555

./a.out 5 &
pstree | grep a.out
sleep 5
pstree | grep a.out
sleep 5
pstree | grep a.out
sleep 5
pstree | grep a.out
sleep 5
pstree
