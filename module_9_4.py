from random import choice
""" Задание 1"""

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda  f, s : f == s, first, second)))

"""Задание 2"""
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "a", encoding="utf-8") as file:
            for data in data_set:
                file.write(f"{data}\n")
    return write_everything



write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"""Задание 3"""

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):

        return choice(self.words)




first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())