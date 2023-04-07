#Dylan Miller

#this function tells the fibonacci numbers up to the n value
    #parameters: n = number in fibonacci sequence
    #total = numb of sequence printed
    #numb1 = one of the numbers needded to be added
    #numb2 = the second number needed to be added

def fibonacci(n):
    #sets the total for the value we want to print and the two variables
    #that will keep track of what two numbers we are on
    total = 0
    numb = 0
    numb2 = 1

    #prints 1 to start the sequence if n = 0
    print(1)

    #couldn't get this to work but this would repeatedly increase the values
    #of numb1 and numb2 and add them together to make the number of the
    #sequence we are on
    for i in range (n):
        total = numb + numb2
        numb = total - 1
        numb2 = numb2 + 1

        #makes the sequence appear in a line
        print(total, end = " ")

#tried 3 and 5 for n because gives the repeating digits at the beginning
#of the series and towards the end, however i didn't get the expected outcome
#1,1,2,3,5,8
        
        
