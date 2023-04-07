#Dylan Miller

#this program implements binary search by taking in an array and
#searching between two indices to find a target value

#binary searches a given list from a low to high index and returns
#the index of the target value
    #L - sorted array
    #low - lowest index value to check in the list
    #high - highest index value to check in the list
    #target - value the function searches for
def binarySearch(L,low,high,target):
    #finds the middle value in the array
    half = (low+high)//2
    #if the mid value is the target then return the index
    if L[half] == target:
        return half
    #if the mid value is above the target value then take the first
    #half of the array and perform another binary search
    elif L[half] > target:
        return binarySearch(L,low,half,target)
    #if the mid value is below the target value then take the second
    #half of the array and perform another binary search
    elif L[half] < target:
        return binarySearch(L,half+1,high,target)
    #if the value can't be found return -1
    return -1

def main():
    #print(binarySearch([1,2,3,4,5],0,5,1))
    #print(binarySearch([1,2,3,4,5],0,5,2))
    #print(binarySearch([1,2,3,4,5],0,5,3))
    #print(binarySearch([1,2,3,4,5],0,5,4))
    #print(binarySearch([1,2,3,4,5],0,5,5))
    print(binarySearch([1,2,3,4,5],0,5,6))
    #print(binarySearch([1,3,4,5],0,6,2))
    #print(binarySearch([1,1,1,1,1],0,4,1))
main()

