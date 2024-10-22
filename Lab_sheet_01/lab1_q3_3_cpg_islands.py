# '''
# find CpG islands
# 08/12/2023
# Nimna Gamage
# s14682
# Lab 01-Question3_Sub_question3
# '''

#import modules
from Bio.SeqUtils import nt_search

#define function
def find_cpg_islands(dnaSequence, min_cpg_length=200, cpg_obs_exp_ratio=0.5):

    cpg_islands = []
    window_size = min_cpg_length

    for i in range(len(dnaSequence) - window_size + 1):
        sub = dnaSequence[i:i + window_size].upper()
        count_CG = sub.count('G') + sub.count('C')
        content_of_CG = count_CG / window_size
        obs = nt_search(sub, 'CG')

        if content_of_CG >= cpg_obs_exp_ratio and obs:
            cpg_islands.append((i, i + window_size))

    return cpg_islands


# given dna sequence
given_sequence = "CGCGCGCGCGCGCCGGCGCGCGCGCGCGCGCGCGCATATATATATAGATAGATAGTAGCGCGCGCGCGCGCCGGCGCGCGCGCGCGCGCGCGCGGCGCGCGCGCGCGCCGGCGCGCGCGCGCGCGCGCGCGGCGCGCGCGCGCGCGCGCGCGGCGCGCGCGCGCGCGCGCGCGATCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGATCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCG"

islands_cpg = find_cpg_islands(given_sequence)

#print each cpg island
print("CpG Islands : ")
for start, end in islands_cpg:
    print(f"Start position: {start}, end position : {end}")

