
import sys
input = sys.stdin.readline


string = input()

n =len(string)


def check_prefix_equal_suffix(s):
    length = len(s)
    pi = [0] * length
    j = 0
    res = 0
    for i in range(1, length):
        while(j > 0 and s[i] != s[j]):
            j = pi[j - 1]
        if(s[i] == s[j]):
            j += 1
            pi[i] = j
            res = max(res, j)
    return res


res = 0

for i  in range(0, n):
    substr = string[i:n]
    res = max(res, check_prefix_equal_suffix(substr))

print(res)
    