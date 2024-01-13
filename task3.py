"""
Найти сумму и количество чисел в диапазоне от 1 до 2023, которые в своей записи содержат число 3.
"""

count = 0
total = 0

for number in range(1, 2024):
    if '3' in str(number):
        count += 1
        total += number

print("Количество чисел:", count)
print("Сумма чисел:", total)