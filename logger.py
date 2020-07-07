
from datetime import datetime


def logger_with_path(path):
    path_to_wright = path
    
    def logger(function_name):
        name_to_indicate = str(function_name)

        def new_function(*args, **kwargs):
            function = function_name(*args, **kwargs)
            time_stamp = datetime.today()
            with open(path_to_wright, 'w') as file:
                file.write("вызов функции в: " + str(time_stamp) + "\n")
                file.write("имя функции: " + str(name_to_indicate) + "\n")
                file.write("аргументы: " + str(args) + str(kwargs) + "\n")
                file.write("результат: " + str(function) + "\n")
            return function
        return new_function
    return logger

# def logger(function_name):
#     name_to_indicate = str(function_name)
#
#     def new_function(*args, **kwargs):
#         function = function_name(*args, **kwargs)
#         time_stamp = datetime.today()
#         with open('logs.txt', 'w') as file:
#             file.write("вызов функции в: " + str(time_stamp) + "\n")
#             file.write("имя функции: " + str(name_to_indicate) + "\n")
#             file.write("аргументы: " + str(args) + str(kwargs) + "\n")
#             file.write("результат: " + str(function) + "\n")
#         return function
#     return new_function


@logger_with_path("logs1.txt")
# @logger
def old_function(x, y):
    z = x + y
    return z


old_function(2, 3)


# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
#
# Написать декоратор из п.1, но с параметром – путь к логам.
#
# Применить написанный логгер к приложению из любого предыдущего д/з.
