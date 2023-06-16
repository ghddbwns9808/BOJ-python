def dfs(startX, startY, N):
    cnt = 1
    stack = [[startX, startY]]
    visited[startX][startY] = True

    while len(stack) > 0:
        curNode = stack.pop()

        for i in range(4):
            nextX = curNode[0] + dx[i]
            nextY = curNode[1] + dy[i]

            if nextX in range(N) and nextY in range(N):
                if not visited[nextX][nextY] and graph[nextX][nextY] == '1':
                    stack.append([nextX, nextY])
                    visited[nextX][nextY] = True
                    cnt += 1
    
    return cnt


N = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = [[False for _ in range(N)] for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(input())
village = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == '1':
            village.append(dfs(i, j, N))

print(len(village))
for n in sorted(village):
    print(n)