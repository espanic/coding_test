import heapq
import sys

readline = sys.stdin.readline
N = int(readline())
inputs = [int(readline()) for  _ in range(N)]

heap = []

for value in inputs:
    if value == 0:
        try:
            out = heapq.heappop(heap)
        except:
            out  = 0
        finally:
            print(out)
    else:
        heapq.heappush(heap, value)
            


