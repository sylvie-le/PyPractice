import math

def print_pi(): #Ask to input a positive integer and round pi up to that
    while True:
        dec_num = int(input("Please place the number of decimals for pi: "))
        if dec_num < 0:
            print("Sorry, you must choose a positive number.")
        elif dec_num > 20:
            print("Sorry, you can't print more than 20 decimal places.")
        else:
            new_pi = round(math.pi, dec_num)
            print(new_pi)
            break