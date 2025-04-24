def get_input():
    # Get initial head position first
    head = int(input("Enter the initial head position (single number): "))
    
    # Get the list of disk requests
    requests = list(map(int, input("Enter the list of disk requests (comma-separated): ").split(',')))
    
    return requests, head

def fcfs_scheduling(requests, head):
    sequence = [head]
    total_movement = 0
    for request in requests:
        total_movement += abs(head - request)
        head = request
        sequence.append(request)
    return sequence, total_movement

def sstf_scheduling(requests, head):
    sequence = [head]
    total_movement = 0
    requests = sorted(requests)
    while requests:
        closest = min(requests, key=lambda x: abs(x - head))
        total_movement += abs(closest - head)
        head = closest
        sequence.append(head)
        requests.remove(closest)
    return sequence, total_movement

def scan_scheduling(requests, head, disk_size=200):
    sequence = [head]
    total_movement = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.sort()
    right.sort()
    
    # SCAN (Moving Right First)
    for track in right:
        total_movement += abs(head - track)
        head = track
        sequence.append(track)
    if right:
        total_movement += abs(head - (disk_size - 1))
        head = disk_size - 1
        sequence.append(disk_size - 1)
    for track in reversed(left):
        total_movement += abs(head - track)
        head = track
        sequence.append(track)
    
    return sequence, total_movement

def c_scan_scheduling(requests, head, disk_size=200):
    sequence = [head]
    total_movement = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.sort()
    right.sort()

    # C-SCAN
    for track in right:
        total_movement += abs(head - track)
        head = track
        sequence.append(track)

    if right:
        total_movement += abs(head - (disk_size - 1))
        head = disk_size - 1
        sequence.append(disk_size - 1)

    total_movement += abs(head - 0)
    head = 0
    sequence.append(0)

    for track in left:
        total_movement += abs(head - track)
        head = track
        sequence.append(track)

    return sequence, total_movement

def look_scheduling(requests, head):
    sequence = [head]
    total_movement = 0
    requests.sort()
    left = [track for track in requests if track < head]
    right = [track for track in requests if track >= head]
    
    # LOOK
    for track in right:
        total_movement += abs(head - track)
        head = track
        sequence.append(track)

    for track in reversed(left):
        total_movement += abs(head - track)
        head = track
        sequence.append(track)

    return sequence, total_movement

def c_look_scheduling(requests, head):
    sequence = [head]
    total_movement = 0
    requests.sort()
    left = [track for track in requests if track < head]
    right = [track for track in requests if track >= head]
    
    # C-LOOK
    for track in right:
        total_movement += abs(head - track)
        head = track
        sequence.append(track)

    if left:
        total_movement += abs(head - left[-1])  # Jump to the smallest request
        head = left[-1]

    for track in reversed(left):
        total_movement += abs(head - track)
        head = track
        sequence.append(track)

    return sequence, total_movement

if __name__ == "__main__":
    # Get user input
    requests, head = get_input()

    # FCFS
    sequence, movement = fcfs_scheduling(requests, head)
    print(f"FCFS Seek Sequence: {sequence}")
    print(f"Total Head Movement: {movement}\n")

    # SSTF
    sequence, movement = sstf_scheduling(requests, head)
    print(f"SSTF Seek Sequence: {sequence}")
    print(f"Total Head Movement: {movement}\n")

    # SCAN
    sequence, movement = scan_scheduling(requests, head)
    print(f"SCAN Seek Sequence: {sequence}")
    print(f"Total Head Movement: {movement}\n")

    # C-SCAN
    sequence, movement = c_scan_scheduling(requests, head)
    print(f"C-SCAN Seek Sequence: {sequence}")
    print(f"Total Head Movement: {movement}\n")

    # LOOK
    sequence, movement = look_scheduling(requests, head)
    print(f"LOOK Seek Sequence: {sequence}")
    print(f"Total Head Movement: {movement}\n")

    # C-LOOK
    sequence, movement = c_look_scheduling(requests, head)
    print(f"C-LOOK Seek Sequence: {sequence}")
    print(f"Total Head Movement: {movement}\n")
