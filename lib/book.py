#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count = 0):
        self.title  = title
        self.page_count = page_count
    def get_page_count(self):
        return self._page_count
    def set_page_count(self, pages):
        if(type(pages)==int):
            self._page_count = pages
        else:
            print("page_count must be an integer")
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    page_count = property(get_page_count, set_page_count)






# def get_title(self):
#         return self._title
#     def set_title(self, title):
#         if(isinstance(title,str)):
#             self._title = title
#         else:
#             print("Title must a be a string")