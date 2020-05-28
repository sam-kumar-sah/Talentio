Question No: 1
Steve has a string of lowercase and uppercase characters in range ascii[‘a’..’z’] /[1...9] .He wants to remove vowels from the string by doing a series of operations.For instance, the string aab could be shortened to b at the end of operation.
Steve’s task is to delete vowels and print the resulting string.If the string is not having vowels, print same String

Input format
A single string, S.
Output format
Print the final non-vowel string .
Code constraints
1<=S<=100

Sample testcases
Input 1
hello
Output 1
String after deleting vowels: hll

================================
solution: python 
================================
s=input()
v='aeiou'
l=[]
for i in s:
    if i not in v:
        l.append(i)
ss=""
for i in l:
    ss+=i
print("String after deleting vowels:",ss)

====================================
solution: c Language
====================================
#include <stdio.h>
#include <string.h>

int check_vowel(char);
int main()
{
char s[100], t[100];
int i, j = 0;
scanf("%s",s);
for(i = 0; s[i] != '\0'; i++) {
if(check_vowel(s[i]) == 0) {	
t[j] = s[i];
j++;
}
}
t[j] = '\0';
strcpy(s, t);	
printf("String after deleting vowels: %s\n", s);
return 0;
}
int check_vowel(char c)
{
switch(c) {
case 'a':
case 'A':
case 'e':
case 'E':
case 'i':
case 'I':
case 'o':
case 'O':
case 'u':
case 'U':
return 1;
default:
return 0;
}
}