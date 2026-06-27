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

#6
'''
Pattern 6: Inverted Right-Angled Number Pyramid
1 2 3 4
1 2 3
1 2
1

n = int(input("Enter a number: "))
i = 0
while i < n:
    j = n - i
    num = 1
    while j > 0:
        print(num, end=" ")
        num += 1
        j -= 1
    print()
    i += 1
'''

#7
'''
Pattern 7:Star pyramid
    *
   ***  
  *****

n = int(input("Enter a number: "))
num = 0
for i in range(1, n+1):
    spaces = n - i
    for j in range(spaces):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
'''

#8 Inverted Star Pyramid
'''
    *****
     ***
      *


n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(2 * (n - i) - 1):
        print("*", end="")
    for j in range(i):
        print(" ", end="")
    print()

'''

#9 Diamond Pattern
'''
    *
   ***
  *****
   ***
    *
n = int(input("Enter a number: "))
num = 0
for i in range(1, n+1):
    spaces = n - i
    for j in range(spaces):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(2 * (n - i) - 1):
        print("*", end="")
    for j in range(i):
        print(" ", end="")
    print()

'''

#10 Half Diamond Pattern
'''
*
**
***
****
*****
****
***
**
*


n = int(input("Enter a number: "))
for i in range(2 * n - 1):
    if i < n:
        for j in range(i + 1):
            print("*", end="")
    else:
        for j in range(2 * n - i - 1):
            print("*", end="")
    print()

    '''



'''
Pattern 11: Alternating Number Pattern
1
0 1
1 0 1
0 1 0 1


n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

'''