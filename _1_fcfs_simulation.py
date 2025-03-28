# FCFS Disk Scheduling Algorithm with Visualization

import matplotlib.pyplot as plt

def fcfs_scheduling(requests, head):
    sequence = []
    total_movement = 0

    for request in requests:
        total_movement += abs(head - request)
        head = request
        sequence.append(head)

    return sequence, total_movement


def visualize_fcfs(requests, head, sequence):
    x = [0]
    y = [head]
    x_pos = 1

    for req in sequence:
        x.append(x_pos)
        y.append(req)
        x_pos += 1

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='green')
    plt.title("FCFS Disk Scheduling")
    plt.xlabel("Sequence")
    plt.ylabel("Track Number")
    plt.grid(True)
    plt.xticks(range(len(x)))
    plt.show()


# Example usage
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53

    sequence, movement = fcfs_scheduling(requests, head)

    print("FCFS Seek Sequence:", sequence)
    print("Total Head Movement:", movement)

    visualize_fcfs(requests, head, sequence)
