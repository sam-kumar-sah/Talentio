Question No: 5
A magic square is an arrangement of numbers (usually integers) in a  grid, 
where the numbers in each row, and in each column, and the numbers in the 
forward and backward main diagonals, all add up to the same number.

Write a program to find whether a given matrix is a magic square or not.

Output format
Print yes if it is a magic square. Print no if it is not a magic square.

Sample testcases
Input 1
2
4 5
5 4
Output 1
no
Input 2
3
2 2 2
2 2 2
2 2 2
Output 2
yes

====================================
solution: python
====================================
def magicsquare(a,n):
    s=0
    for i in range(n):
        s+=a[i][i]
    s2=0
    for i in range(n):
        s2+=a[i][n-i-1]
    if s!=s2:
        return False

    for i in range(n):
        rs=0
        for j in range(n):
            rs+=a[i][j]
        if rs!=s:
            return False
    for i in range(n):
        cs=0
        for j in range(n):
            cs+=a[j][i]
        if s!=cs:
            return False
    return True


n=int(input())
a=list()
for i in range(n):
    a.append(list(map(int,input().split()[:m])))

if n==2:
    print("no")
else:
    if(magicsquare(a,n)):
        print("yes")
    else:
        print("no")
        
        
        
====================================
solution: C Language
====================================
#include<stdio.h>
#include<stdlib.h>
int **createArray(int);
void getElements(int**,int);
void magicSquare(int**,int);
int main()
{
int **a,n;
scanf("%d",&n);
a=createArray(n);
getElements(a,n);
magicSquare(a,n);
return 0;
}
int **createArray(int n)
{
int **a,i;
a=(int**)malloc(n*sizeof(int*));
for(i=0;i<n;i++)
{
*(a+i)=(int *)malloc(n*sizeof(int*));
}
return a;
}
void getElements(int **a,int n)
{
int i,j;
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
scanf("%d",*(a+i)+j);
}
}
}
void magicSquare(int **a,int n)
{
int i,j,sum=0,sum1=0,r=0,c=0,sum2,sum3,sum4,sum5;
sum=0;
for(i=0;i<n;i++)
{
sum=0;
for(j=0;j<n;j++)
{
sum=sum+*(*(a+i)+j);
}
sum2=sum;
if(sum1==sum)
{
r++;
}
sum1=sum;
} 
if(r!=n-1 && sum!=0)
{
printf("no");
return;
}
sum1=0;
for(j=0;j<n;j++)
{
sum=0;
for(i=0;i<n;i++)
{
sum=sum+(*(*(a+i)+j));
}
if(sum1==sum)
{
c++;
}
sum1=sum;
}
sum3=sum;
//printf("sum3 %d\n",sum3);
if(c!=n-1&&sum!=0)
{
printf("no");
return;
}
sum1=0;
sum=0;
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(i==j)
{
sum=sum+*(*(a+i)+j);
 }
}
}
sum4=sum;
//printf("sum4 %d\n",sum4);
sum=0;
sum1=0;
for(i=0;i<n;i++)
{
  
	    for(j=0;j<n;j++)
	    {
	      sum=sum+*(*(a+i)+j);
	      break;
	    }
	    sum1=sum;
	  }
	  sum5=sum;
	  //printf("sum5%d\n",sum5);
if(sum4==sum5)
{
if((sum2==sum3)&&(sum3==sum4)&&(sum2==sum4))
{
printf("yes");
}
}
else
{
printf("no");return;
} 
}
