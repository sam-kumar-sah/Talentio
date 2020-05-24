Question No: 2
Coding Type Question
----------------------------------------------------
The whitewalkers are here and the Great War is on. Each and every living being is giving their best to save the world from the dead. Arya fighting with full dedication found that whitewalkers need to be killed with a pattern or else they wont die. So that she can fight till the end of the war. She tried to understand the pattern. She kills every 'Xth'whitewalker by stabbing them 'N' times .

Whitewalker approaching order (X)   Number of times-stabbing(N)

1                                                               1

2                                                               1

3                                                               2

.                                                                .

.                                                                .

55                                                             5

.                                                                .

98                                                             3

.                                                                 .

.                                                                 .

101                                                            4

.                                                                 .

.                                                                 .

.                                                                 .

198                                                             4

This is the hint of the pattern that Arya needs to follow. Help Arya!

Input format
The first line of the input contains an integer T, denoting the number of test cases. The description of each test case follows. Each test case contains a single line with one integer 'X' the Xth whitewalker .

Output format
For each test case in, a new line print the number of stabs required to kill the 'Xth' whitewalker.

Sample testcases
Input 1
4
102
95
72
60
Output 1
4
6
2
4
Input 2
3
9
75
6
Output 2
2
4
2

===============================================
solution: python
===============================================
def binary(n):
    temp=0
    while(n>0):
        if n%2==1:
            temp+=1
        n=n//2
    return temp
    
t=int(input())
for i in range(t):
    n=int(input())
    print(binary(n))