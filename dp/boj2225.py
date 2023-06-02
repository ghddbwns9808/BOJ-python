def solution(N, K):
    for i in range(1, K):
        for j in range(0, N+1):
            for k in range(0, j+1):
                dp[j][i] = (dp[j][i] + dp[k][i-1]) % 1000000000

N, K = map(int, input().split())

dp = [[0 for _ in range(K)] for _ in range(N+1)]
for i in range(0, N+1):
    dp[i][0] = 1
solution(N, K)
print(dp[N][K-1])