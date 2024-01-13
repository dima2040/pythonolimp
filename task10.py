"""
Необходимо написать функцию, которая принимает 2 параметра: число и систему счисления,
в которую это число будет переведено, в результате функция должна вернуть число в новой системе счисления.

Входные данные:
2, 10

Выходные данные:
1010
"""

def convert_number(number, base):
    # Проверяем, что число и система счисления являются положительными целыми числами
    if not isinstance(number, int) or not isinstance(base, int) or number < 0 or base < 0:
        return "Ошибка: входные данные должны быть положительными целыми числами"
    
    # Проверяем, что система счисления находится в диапазоне от 2 до 36
    if base < 2 or base > 36:
        return "Ошибка: система счисления должна быть в диапазоне от 2 до 36"
    
    converted_number = ""
    while number > 0:
        remainder = number % base
        converted_number = str(remainder) + converted_number
        number = number // base
    
    return converted_number

base, number = map(int, input("Введите систему счисления и число(например 2 10): ").split())
result = convert_number(number, base)
print(result)
