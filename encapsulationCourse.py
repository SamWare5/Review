class Book:
    isdn = 0
    def __init__(self, input_isdn):
        self.__isdn = input_isdn

    def set__isdn(self, set_to_isdn):
        self.__isdn = set_to_isdn

    def get__isdn(self):
        return self.__isdn


new_book = Book(15666)

print(new_book.isdn)


