# DNA2mRNA2AUG
과학 수업에서 배우는 DNA 전사 과정과, 인슐린 번역 과정을 파이썬 코드를 활용하여 제작함. 

# Why did u made it?
사실 이 코드를 만든건 고등학교 1학년 때 과학 수업 시간에 배운 인슐린 번역 과정을 코드로 짜면 쉬울거 같아서 진행 했다. ~~가장 큰 이유는 선생님이 세특에 적어두신다고 했음~~. 무튼 파이썬을 통해서 직접 DNA 전사 과정을 진행 하게 되었다.

# Yo, wait for it. You need to tell what are thoes.
ㅇㅋ. 설명 들어간다.

일단 transcripition.py는 주 메인코드 이다 ~~(사실 당연한 얘기)~~. transcription.exe 파일은 transcripition.py코드를 exe로 변환한 파일이다. 해당 파일을 __굳이__ exe로 변환한 이유는 선생님 께서 파이썬 코드를 실행 할 수 없기 때문이다. 당연한 이유다. 과학 선생님이라도 각자마다 전공이 있는거닌까 ~~뭐가 되었던 나는 정말 윈도우가 싫다~~.

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