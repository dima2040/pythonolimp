"""
Напишите программу, находящую количество троек целых чисел a, b, p таких,
что p — простое число, числа удовлетворяют равенству:

√a - √b = √p>

и каждое из чисел a, b и p лежит в промежутке от N до M (то есть N≤a≤M, N≤b≤M, N≤p≤M).

Входные данные:
Вводятся два целых числа N и M (0≤N≤M≤100000)

Выходные данные:
Выведите искомое количество троек чисел a, b, p.

Решение:
1. Считать значения N и M.
2. Создать переменную count и инициализировать ее нулем. Она будет считать количество троек чисел, удовлетворяющих условию.
3. Пройти циклом по всем возможным значениям a от N до M.
4. Внутри первого цикла пройти циклом по всем возможным значениям a от N до M.
5. Внутри второго цикла пройти циклом по всем возможным значениям b от N до M.
6. Внутри третьего цикла проверить выполнение условия √a - √b = √p. Если условие выполняется, увеличить значение count на единицу.
7. Вывести значение count.
"""

from math import sqrt


def is_prime(n: int) -> bool:
    """Проверяем что число простое"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def count_numbers(N: int, M: int) -> int:
    count = 0

    # Составляем коллекцию простых чисел
    primes = set()
    for p in range(N, M+1):
        if is_prime(p):
            primes.add(p)

    for a in range(N, M+1):
        for b in range(N, M+1):
            for p in primes:
                if sqrt(a) - sqrt(b) == sqrt(p):
                    count += 1
    
    return count

N, M = map(int, input("Ввелите числа N и M через пробел, такие что (0≤N≤M≤100000): ").split())
count = count_numbers(N, M)
print("Количество троек чисел:", count)