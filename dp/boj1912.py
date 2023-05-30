def solution(N):
    for i in range(1, N):
        dp[i] = max(numbers[i], dp[i-1] + numbers[i])

N = int(input())
numbers = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = numbers[0]
if N == 1:
    print(dp[0])
else:
    solution(N)
    print(max(dp))