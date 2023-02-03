import sys
input = sys.stdin.readline
k = int(input())
num_of_vertex = pow(2, k + 1) - 1
# i의 자식은 2i +1, 2i + 2
# i의 부모는 i - 1 // 2
# i의 자식쪽 edge는 각각 edges[2*i] edges[2i + 1]
edges = list(map(int, input().split()))
both_side_equal = [False for _ in range(num_of_vertex)]
children_val = [None for _ in range(num_of_vertex)]

for j in range(num_of_vertex - pow(2, k),num_of_vertex):
    both_side_equal[j] = True
    children_val[j] = 0

# 마지막 vertex의 부모부터 시작
i = (num_of_vertex - 2) // 2
while i >= 0:
    leftchild, rightchild = 2* i + 1, 2 * i + 2
    leftedge, rightedge = edges[2*i], edges[2*i +1]
    
    left_val = children_val[leftchild] + leftedge
    right_val =children_val[rightchild] + rightedge
    if left_val != right_val:
        max_val = max(left_val, right_val)
        if left_val < right_val:
            edges[2 * i] += max_val - left_val
        else:
            edges[2*i + 1] += max_val - right_val
    children_val[i] = children_val[leftchild] + edges[2 * i]
    
    
    
    
    i -= 1
    
print(sum(edges))