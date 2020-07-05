

class PhoneBook:
    def __init__(self, book_name):
        self.contacts = []
        self.book_name = book_name

    def add_contact(self, contact):
        self.contacts.append(contact)

    def contact_list(self):
        print(f"Список контактов телефонной книги <{self.book_name}>")
        print()
        for person in self.contacts:
            # person.print_entree()
            print(person)
            print()

    def contact_delete(self, phone_number_delete):
        for person in self.contacts:
            if person.phone_number == phone_number_delete:
                print(f"удаляю контакт {person.second_name}")
                self.contacts.remove(person)

    def looking_for_favorites(self):
        print("Избранные номера: ")
        for person in self.contacts:
            if person.favorite:
                print(person.phone_number)

    def search_for_names(self, first_name_entree, second_name_entree):
        for person in self.contacts:
            if person.first_name == first_name_entree and person.second_name == second_name_entree:
                # person.print_entree()
                print(person)


class Contact:
    def __init__(self, first_name, second_name, phone_number, favorite=False, *args, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.favorite = favorite
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if self.favorite:
            fav = "В избранных: да"
        else:
            fav = "В избранных: нет"
        additional_print = ""
        for additional_items in self.kwargs:
            additional_print = additional_print + str(additional_items) + ": " + str(self.kwargs[additional_items]) + "\n"

        return f'''Имя:  {self.first_name}
Фамилия:  {self.second_name}
Телефон:  {self.phone_number}
Дополнительная информация:
{fav}
{additional_print}
    '''

    # def print_entree(self):
    #     print("Имя: " + self.first_name)
    #     print("Фамилия: " + self.second_name)
    #     print("Телефон: " + self.phone_number)
    #     print("Дополнительная информация: ")
    #     if self.favorite:
    #         print("   В избранных: да")
    #     else:
    #         print("   В избранных: нет")
    #     # print(self.args)
    #     for additional_items in self.kwargs:
    #         print("   " + str(additional_items) + " : " + str(self.kwargs[additional_items]))


john = Contact("Вася", "Smith", "5555")
bill = Contact("Боря", "Тамагочи", "4444", True, telegram='@jhony', email='jhony@smith.com')


MyPhoneBook = PhoneBook("Мои контакты")

MyPhoneBook.add_contact(john)
MyPhoneBook.add_contact(bill)

MyPhoneBook.contact_list()

MyPhoneBook.looking_for_favorites()
print()
MyPhoneBook.search_for_names("Боря", "Тамагочи")
print()
MyPhoneBook.contact_delete("4444")
print()
MyPhoneBook.contact_list()
print()