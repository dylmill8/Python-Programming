def wage():
    # open file and read
    filename = input("What is the filename: ")
    file = open(filename, "r")
    text = file.readlines()
    
    # multiple each person by wage
    for i in range(len(text)):
        person = text[i]
        person = person.split(" ")
        wage = eval(person[1])
        hrs = eval(person[2])
        total = wage * hrs
        print(person[0], total)
wage()
        
