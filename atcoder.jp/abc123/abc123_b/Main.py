menu = [input() for _ in range(5)]
long = 9
sum = 0
index = 0
for i in range(5):
  if int(menu[i][-1]) != 0 and long > int(menu[i][-1]):
    long = int(menu[i][-1])
    index = i
for i in range(5):
  sum += int(menu[i]) if i == index or int(menu[i][-1]) == 0 else int(menu[i])// 10 * 10 + 10
print(sum)