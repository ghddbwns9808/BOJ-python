import datetime
weekdays = {0 : "MON", 1 : "TUE", 2 : "WED", 3 : "THU", 4 : "FRI", 5 : "SAT", 6 : "SUN"}
base = datetime.date(2007, 1, 1)
month, day = map(int, input().split())
cur = datetime.date(2007, month, day)

print(weekdays[(cur - base).days % 7])