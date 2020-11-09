#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary, arg3):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        self.arg3 = arg3
    def displayCount(self):
        print("TotalEmployee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

    def printinfo(self, *arg1):
        print("输出: ", arg1)  # "打印任何传入的参数"
        self.ptintaa(*arg1)
        #for var in vartuple:
         #   print(var)

    def ptintaa(self, arg2):
        print("arg2: ", arg2)

    def prinbb(self):
        print("arg3:", self.arg3)
        #self.printinfo(arg3)

def test1(a, b=2, c=None):
    print(a, b, c)
if __name__ == '__main__':
    '''
    "创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
    "创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print("TotalEmployee %d" % Employee.empCount)
    
    arg3 = (1, 2, 3)
    a = Employee("aaa", 2, 3)
    a.printbb()
    '''
    #emp1 = Employee("Zara", 2000, 1000)
    test1(1, 4)