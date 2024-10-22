# '''
# predict TFBS
# 08/12/2023
# Nimna Gamage
# s14682
# Lab 01-Question2_Sub_question3
# '''
#
# #method 1
#
# import re
#
# filename = "search_seq.fasta"
# tf = "TGIF1"
# header = ""
# sequence = ""
#
# with open(filename, 'r') as file:
#     for line in file:
#         if line != '\n':
#             if '>' in line:
#                  header += line
#             else:
#                 sequence += line
#
#
# matches = re.finditer("[AT]GACAG[CGT]", sequence)
#
# print("The header of the searched fasta sequence: ", header)
# print("The transcription factor: ", tf)
# print("Matched positions; ")
#
# for match in matches:
#     start, end = match.start(), match.end()
#     matched_sequence = sequence[start:end]
#     print(f"    The matched position: {start}-{end}     The matched sequence: {matched_sequence}")


###method 2

#define function
def read_code_representations(code_file):
    code_representations = {}
    with open(code_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                code, description = parts[0], ' '.join(parts[1:])
                code_representations[code] = description
    return code_representations

#define function
def search_tfbs(sequence, tfbs, code_representations):
    positions = []
    for i in range(len(sequence) - len(tfbs) + 1):
        match = True
        for j in range(len(tfbs)):
            current_nucleotide = sequence[i + j]
            if current_nucleotide not in code_representations[tfbs[j]]:
                match = False
                break
        if match:
            positions.append((i, i + len(tfbs)))
    return positions

##main
if __name__ == "__main__":
    code_file = "code_represents.txt"
    sequence_file = "search_seq.fasta"

    #transcription factor binding sites
    tfbs_name = "RUNX1"
    tfbs_sequence = "BHTGTGGTYW"

    #code representations
    code_representations = read_code_representations(code_file)

    # Read DNA sequence by opening file
    with open(sequence_file, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip()
        sequence = "".join(line.strip() for line in lines[1:])

    # Search for TFBS positions with the binding site pattern for RUNX1
    tfbs_positions = search_tfbs(sequence, tfbs_sequence, code_representations)

    # Print results
    print(f"The header of the searched fasta sequence: {header}")
    print(f"{tfbs_name} TFBS positions:")
    for start, end in tfbs_positions:
        binding_site = sequence[start:end]
        print(f"    The matched position: {start}-{end}    The matched sequence: {binding_site}")

