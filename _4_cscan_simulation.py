# C-SCAN (Circular SCAN) Disk Scheduling with Visualization

import matplotlib.pyplot as plt

def cscan_scheduling(requests, head, disk_size=200):
    sequence = []
    total_movement = 0

    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]

    left.sort()
    right.sort()

    # Move towards higher end
    for track in right:
        total_movement += abs(head - track)
        head = track
        sequence.append(track)

    # Jump to start of the disk
    if left:
        total_movement += abs(head - (disk_size - 1))  # go to end
        total_movement += (disk_size - 1)  # jump to 0
        head = 0

        for track in left:
            total_movement += abs(head - track)
            head = track
            sequence.append(track)

    return sequence, total_movement

def visualize_cscan(requests, head, sequence):
    x = [0]
    y = [head]
    x_pos = 1

    for req in sequence:
        x.append(x_pos)
        y.append(req)
        x_pos += 1

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='teal')
    plt.title("C-SCAN Disk Scheduling")
    plt.xlabel("Sequence")
    plt.ylabel("Track Number")
    plt.grid(True)
    plt.xticks(range(len(x)))
    plt.show()

# Example usage
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53

    sequence, movement = cscan_scheduling(requests, head)
    print("C-SCAN Seek Sequence:", sequence)
    print("Total Head Movement:", movement)

    visualize_cscan(requests, head, sequence)
