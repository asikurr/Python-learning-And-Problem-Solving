import random
winnig_number = random.randint(1,100)
gussing_time = 1

number = int(input("Enter any number between 1 to 100 : "))
game_over = False

while not game_over:
    if number == winnig_number:
        print(f"Wow You Win...! You enter {gussing_time} time and number {number}")
        game_over = True
    else:
        if number < winnig_number:
            print("Number is too low..!")       
        else:
            print("Number is too High..!")
        gussing_time+=1
        number = int(input("Enter a Number again : "))
           
   
