from random import randint
class MyCalculator():

    def __init__(self, _list=[]):
        self.__list = _list


    def average(self):
        count=0
        sum=0

        for item in self.__list:
            sum +=item
            count+=1
        return sum/count

    def min(self):
        min_value = self.__list[0]
        for item in self.__list:
            if min_value>item:
                min_value=item

        return min_value


    def max(self):
        max_value= self.__list[0]
        for item in self.__list:
            if max_value<item:
                max_value=item
        return max_value

    def clear_list(self):
        self.__list.clear()


    def generate(self, number, start_number, to_number):
        new_list = []
        for x in range(number):
            new_list.append(randint(start_number, to_number))
        return new_list

list1 = [2,3,4,5]
c = MyCalculator(list1)
print("Average is ", (c.average()))
print("Minimum value is ", c.min())
print("Maximum value is ", c.max())
print(c.clear_list())
print(c.generate(9, 3, 5))















