#Dylan Miller

def binarySearch(L,low,high,target):
    # Check base case
    if high >= low:

        half = (high + low) // 2
 
        # If element is present at the middle itself
        if L[half] == target:
            return half
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif L[half] > target:
            return binarySearch(L, low, half - 1, target)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(L, half + 1, high, target)
 
    else:
        # Element is not present in the array
        return -1

def main():
    #print(binarySearch([],0,4,1))
    print(binarySearch([1],0,4,1))
    print(binarySearch([1,2,3,4,5],0,4,3))
    print(binarySearch([1,2,3,4,5],0,4,6))
main()
