#Dylan Miller

#This program finds the value of 2**n recursively

#takes a non-negative integer n
def exp(n):
    #base case if 2 is raised to 1 then return 2
    if n == 1:
        return 2
    #base case if 2 is rased to 0 then return 1
    if n == 0:
        return 1
    #multiply 2 times 2... lowering n by 1 each time until we reach 2**1
    return 2*exp(n-1)

def main():
    print(exp(4))
    print(exp(0))
    print(exp(2))
    print(exp(1))
main()
