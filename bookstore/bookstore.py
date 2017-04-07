class Bookstore(object):
    
    def __init__(self, name):
        self.name = name
        self.books = []
        
# initialize bookstore with name and books which is empty list

# need to show the books in the bookstore
    def get_books(self):
        return self.books
        
# add book to bookstore
    def add_book(self, book):
        self.books.append(book)

#search Bookstore class list of book by Author and/or title
# if they are not in Bookstore add the book by title or author
#first checks to see if there is a title and author, if there isnt.
# add the book by tytle or add the book by author
    def search_books(self, title = None, author = None):
        result = []
        for book in self.books:
            if title != None:
                if title.lower() in book.title.lower():
                    result.append(book)
            elif author != None:
                if author == book.author:
                    result.append(book)
            elif author != None and title != None:
                if author == book.author and title.lower() in book.title.lower():
                    result.append(book)
        return result
            
            

# author needs to have name, nationality. Corresponds to search 
class Author(object):
    
# define author class with name and nationality

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self):
        return self.books
    
# copy functions regarding getting book and adding book but by author alone


class Book(object):
#def Book class with title and author... goes back to bookstore list
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.add_book(self)
# special tie between Author class and Book class is the self.author.add_book in order to add books
