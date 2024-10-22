# '''
# Extract sample names
# 08/12/2023
# Nimna Gamage
# s14682
# Lab 01-Question2_Sub_question1
# '''
#
# #method 1
#
# #define function
# def extract_sample_name(file_name):
#     # Split the file name using underscores
#     parts = file_name.split('_')
#
#     # Check the file name for the expected format
#     if len(parts) >= 5 and parts[0].startswith('lane') and parts[-1].endswith('.fastq.gz'):
#         # Extract the sample name from the appropriate position
#         sample_name = parts[2:-2]
#
#         # Join parts[2:] to handle cases where the sample name contains underscores
#         return '_'.join(sample_name)
#     else:
#         return None
#
#
# # List of given file names
# file_names = [
#     "lane1_NewCode_L001_R1.fastq.gz",
#     "lane1_NoIndex_L001_R1.fastq.gz",
#     "lane1_NoIndex_L001_R2.fastq.gz",
#     "pipeline_processing_output.log",
#     "lane7027_ACTGAT_JH25_L001_R1.fastq.gz",
#     "lane7027_ACTTGA_E30_1_2_Hap4_24h_L001_R1.fastq.gz",
#     "lane7027_AGTTCC_JH14_L001_R1.fastq.gz",
#     "lane7027_CGGAAT_JH37_L001_R1.fastq.gz",
#     "lane7027_GCCAAT_E30_1_2l_Hap4_log_L001_R1.fastq.gz",
#     "lane7127_GGCTAC_E30_1_4_Hap4_48h_L001_R1.fastq.gz"
# ]
#
# # Extract and print sample names
# for file_name in file_names:
#     sample_name = extract_sample_name(file_name)
#     if sample_name is not None:
#         print(f"File: {file_name}, Sample Name: {sample_name}")
#


#method 2 - using regulare expressions

import re

#define function
def extract_sample_name(file_name):
    # Define the pattern for matching the desired format
    pattern = re.compile(r'^lane\d+_[A-Z0-9]+_([A-Za-z0-9_]+)_L\d+_[R]\d\.fastq\.gz$')

    # Attempt to match the pattern with the file name
    match = pattern.match(file_name)

    # If there is a match, return the extracted sample name
    if match:
        return match.group(1)
    else:
        return None

# Read file names from a text file
file_names_file = "file_names.txt"
output_file_path = "output_sample_names.txt"

#open the text file
with open(file_names_file, "r") as file:
    file_names = file.read().splitlines()

# Extract and write sample names to an output file
with open(output_file_path, "w") as output_file:
    for file_name in file_names:
        sample_name = extract_sample_name(file_name)
        if sample_name is not None:
            output_file.write(f"File: {file_name}, Sample Name: {sample_name}\n")

print("Output written to", output_file_path)
