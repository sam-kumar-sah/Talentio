problem:
-----------------------------------------
Avanthika is weak in the concepts of number series. She is given a number L and has 
to find L terms of the series.
The series is as follows
1, 2, 5, 8,15. . . .

Input format
You are given an integer p denoting the number of test cases. The next subsequent 
lines contain an integer L denoting the number of terms till which the series needs 
to be printed.

Output format
For each test case, print the series up to L terms.

Sample testcases
Input 1
2
5
8
Output 1
1 2 5 8 15 
1 2 5 8 15 28 51 94 

=================================
solution: python
=================================
t=int(input())
while(t):
    n=int(input())
    a=[1,2,5]
    for i in range(n):
        aa=a[-1]+a[-2]+a[-3]
        a.append(aa)
    for i in range(n):
        print(a[i],end=" ")
    t-=1
    
