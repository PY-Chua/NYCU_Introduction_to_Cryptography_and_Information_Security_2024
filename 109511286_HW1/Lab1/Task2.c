#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define KEYSIZE 16

#define START 1524013729
#define END 1524020929

void main()
{
    int i;
    time_t t;
    char key[KEYSIZE];
    
    FILE *f;
    f = fopen("key.txt", "w");
    
    for (t = START; t < END; t++)
    {
        srand((unsigned)t);

        for (i = 0; i < KEYSIZE; i++)
        {
            key[i] = rand() % 256;
            fprintf(f, "%.2x", (unsigned char)key[i]);
        }
        fprintf(f, "\n");
    }
}
