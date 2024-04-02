try:
    file = open('a.xt','r')
except EOFError as e:
    print(e , "EOEERROR")
except IOError as e:
    print(e, "IOERROR")

finally:
    print("run finally ")