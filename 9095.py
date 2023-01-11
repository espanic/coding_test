# 14분 시작 22분 걸림 > 말도 안된다...


def compute_the_number_of_adding(n):
    records = [1]

    for i in range(1, n + 1):

        substactBy1 = i - 1
        substractBy2 = i - 2
        substractBy3 = i - 3

        record = 0

        if substactBy1 >=  0 :
            record += records[substactBy1]
            if substractBy2 >= 0:
                record += records[substractBy2]
                if substractBy3 >= 0:
                    record += records[substractBy3]

        records.append(record)
    return records[n]
        





if __name__ == "__main__":
    test_case_num = int(input())
    test_case_list = [int(input()) for _ in range(test_case_num)]
    for n in test_case_list:
        print(compute_the_number_of_adding(n))



