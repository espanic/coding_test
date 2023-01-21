N, M = list(map(int, input().split()))

def print_arr(arr):
    for i in range(len(arr) - 1):
        print(arr[i], end = " ")
    print(arr[-1])

def generate(arr):
    if len(arr) ==  M:
        print_arr(arr)
        return
    last_val = arr[-1] if arr else 1
    for i in range(last_val, N + 1):
        arr.append(i)
        generate(arr)
        arr.pop()
        
        
generate([])
        