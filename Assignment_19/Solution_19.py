#!Solution-1
def Sum_of_first_n_natural(n: int):
    if (n == 1):
        return n
    else:
        a = Sum_of_first_n_natural(n-1)
        return a+n


# print(Sum_of_first_n_natural(50))


#!Solution-2
def Sum_of_first_n_odd_Numbers(n: int):
    if (n == 1):
        return n
    elif (n % 2 == 0):
        a = Sum_of_first_n_odd_Numbers(n-1)
        return a
    else:
        a = Sum_of_first_n_odd_Numbers(n-2)
        return a+n


# a = int(input("Enter Number:\n"))
# print(Sum_of_first_n_odd_Numbers(a*2))


#!Solution-3
def Sum_of_first_n_even_Numbers(n: int):
    if (n <= 1):
        return n
    elif (n % 2 == 0):
        a = Sum_of_first_n_even_Numbers(n-2)
        return a+n
    else:
        a = Sum_of_first_n_even_Numbers(n-1)
        return a


# a = int(input("Enter Number:\n"))
# print(Sum_of_first_n_even_Numbers(a*2))

#!Solution-4
def Factorial(n: int):
    if (n <= 1):
        return 1
    else:
        a = Factorial(n-1)
        return a*n


# print(Factorial(10))


#!Solution-5
def Sum_of_Square_of_first_n_Numbers(n: int):
    sum = 0
    if (n <= 1):
        return 1
    else:
        return (n*n)+Sum_of_Square_of_first_n_Numbers(n-1)


# print(Sum_of_Square_of_first_n_Numbers(5))
