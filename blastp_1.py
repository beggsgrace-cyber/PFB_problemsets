#!/usr/bin/env python3

import sys



def collect_info(length_of_seq, matrix):
    matrix_dict = {}
    parts = []
    field_names = []
    with open(f'blast_{length_of_seq}_v_qfo_{matrix}.txt', 'r') as file1:
        for line in file1:
            line = line.rstrip()
            if '# Fields' in line:
                field_names = line.split(',')
            if '#' not in line:
                parts = line.split('\t')
                matrix_dict[matrix] = dict(zip(field_names, parts))
                break
    return matrix_dict



def main():
    length_of_seq = sys.argv[1]
    blosum62_dict = collect_info(length_of_seq, 'BLOSUM62')
    blosum80_dict = collect_info(length_of_seq, 'BLOSUM80')
    pam30_dict = collect_info(length_of_seq, 'PAM30')
    pam70_dict = collect_info(length_of_seq, 'PAM70')
#make all the dictionaries for one sequence length

#see solution on website for looking at median --> should be around 1

#print alignment length, percent identity, evalue for each
    print(f'Matrix  \talen\t%id\tevalue\nBLOSUM62\t{blosum62_dict['BLOSUM62'][' alignment length']}\t{blosum62_dict['BLOSUM62'][' % identity']}\t{blosum62_dict['BLOSUM62'][' evalue']}\nBLOSUM80\t{blosum80_dict['BLOSUM80'][' alignment length']}\t{blosum80_dict['BLOSUM80'][' % identity']}\t{blosum80_dict['BLOSUM80'][' evalue']}\nPAM70   \t{pam70_dict['PAM70'][' alignment length']}\t{pam70_dict['PAM70'][' % identity']}\t{pam70_dict['PAM70'][' evalue']}\nPAM30   \t{pam30_dict['PAM30'][' alignment length']}\t{pam30_dict['PAM30'][' % identity']}\t{pam30_dict['PAM30'][' evalue']}')

if __name__ == '__main__':
    main()