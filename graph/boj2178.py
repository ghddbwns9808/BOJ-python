def bfs(N, M):
    queue = [[0,0]]

    while len(queue) > 0:
        cur = queue.pop(0)

        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]

            if x in range(N) and y in range(M):
                if graph[x][y] == '1' and not visited[x][y]:
                    visited[x][y] = True
                    minPath[x][y] = minPath[cur[0]][cur[1]] + 1
                    queue.append([x, y])

    return

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())

minPath = [[1 for _ in range(M)] for _ in range(N)]
graph = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(input())

visited[0][0] = True
bfs(N, M)
print(minPath[N-1][M-1])