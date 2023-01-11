 #47분 ~ 50분 중단 2분 시작

if __name__ == "__main__":
    n = int(input())
    records = [1]

    for i in range(1, n + 1):
        record = 0
        if i == 1:
            record += 1
        else:
            record += records[i-1] + records[i-2]
        records.append(record)
    print(records[n] % 10007)