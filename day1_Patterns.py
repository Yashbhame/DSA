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


#12 Number crown pattern
'''
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1

n = int(input("Enter number of rows:"))
for i in range(1, n+1):
    for j in range(1, i + 1):
        print(j,end = " ")
    for j in range(2 * (n - i)):
        print(" ",end = " ")
    for j in range(i , 0 , -1):
        print(j ,end = " ")
    print()
'''



#13 Increasing number triangle pattern
'''
n = int(input("Enter number:"))
start = 1
for i in range(n):
    for j in range(i + 1):
        print(start , end = " ")
        start += 1
    print()
'''


'''
#14 Increasing letter triangle pattern
n = int(input("Enter number:"))
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j) , end = " ")
    print()
'''


'''
#15 
n = int(input("Enter number:"))
for i in range(n):
    for j in range(n - i):
        print(chr(65 + j) , end = " ")
    print()
'''

'''
#16
n = int(input("Enter number:"))
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i) , end = " ")
    print()
'''


#17
'''
n = int(input("ENTER NUMBER:"))
for i in range(n):
    for j in range(n - i - 1):
        print(" ",end = "")
    ch = ord('A')
    breakpoint = (2 * i + 1) // 2
    for j in range(1,2 * i + 2):
        print(chr(ch), end="")
        if j <= breakpoint:
            ch += 1
        else:
            ch -= 1
    print()
'''


#18
'''
n = int(input("Enter number of rows:"))
for i in range(1, n + 1):
    char = ord('A')
    for j in range (i):
        print(chr(char + n + j -i), end = " ")
        
    print()
'''


#19
'''
n = int(input("Enter number of rows:"))
inis = 0
for i in range(n):
    print("*" * (n - i), end = "")
    print(" " * inis, end = "")
    print("*" * (n - i))
    inis += 2

inis = 2 * (n - 1)
for i in range(1, n + 1):
    print("*" * i, end = "")
    print(" " * inis, end = "")
    print("*" * i)
    inis -= 2
'''


#20
'''
n = int(input("Enter number of rows:"))
inis = (n * 2 - 2)
for i in range(n):
    print("*" * (i + 1), end = "")
    print(" " * inis, end = "")
    print("*" * (i + 1))
    inis -= 2
for i in range(n - 1):
    print("*" * (n - i - 1), end = "")
    print(" " * (2 * i + 2), end = "")
    print("*" * (n - i - 1))
'''


#21
'''
n = int(input("Enter number of rows:"))
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n, end = "")
    else:
        print("*" + " " * (n - 2) + "*", end = "")
    print()
'''

#22
n = int(input("Enter number of rows:"))
for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        top = i
        left = j
        right = (2 * n - 2) - j
        bottom = (2 * n - 2) - i

        min_distance = min(top, left, right, bottom)
        print(n - min_distance, end = " ")
    print()