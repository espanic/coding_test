import sys
from math import sqrt
input = sys.stdin.readline

records = [None for _ in range(123456 * 2 + 1)]


# def get_prime_number_count(n):
#     max_boundary = int(sqrt(2 * n))
#     num_list = [True for _ in range(2 * n +1)]
#     for i in range(2, max_boundary + 1):

#         if not num_list[i]:
#             continue
#         for j in range(max(i, n), 2 * n + 1):
#             if i!= j and j % i == 0:
#                 num_list[j] =False


#     res = sum(num_list[n+1:])
#     records[n] = res
#     return res
                
                
    
def is_prime_number(n):
    if records[n] is not None:
        return records[n]
    
    root = int(sqrt(n))
    for i in range(2, root + 1):
        if i != n and n % i == 0:
            records[n] = False
            return False
        
    records[n] = True
    return True
    
                
def get_prime_number_count(n):
    count  = 0
    for i in range(n + 1, 2*n + 1):
        count += is_prime_number(i)
    return count
    
    


while True:
    n = int(input())
    if n == 0:
        sys.exit()
    if n == 1:
        print(1)
    else:

        print(get_prime_number_count(n))

    