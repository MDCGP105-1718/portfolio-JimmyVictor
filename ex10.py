x=0
y=0
def Fizzbuzz(x,y):
    """
    Input: x, a positive int from 1 to 100
    Returns Fizz, Buzz, FizzBuzz or a value
    """
    x = int(input("Minimum value: "))
    y = int(input("Maximum value: "))
    for a in range(x,y+1):
        if (a % 3 == 0) and (a % 5 == 0):
            print("FizzBuzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a)
Fizzbuzz(x,y)
