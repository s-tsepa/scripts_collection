#!/bin/sh


inodenum=791533

echo "Stepan" > ../week01/file.txt
link ../week01/file.txt _ex2.txt
ls -i _ex2.txt
find ../ -inum $inodenum
find ../ -inum $inodenum > ex2.txt
find ../ -inum $inodenum -exec rm {} \; >> ex2.txt
