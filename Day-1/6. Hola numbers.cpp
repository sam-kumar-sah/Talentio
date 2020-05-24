Question No: 6
Coding Type Question
Raichu is in love with Hola numbers! A positive integer x is called Hola if and only 
if there is no such positive integer a> 1 such that a^2 is a divisor of x.
Arceus has a number store! In his store, he has only divisors of positive integer n 
(and he has all of them). As a birthday present, Arceus wants to give her a Hola number
from his store. He wants this number to be as big as possible.
Arceus always had issues in math, so he asked for your help. Please tell him what is 
the biggest Hola number in his store.

Input format
The first and only line of input contains one integer, n (1 <= n <= 10^12).

Output format
Print the answer in one line.

Sample testcases
Input 1
10
Output 1
10
Input 2
8
Output 2
2

=============================
solution: c++ Language
=============================
#If u find solution in python mail me.
#samsahp9@gmail.com 

#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    long long int n,i;
    while(cin>>n)
    {
        for(i=2; i*i<=n; i++)
        {
            while(n%(i*i)==0)
            {
                n=n/i;
            }
        }
         cout<<n<<endl;

    }
}
