#include<stdio.h>
#include"Cal.h"

int main(){
    int a, b, n, r, final_answer, choice;
   
    printf("\n 1 for Addition");
    printf("\n 2 for Subtraction");
    printf("\n 3 for Multiplication");
    printf("\n 4 for Division");
    printf("\n 5 for area of square");
    printf("\n 6 for area of circle");
    printf("\nEnter choice: ");
    scanf("%d", &choice);

    switch (choice){
        case 1:
            printf("enter a: ");
            scanf("%d", &a);
            printf("enter b: ");
            scanf("%d", &b);
            final_answer = add(a, b);
            printf("\nAddition: %d", final_answer);
            break;
           
        case 2:
            printf("enter a: ");
            scanf("%d", &a);
            printf("enter b: ");
            scanf("%d", &b);
            final_answer = sub(a, b);
            printf("\nSubtraction: %d", final_answer);
            break;
       
        case 3:
            printf("enter a: ");
            scanf("%d", &a);
            printf("enter b: ");
            scanf("%d", &b);
            final_answer = mul(a, b);
            printf("\nMultiplication: %d", final_answer);
            break;
       
        case 4:
            printf("enter a: ");
            scanf("%d", &a);
            printf("enter b: ");
            scanf("%d", &b);
            final_answer = div(a, b);
            printf("\nDivision: %d", final_answer);
            break;
       
        case 5:
            printf("enter n: ");
            scanf("%d", &n);
            final_answer = sqr(n);
            printf("\nArea of square: %d", final_answer);
            break;
       
        case 6:
            printf("enter r: ");
            scanf("%d", &r);
            final_answer = cir(r);
            printf("\nArea of circle: %d", final_answer);
            break;
       
        default:
            printf("Enter valid input");
    }      
    
    return 0;
}
