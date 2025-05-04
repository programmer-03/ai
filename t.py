from heapq import heappush, heappop

def heuristic(state, goal):
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)

def get_neighbors(state):
    zero = state.index(0)
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, up, down
    row, col = divmod(zero, 3)
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            ni = r * 3 + c
            new_state = state[:]
            new_state[zero], new_state[ni] = new_state[ni], new_state[zero]
            neighbors.append(new_state)
    return neighbors

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def best_first(start, goal):
    visited = set()
    pq = [(heuristic(start, goal), start, "Start")]
    steps = 0
    while pq:
        h, state, move = heappop(pq)
        print(f"\nMove {steps}: {move}")
        print_board(state)
        if state == goal:
            print("Goal reached!")
            return
        visited.add(tuple(state))
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                heappush(pq, (heuristic(neighbor, goal), neighbor, "Move"))
        steps += 1
    print("No solution.")

# Example run
if __name__ == "__main__":
    best_first([1,2,3,4,5,6,0,7,8], [1,2,3,4,5,6,7,8,0])
