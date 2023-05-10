N = int(input())
for i in reversed(range(1, N+1, 1)):
    print('{}{}'.format(' ' * (N - i), '*' * i))