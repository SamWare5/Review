import datetime


class Worker():

    auto_id = 0

    def __init__(self, first_name: str, last_name: str, hire_date=datetime):
        self.__id = Worker.auto_id + 1
        Worker.auto_id = self.__id
        self.__first_name = first_name
        self.__last_name = last_name
        self.hire_date = hire_date

    def set_first_name(self, first_name):
        self.__first_name=first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def set_get_last_name(self):
        return self.__last_name


class Employee(Worker):

    def __init__(self, first_name: str, last_name: str, hire_date=datetime, salary=float):
        self.__salary = salary
        super().__init__(first_name, last_name, hire_date)

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_hourly_salary(self):
        return self.__salary/261/8


class Contractor(Worker):

    def __init__(self, first_name: str, last_name: str, hire_date=datetime, hourly_salary=float):
        self.__hourly_salary = hourly_salary
        super().__init__(first_name, last_name, hire_date)

    def set_hourly_salary(self, hourly_salary):
        self.__hourly_salary = hourly_salary

    def get_hourly_salary(self):
        return self.__hourly_salary


class Task():
    def __init__(self, id: int, name: str, description:str, assignedTo:Worker, duration_hours:float):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__assignedTo = assignedTo
        self.__duration_hours = duration_hours
        self.__hours_completed = 0.0

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
    def __init__(self, id: int, name: str, hours_estimated: float):
        self.__id=id
        self.__name=name
        self.__hours_estimated=hours_estimated
        self.__tasks = []

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

    def add_task(self, task: Task):
        self.__tasks.append(task)

    def get_project_cost(self):
        total_cost = 0
        for task in self.__tasks:
            total_cost+=task.get_duration_hours()*task.get_assignedTo().get_hourly_salary()
        return total_cost

    def get_project_hours_completed(self):
        for task in self.__tasks:
            total_hours += task.get_hours_completed()
            return total_hours

    def get_project_elapsed_cost(self):
        total_elapsed_cost = 0.00
        for task in self.__tasks:
            total_elapsed_cost += task.get_hours_completed() * task.get_assignedTo().get_hourly_salary()
        return total_elapsed_cost


emp = Employee("Sami", 'Bassata', None, 80000)

contr = Contractor("Sami", "Bassata", None, 78)


task1 = Task(1, "Cook Breakfast", "Cook a great Breakfast", emp, 10 )
task2 = Task(2, "Make lunch", "Lunch is important", contr, 10)
task1.add_time(8)
task2.add_time(9)

proj1 = Project(1, "Project #1", 38)

proj1.add_task(task1)
proj1.add_task(task2)

print("The total estimated cost for project :" + proj1.get_name() + "is " + str(proj1.get_project_cost()))
print("The final cost for Project " + proj1.get_name() + "is " + '${:,.2f}'.format((proj1.get_project_elapsed_cost())))

print(emp.get_salary())
print(emp.get_hourly_salary())
print(emp.get_first_name())
print(emp.set_get_last_name())
print(emp.set_get_id())

















