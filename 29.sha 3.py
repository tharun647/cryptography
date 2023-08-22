import random

def has_nonzero(state):
    for row in state:
        if any(row):
            return True
    return False

def simulate_sha3(block_size):
    state = [[0] * block_size for _ in range(block_size)]
    rounds = 0

    while not has_nonzero(state):
        # Randomly change state
        i, j = random.randint(0, block_size-1), random.randint(0, block_size-1)
        state[i][j] ^= 1
        rounds += 1

    return rounds

def main():
    print(f"Rounds needed: {simulate_sha3(1024)}")

if __name__ == "__main__":
    main()

Rounds needed: 1
