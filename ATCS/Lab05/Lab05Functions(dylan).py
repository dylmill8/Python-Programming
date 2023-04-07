#Dylan Miller

#This program compares my own Hash fucntion
#that uses unicode values with the built in python Hash function

#creates a Hash value for a string using the sum of its unicode values
#divided by a given number of buckets
def Hash(key,bucket):
    wordValue = 0
    #for the length of the word, accumulates the sum of its unicode letter values
    for i in range(len(key)):
        wordValue = wordValue + ord(key[i])
    #mods the sum by the number of buckets to return the hash value
    return wordValue%bucket

#returns all names of students that share the same hash
#value as the input name
def CSUSName(data,name,bucket):
    #sets the target value equal to the hash of the input name
    target = Hash(name,bucket)
    listNames = []
    #for every data point in the csus dataset
    for i in range(1,len(data)):
        #if the hash value is equal to the target then
        #add the person's name to the list
        if Hash(data[i],bucket) == target:
            listNames = listNames + [data[i]]
    return listNames

#returns the number of collisions at a given bucket value
def Collisions(data,bucket):
    count = 0
    hashValues = []

    ###creates a list with 100 indices where the index is the hash
    ###value and the item is the number of keys with that hash
    ###hashCount = []
    ###for i in range(100):
        ###hashCount = hashCount + [0]

    for i in range(1,len(data)):
        currentHash = Hash(data[i],bucket)

        ###hashCount[currentHash] += 1

        #if the hash of the current datapoint is already in the list
        #then count one collision
        if currentHash in hashValues:
            count += 1
        #otherwise add the new unique hash to the list
        else: hashValues = hashValues + [currentHash]
        
    ###prints the number of keys at each hash in the list
    ###for i in range(len(hashCount)):
        ###print(str(i)+"\t"+str(hashCount[i]))
    
    return count

#uses the python hash functuon to find the names with the same hash
#as the input name
def CSUSNamePythonHash(data,name,bucket):
    target = hash(name)%bucket
    listNames = []
    for i in range(1,len(data)):
        if hash(data[i])%bucket == target:
            listNames = listNames + [data[i]]
    return listNames

#uses the python hash function to find the number of collisions
#at a given bucket value
def CollisionsPython(data,bucket):
    count = 0
    hashValues = []

    #hashCount = []
    #for i in range(100):
        #hashCount = hashCount + [0]
    
    for i in range(1,len(data)):
        currentHash = hash(data[i])%bucket

        #hashCount[currentHash] += 1
        
        if currentHash in hashValues:
            count += 1
        else: hashValues = hashValues + [currentHash]

    #for i in range(len(hashCount)):
        #print(str(i)+"\t"+str(hashCount[i]))
    
    return count
        

def main():
    print(Hash('Dylan Miller',100))

    #cleans the dataset to contain only the 'Firstname Lastname'
    data = open("Lab05Data.tsv","r")
    data = data.readlines()
    for i in range(1,len(data)):
        data[i] = data[i].replace(",","")
        line = data[i].split("\t")
        data[i] = line[0]
        line = data[i].split(" ")
        data[i] = line[1] +" "+ line[0]
    
    print(CSUSName(data,"Dylan Miller",100))

    print(Collisions(data,100))

    print(CSUSNamePythonHash(data,"Dylan Miller",100))

    print(CollisionsPython(data,100000))
main()
