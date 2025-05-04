def magicsquare(n):
    if n%2==0:
        print("odd only")
        return

    mg = [[0]*n for _ in range(n)]    
    i, j = 0, n//2

    for num in range(1, n*n+1):
        mg[i][j] = num
        ni, nj = (i-1)%n, (j+1)%n

        if mg[ni][nj]:
            i = (i+1)%n
        else:
            i, j = ni, nj
    
    for row in mg:
        print(" ".join(str(x).rjust(2) for x in row))
    
magicsquare(3)


