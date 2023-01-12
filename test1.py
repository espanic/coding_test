


def solution(n, lost, reserve):
    students = [0 for _ in range(n)]
    for i in lost:
        students[i - 1] -= 1
    for i in reserve:
        students[i - 1] += 1
        
    for i, student in enumerate(students):
        if student == 1:
            if i > 0 and  students[i - 1] == -1:
                students[i - 1] += 1
                students[i] -=1
            elif i < n- 1 and students[i +1] == -1:
                students[i + 1] += 1
                students[i] -= 1
                
                
    answer = 0
    for i in students:
        if i >= 0:
            answer +=1
    return answer


solution(5, [2,4], [1,3,5])