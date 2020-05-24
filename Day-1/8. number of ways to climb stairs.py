Question No: 8
---------------------------------
Coding Type Question
You have N steps to climb .
You can either take one step or two steps at a time .

You need to find the total number of ways you can reach N steps .
Explanation :
For N=4 , You can either reach 4 steps in following ways
->1111
->112
->121
->211
->22
So total number of ways is 5
Sample testcases
Input :4
Output :5

Input :  6
Output : 13

=========================================
solution: python
=========================================
def fib(n):
    if n<=1:
        return 1 
    return fib(n-1)+fib(n-2)
    
n=int(input())
print(fib(n))