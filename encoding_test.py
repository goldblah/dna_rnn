import sys
def encoding(files):
    import pandas as pd
    for file in files:
        test = pd.read_csv(file, index_col=0)
        test['SequenceCat'] = test['Gene Sequence'].str.replace('a', '0').str.replace('c', '1').str.replace('g','2').str.replace('t', '3').str.replace('A', '4').str.replace('C', '5').str.replace('G', '6').str.replace('T', '7')
        test.to_csv(path_or_buf=file)

def main(argv):
    for i,arg in enumerate(argv):
        print(i, arg)
    encoding(argv)

if __name__ == '__main__':
    main(sys.argv[1:])