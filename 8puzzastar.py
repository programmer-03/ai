from heapq import heappush, heappop

def heuristic(state, goal):    
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def print_board(state, step):
    print(f"Step {step}:")
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else ' ' for x in state[i:i+3]))
    print("-" * 10)

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    moves = [(-1, "LEFT"), (1, "RIGHT"), (-3, "UP"), (3, "DOWN")]

    for move, name in moves:
        ni = zero + move
        if 0 <= ni < 9:
            if move == -1 and zero % 3 == 0: continue
            if move == 1 and zero % 3 == 2: continue
            new_state = state[:]
            new_state[zero], new_state[ni] = new_state[ni], new_state[zero]
            neighbors.append((new_state, name))
    return neighbors

def astar(start, goal):
    visited = set()
    pq = []
    heappush(pq, (heuristic(start, goal), 0, start, "Start"))

    while pq:
        f, g, state, move = heappop(pq)
        print_board(state, g)
        print(f"Move: {move}, f={f}, g={g}, h={f-g}")

        if state == goal:
            print(f"Goal reached in {g} steps!")
            return

        visited.add(tuple(state))
        for neighbor, direction in get_neighbors(state):
            if tuple(neighbor) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor, goal)
                heappush(pq, (new_f, new_g, neighbor, direction))

start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal =  [1, 2, 3, 4, 5, 6, 7, 8, 0]
astar(start, goal)