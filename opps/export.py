import os

print(os.listdir("/home/ashok")) 

def my_fun():
    print("functin -> my fun")

def main():
    print("main function")
    
if __name__=="__main__":
    print("call ony in this file")
    main()