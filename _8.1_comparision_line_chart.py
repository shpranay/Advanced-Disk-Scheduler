import matplotlib.pyplot as plt

# FCFS Disk Scheduling Algorithm
def fcfs(requests, head):
    total = 0
    sequence = []
    for req in requests:
        total += abs(head - req)
        head = req
        sequence.append(req)
    return sequence, total

# SSTF Disk Scheduling Algorithm
def sstf(requests, head):
    total = 0
    sequence = []
    reqs = requests.copy()
    while reqs:
        closest = min(reqs, key=lambda x: abs(x - head))
        total += abs(head - closest)
        head = closest
        sequence.append(head)
        reqs.remove(closest)
    return sequence, total

# SCAN Disk Scheduling Algorithm (No Direction Sense)
def scan(requests, head, disk_size=200):
    total = 0
    sequence = []
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.sort()
    right.sort()

    # Process requests in left and right order
    for r in right:
        total += abs(head - r)
        head = r
        sequence.append(r)
    if right:
        total += abs(head - (disk_size - 1))
        head = disk_size - 1
        sequence.append(head)
    for r in reversed(left):
        total += abs(head - r)
        head = r
        sequence.append(r)

    return sequence, total

# C-SCAN Disk Scheduling Algorithm (No Direction Sense)
def cscan(requests, head, disk_size=200):
    total = 0
    sequence = []
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.sort()
    right.sort()

    # Process requests in right order
    for r in right:
        total += abs(head - r)
        head = r
        sequence.append(r)
    if right:
        total += abs(head - (disk_size - 1))
        head = disk_size - 1
        sequence.append(head)
        total += head  # from end to beginning (wrap around)
        head = 0
        sequence.append(head)
    for r in left:
        total += abs(head - r)
        head = r
        sequence.append(r)

    return sequence, total

# LOOK Disk Scheduling Algorithm (No Direction Sense)
def look(start, requests):
    requests = sorted(requests)
    head = start
    total = 0
    sequence = []

    # Simply process the requests from lowest to highest track
    for r in requests:
        total += abs(head - r)
        head = r
        sequence.append(r)

    return sequence, total

# C-LOOK Disk Scheduling Algorithm (No Direction Sense)
def c_look(start, requests):
    requests = sorted(requests)
    head = start
    total = 0
    sequence = []

    # Process requests in sorted order
    for r in requests:
        total += abs(head - r)
        head = r
        sequence.append(r)

    return sequence, total

# Function to get user input for head position and requests
def get_user_input():
    try:
        head = int(input("Enter the initial head position: "))
        req_input = input("Enter disk requests (comma-separated): ")
        requests = [int(x.strip()) for x in req_input.split(',') if x.strip().isdigit()]
        return head, requests
    except ValueError:
        print("Invalid input. Please try again.")
        return None, None

# Function to compare all algorithms and plot results
def compare_algorithms(requests, head, disk_size=200):
    fcfs_seq, fcfs_total = fcfs(requests, head)
    sstf_seq, sstf_total = sstf(requests, head)
    scan_seq, scan_total = scan(requests, head, disk_size)
    cscan_seq, cscan_total = cscan(requests, head, disk_size)
    look_seq, look_total = look(head, requests)  # Direction removed
    clook_seq, clook_total = c_look(head, requests)

    algorithms = ["FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK", "C-LOOK"]
    totals = [fcfs_total, sstf_total, scan_total, cscan_total, look_total, clook_total]

    print("\nTotal Head Movements:")
    print(f"FCFS   : {fcfs_total}")
    print(f"SSTF   : {sstf_total}")
    print(f"SCAN   : {scan_total}")
    print(f"C-SCAN : {cscan_total}")
    print(f"LOOK   : {look_total}")
    print(f"C-LOOK : {clook_total}")

    # Plot the results
    plt.figure(figsize=(8, 5))
    plt.plot(algorithms, totals, marker='o', linestyle='-', color='blue')
    plt.title("Disk Scheduling Algorithms Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Total Head Movement")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    head, requests = get_user_input()
    if head is not None and requests:
        compare_algorithms(requests, head)
    else:
        print("Error: Invalid input provided.")
