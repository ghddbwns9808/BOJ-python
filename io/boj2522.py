N = int(input())
for i in range(1, N+1):
    print('{}{}'.format(' ' * (N - i), '*' * i))
for i in range(1 ,N):
    print('{}{}'.format(' ' * i, '*' * (N - i)))