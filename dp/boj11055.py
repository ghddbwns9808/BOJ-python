def solution(N):
    for i in range(1, N):
        dp[i] = numbers[i]
        for j in range(0, i):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j]+numbers[i])

N = int(input())
numbers = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = numbers[0]

if N == 1:
    print(dp[0])
else:
    solution(N)
    print(max(dp))