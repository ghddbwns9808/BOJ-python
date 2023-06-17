import sys
sys.setrecursionlimit(10**7)

def dfs(parent, cur):
    root[cur] = parent

    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True
            dfs(cur, i)
    return


N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[1] = True
root = [-1 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(-1, 1)

for i in range(2, N+1):
    print(root[i])