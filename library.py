__author__ = 'miked'


class Library(object):
    def __init__(self, num_shelves):
        self.shelves = {}
        for i in range(1, num_shelves + 1):
            self.shelves[i] = Shelf()

    def __str__(self):
        lib_string = 'Library Contents:\n'
        for shelf in self.shelves:
            lib_string += 'Shelf %s: %s\n' % (str(shelf),
                                              str(self.shelves[shelf]))
        return lib_string


class Shelf(object):
    def __init__(self, books=[]):
        self.books = books[:]

    def __str__(self):
        if len(self.books) == 0:
            return 'Empty'
        return ', '.join(self.books)


class Book(object):
    def __init__(self, title):
        self.title = title

    def enshelf(self, shelf_num, library):
        print 'Adding %s to Shelf %d' % (self.title, shelf_num)
        try:
            library.shelves[shelf_num].books.append(self.title)
        except KeyError:
            print 'Shelf %d does not exist!\n' % shelf_num
        
    def unshelf(self, shelf_num, library):
        print 'Removing %s from Shelf %d' % (self.title, shelf_num)
        try:
            library.shelves[shelf_num].books.remove(self.title)
        except ValueError:
            print '%s not found on Shelf %d!\n' % (self.title, shelf_num)
        except KeyError:
            print 'Shelf %d does not exist!\n' % shelf_num


# declare arbitrary number of shelves
num_shelves = 3

# initialize library
library = Library(num_shelves)
print 'Created library with %d shelves\n' % num_shelves

# create sample books
book_1 = Book('Jet')
book_2 = Book('War & Peace')
book_3 = Book('A Game of Thrones')
book_4 = Book('1984')
book_5 = Book('Quantum Physics')

# add books to shelves
book_1.enshelf(1, library)
book_2.enshelf(1, library)
book_3.enshelf(2, library)
book_4.enshelf(3, library)

# print library contents, add blank line for clarity
print ''
print library

# add a book to a non-existent shelf
book_5.enshelf(6, library)

# remove some books
book_1.unshelf(1, library)
book_4.unshelf(3, library)

# remove a book from the wrong shelf
book_2.unshelf(2, library)

# remove a book from a non-existent shelf
book_2.unshelf(4, library)

# print final library contents
print ''
print library
