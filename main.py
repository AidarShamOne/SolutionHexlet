# print('Hello World!')
#
# print('')
# print('')
# print('')
#
# 2.Задание на арифметику
#
# print(3 ** 5)
# print(-8 / -4)
# print(100 % 3)
# print((3 ** 5) + (-8 / -4) + (100 % 3))
#
# 3.Задание ваша программа должна использовать только один print()
#
# print("- Did Joffrey agree?\n- He did. He also said \"I love using \\n\".")
#
# 4. Переменные
#
# euro_count = 100
# euro_per_dollar = euro_count * 1.25
# print(euro_per_dollar)
# dollar_per_rubles = euro_per_dollar * 60
# print(dollar_per_rubles)
#
# 5. магические числа
#
# king = 'King Balon the 6th'
# generation_of_kings = 6
# rooms_in_castle = 17
# print(king + ' has ' + str(generation_of_kings * rooms_in_castle) + 'rooms.')
#
# 6. Две строки
#
# stark = 'Arya'
#
# print(f"Do you want to eat, {stark}? \nYes, I'm hungry, mom.")
#
# 7. Три переменные с фамилиями
#
# one = 'Naharis'
# two = 'Mormont'
# three = 'Sand'
#
# # BEGIN (write your solution here)
# print(f"{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}")
# # END
#
# 8. Срезы
# value = 'Hexlet'
# print(value[2:-1])
#
# 9.Вывод двух строк
# print(str(2) + 'times')
#
# 10. Строковое представление числа
# value = "-42"
# value = abs(int(value))
# print(value)
#
# 11. Две переменные
# company1 = "Apple"
# company2 = "Samsung"
#
# count_length = len(company1 + company2)
# print(count_length)
#
# 12. Программа с использванием функций abs()
# num1 = 10
# num2 = -13
#
# sum_two_numbers = abs(num1 + num2)
# print(sum_two_numbers)
#
# 13. Шестнадцатеричное значение переменной
# number = 10.1234
# print(hex(round(number)))
#
# 14. Вернуть случайное число от 1-10
#
# from random import randint
#
# print(randint(1, 10))
#
# 15. Определить тип передаваемого аргумента
#
# motto = 'Family, Duty, Honor'
# print(type(motto))
#
# 16. Данные, вводимые пользователями с лишними символами
#
# first_name = '  Grigor   \n '
# first_name = first_name.strip()
# print(first_name)
#
# 17. Цепочка методов
#
# text = 'When \t\n you play a \t\n game of thrones you win or you die.'
#
# print(len(text[5:16:].strip()))
#
# 18. Реализуйте функцию print_motto(), которая печатает на экран фразу Winter is coming:
#
# def print_motto():
#     text = 'Winter is coming'
#     print(text)
#
# 19. Определите функцию say_hurray_three_times()
#
# def say_hurray_three_times():
#     cry = 'hurray! hurray! hurray!'
#     return cry
#
# 20. Реализуйте функцию truncate()
#
# def truncate(text, length):
#     truncate_text = text[:length] + '...'
#
#     return truncate_text
#
# 21.Реализуйте функцию get_hidden_card()
#
# def get_hidden_card(credit_card, show_number = 4):
#     hidden_credit_card = '*' * show_number + credit_card[-4:]
#
#     return hidden_credit_card
#
# print(get_hidden_card('1234567812345678', 3))
#
# 22.Реализуйте функцию trim_and_repeat(), которая принимает три параметра


# def trim_and_repeat(text, offset = 1, repetitions = 0):
#
#     cut_str = text[offset:]
#     repeated_str = cut_str * repetitions
#
#     return repeated_str
#
# print(trim_and_repeat('python', offset=4, repetitions=5))
# print(trim_and_repeat('python', offset= 3))
# print(trim_and_repeat('python'))

# 23. Реализуйте функцию letter_multiply().

# def letter_multiply(text: str, character: str, repead: int) -> str:
#     repeat_character: str = text.replace(character, character * repead)
#     return repeat_character
#
# print(letter_multiply('pythton', 'p', 5))

# 24. Напишите функцию get_age_difference()
#
#  def get_age_difference(one_age, two_age):
#      calculating_difference = f"The age difference is {abs(one_age - two_age)}"
#
#      return calculating_difference

# print(get_age_difference(2004, 1992))

# 25.Реализуйте функцию has_upper_case(), которая определяет, содержит ли строка заглавные буквы.
# def has_upper_case(string):
#      check_char = string.lower() != string
#
#      return check_char
#
# print(has_upper_case('pyThon'))
# print(has_upper_case('Python'))
# print(has_upper_case(''))
# print(has_upper_case('python'))

# 26.Реализуйте функцию is_leap_year(), которая определяет, является ли год високосным
# def is_leap_year(year: int)-> int:
#     calculate_year = year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)
#
#     return calculate_year
#
# print(is_leap_year(2020))

# 27.