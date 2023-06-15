import sys
sys.setrecursionlimit(10**6)

def dfs(cur, queue):
    if visited[cur]:
        cnt = 0
        while len(queue) > 0:
            if queue.pop(0) == cur:
                break
            cnt += 1
        global CNT
        CNT += cnt

    else:
        visited[cur] = True
        next = graph[cur]
        queue.append(cur)
        dfs(next, queue)
    
    return


T = int(input())

for _ in range(T):
    N = int(input())
    CNT = 0
    graph = [-1]
    graph += list(map(int, input().split()))
    visited = [False] * (N + 1)

    for start in range(1, N+1):
        if not visited[start]:
            queue = []
            dfs(start, queue)
    print(CNT)

