class Student:
    def __init__(self , fname,lname):
        self.fname = fname
        self.lname = lname
    
    def student(self):
        print(f"Student name is {self.fname} {self.lname}")

    @property
    def email(self):
        self.__email = f"{(self.fname).lower()}.{(self.lname).lower()}@apple.com"
        print(self.__email)

obj = Student('Ashok','Kumar')
obj.student()
# obj.email()
obj.email

