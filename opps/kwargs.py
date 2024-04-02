dis = {
    "a": 50,
    "b": 70,
    "c": 80,
    "d": 90
}

lis = [1,2,3,4,5]

def fun(**kwargs):
    for i, j in kwargs.items():
        print(f"key: {i} , value: {j}")



def master(normal , *a , **b):
    print(normal)

    for i in a:
        print(i)
    
    for i, j in b.items():
        print(f"key: {i} , value: {j}")

if __name__=="__main__":
    fun(**dis)
    master("normal arg " , *lis , **dis)
