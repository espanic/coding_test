def permutation(iterable, r):
    arr = list(iterable)
    arr = sorted(arr)
    used = [False] * len(arr)
    count = 0
    
    def generate(chosen):
        if len(chosen)  == r:
            print(chosen)
            count += 1
            return
        
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = True
                generate(chosen)
                used[i ] = False
                chosen.pop()
    generate([])
    print(count)
    
    
def combination(iterable, r):
    arr = list(iterable)
    arr = sorted(arr)
    indices = list(range(len(arr)))
    count = 0
    
    def generate(chosen):
        nonlocal count
        if len(chosen) == r:
            for i in chosen:
                print(arr[i], end= " ")
            print("")
            count += 1
            return
        start = chosen[-1] + 1 if chosen else 0
        for i in range(start, len(indices)):
            chosen.append(indices[i])
            generate(chosen)
            chosen.pop()
    generate([])
    print(count)



test_arr = ["A", "B", "C", "D", "E"]
combination(test_arr, 3)                

