#
#
#

a = ["f"]
print(type(a))
print(a[0])

# class Cat:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def __str__(self):
#         return f'''Cat!
#     Name: {self.name}
#     Color: {self.color}'''
#
# murka = Cat('murka', 'black')
#
# print(murka)
#
# murkastr = str(murka)
# with open('cats.txt', 'w') as file:
#     file.write(murkastr)
#
#
# # #
# #
# # import requests
# #
# # URL = 'https://namo-memes.herokuapp.com/'
# #
# #
# # class MemeIterator:
# #     def __init__(self, start, end):
# #         self.start = start
# #         self.end = end
# #         self.current = start - 1
# #         self.session = requests.Session()
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         self.current += 1
# #         if self.current == self.end:
# #             raise StopIteration
# #         return self.get_page(self.current)
# #
# #     def get_page(self, n):
# #         result = self.session.get(f'{URL}memes/page/{n}/10')
# #         return result.json()
# #
# #
# # for item in MemeIterator(1, 10):
# #     print(item)
# #
# #
# #
# # # import wikipedia
# # # ny = wikipedia.page("America")
# # # print(ny.url)
# # #
# # # #
# # # # >>> print wikipedia.summary("Wikipedia")
# # # # # Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...
# # # #
# # # # >>> wikipedia.search("Barack")
# # # # # [u'Barak (given name)', u'Barack Obama', u'Barack (brandy)', u'Presidency of Barack Obama', u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, 2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']
# # #
# # # ny = wikipedia.page("America")
# # # # >>> ny.title
# # # # u'New York'
# # # print(ny.url)
# # # # # u'http://en.wikipedia.org/wiki/New_York'
# # # # >>> ny.content
# # # # # u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
# # # # >>> ny.links[0]
# # # # # u'1790 United States Census'
# # #
# # #
# # # #
