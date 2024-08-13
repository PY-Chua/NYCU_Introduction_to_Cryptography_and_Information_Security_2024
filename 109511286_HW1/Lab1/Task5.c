#include <stdio.h>
#include <stdlib.h>

#define LEN 32 // 256 bits

int main() {
    int i;
    unsigned char *key = (unsigned char *)malloc(sizeof(unsigned char) * LEN);
    
    FILE *random = fopen("/dev/urandom", "r");
    if (random == NULL) {
        fprintf(stderr, "Error opening /dev/urandom\n");
        return 1;
    }
    
    fread(key, sizeof(unsigned char) * LEN, 1, random);
    fclose(random);
    
    printf("Random key: ");
    for (i = 0; i < LEN; i++) {
        printf("%.2x", key[i]);
    }
    printf("\n");
    return 0;
}

