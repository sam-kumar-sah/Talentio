Question No: 2
Sam hates two similar continuous letters in a string S. He calls these strings as worst strings. 
So,Good strings are the strings which do not have similar continuous 
letters.Given a string S, you need to convert it into a Good String.You 
simply need to perform one operation - if there are two same continuous letters, delete one of them.

Input format
The first line contains an integer T, denoting the number of test cases.
Each test case consists of a string S, which consists of only lower case letters.
Output format
For each test case, print the answer to the given problem.
Code constraints
1 <= T <= 10
1 <=|S| <= 30

Sample testcases
Input 1
1
abbbbbbb
Output 1
ab
Input 2
2
ADD
ADE
Output 2
ADADE

================================
solution: python
================================
def sam(l):
    n=len(l)
	s=[]
    for i in l:
        s.append(i)
    if n<2:
        return 
    j=0
    for i in range(n):
        if s[j]!=s[i]:
            j+=1
            s[j]=s[i]
    j+=1
    s=s[:j]
    ss=""
    for i in s:
        ss+=i
    #print("s=",ss)
    return ss

super=""
t=int(input())
while(t):
    l=input()
    aa=sam(l)
    super+=aa
    t-=1
print(super)


================================
solution: C Language
================================
#include<stdio.h>
#include<string.h>
int main()
{
	int t,i,n;
	char str[20];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",str);
		n=strlen(str);
		for(i=0;i<n;i++)
		{
			printf("%c",str[i]);
			while(i<n && str[i]==str[i+1])
				i++;
		}
	}
	return 0;
}