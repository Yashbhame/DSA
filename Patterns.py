#1
'''
Pattern 1: Square Pattern
***
***
***
n = int(input("Enter a number: "))

for i in range(0, n):
    for j in range(0, n):
        print("*", end=" ")
    print()
'''
#2
'''
Pattern 2: Right-Angled Triangle Pattern
*
**
***
****
*****
n = int(input("Enter a number: "))

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()
'''


#3
'''
Pattern 3 :Right-Angled Number Pyramid
1
1 2
1 2 3
1 2 3 4

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''

#4
'''
Pattern 4:Right-Angled Number Triangle-2
1
2 2
3 3 3
4 4 4 4

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
'''


#5
'''
Pattern 5:Inverted Right-Angled Triangle Pattern
*****
****
***
**
*

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()
'''

