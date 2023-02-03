N = int(input())

a1 = list(map(int, input().split()))
b1 = list(map(int, input().split()))

def get_extend(arr):
    arr_extend = arr.copy()
    for i in range(N - 1):
        arr_extend.append(arr[i])
    return arr_extend

a_extend = get_extend(a1)
b_extend = get_extend(b1)


def compute_pi(pattern):
    pi = [None] * N
    i = 1
    j = 0
    pi[0] = 0
    while i < N:
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
            i += 1
        else:
            if j != 0:
                j = pi[j - 1]
            else:
                pi[i] = 0
                i += 1
    return pi

def kmp(txt, pat):
    pi = compute_pi(pat)
    i = 0
    j = 0
    while i < 2*N - 1:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            if j == N:
                return 1
        else:
            if j != 0:
                j = pi[j-1]
            else:
                i += 1
    return 0

res = kmp(a_extend, b_extend)
if res > 0:
    print("YES")
else:
    print("NO")
