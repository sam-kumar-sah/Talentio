Question No: 2
Given an array with possibly duplicate elements the task is to find the index of the first and last occurrences of an element x in the given array.(Note: If there are no duplicate elements, print the index of the given element. If the element doesn't exist in the array, print "not found") 

Input format
The first line consist of an integer to give the number of elements to array.
The second line consist of an integer array .
The third line consist of an integer which is duplicate element. 

Output format
The output consists of integers , which represent the indexes of duplicate element.
Code constraints
1 <= N<= 100

Sample testcases
Input 1:
6
1 2 3  4 5 3
3
Output 1:
2
5
Input 2:
4
1 2 3 4
5
Output 2: not found


========================
solution :python
========================
n=int(input())
a=list(map(int,input().split()[:n]))
k=int(input())
l=[]
for i in range(n):
    if a[i]==k:
        l.append(i)
if len(l)==0:
    print("not found")

elif len(l)==1:
    print(l[0])

elif len(l)==2:
    print(l[0])
    print(l[-1])

