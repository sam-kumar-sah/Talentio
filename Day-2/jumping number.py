Question No: 1 
#Jumping Numbers
'''
Coding Type Question
Given a positive number X. Find all Jumping Numbers smaller than or equal to X.

Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7,8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Input format
The first line of the input contains T denoting the number of test cases. Each test case contain a positive number X

Output format
Output all the jumping numbers less than X in sorted order. Jump to example for better understanding.

Sample testcases
Input 1
2
10
50
Output 1
0 1 2 3 4 5 6 7 8 9 10 
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45 
'''

===================================
solution: python
===================================
def jump(x,jnum,num):
    l=[]
    if x>num:
        return 0 
    if jnum==0:
        print(x,end= " ")
        return 1 
    t=x%10
    f=0
    if t>0:
        f=jump(x*10+(t-1),jnum-1,num)
    if t<9:
        f=jump(x*10+(t+1),jnum-1,num)
    return f 
    

t=int(input())
while(t):
    f,jnum=1,0 
    num=int(input())
    print(0)
    while(f):
        for i in range(0,10):
            f=jump(i,jnum,num)
        jnum+=1 
    print()
    t-=1 