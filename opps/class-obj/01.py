#this is class demo

class Demo:
    a= 10
    
    def showvalue(self):
        print("hi , it is test value")
        print(self.a+self.a)
        
    def showvalue1(self,a,b):
        print(a+b) #user define variable
        print(self.a*2) #it point to variable in class


a = Demo()
a.showvalue()
a.showvalue1(12,15)