def testPrep(n):
    print(int(n),end=" ")
    if n == 1:
        return print()
    elif n%2 == 0:
        testPrep(n/2)
    else:
        testPrep((3*n)+1)
     
def main():
    testPrep(3)
    testPrep(5)
main()
