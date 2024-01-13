"""
Напишите функцию, которая принимает строку и возвращает новую строку, в которой каждое слово из трех букв заменено на "###"
"""

def replace_words(text):
    # Разбиваем строку на слова
    words = text.split()
    # Проходим по каждому слову
    for i in range(len(words)):
        # Если слово состоит из трех букв, заменяем его на "###"
        if len(words[i]) == 3:
            words[i] = "###"

    # Собираем новую строку из измененных слов
    new_text = " ".join(words)
    # Возвращаем новую строку
    return new_text

# Пример использования функции
text = input("Введите строку: ")
new_text = replace_words(text)
print(new_text)