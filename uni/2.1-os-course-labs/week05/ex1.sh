#!/bin/bash


term=alacritty

gcc publisher.c -o publisher
gcc subscriber.c -o subscriber

$term -e ./publisher $1 --hold &

for i in `seq 1 $1`;
do
    $term -e ./subscriber --hold &
done
