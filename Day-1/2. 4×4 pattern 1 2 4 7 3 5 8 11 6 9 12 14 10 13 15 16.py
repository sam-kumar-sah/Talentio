Question No: 2
-------------------------------------
Coding Type Question
Consider the following 4×4 pattern:

 1 2 4 7
 3 5 8 11
 6 9 12 14
10 13 15 16

You are given an integer N. Print the N×N pattern of the same kind (containing 
integers 1 through N2).

Input format
The first line of the input contains a single integer T denoting the number of 
test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.

Output format
For each test case, print N lines; each of them should contain N space-separated 
integers.
Code constraints
1<=T<=10
1<=N<=100

Sample testcases
Input 1
1
4
Output 1
1 2 4 7 
3 5 8 11 
6 9 12 14 
10 13 15 16 

===========================
solution: C Language
===========================
#include <stdio.h>

int main()
{
    int i,j,k,c,n,t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        int a[n+1][n+1];
        c=1;
    for(k=1;k<=n;k++)
    {
        for(i=1,j=k;i<=k&&j>=1;i++,j--)
        a[i][j]=c++;
    }
    for(k=2;k<=n;k++)
    {
        for(i=k,j=n;i<=n&&j>=k;i++,j--)
        a[i][j]=c++;
    }
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    }
    return 0;
}