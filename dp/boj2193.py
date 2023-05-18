def dp(N):
    for i in range(4, N+1):
        cache[i][0] = cache[i-1][0] + cache[i-1][1]
        cache[i][1] = cache[i-1][0]

N = int(input())
cache = [[0, 0] for _ in range(91)]
cache[1][1] = cache[2][0] = cache[3][0] = cache[3][1] = 1
dp(N)
print(cache[N][0] + cache[N][1])