Question No: 3
Sashi has got the task to frame a speech for his professor at the university at the Annual sports meet.But the problem is that the professor can't speak the words clearly which have vowels in them. So sashi has to avoid such words and has to minimise their usage in the speech letter. Your task is to help Sashi mark the vowels in the words so that he can minimise their use. 
You are given a string S consisting of lower case letters only. You need to count the number of vowels in the string S.

Input format
The first line will contain an integer T denoting the number of test cases. 
The following T lines will contain a string S in lower case letters only.
Output format
Print the number the vowels in the string S.
Code constraints
1<=T<=100

Sample testcases
Input 1
1
bashes
Output 1
2

================================
solution: python 
================================
t=int(input())
for i in range(t):
    s=input()
    vowel='aeiou'
    c=0
    for i in s:
        if i in vowel:
            c+=1
    print(c)
	
====================================
solution: c Language
====================================
#include <stdio.h>
#include <string.h>
int main()
{
    int t;
    scanf("%i",&t);
    while(t--){

        char str[12345];
        int len,c=0;
        scanf("%s%n",str,&len);
        len--;
        for(int i=0;i<len;i++)
            if(strchr("aeiou",str[i]))
                c++;
        printf("%i\n",c);
    }
    return 0;
}
