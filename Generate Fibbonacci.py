def gen_fibb(): #Generate Fibbonacci sequence
    a = 0
    b = 1
    fibb_list = [1]
    while True:
        num = int(input("How many numbers do you want to print? "))
        if num < 0:
            print("Sorry, please enter a number greater than 0.")
        elif num > 30: #Limit the print to maximum 30 numbers only
            print("Sorry, you can't print more than 30 numbers.")
        else:
            for i in range(num-1):
                c = a + b
                a, b = b, c
                fibb_list.extend([c])
            print(fibb_list)
            break