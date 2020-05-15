import requests


r = requests.get("https://stepic.org/media/attachments/course67/3.6.2/603.txt")
text = r.text

line = text.splitlines()
y = 0
for x in line:
    y += 1
    print(y)
