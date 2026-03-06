from itertools import count
from re import search
from shlex import join

adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_tom_sawer = adventures_of_tom_sawer.split()
adventures_of_tom_sawer = " ".join(adventures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_repeats = adventures_of_tom_sawer.count("h")
print(f"Буква h зустрічається: {h_repeats} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adventures_of_tom_sawer_split = adventures_of_tom_sawer.split()
words_with_upper_letter_count = 0
for word in adventures_of_tom_sawer_split:
    if word[0].isupper():
        words_with_upper_letter_count += 1
print(f"У тексті {words_with_upper_letter_count} слів починаються з великої літери")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom_word_index = adventures_of_tom_sawer.find("Tom")
second_tom_word_index = adventures_of_tom_sawer.find("Tom", first_tom_word_index + 3)
print(f"Вдруге слово Tom зустрічається на позиції {second_tom_word_index}")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adventures_of_tom_sawer.split(". ")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
print(fourth_sentence + ".")
fourth_sentence_lower = fourth_sentence.lower()


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print('У тексті є рядок який починається с "By the time".')
        break

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
last_sentence_words = len(last_sentence.split())
print(f"У останньому реченні {last_sentence_words} слова.")
