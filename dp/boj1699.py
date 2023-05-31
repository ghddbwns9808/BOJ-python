import sys
import math

def solution(N):
    for i in range(2, N+1):
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], 1 + dp[i -j*j])

N = int(input())
dp = [sys.maxsize for _ in range(N+1)]
dp[0] = 0
dp[1] = 1
if N == 1:
    print(1)
else:
    solution(N)
    print(dp[N])