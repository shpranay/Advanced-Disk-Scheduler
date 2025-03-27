def sstf_scheduling(requests, head):
    sequence = []
    total_movement = 0
    requests = sorted(requests)  # Sort the requests in ascending order

    while requests:
        closest = min(requests, key=lambda x: abs(x - head))  # Find the nearest request
        total_movement += abs(closest - head)  # Calculate movement
        head = closest  # Move head to closest request
        sequence.append(head)  # Save the sequence
        requests.remove(closest)  # Remove processed request

    return sequence, total_movement


# Example Usage
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]  # Example requests
    head = 53  # Initial head position

    sequence, movement = sstf_scheduling(requests, head)
    
    print("Seek Sequence:", sequence)
    print("Total Head Movement:", movement)


def scan_scheduling(requests, head, direction, disk_size=200):
    sequence = []
    total_movement = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]

    left.sort()
    right.sort()

    if direction == "left":
        for track in reversed(left):
            total_movement += abs(head - track)
            head = track
            sequence.append(track)
        if left:
            total_movement += abs(head - 0)
            head = 0
            sequence.append(0)
        for track in right:
            total_movement += abs(head - track)
            head = track
            sequence.append(track)
    
    elif direction == "right":
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

# Example Usage
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53
    direction = "right"  # Change to "left" to move in the other direction

    sequence, movement = scan_scheduling(requests, head, direction)

    print("SCAN Seek Sequence:", sequence)
    print("Total Head Movement:", movement)

