#Dylan Miller

#This function will calculate the total value of any word(s) given by checking
#where it occurs in the alphabet and adding every letter

#This function will take a given word and add up the value of it letter
#by letter
    #parameters: word - input word/phrase
def wordValue(word):

    #sets the first letter to alpha
    alpha = word[0]
        
    numb = 0
    total = 0

    #interates for every letter in the word/phrase
    for i in range(len(word)):

        #plugs letter into letterValue function to find the value of that
        #letter and then adds to the total
        total = letterValue(alpha) + total

        #increases alpha by 1 and "%len(word)" will make sure that the
        #counter doesn't surpass the total letters in the list
        #since we are adjusting alpha after calculating the total
        alpha = word[(numb+1)%len(word)]

        #tracks the currrent letter we are on
        numb = numb + 1

    #returns the number value of the word/phrase
    return(total)

#This function will take a letter alpha and calculate the value based on the
#position in the alphabet
#parameters: alpha - letter of the word/phrase
def letterValue(alpha):

    #only uppercase alphabet to make the value easier to calculate/not
    #necessary to have lower case if they have the same value anyway
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #this finds the letter's position in the list, since punctuation is not
    #included in the alphabet it will return none and not affect the total
    value = (alphabet.find(alpha))+1
    return(value)

#Gathers the users input and prints out the user's original word along
#with the value
    #parameters: none
def main():
    
    print("This program will determine the numeric value of your name!")
    word = input("Enter your full name: ")

    #This creates 2 variables, the original "word" will be set to the
    #word/phrase in all capitals to make it easier to sort later and wordLower
    #is set to the original message to be printed back at the end
    word,wordLower = str(word.upper()),word

    #prints the original phrase and the total found by the combined functions
    print("The numeric value of",wordLower,"is",wordValue(word))
    
main()
