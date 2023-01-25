

def partition(A, p, r):
    i = p - 1
    pivot = A[r] 
    for k in range(p, r):
        if A[k] < pivot:
            i += 1
            temp = A[k]
            A[k] = A[i]
            A[i] = temp
    i += 1
    temp = A[i] 
    A[i] = pivot
    A[r] = temp
    return i
      
    

def select(A, p, r, i):
    if p == r:
        return A[p]
    q =  partition(A, p, r)
    k = q - p + 1
    if i < k:
        return select(A, p, q - 1, i)
    elif i == k:
        return A[q]
    else:
        return select(A, q +1, r, i - k)
    
    
A = [1,3,4,56,7,5,2]
print(select(A, 0, len(A) - 1, 7))
    