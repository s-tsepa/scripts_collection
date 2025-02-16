sudo mkdir /mnt/lofsdisk/lib
sudo mkdir /mnt/lofsdisk/lib64
sudo mkdir /mnt/lofsdisk/bin

sudo touch /mnt/lofsdisk/file1
sudo touch /mnt/lofsdisk/file2

sudo cp /usr/lib/libreadline.so.8 /mnt/lofsdisk/lib
sudo cp /usr/lib/libdl.so.2 /mnt/lofsdisk/lib
sudo cp /usr/lib/libc.so.6 /mnt/lofsdisk/lib
sudo cp /usr/lib/libncursesw.so.6 /mnt/lofsdisk/lib
sudo cp /usr/lib64/ld-linux-x86-64.so.2 /mnt/lofsdisk/lib64

sudo cp /usr/lib/libcap.so.2 /mnt/lofsdisk/lib
sudo cp /bin/ls /mnt/lofsdisk/bin

sudo mkdir /mnt/lofsdisk/usr
sudo mv /mnt/lofsdisk/lib /mnt/lofsdisk/lib64 /mnt/lofsdisk/usr

sudo ln -s /mnt/lofsdisk/usr/lib /mnt/lofsdisk/lib
sudo ln -s /usr/lib64 /mnt/lofsdisk/lib64

sudo cp /bin/bash /mnt/lofsdisk/bin/


gcc ex2.c -o ex2.out
sudo cp ex2.out /mnt/lofsdisk/bin/

sudo chroot /mnt/lofsdisk /bin/ex2.out > ex2.txt
echo >> ex2.txt
./ex2.out >> ex2.txt

# sudo umount /mnt

