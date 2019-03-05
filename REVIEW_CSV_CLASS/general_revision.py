class item():

    def __init__(self, description:str, price:float):
        self.__description = description
        self.__price = price
    def get_description(self):
        return self.__description
    def set_description (self, new_description:str):
        self.__description = new_description
        