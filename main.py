# -*- coding: utf-8 -*-

import datetime as dt
import time as t

import pandas as pd

# Время начала замера
startTime = t.time()

# Праздничные дни РФ
public_holiday = {
    1: [1, 2, 3, 4, 5, 6, 7, 8],
    2: [23],
    3: [8],
    4: [],
    5: [1, 9],
    6: [12],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [4],
    12: []
    }


# Проверка выходного дня
def is_business_day(date):
    days = len(pd.bdate_range(date, date))
    return bool(days)


# Проверка праздничного дня
def check_holiday(month_x, days_x):
    holiday_x = None
    if not month_x:
        return False
    else:
        for i in month_x:
            if i == days_x:
                return True
            else:
                holiday_x = False
    return bool(holiday_x)


# Проверка дня
def check_day(date_x):
    if is_business_day(date_x) is False:
        print("Выходной день")
    else:
        months = pd.Series(public_holiday)
        holiday_month = months[date_x.month]
        if check_holiday(holiday_month, date_x.day) is not False:
            print("Праздничный день")
        else:
            print("Рабочий день")


# Проверка времени
def check_time(date_x):
    if date_x.hour >= 23 and date_x.minute >= 0:
        print("Ночное время")
    else:
        if date_x.hour >= 18 and date_x.minute >= 0:
            print("Вечернее время")
        else:
            if date_x.hour >= 9 and date_x.minute >= 0:
                print("Дневное время")
            else:
                print("Не рабочее время")
    # return


# *******************************************************************

# Проверяемая дата
# date_x = dt.datetime.now()

date_d = dt.datetime.now() + dt.timedelta(days=626)

date_t = dt.datetime.strptime("0:10:03", "%H:%M:%S")

# *******************************************************************

# Pause 0.1 seconds
t.sleep(0.1)

# время конца замера
endTime = t.time()

# *******************************************************************

print("Год:", date_d.year, "\nМесяц:", date_d.month, "\nДень:", date_d.day)
check_day(date_d)
print("Время:", date_t.strftime("%H:%M:%S"))
check_time(date_t)

# *******************************************************************

# Вычисляем затраченное время
totalTime = endTime - startTime
tt = str(dt.timedelta(seconds=float(totalTime)))

print("Затраченное время:", tt, "сек.")
# *******************************************************************
