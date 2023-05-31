def solution(N):
    for i in range(4, N+1, 2):
        for j in range(0, i-1, 2):
            dp[i] += 2*dp[j]
        dp[i] += dp[i-2]

N = int(input())
if N % 2 == 1:
    print(0)
else:
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    dp[2] = 3
    solution(N)
    print(dp[N])