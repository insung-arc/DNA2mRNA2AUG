#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char result[100] = { '\0' };

int transcription(char dna[]){
    int dnaLengs = strlen(dna);
    for (int i = 0; dna[i] != '\0'; i++) {
        switch(dna[i]) {
            case 'T':
                result[i] = 'A';
                printf("%c", result[i]);
                break;
            case 'A':
                result[i] = 'U';
                printf("%c", result[i]);
                break;
            case 'G':
                result[i] = 'C';
                printf("%c", result[i]);
                break;
            case 'C':
                result[i] = 'G';
                printf("%c", result[i]);
                break;
        }
    }
    return dnaLengs;
}

int main() {
    char result[100] = { '\0' };
    char dna[100] = { '\0' };

    printf("Input DNA\n>>> "); 
    gets(dna);
    transcription(dna);

    for (int i = 0; dna[i] != '\0'; i++) {
        printf("%c", result[i]);
        if (i % 3 == 0) {
            printf(" ");
        }
    }

    return 0;
}