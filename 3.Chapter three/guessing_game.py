winning_number = 25
guess_number = input("Enter any guessing number b/w 1 to 80 : ")
guess_number = int(guess_number)

if guess_number == winning_number:
    print("You win !!!")
else:
    if guess_number<winning_number:
        print("You enter too low number !")
    else:
        print("You entered too high number !")