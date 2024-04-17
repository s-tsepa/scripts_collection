#!/bin/bash

DOCKER_BASE="my-base-image"
ROOTFS_TAR="./rootfs.tar"
IMAGE_NAME="img1"
IMAGE_PATH="./$IMAGE_NAME"
MOUNT_PATH="./mnt"
FS_SIZE="1G"

# --- Build ---

mkdir workdir
chmod 777 workdir
cd workdir

echo "FROM ubuntu
RUN apt update -y && apt install -y sysbench" >Dockerfile

# --- Building rootfs image ---

docker build ./ -t $DOCKER_BASE
container_id=$(docker create $DOCKER_BASE)
echo "container_id: $container_id"

docker export $container_id -o $ROOTFS_TAR

# --- Creating loop device ---

fallocate -l $FS_SIZE $IMAGE_PATH
loop_device=$(losetup -fP --show $IMAGE_PATH)
echo "loop_device: $loop_device"
mkfs.ext4 $loop_device

mkdir -p $MOUNT_PATH
mount -o loop $loop_device $MOUNT_PATH

tar xf $ROOTFS_TAR -C $MOUNT_PATH

# --- Run ----

control_group="cpu,memory:$IMAGE_NAME"
cgcreate -g $control_group
cgexec -g $control_group unshare --fork --mount --pid chroot $MOUNT_PATH /bin/bash

# --- Removal ---

cgdelete $control_group

umount -r $MOUNT_PATH
# rm -rf $MOUNT_PATH $ROOTFS_TAR $IMAGE_PATH
cd ../
rm -rf workdir

docker container rm $container_id
docker image rm $DOCKER_BASE
