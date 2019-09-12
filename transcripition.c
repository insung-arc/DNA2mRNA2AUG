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
                break;
            case 'A':
                result[i] = 'U';
                break;
            case 'G':
                result[i] = 'C';
                break;
            case 'C':
                result[i] = 'G';
                break;
            default:
                printf("PROGRAM HAS SOME PROBLEM.\nEXIT_CODE.\n");
//                exit(1);
        }
    }
    return dnaLengs;
}

int main() {
    char result[100] = { '\0' };
    char dna[100] = { '\0' };

    printf("Input DNA\n>>> "); 
    gets(dna);
    int lensDNA = transcription(dna);

    for (int i = 0; i <= lensDNA; i++) {
        printf("%s", result);
    }
    return 0;
}