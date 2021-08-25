# DNA2mRNA2AUG
과학 수업에서 배우는 DNA 전사 과정과, 인슐린 번역 과정을 파이썬 코드를 활용하여 제작함. 

# Why did u made it?
사실 이 코드를 만든건 고등학교 1학년 때 과학 수업 시간에 배운 인슐린 번역 과정을 코드로 짜면 쉬울거 같아서 진행 했다. ~~가장 큰 이유는 선생님이 세특에 적어두신다고 했음~~. 무튼 파이썬을 통해서 직접 DNA 전사 과정을 진행 하게 되었다.

# Yo, wait for it. You need to tell what are thoes.
ㅇㅋ. 설명 들어간다.

일단 transcripition.py는 주 메인코드 이다. transcription.exe 파일은 transcripition.py코드를 exe로 변환한 파일이다. 해당 파일을 __굳이__ exe로 변환한 이유는 선생님 께서 파이썬 코드를 실행 할 수 없기 때문이다. 당연한 이유다. 과학 선생님이라도 각자마다 전공이 있는거닌까 ~~뭐가 되었던 나는 정말 윈도우가 싫다~~.

## How works it?
일단 DNA.txt 에다가 번역을 할 RNA를 작성한다. 
```txt
TACCGGGACA CCTACGCGGA GGACGGGGAC GACCGCGACG ACCGGGAGAC CCCTGGACTG GGTCGGCGTC
GGAAACACTT GGTTGTGGAC ACGCCGAGTG TGGACCACCT TCGAGAGATG GATCACACGC CCCTTGCTCC
GAAGAAGATG TGTGGGTTCT GGGCGGCCCT CCGTCTCCTG GACGTCCACC CCGTCCACCT CGACCCGCCC
CCGGGACCAC GTCCGTCGGA CGTCGGGAAC CGGGACCTCC CCAGGGACGT CTTCGCACCG TAACACCTTG
TTACGACATG GTCGTAGACG AGGGAGATGG TCGACCTCTT GATGACGTTG ATC

DNA.txt
```
이런식으로 작성을 하면 transcripition.py에서 읽어서 번역 결과 값을 출력해준다. exe 도 마찬가지이다. 뭐 당연한 얘기 이긴 하지만 exe 나 py 모두 DNA.txt가 없으면 안된다.

# How code works?
```python
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
```
file은 DNA.txt을 갖고 오고, dna에서 String으로 읽어준다. 그리고 dna를 먼저 출력 해주고 rna와 단백질 정보를 담을 String을 미리 생성해준다.
```python
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
```

위에서 읽어온 dna 정보를 rna에 변환하여 담아주는데 각 문자열 하나하나를 확인해 가면서 변환을 해주면 된다. 쉽다. __Easy__

```python
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
input("Press Enter to continue...")
```
rna_codon 는 각 RNA 정보를 해당 단백질로 변경을 해주는 것인데 어떤 단백질인지를 딕센너리로 정의를 해준다. 그러고 rna의 길이에서 3개씩 나뉘어서 3개씩 검사를 해주고 어떤 단백질이 들어가 있는지 출력을 해준다. 얼마나 깔-끔하고 펜-시한 프로그램인가.