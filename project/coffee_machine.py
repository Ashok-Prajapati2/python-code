MENU= {
    "espress" : {
        "ingrediets" : {
            "water" : 50,
            "milk" : 50,
            "coffee": 8 
        } 
        , 'cost' : 15
    },
    "latte" : {
        "ingrediets" : {
            "water" : 200,
            "milk" : 150,
            "coffee": 25 
        } 
        , 'cost' : 25
    },
    "cappuccino" : {
        "ingrediets" : {
            "water" : 300,
            "milk" : 200,
            "coffee": 24
        } 
        , 'cost' : 35
    },
}

profit = 0.0

resourees = {
            "water" : 500,
            "milk" :  300,
            "coffee": 100,
            
}


def is_resouress_sufficient(drink):
    drink = drink['ingrediets']
    for item in drink:
        if resourees[item] <= drink[item]:
            print(f"{item} is not sufficient")
            return False 
    return True
   
def  payment_succeful(payment):
    if payment >= drink['cost']:
        print(f"your change {payment - drink['cost']}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink):
    
    for item in drink['ingrediets']:
        resourees[item] = resourees[item]-drink['ingrediets'][item]
    print(f"Here is your {choice}. Enjoy!")
    return drink['cost']

is_it = True

while is_it:
    choice = input("what you like (espress ,latte,cappuccino ) : ")
    
    if choice == "off":
        is_it = False
    elif choice == "report":
        print(resourees)
        print(f"profit is ${profit}")
    else:
        drink = MENU[choice]
        
        
        if is_resouress_sufficient(drink):
            
            payment = int(input("Make payment  : "))
            
            if payment_succeful(payment):
               profit += make_coffee(drink)
                
            
