lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
filtered_elements = [num for num in lst if num < 30 and num % 3 == 0]
print("Элементы меньше 30 и делящиеся на 3 без остатка:", filtered_elements)
