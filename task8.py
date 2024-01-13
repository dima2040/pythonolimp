"""
Однажды ковбой нанялся в помощники шерифа.
Шериф выдал ковбою строку s и попросил собрать из её букв как можно больше слов sherriff.
Каждая буква может использоваться не более чем в одном слове.

Формат входных данных:
Дана строка s (1≤ ∣s∣ ≤2⋅10^5) состоящая из маленьких букв латинского алфавита.

Формат выходных данных:
Выведите максимальное количество слов sherriff , которое можно собрать из букв строки s.
"""

from collections import Counter

def count_words(s):
    # Создаем словарь для подсчета количества каждой буквы
    letter_count = Counter(s)
    # Определяем максимальное количество слов "sherriff", которое можно собрать
    max_words = min(letter_count['s'], letter_count['h'], letter_count['e'], letter_count['r'] // 2, letter_count['i'], letter_count['f'] // 2)
    # Возвращаем максимальное количество слов
    return max_words

# Пример использования функции
s = input("Введите строку: ")
# s = "sherriffsherriffsherrifshrriff"
max_words = count_words(s)
print(max_words)
