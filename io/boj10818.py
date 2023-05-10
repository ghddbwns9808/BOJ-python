N = int(input())
numbers = sorted(list(map(int, input().split())))
print(numbers[0], numbers[N - 1])