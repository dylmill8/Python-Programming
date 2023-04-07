def squareDigits():
    print("Tell me an integer")
    integer = eval(input("I will square and sum the digits: "))
    integer = abs(integer)
    digit = 0
    square = 0
    total = 0
    
    for i in range(len(str(integer))):
        digit = (integer % 10)
        integer = (integer - digit)/10
        square = digit ** 2
        total = square + total
        square = 0
        digit = 0
    print()
    total = int(total)
    print(total)

def test():
    number = eval(input("number: "))
    number = abs(number)
    print(number)
