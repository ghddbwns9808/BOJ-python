def dfs(initial, cur):
    visited[cur] = True
    next = graph[cur]

    if graph[cur] == initial:
        global cnt
        cnt += 1
        return
    else:
        if visited[next]:
            return
        else:
            dfs(initial, next)

T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    graph = [-1]
    graph = graph+list(map(int, input().split()))
    visited = [False for _ in range(N + 1)]

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i, i)

    print(cnt)