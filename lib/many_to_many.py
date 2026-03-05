class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        # Filter the global list of contracts for this author
        return [c for c in Contract.all if c.author == self]

    def books(self):
        # Get unique books from this author's contracts
        return list(set([c.book for c in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        # Helper method to instantiate a new bridge object
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Sum royalties from all contracts related to this author
        return sum([c.royalties for c in self.contracts()])


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        # Filter the global list of contracts for this book
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        # Get unique authors from this book's contracts
        return list(set([c.author for c in self.contracts()]))


class Contract:
    all = []  # Class attribute to track every contract created

    def __init__(self, author, book, date, royalties):
        # Validation Logic
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        # Add the new contract to the tracking list
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date_string):
        # Class method to find specific contracts across the whole system
        return [c for c in cls.all if c.date == date_string]