import random
counts = []
counts0 = []
f = int(input())
number = [[random.randint(0, f)for j in range(2)],[random.randint(0, f)for d in range(2)], [random.randint(0, f)for g in range(2)], [random.randint(0, f)for h in range(2)], [random.randint(0, f)for k in range(2)], [random.randint(0, f)for _ in range(2)]]
print(number)
for i in range(1):
    cou = number[i][0] * number[i][1]
for _ in range(2):
    cou1 = number[_][0] * number[_][1]
for h in range(3):
    cou2 = number[h][0] * number[h][1]
for g in range(4):
    cou3 = number[g][0] * number[g][1]
for k in range(5):
    cou4 = number[k][0] * number[k][1]
for l in range(6):
    cou5 = number[l][0] * number[l][1]
if cou / 26 <= 1:
    counts.append(1)
else:
    counts0.append(0)
if cou1 / 26 >= 1:
    counts.append(1)
else:
    counts0.append(0)
if cou2 / 26 >= 1:
    counts.append(1)
else:
    counts0.append(0)
if cou3 / 26 >= 1:
    counts.append(1)
else:
    counts0.append(0)
if cou4 / 26 >= 1:
    counts.append(1)
else:
    counts0.append(0)
if cou5 / 26 >= 1:
    counts.append(1)
else:
    counts0.append(0)
result = counts[0] + counts[1] + counts[2]
print(f"Сколько числе деляться на 26: {result}")
print(f"Сколько чисел не деляться на 26: {counts0}")
