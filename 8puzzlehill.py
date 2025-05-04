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

def hill_climbing(start, goal):
    current = start
    step = 0
    while True:
        print_board(current, step)
        h = heuristic(current, goal)
        neighbors = get_neighbors(current)
        
        best = None
        best_h = h
        move_dir = ""

        for neighbor, direction in neighbors:
            h_neighbor = heuristic(neighbor, goal)
            if h_neighbor < best_h:
                best = neighbor
                best_h = h_neighbor
                move_dir = direction

        if best is None:
            print("Stuck in local minimum.\n")
            return

        print(f"Move: {move_dir}, Heuristic: {best_h}")
        current = best
        step += 1

        if current == goal:
            print("Goal reached!")
            return
start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal =  [1, 2, 3, 4, 5, 6, 7, 8, 0]
hill_climbing(start, goal)
