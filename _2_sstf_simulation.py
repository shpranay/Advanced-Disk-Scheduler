# SSTF (Shortest Seek Time First) Disk Scheduling with Visualization

import matplotlib.pyplot as plt

def sstf_scheduling(requests, head):
    sequence = []
    total_movement = 0
    requests = requests.copy()

    while requests:
        closest = min(requests, key=lambda x: abs(x - head))
        total_movement += abs(closest - head)
        head = closest
        sequence.append(closest)
        requests.remove(closest)

    return sequence, total_movement

def visualize_sstf(requests, head, sequence):
    x = [0]
    y = [head]
    x_pos = 1

    for req in sequence:
        x.append(x_pos)
        y.append(req)
        x_pos += 1

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title("SSTF Disk Scheduling")
    plt.xlabel("Sequence")
    plt.ylabel("Track Number")
    plt.grid(True)
    plt.xticks(range(len(x)))
    plt.show()

# Example usage
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53

    sequence, movement = sstf_scheduling(requests, head)
    print("SSTF Seek Sequence:", sequence)
    print("Total Head Movement:", movement)

    visualize_sstf(requests, head, sequence)
