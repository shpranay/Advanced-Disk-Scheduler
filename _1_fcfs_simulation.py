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

def visualize_fcfs(head, sequence):
    x = [0]
    y = [head]
    x_pos = 1

    for req in sequence:
        x.append(x_pos)
        y.append(req)
        x_pos += 1

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='green')

    for i in range(len(x)):
        plt.text(x[i], y[i], str(y[i]), fontsize=9, ha='right')

    plt.title("FCFS Disk Scheduling")
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
        sequence, movement = fcfs_scheduling(requests, head)

        print("\nFCFS Seek Sequence:", sequence)
        print("Total Head Movement:", movement)

        visualize_fcfs(head, sequence)
    else:
        print("No valid data to process.")

