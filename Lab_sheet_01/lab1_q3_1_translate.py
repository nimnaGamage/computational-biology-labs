'''
asks the user to input a DNA-sequence and then translates the sequence to protein sequence
Input: DNA-sequence
Output: The translated protein sequence
08/12/2023
Nimna Gamage
s14682
Lab 01-Question3_Sub_question1
'''

#import biopython sub-module
from Bio.Seq import Seq

#get the user input
dna_seq = input("Enter the DNA-sequence : ")

#create the biopython Seq object from the entered sequence
dna_sequence = Seq(dna_seq)

#translate the DNA sequence to protein sequence until it encounters a stop codon
protein_sequence = dna_sequence.translate(to_stop=True)

#print the output
print("\nThe entered DNA-sequence by the user : ", dna_seq)
print("The translated protein sequence : ", protein_sequence)
