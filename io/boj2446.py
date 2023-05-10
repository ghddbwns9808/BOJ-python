N = int(input())
for i in range(N):
    print('{}{}'.format(' ' * i, '*' * (2*(N - i) - 1)))
for i in reversed(range(N-1)):
    print('{}{}'.format(' ' * i, '*' * (2*(N - i) - 1)))