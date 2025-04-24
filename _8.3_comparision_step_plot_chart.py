import matplotlib.pyplot as plt

# Scheduling Algorithms

def fcfs(requests, head):
    seq, movement = [], 0
    for r in requests:
        movement += abs(head - r)
        seq.append(r)
        head = r
    return seq, movement

def sstf(requests, head):
    seq, movement = [], 0
    pending = requests[:]
    while pending:
        closest = min(pending, key=lambda x: abs(head - x))
        movement += abs(head - closest)
        seq.append(closest)
        head = closest
        pending.remove(closest)
    return seq, movement

def scan(requests, head, disk_size=200):
    seq, movement = [], 0
    left = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])

    # Process requests in left and right order (No direction sense)
    for r in right:
        movement += abs(head - r)
        seq.append(r)
        head = r
    if right:
        movement += abs(head - (disk_size - 1))
        head = disk_size - 1
    for r in reversed(left):
        movement += abs(head - r)
        seq.append(r)
        head = r

    return seq, movement

def cscan(requests, head, disk_size=200):
    seq, movement = [], 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    # Process requests in right order and wrap around (No direction sense)
    for r in right:
        movement += abs(head - r)
        seq.append(r)
        head = r
    if right:
        movement += abs(head - (disk_size - 1))
        head = disk_size - 1
        movement += head  # jump to 0
        head = 0
    for r in left:
        movement += abs(head - r)
        seq.append(r)
        head = r

    return seq, movement

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

# Main Comparison

head, requests = get_user_input()

if head is not None and requests:
    algos = {
        "FCFS": fcfs,
        "SSTF": sstf,
        "SCAN": lambda r, h: scan(r, h),
        "C-SCAN": cscan
    }

    results = {}
    for name, algo in algos.items():
        seq, movement = algo(requests, head)
        results[name] = (seq, movement)

    # Plot Step Comparison
    plt.figure(figsize=(10, 6))
    for name, (seq, movement) in results.items():
        x = list(range(len(seq)))
        plt.step(x, seq, where='mid', label=f"{name} ({movement})")
        plt.text(x[-1], seq[-1], str(movement), fontsize=8, ha='left', va='bottom')

    plt.title("Step Plot: Disk Scheduling Algorithms")
    plt.xlabel("Sequence Step")
    plt.ylabel("Track Number")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print("Error: Invalid input provided.")
