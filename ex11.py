from random import randint
x = randint (1, 100)
#minimum and maximum values of random numbers
count = 0
guess = 0
#start counting and guessing from 0
def guessing(guess, count):
    """
    Guess a random number.
    The program counts how many times you guessed.
    """
while guess != x:
#we need a while, which stops when you guess
        guess = int(input("Add your winning number!: "))
        count += 1
        #increases the count by one after each guess
        if (guess < x):
            print("The number is higher than your guess. ")
        if (guess > x):
            print("The number is lower than your guess. ")
        if (guess == x):
            print("WE HAVE A WINNER! ")
            print("Your number of guesses is: ", count)
guessing
