import os

def transcripition(dna):
    result = dna
    for x in range(0, len(dna)):
        if (dna[x] == 'T'):
            result = result + 'A'

        if (dna[x] == 'A'):
            result[x] + 'U'
            
        if (dna[x] == 'C'):
            result[x] + 'G'

        if (dna[x] == 'G'):
            result[x] + 'C'

            
    for x in range(0, len(dna)):
        print(dna[x], end=' ')

    for x in range(0, len(dna)):
        print(result[x], end=' ')
    
if __name__ == "__main__":
    #TACCGGGACA CCTACGCGGA GGACGGGGAC GACCGCGACG ACCGGGAGAC CCCTGGACTG GGTCGGCGTC
    dna1, dna2, dna3, dna4, dna5, dna6, dna7 = input("Input DNA > ").split()
    print("[INFO] Start Transcripition...")
    transcripition(dna1)
