#include <stdio.h>
int isMultipleOfSeven(int num) {
    return (num % 7 == 0);
}

int main() {
    printf("Cac so nguyen co 2 chu so va la boi cua 7 la:\n");
    
    for (int i = 10; i < 100; i++) {
        if (isMultipleOfSeven(i)) {
            printf("%d ", i);
        }
    }

    return 0;
}
