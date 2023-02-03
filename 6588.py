import sys
from math import sqrt
input = sys.stdin.readline
MAX = 1000000
records = [True for _ in range(MAX+ 1)]
records[0] = False
records[1] = False
already_calculated = 1

def getPrimeNumber(n):
    global already_calculated

    if already_calculated > n:
        return 
    
    for i in range(already_calculated + 1, n + 1):
        if records[i]:
            j =2
            while i * j <= MAX:
                records[i*j] = False
                j += 1
    already_calculated = n
        



def goldbach(n):
    getPrimeNumber(n)
    i = 1
    while i <= n // 2:
        # if i in primes and n - i in primes:
        if records[i] and records[n - i]:
            return f"{n} = {i} + {n-i}"
        i += 1
    return  "Goldbach's conjecture is wrong."

while True:
    n = int(input())
    if n == 0:
        break
    print(goldbach(n))
    

