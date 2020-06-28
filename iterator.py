

import json
import wikipedia


def file_reader(file_name):

    with open(file_name) as f:
        file_content = f.read()
        content = json.loads(file_content)
        land_list = []
        for land_entree in content:
            land = land_entree["name"]["common"]
            land_list.append(land)

    return land_list


class WikiList:
    def __init__(self, working_list):
        self.working_list = working_list
        self.index = -1
        self.end = len(working_list) - 245
        self.element = ""

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.element = self.working_list[self.index]
        if self.index == self.end:
            raise StopIteration
        return self.wiki_find(self.index)

    def wiki_find(self, index):
        try:
            page = wikipedia.page(self.working_list[self.index])
            link = page.url
            lands_with_url = self.working_list[self.index] + " " + link
        except:
            lands_with_url = self.working_list[self.index] + " ссылку в Википедиа не нашли"

        return lands_with_url


lands = WikiList(file_reader("countries.json"))

with open("wiki_land_list.txt", "w") as wiki_land_list:
    for line in lands:
        wiki_land_list.write(line + "\n")


#
# for i in lands:
#     print(i)


# Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.
#
# Написать генератор, который принимает путь к файлу.
# При каждой итерации возвращает md5 хеш каждой строки файла.