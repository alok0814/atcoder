import re
A,B = map(str, input().split())
s = input()
reg = r"^[0-9]{"+A+"}\-[0-9]{"+B+"}$"
search = re.search(reg, s)
if search:print("Yes")
else:print("No")