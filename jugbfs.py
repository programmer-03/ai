from collections import deque

def bfs(target):
    visited = set()
    q = deque([(0, 0)])
    while q:
        j1, j2 = q.popleft()
        
        if(j1, j2) in visited:
            continue
        visited.add((j1, j2))
        print(f"(Jug1: {j1}, jug2: {j2})")
        if j1 == target or j2 == target:
            break

        max1, max2 = 4, 3

        q.extend([
            (0, j2), (j1, 0), (max1, j2), (j1, max2),
            (min(j1+j2, max1), j2-(min(j1+j2, max1)-j1)),
            (j1-(min(j1+j2, max2)-j2), min(j1+j2, max2))
        ])

bfs(2)
