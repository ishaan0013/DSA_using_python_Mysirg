# !Solution-1
def First_N_Natural_Numbers(n: int):
    if (n != 1):
        First_N_Natural_Numbers(n-1)
        print(n, end=" ")
    else:
        print(n, end=" ")

# !Solution-2


def First_N_Natural_Numbers_Reverse(n: int):
    if (n == 1):
        print(n, end=" ")
    else:
        print(n, end=" ")
        First_N_Natural_Numbers_Reverse(n-1)

# !Solution-3


def First_N_Odd_Numbers(n: int):
    if (n == 1):
        print(n, end=" ")
    elif (n % 2 == 0):
        First_N_Odd_Numbers(n-1)
    else:
        First_N_Odd_Numbers(n-2)
        print(n, end=" ")

# !Solution-4


def First_N_Even_Numbers(n: int):
    if (n == 2):
        print(n, end=" ")
    elif (n % 2 != 0):
        First_N_Even_Numbers(n-1)
    else:
        First_N_Even_Numbers(n-2)
        print(n, end=" ")

#  !Solution-5


def First_N_Odd_Numbers_Reverse(n: int):
    if (n % 2 == 0):
        # print(n-1, end=" ")
        First_N_Odd_Numbers_Reverse(n-1)
    elif (n == 1):
        print(n, end=" ")
    else:
        print(n, end=" ")
        First_N_Odd_Numbers_Reverse(n-2)

# Solution-6


def First_N_Even_Numbers_Reverse(n: int):
    if (n % 2 != 0):
        First_N_Even_Numbers_Reverse(n-1)
    elif (n == 2):
        print(n, end=" ")
    else:
        print(n, end=" ")
        First_N_Even_Numbers_Reverse(n-2)


a = int(input("Enter Number:\n"))
First_N_Even_Numbers_Reverse(a*2)
