#Define the input function. I only allow integer input
def input_n():
    while True:
        try:
            n = input("What is your positive integer number? ")
            float(n)
        except ValueError:
            print("Please input a number, not words.")
        else:
            if float(n).is_integer() and float(n) > 0:
                number = int(n)
                break
            else:
                print("Please input a positive integer.")
    return number
    

#Count the calculation steps for Collatz Conjecture
def count_step(number):
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number*3 + 1
        count += 1
    return count
    
    
#Asking if the user want to play again
def game_control():
    for i in range(3):
        answer = input("Do you want to calculate again? Answer Yes or No. ")
        if answer[0].lower() == "y":
            return True
        elif answer[0].lower() == "n":
            return False
        else:
            print("Please answer Yes or No.")
    if answer[0].lower() not in ["y", "n"]:
        print("You exceeded the number of answers allowed. The game will end.")
        return False
        
        
#Combine everything together and allow users to choose to play as long as they wish
#Call this function only
def collatz_conjecture():
    while True:
        number = input_n()
        step = count_step(number)
        print(step)
        answer = game_control()
        if answer == False:
            print("Thank you for playing.")
            break
        else:
            continue