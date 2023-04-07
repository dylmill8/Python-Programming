#Dylan Miller

#This function will take in multiple scores and tell the user the minimum,
#maximum, and average of the data points

#This function takes in a string and converts it into a list
    #parameters: strList - user's string input
def getScores(strList):

    #converts the string into numbers and then places them into a list
    split = strList.split(",")
    for i in range(len(list(split))):
        split[i] = eval(split[i])
    return(split)

#This will take in a list and find the minimum and maximum and swap them to
#the front and back of the list respectively before summing and calculating
#the average of the data in the function
    #parameters: scoreList - users scores that have been converted to a list
def getStats(scoreList):

    #finds the position of the max and min numbers
    posMax = scoreList.index(max(scoreList))
    posMin = scoreList.index(min(scoreList))

    #sets length to one less than the total because the index counts from 0
    length = len(scoreList)-1

    #Swaps the positions of the minimum and the first position and repeats
    #for the last position and the maximum
    scoreList[0],scoreList[posMin] = scoreList[posMin],scoreList[0]
    scoreList[length],scoreList[posMax] = scoreList[posMax],scoreList[length]

    #sums the list and divides it by the length of the list to get the average
    average = sum(scoreList)/len(list(scoreList))
    return(average)

#Takes the scores the user imputs and prints the min, max, and
#the calculated average
    #parameters: none
def main():
    
    print("This program will calculate some statistics about your list of scores")
    listScores = input("enter all scores (separated by commas): ")

    #prints the min and max using the min() and max() python operators, this can
    #also be done by printing out the first and last positions in the list, both
    #work and I wasn't sure which is preffered so I chose the easiest way
    print("The statistics for these scores are:")
    print("min:",min(getScores(listScores)))
    print("max:",max(getScores(listScores)))

    #prints the returned average from the stats function
    print("average",getStats(getScores(listScores)))
    
main()
