LOGO = '''

 _______  _______  _        _______           _        _______ _________ _______  _______ 
(  ____ \(  ___  )( \      (  ____ \|\     /|( \      (  ___  )\__   __/(  ___  )(  ____ )
| (    \/| (   ) || (      | (    \/| )   ( || (      | (   ) |   ) (   | (   ) || (    )|
| |      | (___) || |      | |      | |   | || |      | (___) |   | |   | |   | || (____)|
| |      |  ___  || |      | |      | |   | || |      |  ___  |   | |   | |   | ||     __)
| |      | (   ) || |      | |      | |   | || |      | (   ) |   | |   | |   | || (\ (   
| (____/\| )   ( || (____/\| (____/\| (___) || (____/\| )   ( |   | |   | (___) || ) \ \__
(_______/|/     \|(_______/(_______/(_______)(_______/|/     \|   )_(   (_______)|/   \__/
                                                                                          


 '''
 
 
def cal():
    print(LOGO)
    def sum(n1,n2):
        return n1 + n2
    def sub(n1,n2):
        return n1 - n2
    def mul(n1,n2):
        return n1 * n2
    def divide(n1,n2):
        return n1 / n2
    
    operations = {
        "+" : sum,
        "-" : sub,
        "*" : mul,
        "/" : divide
    }
    n1 = float(input("Enter first number: "))
    for subol in operations:
        print(subol)
    should_continue = True
    while should_continue:
        operation = input('Enter operation: ')
        n2 = float(input('Enter next number : '))
        fun_cal = operations[operation]
        answer = fun_cal(n1,n2)
        print(f"{n1} {operation} {n2} = {answer}")
        
        if input(f'continue with {answer}  type = "y" , for new type "n" ') == 'y':
            n1 = answer
        else:
            should_continue = False
            cal()
cal()