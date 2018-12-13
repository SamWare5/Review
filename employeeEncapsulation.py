class Worker:

    def __init__(self, worker_name=""):
        self.__name = worker_name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

class Employee(Worker):

    def __init__(self, initial_salary, initial_name):
        #This class specializes worker
        self.__salary = initial_salary
        super().__init__(initial_name)

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def get_salary(self):
        return self.__salary

e1 = Employee(2000, "sam")
e1.set_salary(77)
print(e1.get_name())
print(e1.get_salary())



