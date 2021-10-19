"""1041"""

max_value = 0
NoZero = True
counts = []
while NoZero:
    a = int(input("Введите число"))

    if a != 0:
        counts.append(a)
    else:
        NoZero = False

for i in counts:
    if i % 3 == 0 and i > max_value:
        max_value = i
print(max_value)


"""1040"""

result = 0
counts = []
len_input = int(input("Введите колличество чисел: "))

for i in range(len_input):
    counts.append(int(input("Введите число: ")))

for count in counts:
    if count % 6 == 0 and count % 10 == 4:
        result += 1

print(result)
