'''
class Solution:
    def printN(self,count,n):
        if count > n:
            return
        print(count, end = " ")
        self.printN(count + 1,n)

if __name__ == "__main__":
    sol = Solution()
    n = 6

    sol.printN(1,n)
    print()   

#sum of first n natural numbers
class Sum:
    def SumOfN(self,n):
        if n == 1:
            return 1
        return n + self.SumOfN(n - 1)
obj2 = Sum()
print(obj2.SumOfN(5))
'''
class factorial:
    def fact(self,n):
        if n == 1:
            return 1
        return n * self.fact(n - 1)

obj3 = factorial()
print(obj3.fact(5))
