import matplotlib.pyplot as plt

# Disk Scheduling Algorithms
def fcfs(requests, head):
    sequence = [head]
    for r in requests:
        sequence.append(r)
    return sequence

def sstf(requests, head):
    sequence = [head]
    pending = requests[:]
    while pending:
        closest = min(pending, key=lambda x: abs(head - x))
        sequence.append(closest)
        head = closest
        pending.remove(closest)
    return sequence

def scan(requests, head, disk_size=200):
    sequence = [head]
    left = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])

    # No direction sense for SCAN
    sequence.extend(right)
    if right:
        sequence.append(disk_size - 1)
    sequence.extend(reversed(left))
    return sequence

def c_scan(requests, head, disk_size=200):
    sequence = [head]
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    sequence.extend(right)
    if right:
        sequence.append(disk_size - 1)
    sequence.append(0)
    sequence.extend(left)
    return sequence

# Calculate cumulative movements
def cumulative_movements(sequence):
    total = 0
    result = [0]
    for i in range(1, len(sequence)):
        total += abs(sequence[i] - sequence[i - 1])
        result.append(total)
    return result

# Function to get user input
def get_user_input():
    try:
        head = int(input("Enter the initial head position: "))
        req_input = input("Enter disk requests (comma-separated): ")
        requests = [int(x.strip()) for x in req_input.split(',') if x.strip().isdigit()]
        return head, requests
    except ValueError:
        print("Invalid input. Please try again.")
        return None, None

# Main Execution
head, requests = get_user_input()

if head is not None and requests:
    # Get sequences for each algorithm
    seq_fcfs = fcfs(requests, head)
    seq_sstf = sstf(requests, head)
    seq_scan = scan(requests, head)
    seq_cscan = c_scan(requests, head)

    # Cumulative head movements for each sequence
    cum_fcfs = cumulative_movements(seq_fcfs)
    cum_sstf = cumulative_movements(seq_sstf)
    cum_scan = cumulative_movements(seq_scan)
    cum_cscan = cumulative_movements(seq_cscan)

    # Plot the cumulative head movement comparison
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(cum_fcfs)), cum_fcfs, label=f'FCFS ({cum_fcfs[-1]})', marker='o')
    plt.plot(range(len(cum_sstf)), cum_sstf, label=f'SSTF ({cum_sstf[-1]})', marker='o')
    plt.plot(range(len(cum_scan)), cum_scan, label=f'SCAN ({cum_scan[-1]})', marker='o')
    plt.plot(range(len(cum_cscan)), cum_cscan, label=f'C-SCAN ({cum_cscan[-1]})', marker='o')

    plt.xlabel('Sequence Step')
    plt.ylabel('Cumulative Head Movement')
    plt.title('Cumulative Head Movement Comparison')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print("Error: Invalid input provided.")
