class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


ravi = Employee()
# ravi.language = "JavaScript" # This is an instance attribute
ravi.greet()
ravi.getInfo() 
# Employee.getInfo(ravi)
 