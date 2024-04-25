import math


data = []
for i in range(1, 10**6+1):
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        data.append(i)
        
print(*data)

