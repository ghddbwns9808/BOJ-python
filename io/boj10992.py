N = int(input())

for i in range(N):
    if i == 0:
        print('{}*'.format(' '*(N - 1)))
    elif i == (N - 1):
        print('*'* (2*N - 1))
    else:
        print('{}*{}*'.format(' '*(N-1-i), ' '*(2*i - 1)))