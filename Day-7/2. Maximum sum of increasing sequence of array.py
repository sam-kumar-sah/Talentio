Question No: 2
Sindhu has set of numbers which are placed in an order. Sindhu needs our 
help in finding the maximum sum formed by the elements of the array in the 
increasing sequence of the given elements.

Input format
The first line consist of size of the array.
The second line consist of an array elements.
Output format
The output consists of an integer value .

Sample testcases
Input 1
5
1 2 3 4 5
Output 1
15
Input 2
7
1 101 2 3 100 4 5
Output 2
106

==============================
solution: python
==============================

def sumLIS(l):
    dp = [0] * len(l)
    max = 0
    for i in range(len(l)):
        dp[i] = l[i]
    for i in range(1, len(l)):
        for j in range(i):
            if (l[i] > l[j] and dp[i] < dp[j] + l[i]):
                dp[i] = dp[j] + l[i]
    for i in range(n):
        if max < dp[i]:
            max = dp[i]
    return max

n = int(input())
l = list(map(int, input().split()[:n]))
#print(str(sumLIS(l)))
k=sumLIS(l)     #function call should be stored in variable
print(k)        #Then print variable