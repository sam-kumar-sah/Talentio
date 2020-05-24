problem:
--------------------------------------------------
Chandu has recently entered the Bihar State University for Competitive Programming . 
Chandu has a friend Anuj who has also entered the university. Now they are moving 
into a dormitory.
Chandu and Anuj want to live in the same room. The dormitory has n rooms in total. 
At the moment the i-th room has pi people living in it and the room can accommodate 
qi people in total (pi ≤ qi). Your task is to count how many rooms has free place for 
both Chandu and Anuj.

Input format
The first line contains a single integer n (1 ≤ n ≤ 100) — the number of rooms.
The i-th of the next n lines contains two integers pi and qi (0 ≤ pi ≤ qi ≤ 100) — the number of people who already live in the i-th room and the room's capacity.

Output format
Print a single integer — the number of rooms where Chandu and Anuj can move in.

Sample testcases
Input 1
3
1 2
2 3
3 4
Output 1
0
Input 2
3

21 71

10 88

43 62
Output 2
3

==================================
solution: python
==================================
n=int(input())
c=0
while(n):
    p,q=map(int,input().split())
    if q-p>=2:
        c+=1
    n-=1 
print(c)