print("[INFO] Find Files...")

#DNA.txt File Open & Read
file = open('DNA.txt', 'r')
print("[INFO] Open ", file, " Text...") 
dna = file.read()
print("[INFO] Read ", file, " File...")

print("[Prnt] Start Show DNA...\n")
print("DNA :")
print (dna, "\n")

rna = ""
protein_string = ""

print("[INFO] Start Change DNA to mRNA(Transcripition)...")
for i in dna:
    if i == "T":
        rna += "A"

    if i == "A":
        rna += "U"

    if i == "C":
        rna += "G"

    if i == "G":
        rna += "C"

print("[Prnt] Start Show mRNA...\n")
print("mRNA :")
print(rna, "\n")

print("[.Set] Setup mRNA Codon Dictionary...\n")
rna_codon = {
    "UUU" : "페닐알라닌", "UUC" : "페닐알라닌", "UUA" : "류신", "UUG" :"류신",
    "CUU" : "류신", "CUU" : "류신", "CUC" : "류신", "CUA" : "류신", "CUG" : "류신",
    "AUU" : "아이소류신", "AUC" : "아이소류신", "AUA" : "아이소류신", "AUG" : "메싸이오닌(개시코돈)",
    "GUU" : "발린", "GUC" : "발린", "GUA" : "발린", "GUG" : "발린",
    "UCU" : "세린", "UCC" : "세린", "UCA" : "세린", "UCG" : "세린",
    "CCU" : "프롤린", "CCC" : "프롤린", "CCA" : "프롤린", "CCG" : "프롤린",
    "ACU" : "트레오닌", "ACC" : "트레오닌", "ACA" : "트레오닌", "ACG" : "트레오닌",
    "GCU" : "알라닌", "GCC" : "알라닌", "GCA" : "알라닌", "GCG" : "알라닌",
    "UAU" : "타이로신", "UAC" : "타이로신", "UAA" : "[종결코돈]", "UAG" : "[종결코돈]",
    "CAU" : "히스티딘", "CAC" : "히스티딘", "CAA" : "글루타민", "CAG" : "글루타민",
    "AAU" : "아스파라진", "AAC" : "아스파라진", "AAA" : "라이신", "AAG" : "라이신",
    "GAU" : "아스파트산", "GAC" : "아스파트산", "GAA" : "글루탐산", "GAG" : "글루탐산",
    "UGU" : "시스테인", "UGC" : "시스테인", "UGA" : "[종결코돈]", "UGG" : "트립토판", 
    "CGU" : "아르지닌", "CGC" : "아르지닌", "CGA" : "아르지닌", "CGG" : "아르지닌",
    "AGU" : "세린", "AGC" : "세린", "AGA" : "아르지닌", "AGG" : "아르지닌",
    "GGU" : "글라이산", "GGC" : "글라이신", "GGA" : "글라이신", "GGG" : "글라이신"
    }

for i in range(0, len(rna) - (3+len(rna)%3), 3):
    print(rna[i:i+3], " >> ",rna_codon[rna[i:i+3]],"\t")

print("[INFO] Closing File...")   
file.close()
