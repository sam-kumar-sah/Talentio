Question No: 4
Coding Type Question
You live on the first floor, the way to the first floor is only through the
stairs, there are exactly N stairs. You having long legs, can either step on 
the next stair, or skip it. You obviously start at the ground, below the first 
stair. 
One day, your friend challenges you, how many days can you go home, climbing 
the stairs in a unique way every time.
Formally, the question is, how many days can you climb the stairs in a unique 
way?

Input format
One number N

Output format
The number of days you can go home in a unique way

Sample testcases
Input 1
6
Output 1
13 
Input 2
9
Output 2
55 
====================================
solution-1: python
====================================
def fib(n):
    if n<=1:
        return 1 
    return fib(n-1)+fib(n-2)

n=int(input())
print(fib(n))
