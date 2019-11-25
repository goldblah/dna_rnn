import sys

def encoding(files):
    import pandas as pd
    for file in files:
        test = pd.read_csv(file, index_col=0)
        test['SequenceCat'] = test['Gene Sequence'].str.replace('a', '0').str.replace('c', '1').str.replace('g','2').str.replace('t', '3').str.replace('A', '4').str.replace('C', '5').str.replace('G', '6').str.replace('T', '7')
        test.to_csv(path_or_buf=file)

def oneHotEncoding(files):
    import pandas as pd
    import numpy as np

    for file in files:
        test = pd.read_csv(file, index_col=0)
        ID2Char = ['a', 'c', 'g', 't', 'A', 'C', 'G', 'T', ]
        x_data = list(test['Gene Sequence'].str.lower())

        #print(x_data)
        one_hot_lookup = [[0, 0, 0, 1],  # a
                          [0, 0, 1, 0],  # t
                          [0, 1, 0, 0],  # c
                          [1, 0, 0, 0]]  # g

        one_hot = []

        for sequence in x_data:
            sequence = list(sequence)
            x_one_hot = [one_hot_lookup[0] if x == 'a' else one_hot_lookup[1] if x == 't' else one_hot_lookup[2] if x == 'c' else one_hot_lookup[3] for x in sequence]
            one_hot.append(x_one_hot)

        test['One Hot'] = one_hot

        print(test)

oneHotEncoding(['/Users/homeworkdude/Aedes_albopictus_genes.csv'])

def main(argv):
    for i,arg in enumerate(argv):
        print(i, arg)
    oneHotEncoding(argv)

if __name__ == '__main__':
    main(sys.argv[1:])