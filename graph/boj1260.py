def makeGraph(nodeN, edgeN):
    graph = [[False for _ in range(nodeN + 1)] for _ in range(nodeN + 1)]

    for i in range(edgeN):
        i, j = map(int, input().split())
        graph[i][j] = True
        graph[j][i] = True
    
    return graph

def bfs(startNode):
    queue = []
    queue.append(startNode)
    visited[startNode] = True

    while len(queue) != 0:
        curNode = queue.pop(0)
        print(curNode, end= ' ')
        for i in range(len(graph)):
            if graph[curNode][i] == True and visited[i] == False:
                queue.append(i)
                visited[i] = True

def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for i in range(len(graph)):
        if graph[node][i] and not visited[i]:
            dfs(i)


nodeN, edgeN, startNode = map(int, input().split())
graph = makeGraph(nodeN, edgeN)

visited = [False for _ in range(nodeN + 1)]
dfs(startNode)
print()
visited = [False for _ in range(nodeN + 1)]
bfs(startNode)