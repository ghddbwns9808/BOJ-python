def dp(n):
    for i in range(3, n):
        cache[i] = max(cache[i-1], cache[i-2] + wines[i], cache[i-3] + wines[i-1] + wines[i])


N = int(input())
wines = [0]
for i in range(N):
    wines.append(int(input()))
if N == 1:
    print(wines[1])
else:

    cache = [0 for _ in range(N+1)]
    cache[1] = wines[1]
    cache[2] = wines[1] + wines[2]
    dp(N+1)
    print(cache[N])