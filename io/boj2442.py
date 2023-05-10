N = int(input())
for i in range(1, N+1):
    print('{}{}{}'.format('*' * i, ' ' * 2*(N-i), '*' * i))
for i in reversed(range(N)):
    print('{}{}{}'.format('*' * i, ' ' * 2*(N - i), '*' * i))