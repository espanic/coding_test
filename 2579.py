if __name__ == "__main__":
    step_num = int(input())
    stairs = [int(input()) for _ in range(step_num)]
    score_record = []
    score_maximum = []

    def calculate_score_for_stemp(i):
        if i == 0:
            score_record.append((0, stairs[i]))
        elif i == 1:
            score_record.append((stairs[i], score_record[i-1][1] + stairs[i]))
        else:
            jump_from_2_before_score = max(score_record[i-2]) + stairs[i]
            jump_from_1_before_score = score_record[i - 1][0] + stairs[i]
            score_record.append((jump_from_2_before_score, jump_from_1_before_score))

    for i in range(0, step_num):
        calculate_score_for_stemp(i)

    for i in score_record:
        score_maximum.append(max(i))

    print(score_maximum[step_num - 1])




