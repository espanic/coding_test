
def getLeast(n, mem):
    divide2 = n // 2 if n %2 == 0 else None
    divide3 = n // 3 if n % 3 == 0 else None
    substract1 = n - 1

    a = [divide2, divide3, substract1]
    b = []
    for element in a:
        if element is not None:
            b.append(element)
    
    minVal = mem[b[0]]

    for i in range(1, len(b)):
        if minVal > mem[b[i]]:
            minVal = mem[b[i]]
    return minVal



if __name__ == "__main__":
    x = int(input())
    mem = []
    n = 1
    mem.append(0)
    mem.append(0)
    while n != x:
        n += 1
        mem.append(getLeast(n, mem) + 1)
    print(mem[x])
