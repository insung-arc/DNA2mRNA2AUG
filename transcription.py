import os

whatisthis = {'A' : 'U', 'T' : 'A', 'G' : 'C', 'C' : 'G'}

def transcripition(dna):
    result = dna
    for x in range(0, len(dna)):
        if (result == 'T'):
            print(whatisthis[result], end=' ')

        if (dna[:x] == 'A'):
            print(whatisthis[result], end=' ')
            
        if (dna[:x] == 'C'):
            print(whatisthis[result], end=' ')

        if (dna[:x] == 'G'):
            print(whatisthis[result], end=' ')

            
    for x in range(0, len(dna)):
        print(dna[x], end=' ')

    for x in range(0, len(dna)):
        print(result[x], end=' ')
    
if __name__ == "__main__":
    #TACCGGGACA CCTACGCGGA GGACGGGGAC GACCGCGACG ACCGGGAGAC CCCTGGACTG GGTCGGCGTC
    dna1, dna2, dna3, dna4, dna5, dna6, dna7 = input("Input DNA > ").split()
    print("[INFO] Start Transcripition...")
    transcripition(dna1)
    transcripition(dna2)
    transcripition(dna3)
    transcripition(dna4)
    transcripition(dna5)
    transcripition(dna6)
    transcripition(dna7)