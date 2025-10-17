#!/usr/bin/env python3
list_all = []
list_pigment = []
list_stemcellprolif = []
list_TF = []

#make set for all ferret genes
with open("ferret_all_genes.tsv", "r") as f_all:
    for line in f_all:
        line = line.rstrip()
        if 'Gene stable ID' not in line:
            list_all.append(line)
set_all = set(list_all)

#make set for pigment ferret genes
with open("ferret_pigmentation_genes.tsv", "r") as f_pigment:
    for line in f_pigment:
        line = line.rstrip()
        if 'Gene stable ID' not in line:
            list_pigment.append(line)
set_pigment = set(list_pigment)

#make set for stem cell proliferation ferret genes
with open("ferret_stemcellproliferation_genes.tsv", "r") as f_scp:
    for line in f_scp:
        line = line.rstrip()
        if 'Gene stable ID' not in line:
            list_stemcellprolif.append(line)
set_stemcellprolif = set(list_stemcellprolif)

#all genes that are not stem cell proliferation genes
not_scp = set_all - set_stemcellprolif

#genes that are both stem cell proliferation and pigmentation genes
pigment_and_scp = set_pigment & set_stemcellprolif
print(f' genes that are both pigment and stem cell prolif: {pigment_and_scp}')

#make set for transcriptionFactor ferret genes
with open("ferret_transcriptionFactors.tsv", "r") as f_TF:
    for line in f_TF:
        line = line.rstrip()
        if 'Gene stable ID' not in line:
            list_TF.append(line)
set_TF = set(list_TF)

# all genes that are TFs and that are involved in stem cell prolif
set_TF_scp = set_TF & set_stemcellprolif
print(set_TF_scp)