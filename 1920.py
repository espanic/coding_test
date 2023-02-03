from itertools import combinations

L, C = map(int, input().split())

alphabets = input().split()
alphabets.sort()

moum = ('a', 'e', 'i', 'o', 'u')

def check_moum(arr):
    count = 0
    for i in arr:
        if i in moum:
            count += 1
    return count
    


for col in combinations(alphabets,  L):
    moum_count = check_moum(col)
    jaum_count = L - moum_count
    if moum_count > 0 and jaum_count > 1:
        s = "".join(col)
        print(s)