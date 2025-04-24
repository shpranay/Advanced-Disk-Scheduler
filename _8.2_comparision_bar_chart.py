  import matplotlib.pyplot as plt

# Sample request queue and head position
def get_input():
    # Get input from the user (for head position and request queue)
    head = int(input("Enter the initial head position: "))
    requests = list(map(int, input("Enter the disk request queue (comma separated): ").split(',')))
    return head, requests

# FCFS Disk Scheduling Algorithm
def fcfs(requests, head):
    total = 0
    current = head
    for r in requests:
        total += abs(current - r)
        current = r
    return total

# SSTF Disk Scheduling Algorithm
def sstf(requests, head):
    total = 0
    current = head
    local_requests = requests.copy()
    while local_requests:
        closest = min(local_requests, key=lambda x: abs(x - current))
        total += abs(current - closest)
        current = closest
        local_requests.remove(closest)
    return total

# SCAN Disk Scheduling Algorithm (No Direction Sense)
def scan(requests, head, disk_size=200):
    total = 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r > head])
    
    # Process the requests in left and right order
    for r in right:
        total += abs(head - r)
        head = r
    if right:
        total += abs(head - (disk_size - 1))
        head = disk_size - 1
    for r in reversed(left):
        total += abs(head - r)
        head = r

    return total

# C-SCAN Disk Scheduling Algorithm (No Direction Sense)
def c_scan(requests, head, disk_size=200):
    total = 0
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r > head])
    
    # Process the requests in right order
    for r in right:
        total += abs(head - r)
        head = r
    if right:
        total += abs(head - (disk_size - 1))
        total += disk_size - 1  # from end to beginning (wrap around)
        head = 0
    for r in left:
        total += abs(head - r)
        head = r

    return total

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

    return total, sequence

# C-LOOK Disk Scheduling Algorithm (No Direction Sense)
def c_look(start, requests):
    requests = sorted(requests)
    head = start
    total = 0
    sequence = []

    # Process requests in sorted order, from head position
    for r in requests:
        total += abs(head - r)
        head = r
        sequence.append(r)

    return total, sequence

# Function to compute movements and plot graph
def plot_comparison(requests, head):
    # Compute head movements for each algorithm
    fcfs_movement = fcfs(requests, head)
    sstf_movement = sstf(requests, head)
    scan_movement = scan(requests, head)
    cscan_movement = c_scan(requests, head)
    look_movement, _ = look(head, requests)
    clook_movement, _ = c_look(head, requests)

    # Plot bar chart
    algorithms = ['FCFS', 'SSTF', 'SCAN', 'C-SCAN', 'LOOK', 'C-LOOK']
    movements = [fcfs_movement, sstf_movement, scan_movement, cscan_movement, look_movement, clook_movement]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(algorithms, movements, color=['blue', 'green', 'orange', 'red', 'purple', 'cyan'])
    plt.title('Disk Scheduling Algorithm Comparison')
    plt.xlabel('Algorithms')
    plt.ylabel('Total Head Movement')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Annotate bars with values
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height + 5, f'{height}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    head, requests = get_input()  # Get user input
    plot_comparison(requests, head)  # Plot the comparison
