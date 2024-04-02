# *args and kwargs 
# or *vars and kwvars 

def my_fun(name,age,roll):
    print(name , age , roll)

my_fun("kumar",22,12345)

def my_fun1(*args):
    if len(args)==3:
        print(args[0] , args[1], args[2])
    else :
        print(args[0] , args[1])


my_fun1("Ashok",20,12345)
my_fun1("Ramesh",30)

lis = ["list",20]
my_fun1(*lis)