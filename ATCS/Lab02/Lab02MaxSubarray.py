#Dylan Miller

#This program finds the subarray that sums to the highest value within a larger
#input array. It can also use both iterative and recursive methods and
#compare the runtime for each

import math, random, time

# Input a list (L) and the low (inclusive) and high (not inclusive) indices for the 
# array that you want to find the maximum subarray
# Output will be the left and right indices of the max subarray and the sum
def maxSubarray(L,low,high):
    # if there's only one item in the subarray then the max is it
    if low+1 == high: return low,high,L[low]

    # otherwise, divide the list in half and look for the max subarray in each side
    mid = (low + high) // 2
    leftLow,leftHigh,leftSum = maxSubarray(L,low,mid)
    rightLow,rightHigh,rightSum = maxSubarray(L,mid,high)

    # check for a max subarray that crosses the midpoint
    crossLow,crossHigh,crossSum = maxCrossingSubarray(L,low,mid,high)

    # compare the 3 sums and return the data for the max
    if leftSum >= rightSum:
        if leftSum >= crossSum: return leftLow,leftHigh,leftSum
    elif rightSum >= crossSum: return rightLow,rightHigh,rightSum
    return crossLow,crossHigh,crossSum

#finds the subarray with the highest value that crosses the
#middle point of the input array
def maxCrossingSubarray(L,low,mid,high):
    crossSumLeft = L[mid]
    crossLow = mid
    newSum = 0
    #starts from the middle and iterates out to the left
    for i in range(mid,low-1,-1):
        newSum = newSum + L[i]
        #only saves the subarray of highest sum value
        if newSum > crossSumLeft:
            crossSumLeft = newSum
            crossLow = i
    crossSumRight = L[mid]
    crossHigh = mid
    newSum = 0
    #starts from the middle and iterates out to the right
    for i in range(mid,high):
        newSum = newSum + L[i]
        #only saves the subarray of highest sum value
        if newSum > crossSumRight:
            crossSumRight = newSum
            crossHigh = i + 1
    #adds the sums of the left and right subarrays to get the max crossing array
    #and subtracts the middle value since it was counted twice in each loop
    crossSum = crossSumLeft + crossSumRight - L[mid]
    return crossLow, crossHigh, crossSum

#uses the brute force method to find the max subarray
def maxSubarrayBF(L):
    #saves the current and final values for the indices and value
    currentLow = 0
    currentHigh = 0
    currentSum = 0
    maxSum = 0
    low = 0
    high = 0
    #repeats until the low value has traversed the list
    while True:
        if currentLow == len(L):
            return low, high, maxSum
        #starts at the current low value and moves to the right across the list
        for i in L[currentLow:]:
            #adds the next value in the list to the current total
            #and increases the index variable by one
            currentSum = currentSum + i
            currentHigh = currentHigh + 1
            #if the a higher value subarray has been found than the one that
            #is stored, then replace it with the new max subarray and
            #change the low and high indicies
            if currentSum > maxSum:
                maxSum = currentSum
                high = currentHigh
                low = currentLow
        #increases the low by one to iterate across the list
        currentLow = currentLow + 1
        #resets the high value to begin at the leftmost position
        currentHigh = currentLow
        #resets the current sum, but saves the max sum to be compared later
        currentSum = 0

#finds the length n of a list at which it is faster to find the max subarray
#using #divide and conquer than it is using brute force
def findDCCrossover():
    #starts with a list value of 3
    n = 3
    testcases = 5000
    while True:
        dtBF, dtDC = 0,0
        #tests 5000 cases
        for i in range(testcases):
            #makes a list with 3 random numbers from -20 to 20
            L = makeList(n)
            #sums the total time to run the brute force as well as
            #the divide and conquer methods for all 5000 lists
            dtBF += timeBF(L)
            dtDC += timeDC(L)
        #takes the average runtime by dividing total time by 5000
        avgBF, avgDC = dtBF/testcases, dtDC/testcases
        #prints when brute force average runtime is slower
        if avgDC < avgBF:
            #prints the length of the list at which the divide and conquer
            #method becomes faster than brute force and breaks the loop
            print("DC is faster than BF when n =", n)
            break
        #increases values of n until divide and conquer becomes more efficient
        n += 1

# Divide and conquer method for solving max subarray that is same as above except
# the base case uses the brute-force strategy when the array is small enough
def maxSubarrayMod(L,low,high):
    ### (d) CHANGE YOUR BASE CASE HERE

    #I copy pasted from above because it is faster in runtime than calling
    #the brute force method each time
    if len(L)<40:
        currentLow = 0
        currentHigh = 0
        currentSum = 0
        maxSum = 0
        low = 0
        high = 0
        while True:
            if currentLow == len(L):
                return low, high, maxSum
            for i in L[currentLow:]:
                currentSum = currentSum + i
                currentHigh = currentHigh + 1
                if currentSum > maxSum:
                    maxSum = currentSum
                    high = currentHigh
                    low = currentLow
            currentLow = currentLow + 1
            currentHigh = currentLow
            currentSum = 0

    # otherwise, divide the list in half and look for the max subarray in each side
    mid = (low + high) // 2
    leftLow,leftHigh,leftSum = maxSubarray(L,low,mid)
    rightLow,rightHigh,rightSum = maxSubarray(L,mid,high)

    # check for a max subarray that crosses the midpoint
    crossLow,crossHigh,crossSum = maxCrossingSubarray(L,low,mid,high)

    # compare the 3 sums and return the data for the max
    if leftSum >= rightSum:
        if leftSum >= crossSum: return leftLow,leftHigh,leftSum
    elif rightSum >= crossSum: return rightLow,rightHigh,rightSum
    return crossLow,crossHigh,crossSum


### (d) ENTER THE n WHERE YOUR ORIGINAL DC BECAME FASTER THAN BF
### YOU DO NOT NEED TO COMMENT THIS FUNCTION
def findDCMCrossover():
    testcases = 5000
    count = 0
    print("n\tBF\tDC\tDCM")
    for n in range(3,2*40):
        dtBF, dtDC, dtDCM = 0,0,0
        for i in range(testcases):
            L = makeList(n)
            dtBF += timeBF(L)
            dtDC += timeDC(L)
            dtDCM += timeDCM(L)
        avgBF, avgDC, avgDCM = dtBF/testcases, dtDC/testcases, dtDCM/testcases
        print(str(n)+"\t"+str(avgBF)+"\t"+str(avgDC)+"\t"+str(avgDCM))



### YOU DO NOT NEED TO MODIFY ANY FUNCTION BEYOND HERE BUT IT'S A GOOD IDEA
### TO MAKE SURE YOU UNDERSTAND THEM

# returns a list of length n that contains integers in the range -20 to 20
def makeList(n):
    L = []
    for i in range(n):
        L.append(random.randint(-20,20))
    return L

# returns the time it takes the brute-force method to find the max subarray of L 
def timeBF(L):
    start = time.time()
    maxSubarrayBF(L)
    end = time.time()
    return end-start

# returns the time it takes the divide and conquer method to find the max subarray of L
def timeDC(L):
    start = time.time()
    maxSubarray(L,0,len(L))
    end = time.time()
    return end-start

# returns the time it takes the modified divide and conquer method to find the
# max subarray of L
def timeDCM(L):
    start = time.time()
    maxSubarrayMod(L,0,len(L))
    end = time.time()
    return end-start

def main():
    print(maxSubarray([1,2,3,4,5],0,5))
    print(maxSubarray([1,2,-2,-12,10],0,5))
    print(maxSubarrayBF([1,2,3,4,5]))
    print(maxSubarrayBF([1,2,-2,-12,10]))
    findDCCrossover()
    findDCMCrossover()
main()
