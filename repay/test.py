from datetime import datetime

d = "2020-2-12"
year_s, mon, day = d.split("-")

a = datetime(int(year_s), int(mon), int(day))
print(a)
