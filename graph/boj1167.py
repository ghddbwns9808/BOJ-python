def dfs(start):
    stack = [start]
    visited[start] = True

    longestV = -1
    maxWeight = -1

    while len(stack) > 0:
        cur = stack.pop()

        if weights[cur] > maxWeight:
            maxWeight = weights[cur]
            longestV = cur

        for v in graph[cur]:
            if not visited[v[0]]:
                visited[v[0]] = True
                weights[v[0]] = weights[cur] + v[1]
                stack.append(v[0])

    return longestV, maxWeight

N = int(input())

graph = [[] for _ in range(N+1)]
weights = [0 for _ in range(N+1)]
visited = [False for _ in range(N + 1)]

for _ in range(1, N + 1):
    edge = list(map(int, input().split()))
    v = edge[0]
    edge = edge[1:len(edge)-1]

    for j in range(int(len(edge)/2)):
        graph[v].append([edge[2*j], edge[2*j + 1]])

startWith, maxWight = dfs(1)
weights = [0 for _ in range(N+1)]
visited = [False for _ in range(N + 1)]
longestV, maxWight = dfs(startWith)
print(maxWight)