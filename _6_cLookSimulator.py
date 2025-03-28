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

# Plotting function for C-LOOK
def plot_c_look(start, sequence, total):
    x = list(range(len(sequence) + 1))
    y = [start] + sequence

    plt.figure(figsize=(10, 5))
    plt.step(x, y, where='mid', label=f'C-LOOK (Total Head Movement: {total})', linewidth=2)

    for i, val in enumerate(y):
        plt.text(x[i], val + 2, str(val), ha='center', va='bottom')

    plt.title('C-LOOK Disk Scheduling')
    plt.xlabel('Sequence')
    plt.ylabel('Disk Track')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    start = 50
    requests = [82, 170, 43, 140, 24, 16, 190]

    total, sequence = c_look(start, requests)
    print("C-LOOK Total Head Movement:", total)
    print("C-LOOK Sequence:", sequence)
    plot_c_look(start, sequence, total)
