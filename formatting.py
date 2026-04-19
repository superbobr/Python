from string import Template
import datetime

template_str = input()
user_name = input()
order_id = input()

t = Template(template_str)
print(t.substitute(user=user_name, order_id=order_id))


event_time = datetime.datetime(2025, 10, 26, 10, 30, 0)

print(f'Дата: {event_time:%d.%m.%Y}')
print(f'Время события: {event_time:%H:%M:%S}')