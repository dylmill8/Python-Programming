def upper():

    try:
        word = input("enter a word: ")
        firstLetter = word[0]

        if firstLetter.upper() == word[0]:
            print("The first letter of",word,"is uppercase!")

        else:
            print("The first letter of",word,"is not uppercase!")

    except:
        print("Dumb, stupid, bad!")

def arcsin():

    try:
        numb = eval(input("Enter a value and I will find the arcsign: "))

        arc = math.asin(numb)

    except NameError:
        print("Thats a letter not a number :(")

    except ValueError:
        print("That is a non-real solution :(")

    except:
        print("You made some other stupid mistake that I can't check for :(")

arcsin()

    
