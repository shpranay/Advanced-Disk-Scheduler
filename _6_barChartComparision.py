# Bar Chart Comparison of Disk Scheduling Algorithms

import matplotlib.pyplot as plt

# Sample request queue and head position
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53

def fcfs(requests, head):
    total = 0
    current = head
    for r in requests:
        total += abs(current - r)
        current = r
    return total

def sstf(requests, head):
    total = 0
    current = head
    local_requests = requests.copy()
    while local_requests:
        closest = min(local_requests, key=lambda x: abs(x - current))
        total += abs(current - closest)
        current = closest
        local_requests.remove(closest)
    return total

def scan(requests, head, direction="right", disk_size=200):
    total = 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r > head])
    if direction == "left":
        for r in reversed(left):
            total += abs(head - r)
            head = r
        if left:
            total += abs(head - 0)
            head = 0
        for r in right:
            total += abs(head - r)
            head = r
    else:
        for r in right:
            total += abs(head - r)
            head = r
        if right:
            total += abs(head - (disk_size - 1))
            head = disk_size - 1
        for r in reversed(left):
            total += abs(head - r)
            head = r
    return total

def c_scan(requests, head, disk_size=200):
    total = 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r > head])
    for r in right:
        total += abs(head - r)
        head = r
    if right:
        total += abs(head - (disk_size - 1))
        total += disk_size - 1  # from end to beginning (wrap around)
        head = 0
    for r in left:
        total += abs(head - r)
        head = r
    return total

# Compute head movements
fcfs_movement = fcfs(requests, head)
sstf_movement = sstf(requests, head)
scan_movement = scan(requests, head)
cscan_movement = c_scan(requests, head)

# Plot bar chart
algorithms = ['FCFS', 'SSTF', 'SCAN', 'C-SCAN']
movements = [fcfs_movement, sstf_movement, scan_movement, cscan_movement]

plt.figure(figsize=(8, 5))
plt.bar(algorithms, movements, color=['blue', 'green', 'orange', 'red'])
plt.title('Disk Scheduling Algorithm Comparison')
plt.xlabel('Algorithms')
plt.ylabel('Total Head Movement')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
