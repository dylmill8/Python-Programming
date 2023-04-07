#Dylan Miller

#Using sorting algorithms to analize and optomize runtimes

#this function returns the jth order statistic of an input array A
    #A is an array of distinct elements
    #j is the jth order statistic of the array
def statistic(A,j):
    #calls quicksort across the whole list the first time
    quicksort(A,0,len(A)-1)
    #returns the value of the jth order statistic
    return A[j-1]

#implements recursivce quicksort to sort the list
def quicksort(A,p,r):
    #if the low value is less than the high value
    if p < r:
        q = partition(A,p,r)
        #recursively called quicksort on each side of the list
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

#sorts the list using a pivot value
def partition(A,p,r):
    #sets the pivot to the highest index in the list
    x = A[r]
    #tracks the lower subarray index
    i = p-1
    for j in range(p,r):
        #if current value is less than or equal to the pivot
        if A[j] <= x:
            i = i+1
            #moves the current value into the lower index
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def main():
    #A = [4,7,3,6,0,8,2,5]
    A = [1,2,3]
    j = 1
    print(statistic(A,j))
main()
