x, y = map(int, input().split())

montly_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = ['MON', 'TUE', "WED", "THU", "FRI" , "SAT", "SUN"]
day_int = 0
for i in range(x - 1):
    day_int += montly_day_list[i]

day_int += y - 1

res = day_int % 7
print(weekday[res])

