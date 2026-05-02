from datetime import datetime


data = list(map(int, input().split()))
result = datetime(*data)
print(f'Дата: {result.date()}')
print(f'Время: {result.time()}')