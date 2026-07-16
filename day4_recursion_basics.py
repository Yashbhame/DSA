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