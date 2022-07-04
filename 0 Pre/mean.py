i = []
sum = 0
while True:
    num = int(input())
    if num != 0:
        i.append(num)
        sum = sum + num
    else:
        break
average = sum / len(i)
print(average)