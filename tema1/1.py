from employee import Employee

class Manager(Employee):

    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"{department}"
        Employee.empCount -= 1 #altfel va creste empCount si pentru obiectele de tip Employee
        Manager.mgr_count += 1


    def display_employee(self):
        if X % 3 == 0:
            print(f"Name: {self.name}")
        elif X % 3 == 1:
            print(f"Salary: {self.salary}")
        elif X % 3 == 2:
            print(f"Department: {self.department}")
    def display_mgr_count(self):
        print(f"Total number of manager(s) is {Manager.mgr_count}")


if __name__ == "__main__":
    X = 6
    Y = 11

    managers = [Manager(f"Manager {i}", 1000 * i, "F22") for i in range(Y // 3)]
    
    for manager in managers:
        manager.display_employee()

    employees = [Employee(f"Employee {i}", 100 * (i+6)) for i in range(5)]
    
    for employee in employees:
        employee.display_employee()
    

    employee.display_emp_count()
    manager.display_mgr_count()