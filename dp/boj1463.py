def solution(target):

    for cur in range(2, target+1):
        candidates = []
        if cur%2 == 0:
            candidates.append(cache[cur//2] + 1)
        if cur%3 == 0:
            candidates.append(cache[cur//3] + 1)
        candidates.append(cache[cur - 1] + 1)
        cache[cur] = min(candidates)

N = int(input())
if N == 1:
    print(0)
else:
    cache = [-1 for _ in range(N+1)]
    cache[1] = 0
    solution(N)
    print(cache[N])
