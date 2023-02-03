N, K = map(int, input().split())


arr = list(map(int, input().split()))

def find_ith(arr, i):
    
    # 0번째가 첫번째이도록
    i = i -1
    
    def recursive(arr, i, p, r):
        if p == r:
            return arr[p]

        # q는 앞에서 k번째이다. 0번째기준
        q= partition(arr, p, r)
        k = q - p
        if k == i:
            return arr[q]
        elif k > i:
            return recursive(arr, i, p, q - 1)
        else: # k < i
            return recursive(arr, i - k - 1, q + 1, r)
            
    
    def partition(arr, p, r):
        pivot = arr[r]
        j = p - 1
        for i in range(p, r):
            if arr[i]< pivot:
                j += 1
                swap(arr, i, j)
        swap(arr, j + 1, r)
        return j + 1
                
    def swap(A, a, b):
        temp = A[a]
        A[a] = A[b]
        A[b] = temp
        
    return recursive(arr, i, 0, len(arr) - 1)

print(find_ith(arr, K))

