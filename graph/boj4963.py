def dfs(x, y, w, h):
    stack = [[x, y]]

    while len(stack) > 0:
        curNode = stack.pop()
        visited[curNode[0]][curNode[1]] = True

        for i in range(8):
            nextX = curNode[0] + dx[i]
            nextY = curNode[1] + dy[i]

            if nextX in range(h) and nextY in range(w):
                if not visited[nextX][nextY] and graph[nextX][nextY] == 1:
                    stack.append([nextX, nextY])
    return
    

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    graph = []
    visited = [[False for _ in range(w)] for _ in range(h)]
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    cnt = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j, w, h)
                cnt += 1
    
    print(cnt)