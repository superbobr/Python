from datetime import datetime, date, timedelta

current_data = date(*map(int, input().split('-')))
day = timedelta(days=int(input()))
print(current_data + day)




data = input().split()
launch_time = datetime(*map(int, data[0].split('-')), *map(int, data[1].split(':')))
data2 = list(map(int, (input().split())))
command_time = timedelta(hours=data2[0], minutes=data2[1], seconds=data2[2])

print(launch_time - command_time)




n = int(input())
time_interval = timedelta()
for _ in range(n):
    days, hours, minutes = map(int, input().split())
    time_interval += timedelta(days=days, hours=hours, minutes=minutes)

print(time_interval.days, time_interval.seconds)





