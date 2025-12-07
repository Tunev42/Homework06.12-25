#                         ________№2_________
import random
counter = []
f = int(input())
number = [[random.randint(0, f)for j in range(2)],
          [random.randint(0, f)for d in range(2)],
          [random.randint(0, f)for g in range(2)],
          [random.randint(0, f)for h in range(2)],
          [random.randint(0, f)for k in range(2)],
          [random.randint(0, f)for _ in range(2)]]
print(number)
for i in range(1):
    counter1 = number[i][0]
    counter11 = number[i][1]
for y in range(2):
    counter2 = number[y][0]
    counter22 = number[y][1]
for t in range(5):
    counter3 = number[t][0]
    counter33 = number[t][1]
for e in range(4):
    counter4 = number[e][0]
    counter44 = number[e][1]
for w in range(5):
    counter5 = number[w][0]
    counter55 = number[w][1]
for q in range(6):
    counter6 = number[q][0]
    counter66 = number[q][1]
if counter1 or counter11 / 2 or 31 or 62 or 92 >= 1:
    counter.append(1)
else:
    counter.append(0)
if counter2 or counter22 / 2 or 31 or 62 or 92 >= 1:
    counter.append(1)
else:
    counter.append(0)
if counter3 or counter33 / 2 or 31 or 62 or 92 >= 1:
    counter.append(1)
else:
    counter.append(0)
if counter4 or counter44 / 2 or 31 or 62 or 92 >= 1:
    counter.append(1)
else:
    counter.append(0)
if counter5 or counter55 / 2 or 31 or 62 or 92 >= 1:
    counter.append(1)
else:
    counter.append(0)
if counter6 or counter66 / 2 or 31 or 62 or 92 >= 1:
    counter.append(1)
else:
    counter.append(0)

result = counter[0] + counter[1] + counter[2] + counter[3] + counter[4] + counter[5]
print(result)