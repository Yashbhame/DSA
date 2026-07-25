'''
class Solution:
    def printName(self,name,count,N):
        if count > N:
            return

        print(name)

        self.printName(name,count + 1,N)


if __name__ == "__main__":
    sol = Solution()
    N = 6
    name = "Yash"

    sol.printName(name, 1, N)

class Solution2:
    def recursion(self,count,n):
        if count > n:
            return
        print(count, end = " ")
        self.recursion(count + 1,n)

sol = Solution2()
sol.recursion(1,5)

class Sol2_backtrack:
    def recursion(self,count,n):
        if count == 0:
            return
        self.recursion(count - 1,n)
        print(count ,end=" ")

sol = Sol2_backtrack()
sol.recursion(5,5)


class Solution3:
    def reverse(self,count,n):
        if count > n:
            return
        self.reverse(count + 1,n)
        print(count ,end=" ")

sol = Solution3()
sol.reverse(1,5)


class SumOfDigits:
    def add(self,n):
        if n == 0:
            return 0
        last_digit = n % 10
        return last_digit + self.add(n // 10)
        

solution = SumOfDigits()
print(solution.add(1234))
'''

class Power:
    def powerOfNum(self,x,n):
        if n == 0:
            return 1
        return x * self.powerOfNum(x, n - 1)
solution = Power()
print(solution.powerOfNum(2,5))