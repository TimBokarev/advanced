from datetime import datetime
from hashlib import md5

path = "/Users/tim/PycharmProjects/advanced/wiki_land_list.txt"


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


@logger_with_path("logs_plus.txt")
def hash_generator(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    index = 0
    end = len(lines)
    while index != end:
        yield lines[index] + " " + str(md5(lines[index].encode()).hexdigest())
        index = index + 1


for items_hash in hash_generator(path):
    print(items_hash)
