N = int(input())
for i in range(1, N+1, 1):
    print('{}{}'.format(' '*(N - i), '*'*(i)))