# 8분 시작 35분 종료 -> 27분 걸림

from enum import Enum

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


if __name__ == "__main__":
    n = int(input())
    cost_for_houses=[list(map(int,input().split())) for _ in range(n)]

    records_paint = []
    records_paint.append({Color.RED : cost_for_houses[0][0] , Color.GREEN : cost_for_houses[0][1] ,Color.BLUE : cost_for_houses[0][2]})

    for i in range(1, n ):
        cost = cost_for_houses[i]
        prev_paint_record = records_paint[i - 1]
        record_paint = {Color.RED : None, Color.GREEN : None , Color.BLUE : None}

        for color in Color:
            if prev_paint_record[color] is None:
                continue
            available_color_list = [c for c in  Color if c != color]
            for available_color in available_color_list:
                v = cost[available_color.value] + prev_paint_record[color]
                if record_paint[available_color] is None or  record_paint[available_color] > v:
                    record_paint[available_color] = v
        records_paint.append(record_paint)

    final_record = records_paint[n-1].values()
    final_record = [i for i in final_record if i is not None]
    print(min(final_record))
        
    