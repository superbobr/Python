from string import Template

template_str = input()
user_name = input()
order_id = input()

t = Template(template_str)
print(t.substitute(user=user_name, order_id=order_id))