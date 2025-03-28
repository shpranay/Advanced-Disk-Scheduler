# SCAN (Elevator) Disk Scheduling with Visualization

import matplotlib.pyplot as plt

def scan_scheduling(requests, head, direction, disk_size=200):
    sequence = []
    total_movement = 0

    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.sort()
    right.sort()

    if direction == "left":
        for track in reversed(left):
            total_movement += abs(head - track)
            head = track
            sequence.append(track)
        if left:
            total_movement += abs(head - 0)
            head = 0
            sequence.append(0)
        for track in right:
            total_movement += abs(head - track)
            head = track
            sequence.append(track)

    elif direction == "right":
        for track in right:
            total_movement += abs(head - track)
            head = track
            sequence.append(track)
        if right:
            total_movement += abs(head - (disk_size - 1))
            head = disk_size - 1
            sequence.append(head)
        for track in reversed(left):
            total_movement += abs(head - track)
            head = track
            sequence.append(track)

    return sequence, total_movement

def visualize_scan(requests, head, sequence):
    x = [0]
    y = [head]
    x_pos = 1

    for req in sequence:
        x.append(x_pos)
        y.append(req)
        x_pos += 1

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='purple')
    plt.title("SCAN Disk Scheduling")
    plt.xlabel("Sequence")
    plt.ylabel("Track Number")
    plt.grid(True)
    plt.xticks(range(len(x)))
    plt.show()

# Example usage
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53
    direction = "right"

    sequence, movement = scan_scheduling(requests, head, direction)
    print("SCAN Seek Sequence:", sequence)
    print("Total Head Movement:", movement)

    visualize_scan(requests, head, sequence)
