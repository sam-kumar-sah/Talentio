Question No: 5
You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
For example, given the string s=AABAAB, remove an A at positions 0 and 3 to make s=ABAB in 2 deletions.

Input format
The first line contains an integer q, the number of queries.
The next q lines each contain a string s.
Output format
For each query, print the minimum number of deletions required on a new line.
Code constraints
1<=q<=10
1<=|s|<=105
Each string s will consist only of characters A and B

Sample testcases
Input 1
1
ABBABBAA
Output 1
3
Input 2
2
AAABBBB
ABABABAAA
Output 2
5
2
================================
solution: python 
================================
t=int(input())
for i in range(t):
    s=input()
    prev=None
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    ss=""
    for ch in l:
        if prev!=ch:
            ss+=ch
            prev=ch
    count=len(s)-len(ss)
    print(count)

	
====================================
solution: c Language
====================================
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char str[100000],temp;
    int i,j,T,count;
    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
        scanf("%s",str);
        temp='\0';
        j=-1;
        count=0;
        while(str[++j]!='\0')
            if(temp==str[j])
                count++;
            else
                temp=str[j];
        printf("%d\n",count);
    }
    return 0;
}
