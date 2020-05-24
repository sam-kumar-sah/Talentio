Question No: 9
Coding Type Question
Suppose you live in a country where 1, 7, and 9 are lucky digits. A lucky number for 
you is a number that contains only your lucky digits in it. 
Example: 1, 71, 999,1917 etc., are lucky, where as 5, 175, 90, 570 are not. Given a integer N, count the number of lucky numbers in the range [1,N]. 

Input format
Input contains one number n. 

Output format
Output contains the count of numbers less than or equal to n which are lucky
Code constraints
2 <= n <= 100000

Sample testcases
Input 1
1
Output 1
1
Input 2
8
Output 2
2

===============================
solution: python
===============================
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int check(int x)
{
    while(x > 0)
    {
        int rem = x%10;
        x/=10;
    	if(!(rem == 1 || rem == 7 ||rem == 9)) 
    	    return 0;
    }
    return 1;
}

int main(){
int i,n,sum=0;
scanf("%d", &n);
for(i = 1; i <= n; i++)
{
    if(check(i)) 
        sum++;
}
printf("%d", sum);
return 0;	
}