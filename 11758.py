import math

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))


INF = float('inf')
def substract(p,q):
    return p[0] - q[0], p[1] - q[1]

p2 = substract(p2, p1)
p3 = substract(p3, p1)



def get_tan(p):
    if p[0] == 0:
        if p[1] >0:
            return INF
        else:
            return -INF
    return p[1] / p[0]

def print_result(p2, p3):
    if a 


if p2[0] > 0 and p2[1] >= 0:
    if p3[0] > 0 and p3[1] >= 0:
        
    






    
