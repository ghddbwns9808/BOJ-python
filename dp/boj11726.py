def dp(N):
    for cur in range(2, N+1):
        cache[cur] = (cache[cur-2] + cache[cur-1]) % 10007

N = int(input())
if N == 1:
    print(1)
else:
    cache = [1 for _ in range(N+1)]
    dp(N)
    
    print(cache[N])
