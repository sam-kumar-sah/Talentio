Question No: 5
Coding Type Question
In a defense research laboratory a group of scientist has decided to 
design a military communication system which accepts a single input from 
the employee at base camp and returns the coded format of the given single
input to their higher officials at the military head quarters 
i.e. the coded format representation of the given input may be in one of 
the regular formats which we use in our number systems.


Your task is develop a program for the scenario.

Input format
Read a number

Output format
Display the coded number

Sample testcases
Input 1
4
Output 1
Equivalent code: 4
Input 2
12
Output 2
Equivalent code: 14

==================================
solution: python
==================================
def codeNum(n):
    s,k=0,1 
    while(n!=0):
        s+=(n%8)*k 
        n//=8 
        k=k*10
    return s 
    
n=int(input())
print("Equivalent code: ", codeNum(n))
