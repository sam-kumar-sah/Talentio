Question No: 4
I created my own text editor there are 3 types of Queries, 
1 : Append a given string s to the current string.
2 : Delete the last 'k' characters, K given.
3 : Print the current word on a newline

Input format
First line contains M, the number of queries, then there are M lines, 
Either: 1 s or 2 k or 3
where S is a string, K is a number
Output format
Print whenever the query 3 is given

Sample testcases
Input 1
5
1 abc
2 2
3
1 xy
3
Output 1
a
axy
Input 2
5
1 abc
2 2
3
1 oiu
3 2
Output 2
a
aoiu

================================
solution: python
================================
t=int(input())
ss=""
for i in range(t):
    st=input().split()
    n=int(st[0])
    
    if n==1:
        s=str(st[1])
        for i in range(len(s)):
            ss+=s[i] 
            
    elif n==2:
        k=int(st[1])
        ss=ss[:k-1]
        
    elif n==3:
        for i in range(len(ss)):
            print(ss[i],end="")
        

================================
solution: c language
================================
#include<stdio.h>
#include<string.h>
int cun[100000];


int main()
{
    int n;
    scanf("%d",&n);
    char a[10000];
    int k=0;
    int i,j;
    char s[10000];
    int temp;
    for(i=0;i<n;i++)
    {
        scanf("%d",&temp);
        if(temp==1){
            scanf(" %s",s);
            for(j=0;j<strlen(s);j++)
            {
                a[k++]=s[j];
            }
        }
        else if(temp==2)
        {
            scanf("%d",&temp);
            k-=temp;
        }
        else
        {
            for(j=0;j<k;j++)
            {
                printf("%c",a[j]);
            }
            printf("\n");
        }
    }
    return 0;
}
