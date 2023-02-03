

def merge_sort(A, cmp):
    temp = [0 for _ in range(len(A))]
    
    def default_cmp(x, y):
        if x < y:
            return 1
        elif x == y:
            return 0
        else:
            return - 1
    
    
    def merge_sort_recursive(A, p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort_recursive(A, p, q)
            merge_sort_recursive(A, q + 1, r)
            merge(A, p, q, r)
            
    def merge(A, p, q, r):
        nonlocal cmp
        i = p
        j = q + 1
        t = p
        while i<= q and j <=r:
            if cmp(A[i], A[j]) >=0:
                temp[t] = A[i]
                i +=1
            else:
                temp[t] = A[j]
                j += 1
            t += 1
            
        while i<=q:
            temp[t] = A[i]
            t += 1
            i += 1
            
        while j <= r:
            temp[t] = A[j]
            t += 1
            j += 1
            
        for i in range(p, r + 1):
            A[i] = temp[i]
    
    if cmp is None:
        cmp = default_cmp
    
    merge_sort_recursive(A, 0, len(A) - 1)
    for i in range(len(A)):
        A[i] = temp[i]

               
        
        
N = int(input())

people = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    people.append([age, i, name])
    
def custom_comparable(p, q):
    if p[0] < q[0]:
        return 1
    elif p[0] > q[0]:
        return -1
    else:
        if p[1] < q[1]:
            return 1
        elif p[1] > q[1]:
            return -1
        else:
            return 0
        
merge_sort(people, cmp=custom_comparable)

for person in people:
    print(f"{person[0]} {person[2]}")


