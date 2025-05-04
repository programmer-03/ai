def dfs(jug1, jug2, target, visited):
    if(jug1, jug2) in visited:
        return
    visited.add((jug1, jug2))
    print(f"( jug1:{jug1}, {jug2})")
    if jug1 == target or jug2 == target:
        return True
    
    max1, max2 = 4, 3

    return(
        dfs(0, jug2, target, visited) or
        dfs(jug1, 0, target, visited) or
        dfs(max1, jug2, target, visited) or
        dfs(jug1, max2, target, visited) or
        dfs(min(jug1 + jug2, max1), jug2 - (min(jug1 + jug2, max1)-jug1), target, visited) or
        dfs(jug1-(min(jug1+jug2, max2)-jug2), min(jug1+jug2, max2), target, visited)
    )
dfs(0, 0, 2, set())
        