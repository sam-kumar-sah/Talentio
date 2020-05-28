Question No: 4
Coding Type Question
Krish given a string S.He need to check whether it's a palindrome or not. Print "YES" (without quotes) if S is a palindrome and "NO" (without quotes) if S is not a palindrome.

Input format
First line will contain an integer T that is the number of test cases. The following T lines will contain: -A string S consisting of only lowercase letters.
Output format
Output YES or NO in new line for each test case.

Sample testcases
Input 1
1
madam
Output 1
YES

================================
solution: python 
================================
t=int(input())
for i in range(t):
    s=input()
    if s==s[::-1]:
        print("YES")
    else:
        print("NO")
		
====================================
solution: c Language
====================================
#include<stdio.h>
int main()
{
    int t;
    scanf("%i",&t);
    while(t--){
        char str[12345];
        int len,i;
        // %n saves the length of the string automatically
        scanf("%s%n",str,&len);
        len--;
        for(i=0;i<len>>1;i++)
            if(str[i]!=str[len-i-1])
                break;
        // i == len/2 , means both half of the string matched
        puts(i==(len>>1) ?"YES":"NO");
    }
    return 0;
}
