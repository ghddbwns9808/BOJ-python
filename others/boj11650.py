N = int(input())

dots = [list(map(int, input().split())) for _ in range(N)]
for dot in sorted(dots):
    print(dot[0], dot[1])