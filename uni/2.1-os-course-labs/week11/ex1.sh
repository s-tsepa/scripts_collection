#!/bin/bash


loop=/dev/loop0

sudo dd if=/dev/zero of=a.img status=progress bs=4M count=20
sudo losetup -f a.img
losetup -a
sudo mkfs.ext4 $loop
sudo mount $loop /mnt
cd /mnt
sudo mkdir lofsdisk
cd /mnt/lofsdisk
