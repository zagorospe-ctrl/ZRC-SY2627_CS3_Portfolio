class Magazine:
    def __init__(self, title, author, issue_number):
        self.title = title
        self.author = author
        __issue_number = issue_number

    @property
    def issue_number(self):
        return f"{self.__issue_number:.0f}"

    @issue_number.setter
    def issue_number(self, new_issue_number):
        if new_issue_number > 0:
            self.__issue_number = new_issue_number
        else:
            print("ISSUE NUMBER MUST BE GREATED THAN ZERO")

class Book:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.__number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return f"{self.__number_of_pages:.0f}"

    @number_of_pages.setter
    def number_of_pages(self, new_number_of_pages):
        if new_number_of_pages > 0:
            self.__number_of_pages = new_number_of_pages
        else:
            print("NUMBER OF PAGES MUST BE GREATED THAN ZERO")

class Publication(Book, Magazine):
    def __init__(self, title, author, issue_number, number_of_pages):
        Book.__init__(self, title, author, number_of_pages)
        Magazine.__init__(self, title, author, issue_number)

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Issue Number: {self.issue_number}")
        print(f"Number of Pages: {self.number_of_pages}")
