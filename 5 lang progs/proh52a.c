#include <stdio.h>

int main(){
    printf("Enter lentgth: ");
    int length;
    scanf("%d", &length);

    printf("Enter width: ");
    int width;
    scanf("%d", &width);

    int area = length * width;
    printf("%d\n", area );

    int perim = 2 * length + 2 * width;
    printf("%d\n", perim );

    

}
/*
Enter lentgth: 2
Enter width: 2
4
8
*/