num1 = list(map(int, input("Enter the numbers ").split()))
num2 = list(map(int, input("Enter the numbers ").split()))
num3 = []
i = 0
if len(num1) <= len(num2):
    for j in range(len(num1)):
        num3.append(num1[i])
        num3.append(num2[i])
        i+=1
    for j in range (len(num2) - len(num1)):
        num3.append(num2[i])
        i+=1
elif len(num1) > len(num2):
    for j in range(len(num2)):
        num3.append(num1[i])
        num3.append(num2[i])
        i+=1
    for j in range (len(num1) - len(num2)):
        num3.append(num1[i])
        i+=1
print(num3)