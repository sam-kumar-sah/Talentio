Question No: 4
Write a program to find the maximum element in each column of the matrix.
Sample testcases
Input 1
2
2
3 4
8 9
Output 1
8
9
Input 2
3
3
1 2 3
4 5 6
7 8 9
Output 2
7
8
9

===================================
solution: python
===================================
def maximum_col(a):
    aa=[]
    for i in range(m):
        col_max=0
        for j in range(n):
            if a[j][i]> col_max:
                col_max=a[j][i]
        print(col_max)
        #aa.append(col_max)
    #return aa

m=int(input())
n=int(input())
a=list()
for i in range(m):
    a.append(list(map(int,input().split()[:n])))
#print(maximum_col(a))
maximum_col(a)