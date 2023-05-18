def dp(N):
    for i in range(2, N+1):
        for j in range(10):
            cache[i][j] = sum(cache[i-1][0:j+1]) 

N = int(input())
cache = [[1 for _ in range(10)] for _ in range(N+1)]
dp(N)
print(sum(cache[N])% 10007)