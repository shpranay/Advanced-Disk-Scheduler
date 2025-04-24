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

def visualize_sstf(head, sequence):
    x = [0]
    y = [head]
    x_pos = 1

    for req in sequence:
        x.append(x_pos)
        y.append(req)
        x_pos += 1

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')

    for i in range(len(x)):
        plt.text(x[i], y[i], str(y[i]), fontsize=9, ha='right')

    plt.title("SSTF Disk Scheduling")
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
        sequence, movement = sstf_scheduling(requests, head)

        print("\nSSTF Seek Sequence:", sequence)
        print("Total Head Movement:", movement)

        visualize_sstf(head, sequence)
    else:
        print("No valid data to process.")
