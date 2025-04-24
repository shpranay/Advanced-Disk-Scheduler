# C-SCAN (Circular SCAN) Disk Scheduling with Visualization

import matplotlib.pyplot as plt

def cscan_scheduling(requests, head, disk_size=200):
    sequence = []
    total_movement = 0

    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]

    left.sort()
    right.sort()

    # Move towards the higher end first
    for track in right:
        total_movement += abs(head - track)
        head = track
        sequence.append(track)

    if left:
        # Go to end of disk
        total_movement += abs(head - (disk_size - 1))
        head = 0  # Jump to beginning (C-SCAN jump)
        total_movement += (disk_size - 1)  # Full disk jump (no servicing during this jump)

        for track in left:
            total_movement += abs(head - track)
            head = track
            sequence.append(track)

    return sequence, total_movement

def visualize_cscan(head, sequence):
    x = [0]
    y = [head]
    x_pos = 1

    for req in sequence:
        x.append(x_pos)
        y.append(req)
        x_pos += 1

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='teal')

    for i in range(len(x)):
        plt.text(x[i], y[i], str(y[i]), fontsize=9, ha='right')

    plt.title("C-SCAN Disk Scheduling")
    plt.xlabel("Sequence")
    plt.ylabel("Track Number")
    plt.grid(True)
    plt.xticks(range(len(x)))
    plt.show()

def get_user_input():
    try:
        head = int(input("Enter initial head position: "))
        requests_input = input("Enter disk requests (comma-separated): ")
        requests = [int(x.strip()) for x in requests_input.split(',') if x.strip().isdigit()]
        return head, requests
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return None, None

if __name__ == "__main__":
    head, requests = get_user_input()

    if head is not None and requests:
        sequence, movement = cscan_scheduling(requests, head)

        print("\nC-SCAN Seek Sequence:", sequence)
        print("Total Head Movement:", movement)

        visualize_cscan(head, sequence)
    else:
        print("No valid data to process.")

