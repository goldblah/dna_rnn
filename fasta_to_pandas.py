import sys
    
def dataFrameGenerator(fasta_file_1000, fasta_file_750, fasta_file_500, output_loc = ''):
    #imports
    import Bio
    from Bio import SeqIO
    import pandas as pd
    import re

    #variable initialization
    organism_finder = re.compile(r'(.*)_output(_500|_750)?.fasta')
    seq1000 = list()
    seq500 = list()
    seq750 = list()
    seq_len = list()
    gene_name = list()
    gene_location = list()
    gene_seq = list()

    #finding pertinent information in each of the fasta files
    print('Parsing Fasta Files')
    for seq_record in SeqIO.parse(fasta_file_1000, "fasta"):
       seq1000.append((seq_record.id, seq_record.seq))

    for seq_record in SeqIO.parse(fasta_file_500, "fasta"):
        seq500.append((seq_record.id, seq_record.seq))

    for seq_record in SeqIO.parse(fasta_file_750, "fasta"):
        seq750.append((seq_record.id, seq_record.seq))

    #generating the final output
    print('Generating lists for DataFrame')
    for i in seq1000:
        seq_len.append(1000)
        gene_name.append(i[0].split(':')[0])
        gene_location.append(i[0].split(':')[1])
        gene_seq = i[1]

    for i in seq750:
        seq_len.append(750)
        gene_name.append(i[0].split(':')[0])
        gene_location.append(i[0].split(':')[1])
        gene_seq = i[1]

    for i in seq500:
        seq_len.append(500)
        gene_name.append(i[0].split(':')[0])
        gene_location.append(i[0].split(':')[1])
        gene_seq = str(i[1])

    print('Generating DataFrame')
    test_df = pd.DataFrame({
        'Sequence Length':seq_len,
        'Gene Name': gene_name,
        'Gene Location': gene_location,
        'Gene Sequence': gene_seq
    })

    file_name = output_loc + '/' + organism_finder.match(fasta_file_1000).group(1) + '_genes.csv'
    test_df.to_csv(path_or_buf=file_name)

def main(argv):
    for i,arg in enumerate(argv):
        print(i, arg)
    dataFrameGenerator(argv[0],argv[1],argv[2],argv[3])

if __name__ == '__main__':
    main(sys.argv[1:])
