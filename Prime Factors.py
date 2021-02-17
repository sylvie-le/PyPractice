import sympy #This package allows you to work with prime numbers

def find_primes():
    prime_list = []
    while True: #You will be asked to input until you input a number
        try:
            num = int(input("We will return prime factors. Input your number here: "))
        except:
            print("You must input a number") #Prevent iputing non-numbers
        else:
            if num > 1000: #Limit the input number to save memory, although not too much
                print("Sorry, you can't enter a number greater than 1000.")
            else:
                for n in sympy.primerange(2, num):
                    if num % n == 0:
                        print(n)
                break