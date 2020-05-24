problem:
----------------------------------
Ritish was a Store Incharge in a Phoneix Mall he was asked to create Codes for Perfumes
of various brands, as Ritish has less knowledge in generating codes can we help Ritish
In making Code for Perfumes Such that Print the Codes and its Sum for N codes

Program to print Series and it's sum till N terms.
First take number of codes, first code as well as common difference as input from 
Ritish using standard input function. Then we calculate the arithmetic series using 
above formula(by adding common difference to previous code) inside a for loop. We keep
on adding the current code value to sum variable.

Input format
Refer Sample Input

Output format
Refer Sample Output

Sample testcases
Input 1
5
2
4
Output 1
2 6 10 14 18 5 50
Input 2
3
1
1
Output 2
1 2 3 3 6

======================================
solution: python
======================================
t=int(input())
a=int(input())
b=int(input())
p=a 
c=0
for i in range(t):
    c=c+p 
    print(p)
    p=p+b 
print(t)
print(c)