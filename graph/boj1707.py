import sys
sys.setrecursionlimit(10**6)

def makeGraph(V, E):
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)

    return graph

def dfs(start, visited, graph, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0:
            result = dfs(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:
                return False
            
    return True

N = int(input())

for _ in range(N):
    V, E = map(int, sys.stdin.readline().split())
    graph = makeGraph(V, E)
    visited = [False for _ in range(V+1)]
    
    for i in range(1, V+1):
        if visited[i] == 0:
            result = (dfs(i, visited, graph, 1))
            if not result:
                break
    print("YES") if result else print("NO")