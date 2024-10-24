def print_even_numbers(number):
  print("Четные числа от 0 до", number, ":", end=" ")
  for i in range(0, number + 1, 2):
    print(i, end=" ")
number = int(input("Введите число: "))
print_even_numbers(number)
