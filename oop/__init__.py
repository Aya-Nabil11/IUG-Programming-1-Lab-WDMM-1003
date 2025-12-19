class Employee :
    def __init__(self,name,salary,ismarried):
        self.name=name
        self.salary=salary
        self.ismarried=ismarried
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.ismarried)
        print(id(self))
    def display2(self):
        print(self)
    def computeSalary(self):
        self.c="aya"
        if self.ismarried:
            self.salary=(self.salary*2)
        return self.salary

employee=Employee("aya",100,False)
employee.display()
employee.display2()
salary=employee.computeSalary()
print(salary)
employee.a="khalid"
print(id(employee))
print(employee.c)
print(employee.a)