Question No: 1
You are given a string S. Count the number of occurrences of all the 
digits in the string S.

Input format
First line contains string S.

Output format
For each digit starting from 0 to 9, print the count of their occurrences in the string S. 
So, print lines, each line containing 2 space separated integers. First 
integer i and second integer count of occurrence of i. See sample output for clarification.

Code constraints
1<=S<=100

Sample testcases
Input 1
77150
Output 1
0 1
1 1
2 0
3 0
4 0
5 1
6 0
7 2
8 0
9 0
Input 2
234
Output 2
0 0
1 0
2 1
3 1
4 1
5 0
6 0
7 0
8 0
9 0

================================
solution: python 
================================
s=input()
l=[]
if len(s)==0:
    for i in range(10):
        if i==0:
            print(i,1)
        else:
            print(i,0)
else:
    for i in s:
        l.append(int(i))
    l.sort()
    h={}
    for i in l:
        if i not in h:
            h[i]=1
        else:
            h[i]+=1
    v=list(h.values())
    k=list(h.keys())
    #print(k,v)
    p=0
    for i in range(10):
        if i in k:
            print(i,v[p])
            p+=1
        else:
            print(i,0)
            
====================================
solution: c Language
====================================
#include <stdio.h>
#include <string.h>
int main()
{
    int c[10],i,p,len;
    char s[100];
    scanf("%s",s);
    len=strlen(s);
    for(i=0;i<10;i++)
        c[i]=0;
    for(i=0;i<len;i++)
    {
        p=s[i]-48;
        c[p]++;
    }
    for(i=0;i<10;i++)
        printf("%d %d\n",i,c[i]);
    
    return 0;
}