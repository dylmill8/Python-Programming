def fileIO():
    myfile = open("CSCh5_sample.py", "r")
    title = myfile.readline()
    paragraph = myfile.readlines()
    myfile.close()

    print(title)
    for line in paragraph:
        print(line[:-1])
        
    print("(The for loop ran", len(paragraph), "times)")

    saveFile = open("CSCh5_output.py", "w")
    print("The End!", file=saveFile)
    saveFile.close()



fileIO()


