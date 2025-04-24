# LOOK Disk Scheduling Algorithm with Visualization

import matplotlib.pyplot as plt

def look(start, requests):
    requests = sorted(requests)
    head = start
    total = 0
    sequence = []

    # Look algorithm without specifying direction
    up = [r for r in requests if r >= head]
    down = [r for r in requests if r < head][::-1]
    path = up + down

    for r in path:
        total += abs(head - r)
        head = r
        sequence.append(r)
    return total, sequence

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

def get_user_input():
    try:
        start = int(input("Enter initial head position: "))
        requests_input = input("Enter disk requests (comma-separated): ")
        requests = [int(x.strip()) for x in requests_input.split(',') if x.strip().isdigit()]
        return start, requests
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        return None, None

if __name__ == "__main__":
    start, requests = get_user_input()

    if start is not None and requests:
        total, sequence = look(start, requests)
        print("\nLOOK Seek Sequence:", sequence)
        print("Total Head Movement:", total)
        plot_look(start, sequence, total)
    else:
        print("No valid data to process.")
