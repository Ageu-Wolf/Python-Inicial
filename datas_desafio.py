from datetime import date,timedelta

dt_1 = date.today()
dt_2 = date(2022, 12, 31)

data_1 = dt_1 + timedelta(days=180)
print(data_1)

print(dt_2 - dt_1)
