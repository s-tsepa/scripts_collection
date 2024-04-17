## Custom Container Script

This Bash script provides a simplified way to create an isolated environment similar to a Docker container.
It combines all the necessary steps to create a working isolated process with its own namespace, filesystem, and resource constraints.
### Usage

Clone this repository or copy the script to your local machine.
Make the script executable and run it:

```bash
chmod +x my-docker.sh
sudo ./my-docker.sh
```
### Description

The script performs the following steps:

- Builds base Docker image which will become rootfs for further process
- Builds the Rootfs image: creates container from image and exports it to `.tar` archive
- Creates a loop device: allocates file with ext4 fs and mounts it to the next available device at `/loop`
- And finally, runs custom "container":
  - creates a `cgroup` for CPU and mem constraints
  - changes further root for process using `chroot`, isolating environment
  - executes a new process with its own namespace using `unshare`, isolating mount, PID, and IPC namespaces
- Cleanup: On exiting process, it deletes cgroup, unmounts fs, removes build docker image & container

### Altering variables

Adjust the script parameters such as image name, size, and mount path as needed for your use case.
