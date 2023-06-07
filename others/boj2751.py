import sys

N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
for i in sorted(numbers):
    sys.stdout.write(str(i)+'\n')