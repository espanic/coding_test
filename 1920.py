import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
check_list = list(map(int, input().split()))



def check(i, s_ind, e_ind):

    mid = (s_ind + e_ind) // 2
    if i == A[mid]:
        return 1
    
    if s_ind > e_ind:
        return 0
    
    if i < A[mid]:
        return check(i, s_ind, mid - 1)
    else:
        return check(i, mid + 1, e_ind)


for i in check_list:
    print(check(i, 0, len(A) - 1))