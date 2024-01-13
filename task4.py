"""
Каролина оказалась в стране кошмаров и ей нужно выбрать пуговички. У Каролины s долларов,
а на выбор представлены n пуговиц с ценами:

i[1], i[2],…,i[n]

Помогите Каролине выбрать самую дорогую пуговицу, которую она может себе позволить или сообщите,
что такой не существует.

Формат входных данных:

В первой строке даны целые числа n, s (1 ≤ n ≤ 2000 ,1 ≤ s ≤ 2000) — количество пуговиц в
магазине и количество долларов у Каролины.
Во второй строке даны n целых чисел a1, a2,…,an (1≤ a[i] ≤10^9, 1≤a[i]≤109) — цены пуговиц в магазине.

Формат выходных данных:

Выведите единственное целое число — цену самой дорогой пуговицы, которую Каролина сможет себе позволить,
если такой нет, выведите 0.

---------------------------------------------------------------------------------------------------

1. Считываем количество пуговиц `n` и количество долларов у Каролины `s`.
2. Считываем цены пуговиц и сохраняем их в список `prices`.
3. Инициализируем переменную `max_price` значением 0.
4. Проходим по каждой цене пуговицы в списке `prices`.
5. Если цена пуговицы меньше или равна количеству долларов у Каролины и больше текущей максимальной цены, обновляем значение `max_price`.
6. Выводим значение `max_price`.
"""

n, s = map(int, input("Введите количество пуговиц и долларов(разделенное пробелами): ").split())
prices = list(map(int, input("Введите цены пуговиц(через пробел): ").split()))

max_price = 0

for price in prices:
    if price <= s and price > max_price:
        max_price = price

print("Цена самой дорогой пуговицы:", max_price)