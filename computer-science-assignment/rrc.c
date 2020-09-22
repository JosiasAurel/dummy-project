#include <stdio.h>

int main(void) {
    int l, w, a;

    printf("Enter the length of the rectangle ");
    scanf("%d", &l);
    printf("Enter the width of the rectangle ");
    scanf("%d", &w);
    a = l*w;

    printf("The area of the rectangle is : %d", a);

    return 0;
}