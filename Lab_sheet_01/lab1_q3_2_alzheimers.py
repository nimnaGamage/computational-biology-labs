'''
Find all articles related to Alzheimer’s in PubMed and print the total number of articles available and the authors
Output: The total number of articles related to Alzheimer’s available in PubMed and the authors
08/12/2023
Nimna Gamage
s14682
Lab 01-Question3_Sub_question2
'''

#import biopython sub-module
from Bio import Entrez

#provide email address to NCBI
Entrez.email = "nimnagamage65@gmail.com"

#query PubMed for all articles having to do with 'Alzheimer’s'
#checking how many such articles are there
handle = Entrez.egquery(term="Alzheimer’s")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"] == "pubmed":
        print("The total number of articles related to Alzheimer’s available in PubMed : ", row["Count"])

        handle = Entrez.esearch(db="pubmed", term="Alzheimer’s", retmax=row["Count"])
        record = Entrez.read(handle)
        handle.close()
        idlist = record["IdList"]


from Bio import Medline
handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = Medline.parse(handle)
records = list(records)
for record in records:
    print("title:", record.get("TI", "?"))
    print("authors:", record.get("AU", "?"))

