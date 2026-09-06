import random



attemp = 0

Comp = random.randrange(0,100,1)
def ch():
    global attemp
    global Comp
    Your_num = input("Choise number (0-100):")
    
    if float(Your_num) > Comp:
        attemp += 1
        print("Your num is beigger than My...!!")
    if float(Your_num) < Comp:
        attemp += 1
        print("yOUR num is smaller than My...)")
        
    if float(Your_num) == Comp:
        print("Your win!")
        print("Your tried times:",attemp)
        print("Lets try again - Chouse a number between 0 and 100?")
        Comp = random.randrange(0,100,1)
        attemp = 0
        return
while True:

    ch()
    
    
