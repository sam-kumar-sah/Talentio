Question No: 3
Design a way to sort a list of positive integers in descending order 
based on the frequency of elements.

Input format
Input consists of two arguments
Size – no of elements
Arr – list of positive integers
Output format
Return a list of positive integers sorted according to the frequency of elements

Sample testcases
Input 1: 10
6 6 6 6 3 3 3 2 1 1
Output 1: 6666333112

Input 2: 19
1 2 2 3 3 3 4 4 5 5 5 5 6 6 6 7 8 9 10
Output 2: 55553336662244910178

============================
solution: python
============================

def sort_freq(l):
    ss=''
    l1=sorted(l)
    s=sorted(l1,key=l1.count,reverse=True)
    for i in s:
        ss+=str(i)
    return ss

n=int(input())
l=list(map(int,input().split()[:n]))
print(sort_freq(l))
