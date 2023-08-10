from operator import attrgetter
class Author:
    def __init__(self, name):
        self.name = name
    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author is self])


class Book:
    def __init__(self, title):
        self.title = title
    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]


class Contract:
    all =[]
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of the Author Class")
        self._author = value

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("Book must be an instance of the Book Class")
        self._book = value

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if type(value) is not str:
            raise TypeError("Date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self,value):
        if type(value) is not int:
            raise TypeError("Royalties must be a number")
        self._royalties = value
    
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=attrgetter('date'))
