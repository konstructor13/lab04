import random
n = int(input("Введите кол-во списков: "))

arrList = []
for i in range (1, n+1):
    k = random.randint(1, 10)
    a = [random.randint(1, 20) for a in range(0, k)]
    arrList.append(a)

print(arrList)

for i in range(n):
    count = 0
    max = -1
    for j in range(len(arrList[i])):
        count = arrList[i].count(arrList[i][j])
        if max < count:
            max = count
    print("В списке " + str(i+1) + " находится " + str(max) + " одинаковых элементов.")