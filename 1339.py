#10분 컷. 

N = int(input())
words = [input() for i in range(N)]

record_dict = {}

for word in words:
    length =len(word)
    for i,c in enumerate(word):
        digit = length - i - 1
        if record_dict.get(c) is None:
            record_dict[c] = pow(10, digit)
        else:
            record_dict[c] += pow(10, digit)
            
arr = list(record_dict.items())
arr.sort(key= lambda x: x[1], reverse=True)

mul = 9
res = 0
for _, n in arr:
    res += mul * n
    mul -=1
print(res)  