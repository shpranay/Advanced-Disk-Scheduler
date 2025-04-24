# C-LOOK Disk Scheduling Algorithm

import matplotlib.pyplot as plt

def c_look(start, requests):
    requests = sorted(requests)
    head = start
    total = 0
    sequence = []

    up = [r for r in requests if r >= head]
    down = [r for r in requests if r < head]
    path = up + down

    for r in path:
        total += abs(head - r)
        head = r
        sequence.append(r)

    return total, sequence

def plot_c_look(start, sequence, total):
    x = list(range(len(sequence) + 1))
    y = [start] + sequence

    plt.figure(figsize=(10, 5))
    plt.step(x, y, where='mid', label=f'C-LOOK (Total Head Movement: {total})', linewidth=2, color='brown')

    for i, val in enumerate(y):
        plt.text(x[i], val + 2, str(val), ha='center', va='bottom')

    plt.title('C-LOOK Disk Scheduling')
    plt.xlabel('Sequence')
    plt.ylabel('Disk Track')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def get_user_input():
    try:
        start = int(input("Enter initial head position: "))
        requests_input = input("Enter disk requests (comma-separated): ")
        requests = [int(x.strip()) for x in requests_input.split(',') if x.strip().isdigit()]
        return start, requests
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        return None, None

if __name__ == "__main__":
    start, requests = get_user_input()

    if start is not None and requests:
        total, sequence = c_look(start, requests)
        print("\nC-LOOK Seek Sequence:", sequence)
        print("Total Head Movement:", total)
        plot_c_look(start, sequence, total)
    else:
        print("No valid data to process.")

