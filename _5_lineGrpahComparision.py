# Compare FCFS, SSTF, SCAN, and C-SCAN using Line Graph

import matplotlib.pyplot as plt

def fcfs(requests, head):
    total = 0
    sequence = []
    for req in requests:
        total += abs(head - req)
        head = req
        sequence.append(req)
    return sequence, total

def sstf(requests, head):
    total = 0
    sequence = []
    reqs = requests.copy()
    while reqs:
        closest = min(reqs, key=lambda x: abs(x - head))
        total += abs(head - closest)
        head = closest
        sequence.append(head)
        reqs.remove(closest)
    return sequence, total

def scan(requests, head, direction, disk_size=200):
    total = 0
    sequence = []
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.sort()
    right.sort()

    if direction == "left":
        for track in reversed(left):
            total += abs(head - track)
            head = track
            sequence.append(track)
        if left:
            total += abs(head - 0)
            head = 0
            sequence.append(0)
        for track in right:
            total += abs(head - track)
            head = track
            sequence.append(track)

    elif direction == "right":
        for track in right:
            total += abs(head - track)
            head = track
            sequence.append(track)
        if right:
            total += abs(head - (disk_size - 1))
            head = disk_size - 1
            sequence.append(head)
        for track in reversed(left):
            total += abs(head - track)
            head = track
            sequence.append(track)

    return sequence, total

def cscan(requests, head, disk_size=200):
    total = 0
    sequence = []
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.sort()
    right.sort()

    for track in right:
        total += abs(head - track)
        head = track
        sequence.append(track)
    if right:
        total += abs(head - (disk_size - 1))
        head = disk_size - 1
        sequence.append(head)
        total += abs(head - 0)
        head = 0
        sequence.append(head)
    for track in left:
        total += abs(head - track)
        head = track
        sequence.append(track)

    return sequence, total

def compare_algorithms(requests, head, disk_size=200):
    fcfs_seq, fcfs_total = fcfs(requests, head)
    sstf_seq, sstf_total = sstf(requests, head)
    scan_seq, scan_total = scan(requests, head, "right", disk_size)
    cscan_seq, cscan_total = cscan(requests, head, disk_size)

    algorithms = ["FCFS", "SSTF", "SCAN", "C-SCAN"]
    totals = [fcfs_total, sstf_total, scan_total, cscan_total]

    plt.figure(figsize=(8, 5))
    plt.plot(algorithms, totals, marker='o', linestyle='-', color='blue')
    plt.title("Disk Scheduling Algorithms Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Total Head Movement")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53
    compare_algorithms(requests, head)
