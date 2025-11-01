# 1-m
a = 0

for i in range(25, 1501):
    if i % 15 == 0 or i % 14 == 0:
        if i % 105 != 0:
            a += 1
print(a)

# 2-m
a = 0

for i in range(1, 2001):
    if i % 6 == 0:
        if i % 2 and i % 9 == 0:
            a += 1
print(a)

# 3-m
a = 0

for i in range(100, 2501):
    if i % 11 == 0 and i % 5 and i % 7 != 0:
        a += 1
print(a)

# 4-m
a = 0

for i in range(1, 1801):
    if i % 20 == 0:
        if i % 4 and i % 10 == 0:
            a += 1
print(a)

# 5-m
a = 0

for i in range(40, 3001):
    if i % 18 == 0 and i % 15 != 0:
        if i % 90 == 0:
            a += 1
print(a)
