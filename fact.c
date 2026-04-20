#include <stdio.h>
#include "fact.h"

int main() {
    int n;
   
    printf("Enter a number: ");
    scanf("%d", &n);
    if (n < 0) {
        printf("Factorial of negative numbers doesn't exist.\n");
    } else {
        printf("Factorial of %d is: %lld\n", n, FACTORIAL(n));
    }

    return 0;
}
