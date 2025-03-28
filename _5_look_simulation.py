# LOOK Disk Scheduling Algorithm with Visualization

import matplotlib.pyplot as plt

# LOOK Algorithm
def look(start, requests, direction='up'):
    requests = sorted(requests)
    head = start
    total = 0
    sequence = []

    if direction == 'up':
        up = [r for r in requests if r >= head]
        down = [r for r in requests if r < head][::-1]
        path = up + down
    else:
        down = [r for r in requests if r <= head][::-1]
        up = [r for r in requests if r > head]
        path = down + up

    for r in path:
        total += abs(head - r)
        head = r
        sequence.append(r)
    return total, sequence

# Visualization Function
def plot_look(start, sequence, total):
    positions = [start] + sequence
    plt.figure(figsize=(10, 5))
    plt.step(range(len(positions)), positions, where='mid', marker='o', color='orange')
    for i, pos in enumerate(positions):
        plt.text(i, pos + 2, str(pos), ha='center')
    plt.title(f'LOOK Disk Scheduling\nTotal Head Movement: {total} cylinders')
    plt.xlabel('Operation Number')
    plt.ylabel('Cylinder Number')
    plt.grid(True)
    plt.show()

# Sample usage
if __name__ == "__main__":
    start = 50
    requests = [82, 170, 43, 140, 24, 16, 190]
    total, sequence = look(start, requests, direction='up')
    print("LOOK Total Head Movement:", total)
    print("LOOK Sequence:", sequence)
    plot_look(start, sequence, total)
