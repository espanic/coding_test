import sys
import heapq
input = sys.stdin.readline

N = int(input())

bundles = [int(input()) for _ in range(N)]
heapq.heapify(bundles)


if N == 1:
    print(0)
else:
    sums = 0
    
    while len(bundles) > 1:
        a = heapq.heappop(bundles)
        b = heapq.heappop(bundles)
        sums += (a + b)
        heapq.heappush(bundles, a + b)
    print(sums)

    

