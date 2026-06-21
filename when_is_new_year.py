from datetime import date


input_date = date(*map(int, input().split('-')))
next_year = input_date.year + 1
new_year = date(next_year, 1, 1)
print(f'До Нового года осталось {abs(input_date - new_year).days} дней')