Question No: 1
Coding Type Question
In this problem, you need to print the pattern of the following form

3
45
678
9101112

Input format
First line of the input number of rows r.

Output format
Print the pattern 

==============================
solution: python
==============================
n=int(input())
p=3
for i in range(n):
    for j in range(i):
        print(p,end="")
        p+=1
    print()