Question No: 1
Shubham is given some data enclosed in a set and he is asked to find the leaders 
in the given data set. An element is leader if it is greater than all the elements 
to its right side. And the rightmost element is always a leader.

Input format
The first line consists of array size.
The second line consist of an array elements.
Output format
The output consists of an integer value .

Sample testcases
Input 1:
5
1 2 3 4 5
Output 1:
5 
Input 2:
5
1 2 3 8 6
Output 2:
6 8 

===================================
solution: python
===================================
#Time Complexity: O(n)

def leadersElem(a,n):
l=[]
Max=a[-1]
l.append(Max)
for i in range(n-2,-1,-1):
	if a[i]> Max:
		l.append(a[i])
		Max=a[i]
print(*l)

n=int(input())
a=list(map(int,input().split()[:n]))
leadersElem(a,n)


===========================
method-2: python
===========================
#Time Complexity: O(n*n)

def leadersElem(a,n):
    l=[]
    for i in range(n):
        for j in range(i+1,n):
            if a[i]<=a[j]:
                break
        if j==n-1:
            l.append(a[i])
    print(*sorted(l))

n=int(input())
a=list(map(int,input().split()[:n]))
leadersElem(a,n)