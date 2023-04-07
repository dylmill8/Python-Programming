#Dylan Miller

#this module practices dynamic programming (DP) grid implementations in Python

#finds the nth Fibonacci number
def fibDP(n):
    #returns the base case when n is 0
    if n <= 0:
        return 0
    #sets up the DP grid with the first 2 values as the base cases in the
    #Fibonacci sequence
    fibSequence = [0,1]
    #loops until the length of the list minus 1 (to account for a 0th term)
    #equals the nth value we're looking for
    while len(fibSequence)-1 != n:
        #adds the previous two elements in the DP grid together
        #and stores it as the current value in the grid
        fibSequence.append(fibSequence[-1]+fibSequence[-2])
    #returns the most recent value in the DP grid which is the nth
    #Fibonacci number
    return fibSequence[-1]

#finds if a given sequence of coins can sum to an exact target value
def exactChange(target,coins):
    #sorts the coins from greatest to least
    coins.sort(reverse = True)
    #checks base cases if the target is greater than the sum of all coins
    if target > sum(coins):
        return False
    if target == 0:
        return True
    DPgrid = []
    for i in coins:
        #if the first item is too large then the DPgrid's highest sum is 0
        if i > target  and len(DPgrid) < 1:
            DPgrid = DPgrid + [0]
        #otherwise the highest sum is just the first coin value
        elif i < target and len(DPgrid) < 1:
            DPgrid = DPgrid + [i]
        #if the sum of the current value plus the previous is less than
        #or equal to the target then it is the new heighest sum
        elif DPgrid[-1] + i <= target:
            DPgrid = DPgrid + [DPgrid[-1] + i]
    #after checking every coin, if the heighest sum that is less than
    #or equal to the target does in fact equal the target then return true
    #otherwise exact change cannot be made so return false
    if DPgrid[-1] == target:
        return True
    else: return False

def main():
    for i in range(10):
        print(fibDP(i))

    coins = [25,10,5,1]
    for i in [13,36,6]:
        print(exactChange(i,coins))
main()
