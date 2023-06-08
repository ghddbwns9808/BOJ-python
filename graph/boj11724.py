def dfs(startNode):
    stack = [startNode]
    visited[startNode] = True

    while len(stack) != 0:
        curNode = stack.pop()
        for i in range(len(graph)):
            if not visited[i] and graph[curNode][i]:
                stack.append(i)
                visited[i] = True

N, M = map(int, input().split())
graph = [[False for _ in range(N+1)] for _ in range(N + 1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    i, j = map(int , input().split())
    graph[i][j] = True
    graph[j][i] = True

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)