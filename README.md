# Advanced Disk Scheduling Simulator

This project is a Python-based simulator for various disk scheduling algorithms. It includes:

- **FCFS (First-Come-First-Serve)**
- **SSTF (Shortest Seek Time First)**
- **SCAN**
- **C-SCAN**
- **LOOK**
- **C-LOOK**


This project is divided into several modules, each implementing a different disk 
scheduling algorithm. Users provide the request queue and initial head position, 
and each module calculates the total head movement and serves the requests 
accordingly. A separate module generates graphs for comparison. 


Module 1: FCFS (First Come First Serve) 
This module services the disk requests in the exact order they arrive. It is simple 
but not always efficient in terms of head movement. 

Module 2: SSTF (Shortest Seek Time First) 
It selects the request closest to the current head position, reducing seek time. 
However, it may cause starvation for distant requests. 

Module 3: SCAN 
Also known as the elevator algorithm, the head moves in one direction, 
servicing requests along the way, then reverses direction at the end. 

Module 4: CSCAN (Circular SCAN) 
Similar to SCAN, but instead of reversing direction, the head returns to the 
beginning and continues in the same direction, providing a more uniform wait 
time. 

Module 5: LOOK 
The head moves in one direction like SCAN, but it only goes as far as the last 
request in that direction, then reverses. 

Module 6: CLOOK (Circular LOOK) 
A variation of LOOK where the head moves only as far as the last request, then 
jumps back to the beginning of the queue and continues. 

Module 7: Graph Comparison Module 
This module plots graphs comparing the total head movements of all algorithms 
for the given input, helping users visualize performance differences. 
