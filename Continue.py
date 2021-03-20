for i in range(100):
    if i == 4:
        continue
    print(i)

for i in range(100):
    if i == 4:
        break
    print(i)

i = 1
while True:
    if i == 11:
        break
    print(i)
    i += 2