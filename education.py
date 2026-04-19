import requests


r = requests.get("")
text = r.text

line = text.splitlines()
y = 0
for x in line:
    y += 1
    print(y)
