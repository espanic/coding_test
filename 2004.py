
n, m = map(int, input().split())
# m = min(n -m , m)

# num_info = []
total_two = 0
total_five = 0

i = 2
while i <= n:
    total_two += n // i
    i = 2 * i

j = 5
while  j<=n:
    total_five += n // j
    j = 5 * j
    
    
i = 2
while i <= m:
    total_two -= m // i
    i = 2 * i

j = 5
while  j<=m:
    total_five -= m // j
    j = 5 * j
    
i = 2
while i <= n-m:
    total_two -= (n-m) // i
    i = 2 * i

j = 5
while  j<= n -m:
    total_five -= (n-m) // j
    j = 5 * j


        
print(min(total_two, total_five))

    