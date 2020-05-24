Question No: 3
Coding Type Question
Write a program which prints 'YES' if the number is a left truncatable 
prime else 'NO'

Explanation:
In number theory, a left-truncatable prime is a prime number which, in a given 
base, contains no 0s, and if the leading ("left") digit is successively removed, 
then all resulting numbers are primes. 
For example 9137 is a left-truncatable prime, since 9137, 137, 37 and 7 
are all prime.1013 is not a left-truncatable prime, as it contains a digit 0.



Note: 

1) Implement a function called 'int sroot(int n)' which can return the 
integer square root of the given parameter n.
2) Implement a function called 'int power(int x, int n)' which can 
return the x^n for the given parameters x and n.

Sample testcases
Input 1
9173
Output 1
YES
Input 2
9991
Output 2
0

=============================
solution: C Language
=============================
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

int sroot(int n) {
    int i;
    for (i = 1; i * i <= n; i++);
    return i - 1;
}

int power(int x, int n) {
    int p = 1;
    for(;n > 1; --n)
        p *= x;
    return p;
}

bool isPrime(int n) {
    int m = sroot(n);
        for (int i = 2; i <= m; ++i) {
            if (!(n%i)) 
                return false;
        }
    return true;
}

int numOfDigits(int n) {
    char st[100];
    int digits = sprintf(st,"%d",n);
    if (strchr(st, '0')) 
        return 0;
    else 
        return digits;
}

bool isLeftTruncatablePrime(int n) {
    int digits = numOfDigits(n);
    if (digits == 0) 
        return false;
    int divisor = power(10, digits);
    int i;
    for (i = 0; i < digits; ++i, divisor /= 10) {
        if (!isPrime(n % divisor)) {
            break;
        }
    }
    return i == digits;
}

int main() {
    int n;
    scanf("%d", &n);
    if (isLeftTruncatablePrime(n)) {
        printf("1\n");
    } else {
        printf("0\n");
    }
    return 0;
}
