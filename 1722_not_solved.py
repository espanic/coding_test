from collections import deque
N = int(input())

factorial_result = [1]

def factorial(n):
    if len(factorial_result) > n:
        return factorial_result[n]
    else:
        res = factorial(n - 1) * n
        factorial_result.append(res)
        return res


def problem1(k):
    num_arr = deque([i+1 for i in range(N)])
    ans = []
    def recursive(k, digit):

        nonlocal ans

        if digit == 0:
            return
        if k < factorial(digit - 1):
            ans.append(num_arr.popleft())
            recursive(k, digit - 1)
        else:
            q, r = divmod(k, factorial(digit - 1))
            if r == 0:
                ans.append(num_arr[q])
                del num_arr[q]
            else:
                # q+1번째를 넣어야 한다. 
                ans.append(num_arr[q])
                del num_arr[q]
            print(ans, r, digit)
            recursive(r, digit - 1)
    recursive(k, N)
    print(ans)
                


    
            
    
    
    
# def problem2(arr):


line2 = list(map(int, input().split()))
k =line2[1]
problem1(k)


# if line2[0] == 1:
#     k = line2[1]
#     problem1(k)
# else:
#     arr = line2[1:]
#     problem2(arr)
    
    
