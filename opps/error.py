try:
    file = open("a.txt",'r')
    for each in file:
        print(each)
    
except Exception as e:
    print(e)
    
try:
    open("b.txt")
except Exception as e:
    print(e)