#Dylan Miller

#This program can encode and decode messages with the caesar cipher using
#the message and key provided in an input file

def caesar():

    #opens the input file and sets the first line to the message and the second
    #line to the number/key of the cipher
    inputFile = open("input.py","r")
    text = inputFile.readline()
    text = text[:-1]
    numb = int(inputFile.readline())
    inputFile.close()

    #defines a variable that holds a string of the alphabet (upper and lowercase)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    #opens a new or existing file in the folder called output to write the
    #encoded/decoded message in
    output = open("output.py","w")

    #loops for every character in the message
    for i in range(len(text)):

        #if the text is in the alphabet then shift the letter by the key
        if text[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            letter = text[i]
            index = alphabet.find(letter)
            index = (index + numb) % 52
            print(alphabet[index],end="", file = output)

        #if the character is not a letter then just print it as normal
        #(punctuation,numbers,etc.)
        else:
            print(text[i],end="", file = output)

    #print the key to undo the changes made by flippe the sign
    print("\n",-1*numb, file = output)

    #close the output file to stop the writing
    output.close()

#automatically starts the program when the file is run
caesar()
        
