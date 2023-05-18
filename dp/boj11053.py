def dp(n):
    for i in range(1, n):
        for j in range(0, i):
            if numbers[j] < numbers[i]:
                cache[i] = max(cache[i], cache[j]+1)
        

N = int(input())
numbers = list(map(int, input().split()))
cache = [1 for _ in range(N)]

if N == 1:
    print(1)
else:
    dp(N)
    print(max(cache))