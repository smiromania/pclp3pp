#lab 3.4


tasks = {
    "task1": "New",
    "task2": "Assigned",
    "task3": "Resolved",
    "task4": "Deprecated"
}
class Employee:
    emp_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
        assignedTasks = []
    def display_emp_count(self):
        print(f"Total number of employee(s) is {Employee.emp_count}")
    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    def updateSalary(self, salary):
        self.salary = salary
    def displayEmployee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    def assignTask(self, task):
        self.assignedTasks.append(task)
    def displayAssignedTasks(self):
        print(self.assignedTasks)
    def removeTask(self, task):
        self.assignedTasks.remove(task)
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.assignedTasks = []
    def displayEmployee(self):
        super().displayEmployee()
        print(f"Department: {self.department}")
    def assignTask(self, task):
        super().assignTask(task)
        self.assignedTasks.append(task)
    def removeTask(self, task):
        super().removeTask(task)

        
    
    