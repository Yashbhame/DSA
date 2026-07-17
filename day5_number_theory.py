import math
#1 Count number of digits

n = int(input("Enter the number:"))
count = 0
while n > 0:
    last_digit = n % 10
    count += 1
    n = n // 10

print(f"The number of digits in the given input is:{count}")

#2 Reverse a number
class Reverse:
    def rev(self,n):
        revnum = 0
        while n > 0:
            last_digit = n % 10
            n = n // 10
            revnum = revnum * 10 + last_digit
        print(revnum)
        return
    
obj1 = Reverse()
obj1.rev(123)
obj1.rev(10400)
#3 Palindrome
class Palindrome:
    def rev(self,n):
        number = n
        revnum = 0
        while number > 0:
            last_digit = number % 10
            number = number // 10
            revnum = (revnum * 10) + last_digit
        print(revnum)
        if revnum == n:
            return True
        else:
            return False
        
obj2 = Palindrome()
num = int(input("Enter a number:"))
print(obj2.rev(num))
print(obj2.rev(1221))
print(obj2.rev(7789))


#4 Armstrong number
class Armstrong:
    def Arm(self,n):
        dup = n
        sum = 0
        while dup > 0:
            last_digit = dup % 10
            dup = dup // 10
            sum = last_digit ** 3 + sum
        print(sum)
        if sum == n:
            print(f"The number {n} is an Armstrong number")
            return
        else:
            print(f"The number {n} is not an Armstrong number")
            return
obj3 = Armstrong()
num = int(input("Enter to check whether it is an armstrong number:"))
obj3.Arm(num) 
#5 Print all divisors
class Solution:
    def getDivisors(self, N):
        res = []

        for i in range(1, int(math.isqrt(N)) + 1):
            if N % i == 0:
                res.append(i)
                if i != N // i:
                    res.append(N // i)
        res.sort()
        return res
obj5 = Solution()
N = int(input("Enter number to find its divisors:"))
result = obj5.getDivisors(N)

print("Divisors of", N, ":", *result)


#6 GCD

class GCD:
    def euclidian(self,a,b):
        while a > 0 and b > 0:
            if (a > b):
                a = a % b
            else:
                b = b % a
        if a == 0:
            print("The GCD of given numbers is:",b) 
        else:
            print("The GCD of given numbers is:",a)

obj6 = GCD()
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
obj6.euclidian(num1,num2)

