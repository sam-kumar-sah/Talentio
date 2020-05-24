Question No: 7
---------------------------
In this problem, you need to print the pattern of the following form 

Sample testcases
Input 1
5
Output 1
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5 

====================================
solution: python
====================================
def pattern(n):
    ps=n*2-1
    res=[[0 for i in range(ps)]
            for j in range(ps)]
    
    for i in range(ps):
        for j in range(ps):
            if abs(i-(ps//2))> abs(j-(ps//2)):
                res[i][j]=abs(i-(ps//2))+1
            else:
                res[i][j]=abs(j-(ps//2))+1 
    
    for i in range(ps):
        for j in range(ps):
            print(res[i][j],end=" ")
        print()

n=int(input())
pattern(n)
