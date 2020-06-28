
from hashlib import md5
path = "/Users/tim/PycharmProjects/advanced/wiki_land_list.txt"


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

# Написать генератор, который принимает путь к файлу.
# При каждой итерации возвращает md5 хеш каждой строки файла.
