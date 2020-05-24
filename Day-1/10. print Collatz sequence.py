Question No: 10
Coding Type Question
To get the Collatz sequence from a number, the respective number needs to be divided 
by 2, if it is even. In case the given number is odd it needs to be multiplied by 3 and incremented by 1.
Same operation needs to be continued on the result of the previous operation until the number becomes 1. For any given number the series will end with 4 2 1.

Write a program to print Collatz sequence.
Input format
Refer Sample Input for the logic
Output format
Refer Sample Output for the logic

Sample testcases
Input 1
5
Output 1
5 16 8 4 2 1 
Input 2
16
Output 2
16 8 4 2 1 

============================
solution: python
============================
n=int(input())
print(n)
while n!=1:
    if n%2==0:
        n//=2
    else:
        n=n*3+1 
    print(n,end=" ")
    