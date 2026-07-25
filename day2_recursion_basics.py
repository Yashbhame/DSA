#1: Sum of first n natural numbers
def sum(n):
    
    # base condition
    if n == 1:
        return 1
    
    return n + sum(n - 1)

if __name__ == "__main__":
    n = 5
    print(sum(n))


#2: Factorial of a number
def fact(n):

    # BASE CONDITION
    if n == 0:
        return 1
    return n * fact(n - 1)

print("Factorial of 5 : ", fact(5))


#3 demonstrate working of recursion

def printFun(test):

    if (test < 1):
        return
    else:

        print(test, end=" ")
        printFun(test-1)  
        print(test, end=" ")
        return

# Driver Code
test = 3
printFun(test)


#4: Fibonacci series using recursion
# Python code to implement Fibonacci series

# Function for fibonacci
def fib(n):

    # Stop condition
    if (n == 0):
        return 0

    # Stop condition
    if (n == 1 or n == 2):
        return 1

    # Recursion function
    else:
        return (fib(n - 1) + fib(n - 2))


# Driver Code

# Initialize variable n.
n = 5
print("Fibonacci series of 5 numbers is :",end=" ")

# for loop to print the fibonacci series.
for i in range(n): 
    print(fib(i),end=" ")