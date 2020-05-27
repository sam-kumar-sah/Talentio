Question No: 5
Prathik have been given a String S consisting of uppercase and lowercase 
alphabets. He need to change the case of each alphabet in this String.That 
is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. Prathik need to print the resultant String to output.

Input format
The first line of input contains the String S

Output format
Print the resultant String on a single line.

Code constraints
1<=|S|<=100

Sample testcases
Input 1
CoLLeGe
Output 1
cOllEgE
Input 2
PROGRAm
Output 2
prograM


================================
solution: python
================================
l=input()
s=[]
for i in l:
    s.append(i)

for i in range(len(s)):
    
    if s[i]>='A' and s[i]<='Z':
        s[i]=chr(ord(s[i])+32)
        
    elif s[i]>='a' and s[i]<='z':
        s[i]=chr(ord(s[i])-32)

for i in range(len(s)):
    print(s[i],end="")


================================
solution: c language
================================
#include <stdio.h>
int main()
{
	char S[100];  
	int i;
	scanf("%s",S);  
	for(i=0;S[i]!='\0';i++)
	{
		if(S[i] >= 65 && S[i] <= 90)
			S[i] = (char)(S[i] + 32);
		else
			S[i] = (char)(S[i] - 32);
	}
    printf("%s",S);  
	return 0;
}
