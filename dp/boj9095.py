def dp(target):
    if cache[target] != -1:
        return
    for cur in range(3, target+1):
        if cache[cur] != -1:
            continue
        cache[cur] = cache[cur-3] + cache[cur-2] + cache[cur-1]


tc = int(input())
cache = [-1 for _ in range(12)]
cache[0] = cache[1] = 1
cache[2] = 2

for _ in range(tc):
    N = int(input())
    dp(N)
    print(cache[N])
