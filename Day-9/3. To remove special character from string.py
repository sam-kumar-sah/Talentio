Question No: 3
Harsha is working as a programmer in a company which process the random 
data and arranges into a structured format . Harsha's task is to segregate 
the random data and obtain only characters data and process them in a meaningful 
way , let us deduce a logic to help Harsha in performing this operation

Input format
Read a string with Characters and Special characters
Output format
Display the string only with characters

Sample testcases
Input 1
harsha@!#3)@^8
Output 1
harsha
Input 2
@#123hello
Output 2
hello


================================
solution: python
================================
a="abcdefghijklmnopqrstuvwxyz"
s=input()
ss=""
for i in s:
    if i in a:
        ss+=i
print(ss)


================================
solution: c language
================================
#include<stdio.h>
int main()
{
    char word[150];
    int i, j;
    scanf("%s",word);

    for(i = 0; word[i] != '\0'; ++i)
    {
        while (!( (word[i] >= 'a' && word[i] <= 'z') || (word[i] >= 'A' && word[i] <= 'Z') || word[i] == '\0') )
        {
            for(j = i; word[j] != '\0'; ++j)
            {
                word[j] = word[j+1];
            }
            word[j] = '\0';
        }
    }
    printf("%s",word);
    return 0;
}