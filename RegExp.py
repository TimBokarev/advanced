from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("org.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

corrected_contacts_list = []

for item in contacts_list:
    item_str = str(item)
    pattern_phone = re.compile(r'7 \(\d{3,4}\)\s\d*\-\d*\-\d*')
    pattern_mail = re.compile(r'([\d\w\.\-\_]+@[\d\w\.\-\_]+)')
    pattern_org = re.compile(r'учреждение\ («.*»)')
    pattern_name = re.compile(r';([а-яёА-ЯЁ]*\ [а-яёА-ЯЁ]*\ [а-яёА-ЯЁ]*);')

    entree = {}
    formated_name = re.findall(pattern_name, item_str)[0]
    corrected_number = "+" + (re.findall(pattern_phone, item_str))[0].replace(' ', '')
    # print(type(corrected_number))
    fio = formated_name.split(' ')
    entree["lastname"] = fio[0]
    entree["firstname"] = fio[1]
    entree["surname"] = fio[2]
    entree["organization"] = (re.findall(pattern_org, item_str))[0]
    entree["position"] = "руководитель"
    entree["phone"] = corrected_number
    entree["email"] = (re.findall(pattern_mail, item_str))[0]

    corrected_contacts_list.append(entree)


# print(corrected_contacts_list)


with open('phonebook.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    unique_names = []
    for address in corrected_contacts_list:
        fio = address["lastname"] + address["firstname"] + address["surname"]
        print(fio)
        if fio not in unique_names:
            unique_names.append(fio)
            for key, value in address.items():
                writer.writerow([key, value])



# print(unique_names)

# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     datawriter.writerows(corrected_contacts_list)


# Кейс основан на реальных данных из https://www.nalog.ru/opendata/, https://www.minfin.ru/ru/opendata/
#
# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
# объединить все дублирующиеся записи о человеке в одну.
