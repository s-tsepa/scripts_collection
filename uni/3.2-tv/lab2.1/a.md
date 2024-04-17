
name: Tsepa Stepan

# Lab 2.1


![](1.png)
![](2.png)
![](3.png)
![](4.png)
![](5.png)
![](6.png)
![](7.png)

Logs: 
`multipass exec ubuntu -- journalctl -e -b -f`

![](8.png)


# Task 2

![](9.png)
![](10.png)
![](11.png)




## Sysbench

`sysbench --num-threads=64 --test=threads --thread-yields=100 --thread-locks=2 run`

| Threads | Latency (min) | (avg)   | (max)   |
|---------|---------------|---------|---------|
| 2       | 15.15         | 16.57   | 52.99   |
| 10      | 35.23         | 83.24   | 156.62  |
| 50      | 136.78        | 408.05  | 668.90  |

![](12.png)

## (3) 

`sysbench --threads=X --time=60 memory --memory-oper=write run`

| Threads | Total time | Latency (max) |
|---------|------------|---------------|
| 2       | 24.9595s   | 12.08         |
| 10      | 23.2246s   | 32.09         |
| 100     | 25.6609s   | 356.02        |


## (4)

`sysbench --test=memory --memory-block-size=1M --memory-total-size=10G run`

![img.png](img.png)

## (5)

Unfortunately, I don't have free 150G on my laptop, so I cannot complete this step 

# Task 3

The default hypervisor for my platform (Archlinux x86-64) is `QEMU`.

Unfortunately, the only **working** hypervisor for my platform is `libvirt`, so I made my first VM on this hypervisor.
Other hypervisors (`qemu` and `lxd`) have some broken drivers, so I cannot make system benchmarking on them. 



