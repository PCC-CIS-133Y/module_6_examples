class Employee:

     #Attributes\Properties of the Employee Class

     name = ""
     salary = 0
     ssn = ""

     #Methods of the Employee Class     

     def updateSalary(self, pctg):
          if pctg > 0:
               self.salary = self.salary * (1 + pctg)



     def showEmployee(self):
         print("Employee Name is {}, their Salary is ${:.2f} and their SSN is {}".format(self.name, self.salary, self.ssn))



#Class is defined above, now we can use it.......GAJ
myEmp = Employee()
myEmp.name = "Greggy Poo"
myEmp.ssn = "123-45-9878"
myEmp.salary = 100000
myEmp.updateSalary(.10)
myEmp.showEmployee()