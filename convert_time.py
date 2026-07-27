from datetime import datetime
from zoneinfo import ZoneInfo


input_time = list(map(int, input().split()))
string_time_zone = input()

input_time_zone = ZoneInfo(string_time_zone)
point_time = datetime(*input_time, tzinfo=input_time_zone)
london_tz = ZoneInfo('Europe/London')
moscow_tz = ZoneInfo('Europe/Moscow')
tokyo_tz = ZoneInfo('Asia/Tokyo')

print(f'Лондон: {point_time.astimezone(london_tz).strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Москва: {point_time.astimezone(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Токио: {point_time.astimezone(tokyo_tz).strftime("%Y-%m-%d %H:%M:%S")}')






