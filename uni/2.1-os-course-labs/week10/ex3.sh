#!/bin/sh

echo "Stepan" > _ex3.txt
chmod -x _ex3.txt >> ex3.txt
chmod 707 _ex3.txt >> ex3.txt
chmod 666 _ex3.txt >> ex3.txt

echo "1) 660 Means read & write permissions for user and group, and no perms for others\n" >> ex3.txt
echo "2) 775 Means all permissions for user and group, and read & execute perms for others\n" >> ex3.txt
echo "3) 777 Means all permissions for user, group, and others\n" >> ex3.txt
