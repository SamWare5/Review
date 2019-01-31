import datetime
class Worker():

    def __init__(self, id:int, first_name: str, last_name: str, hire_date=datetime):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.hire_date = hire_date

    def set_first_name(self, first_name):
        self.__first_name=first_name

    def set_last_name(self, last_name):
        self.__last_name=last_name

    def set_get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def set_get_last_name(self):
        return self.__last_name

class Employee(Worker):

    def __init__(self, id:int, first_name:str, last_name:str, hire_date=datetime, salary=float):
        self.__salary = salary
        super().__init__(id, first_name, last_name, hire_date)

    def set_salary(self, salary):
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def get_hourly_salary(self):
        return self.__salary/261/8

class Contractor(Worker):

    def __init__(self, id:int, first_name:str, last_name:str, hire_date=datetime, hourly_salary=float):
        self.__hourly_salary = hourly_salary
        super().__init__(id, first_name, last_name, hire_date)

    def set_hourly_salary(self, hourly_salary):
        self.__hourly_salary=hourly_salary

    def get_hourly_salary(self):
        return self.__hourly_salary

class Task():
    def __init__(self, id: int, name: str, description:str, assignedTo:Worker, duration_hours:float):
        self.__id=id
        self.__name=name
        self.description=description
        self.assignedTo=assignedTo
        self.duration_hours=duration_hours
        self.hours_completed=0.0


    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_assignedTo(self, assignedTo:Worker):
        self.__assignedTo=assignedTo


    def set_duration_hours(self, duration_hours):
        self.__duration_hours = duration_hours

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_assignedTo(self):
        return self.__assignedTo

    def get_duration_hours(self):
        return self.__duration_hours

    def get_hours_completed(self):
        return self.__hours_completed

    def add_time(self, num_hours:float):
        self.__hours_completed += num_hours

class Project():
    def __init__(self, id: int, name: str, hours_estimated: int):
        self.__id=id
        self.__name=name
        self.__hours_estimated=hours_estimated

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_hours_estimated(self, hours_estimated):
        self.__hours_estimated = hours_estimated

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_hours_estimated(self):
        return self.__hours_estimated

    def add_task(self, task:Task):
        self.__tasks.append(task)

emp=Employee(1, "Sami", 'Bassata', None, 80000)
print(emp.get_salary())
print(emp.get_hourly_salary())
print(emp.get_first_name())
print(emp.set_get_last_name())
print(emp.set_get_id())

















