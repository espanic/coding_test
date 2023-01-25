import sys
input  = sys.stdin.readline
N = int(input())
def solve(str):
    count = 0
    result  = 0
    for c in str:
        if c == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)


for _ in range(N):
    i = input()
    solve(i)