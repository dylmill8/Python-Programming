#Dylan Miller

#this function implements permutation sort and runs a benchmark test to
#calculate the average runtime of t trials at a list length n

from random import *
import time

#randomly shuffles a given list until the list is in sorted order ascending
def permutationSort(List):
    #if the list is one item or less then return the list
    if len(List) <= 1:
        return List
    #loops until the list is in sorted order
    sort = False
    while sort == False:
        #for the length of the list swaps the current index value (i) with
        #a random value at a later index to rnadomly shuffle the list
        for i in range(len(List)):
            j = randint(i,len(List)-1)
            List[i],List[j] = List[j],List[i]
        #assume the list is in sorted order
        sort = True
        #if the current value (k) is greater than the next value in the
        #list then sort is false so we continue the loop
        for k in range(len(List)-1):
            if List[k] > List[k+1]:
                sort = False
    return List

#finds the average runtime of a list length n across t number of trials
def benchmarkSort(n,t):
    total = 0
    #repeats for the number of trials
    for i in range(t):
        List = []
        #generates a random list of length n with integers ranging
        #from -20 to 20
        for i in range(n):
            List = List + [randint(-20,20)]
        #stats the timer
        start = time.time()
        #runs the permutation sort for the random list
        permutationSort(List)
        #stops the timer
        end = time.time()
        #accumulates the total runtime of all trials
        total = total + (end-start)
    #returns the average runtime
    return (total/t)

def main():
    t = 100
    length = 1
    print("List Length (n)\tPermutation Runtime\n")
    for n in range(1,10):
        average = benchmarkSort(n,t)
        print(str(length)+"\t"+str(average))
        length = length + 1
main()
