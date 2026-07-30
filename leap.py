import calendar


def find_leap_year(start_year, end_year):
    for i in range(start_year, end_year + 1):
        if calendar.isleap(i):
            print(i)