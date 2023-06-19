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

n = int(input())

visited = [False for _ in range(n+1)]
weights = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append([c, w])
    graph[c].append([p, w])

startNode, maxWeight = dfs(1)

visited = [False for _ in range(n+1)]
weights = [0 for _ in range(n+1)]

startNode, maxWeight = dfs(startNode)
print(maxWeight)