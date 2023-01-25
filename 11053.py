import sys
input = sys.stdin.readline
length = int(input())
arr = list(map(int, input().split()))
longest_length = [1]


for i in range(1, length):
    curr = arr[i]
    maxlength = 1
    for j in range(i - 1, -1 ,-1):
        if arr[j] < curr and longest_length[j] + 1 > maxlength:
            maxlength = longest_length[j] + 1
    longest_length.append(maxlength)
    
print(max(longest_length))
