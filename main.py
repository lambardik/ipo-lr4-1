number = int(input("Введите число: "))
print("Четные числа от 0 до", number, ":", end=" ")
for i in range(0, number + 1, 2):
  print(i, end=" ")
