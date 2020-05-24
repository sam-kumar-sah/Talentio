Question No: 1
Coding Type Question
Write a program to find the maximum element in each row of the matrix.

Output format
Refer sample output for details.

Sample testcases
Input 1:
3
2
4 5
6 9
0 3
Output 1:
5
9
3
Input 2:
2
2
4 5
6 7
Output 2:
5
7

==============================
solution-1 :python
==============================

def maximimum_elem(a):
    for i in range(m):
        Max = 0
        for j in range(n):
            if a[i][j] > Max:
                Max = a[i][j]
        print(Max)

m = int(input())
n = int(input())
a = list()
if m==0 and n==0:
    print(m)
    print(n)
else:
    for i in range(m):
        a.append(list(map(int, input().split()[:n])))
    maximimum_elem(a)

=================================
solution-2 :C Language
=================================
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a[20][20],i,j,max,m,n;
    scanf("%d%d",&m,&n);
    if (m==0 &&n==0)
    {
        printf("%d\n%d",m,n);
    }
    else
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        for(i=0;i<m;i++)
        {
            max=0;
            for(j=0;j<n;j++)
            {
                if (a[i][j]>max)
                    max=a[i][j];        
            }
            printf("%d\n",max);
        }   
}