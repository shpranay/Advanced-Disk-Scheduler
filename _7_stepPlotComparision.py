# Simplified Step Plot Comparison of Disk Scheduling Algorithms

import matplotlib.pyplot as plt

# Scheduling Algorithms

def fcfs(requests, head):
    seq, movement = [], 0
    for r in requests:
        movement += abs(head - r)
        seq.append(r)
        head = r
    return seq, movement

def sstf(requests, head):
    seq, movement = [], 0
    pending = requests[:]
    while pending:
        closest = min(pending, key=lambda x: abs(head - x))
        movement += abs(head - closest)
        seq.append(closest)
        head = closest
        pending.remove(closest)
    return seq, movement

def scan(requests, head, direction='left', disk_size=200):
    seq, movement = [], 0
    left = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])

    if direction == 'left':
        for r in left:
            movement += abs(head - r)
            seq.append(r)
            head = r
        if left:
            movement += head  # move to 0
            head = 0
        for r in right:
            movement += abs(head - r)
            seq.append(r)
            head = r
    else:
        for r in right:
            movement += abs(head - r)
            seq.append(r)
            head = r
        if right:
            movement += disk_size - 1 - head  # move to end
            head = disk_size - 1
        for r in reversed(left):
            movement += abs(head - r)
            seq.append(r)
            head = r
    return seq, movement

def cscan(requests, head, disk_size=200):
    seq, movement = [], 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    for r in right:
        movement += abs(head - r)
        seq.append(r)
        head = r
    if right:
        movement += (disk_size - 1 - head) + (disk_size - 1)
        head = 0
    for r in left:
        movement += abs(head - r)
        seq.append(r)
        head = r
    return seq, movement

# Main Comparison

requests = [98, 183, 37, 122, 14, 124, 65, 67]
start_head = 53

algos = {
    "FCFS": fcfs,
    "SSTF": sstf,
    "SCAN": lambda r, h: scan(r, h, 'left'),
    "C-SCAN": cscan
}

results = {}
for name, algo in algos.items():
    seq, movement = algo(requests, start_head)
    results[name] = (seq, movement)

# Plot Step Comparison

plt.figure(figsize=(10, 6))
for name, (seq, movement) in results.items():
    x = list(range(len(seq)))
    plt.step(x, seq, where='mid', label=f"{name} ({movement})")
    plt.text(x[-1], seq[-1], str(movement), fontsize=8, ha='left', va='bottom')

plt.title("Step Plot: Disk Scheduling Algorithms")
plt.xlabel("Sequence Step")
plt.ylabel("Track Number")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
