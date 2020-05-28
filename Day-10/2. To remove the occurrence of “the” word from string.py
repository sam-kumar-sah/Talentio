Question No: 2
Write a c program to remove the occurrence of “the” word from entered string.

Input format
Enter the string
Output format
Remove the occurrence of the word from entered string

Sample testcases
Input 1
the is the 
Output 1
is 
Input 2
welcome to the class
Output 2
welcome to class


================================
solution: python 
================================
s=input().split()
w="the"
l=[]
for i in s:
    if i!=w:
        l.append(i)
print(*l)


====================================
solution: c Language
====================================
#include<stdio.h>
int main()
{
char a[100];
int i;
scanf("%[^\n]",a);
for(i=0; a[i]!='\0';i++)
{
if((a[i]=='t' && a[i+1]=='h' && a[i+2]=='e') || (a[i]=='T' && a[i+1]=='H'&& a[i+2]=='E'))
{
i=i+3;
}
else
printf("%c",a[i]);
}
return 0;
}
