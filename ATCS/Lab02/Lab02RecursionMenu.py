#Dylan Miller

#This program is a menu that runs a variety of recurssion functions

#returns whether or not a word is a palindrome
    #word - given word being checked
def palindrome(word):
    #if the word is only a letter long then returns true
    if len(word) == 0 or len(word) == 1:
        return True
    #if the beginning and end of the word are not the same letter
    #returns false
    if word[0] != word[-1]:
        return False
    #recalls the function after removing the front and back letters
    else:
        word = word[1:-1]
        return palindrome(word)

#this program will convert an integer into its written digit components
    #n - given number
def digitsToWords(n):
    #if there are no more digits returns an empty string
    if n == 0:
        return ""
    #creates a list with all the digits written in words zero through nine
    words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    #takes the remainder after dividing by 10 to get the last
    #digit of the number
    digit = n%10
    #removed the last digit from the original number
    n = n//10
    #recalls the function on the remaining number and adds
    #each digit now written out as a string
    string = words[digit]+" "
    return digitsToWords(n) + string

#returns if within a list of numbers a subset of numbers can sum to a target value
    #nums - list of numbers
    #x - the target value
def sumToTarget(nums,x):
    #if the target is 0, meaning that some combination of numbers has
    #reached the target sum then returns true
    if x == 0:
        return True
    #if the list is empty then returns False
    elif len(nums) == 0:
        return False
    #sums every combination of number be creating a decision tree where
    #a number is either subtracted from the target (counted in the sum)
    #or is it discarded. If the base case is reached by any one of the
    #combinations, then the "or" is satisfied and will return true
    return sumToTarget(nums[1:],x - nums[0]) or sumToTarget(nums[1:],x)

#finds the total possible combinations if k items are chosen from the total n
    #n - total
    #k - amount chosen
def choose(n,k):
    #base cases that return 0 when there are no more remaining possible
    #combinations or 1 if there is exactly one remaining combination
    if n < k:
        return 0
    elif k == 0:
        return 1
    #continues to break down the total and choice by going through n factorial
    #possible total items and k factorial possible chosen items to find
    #every possible combination of n and k
    else:
        return choose(n-1,k-1) + choose(n-1,k)

def test():
    print(palindrome('racecar'))
    print(palindrome('tacocat'))
    print(palindrome('dylmill'))
    print(palindrome('racecars'))
    print(palindrome('noon'))
    print(palindrome('civic'))
    print(digitsToWords(34500000214))
    print(digitsToWords(10))
    print(sumToTarget([1,3,7,10],13))
    print(sumToTarget([1,2,3,4,5],7))
    print(sumToTarget([1,3],2))
    print(choose(10,2))
#test()

#runs a menu to choose which program to run
def main():
    print("Welcome to the Recursion Calculator")
    #repeats until user chooses to stop
    loop = True
    while loop == True:
        #input validation for user's input choice
        choice = 0
        while (choice != 1)and(choice != 2)and(choice != 3)and(choice != 4)and(choice != 9):
                try:
                    print("\nChoose a function:")
                    print("1) palindrome")
                    print("2) digitsToWords")
                    print("3) sumToTarget")
                    print("4) choose")
                    print("9) quit")
                    choice = eval(input("option: "))
                except:
                    print("\nInvalid input")
        if choice == 1:
            try:
                word = str(input("\nEnter a word: "))
            except:
                    print("\nInvalid input")
            #runs the recurssive function of coice and returns the output
            if palindrome(word) == True:
                print(word,"is a palindrome")
            else:
                print(word,"is not a palindrome")
        elif choice == 2:
            try:
                n = int(input("\nEnter a positive integer: "))
            except:
                    print("\nInvalid input")
            print(n,"can be read as",digitsToWords(n)) 
        elif choice == 3:
            try:
                nums = list(eval(input("\nEnter a list of numbers seperated by a comma: ")))
                x = eval(input("Enter a target value: "))
            except:
                    print("\nInvalid input")
            if sumToTarget(nums,x) == True:
                print(nums,"can sum to",x)
            else:
                print(nums,"can not sum to",x)
        elif choice == 4:
            try:
                n = int(input("\nEnter a total: "))
                k = int(input("Enter a number to choose: "))
            except:
                    print("\nInvalid input")
            print(n,"choose",k,"is",choose(n,k))
        elif choice == 9:
            loop = False
main()
