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
