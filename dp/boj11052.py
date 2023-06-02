def solution(N):
    for i in range(1, N):
        dp[i] = numbers[i]
        for j in range(0, i):
            dp[i] = max(dp[i], dp[i-j-1] + numbers[j])
    return dp[N-1]

N = int(input())
numbers = list(map(int, input().split()))
dp = [0 for _ in range(N)]

if N == 1:
    print(numbers[0])
else:
    dp[0] = numbers[0]
    print(solution(N))