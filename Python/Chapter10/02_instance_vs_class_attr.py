class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


ravi = Employee()
ravi.language = "JavaScript" # This is an instance attribute
print(ravi.language, ravi.salary)
 