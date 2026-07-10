class Solution:
    def printName(self,name,count,N):
        if count == N:
            return

        print(name)

        self.printName(name,count + 1,N)


if __name__ == "__main__":
    sol = Solution()
    N = 6
    name = "Yash"

    sol.printName(name, 0, N)