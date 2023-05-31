def solution(N):
    for i in range(6, N+1):
        dp[i] = dp[i-1] + dp[i-5]

T = int(input())

for tc in range(T):
    N = int(input())

    if 1 <= N and N < 4:
        print(1)
    elif 4 <= N and N < 6:
        print(2)
    else:
        dp = [1 for i in range(N+1)]
        dp[4] = dp[5] = 2
        solution(N)
        print(dp[N])