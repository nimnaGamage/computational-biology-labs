# '''
# modify fasta header
# 08/12/2023
# Nimna Gamage
# s14682
# Lab 01-Question2_Sub_question2
# '''

#define function
def modify_fasta_header(input_fasta, output_fasta):
    with open(input_fasta, 'r') as input_file, open(output_fasta, 'w') as output_file:
        for line in input_file:
            if line.startswith('>'):
                # Extract the part before the first comma
                header = line.strip().split(',')[0]
                output_file.write(f'{header}\n')
                print(f'{header}\n')
            else:
                output_file.write(line)

modify_fasta_header('dengue_1_envelop_gene_DNA_sequences.fasta', 'output_modified_header_dengue.fasta')
