import sys


def finalDataPrep(csv_list):
    import pandas as pd
    import re
    name_grabber = re.compile(r'(.+)_(genes|lncRNA).csv')
    df_list_1000 = []
    df_list_750 = []
    df_list_500 = []
    
    for csv in csv_list:
        temp = pd.read_csv(csv, index_col = 0)
        temp['Organism Name'] = ' '.join(name_grabber.match(csv).group(1).split('_'))
        if 'genes' in csv:
            type = 'gene'
        else:
            type = 'lncRNA'
        csv1000 = temp[temp['Sequence Length'] == 1000].drop('Sequence Length', axis = 1)
        csv1000['Type'] = type 
        csv750 = temp[temp['Sequence Length'] == 750].drop('Sequence Length', axis = 1)
        csv750['Type'] = type
        csv500 = temp[temp['Sequence Length'] == 500].drop('Sequence Length', axis = 1)
        csv500['Type'] = type
        df_list_1000.append(csv1000)
        df_list_750.append(csv750)
        df_list_500.append(csv500)

    final_data_1000 = pd.DataFrame({
        'Gene Name': [],
        'Gene Location': [],
        'Gene Sequence': [],
        'Organism Name': [],
        'One Hot': [],
        'Type': []
        })

    for csv in df_list_1000:
        final_data_1000 = pd.concat([csv, final_data_1000])

    final_data_750 = pd.DataFrame({
        'Gene Name': [],
        'Gene Location': [],
        'Gene Sequence': [],
        'Organism Name': [],
        'One Hot': [],
        'Type': []
        })

    for csv in df_list_750:
        final_data_750 = pd.concat([csv, final_data_750])

    final_data_500 = pd.DataFrame({
        'Gene Name': [],
        'Gene Location': [],
        'Gene Sequence': [],
        'Organism Name': [],
        'One Hot': [],
        'Type': []
        })

    for csv in df_list_500:
        final_data_500 = pd.concat([csv, final_data_500])

    final_data_1000.to_csv(path_or_buf='all_genes_1000.csv')
    final_data_750.to_csv(path_or_buf='all_genes_750.csv')
    final_data_500.to_csv(path_or_buf='all_genes_500.csv')


def main(argv):
    finalDataPrep(argv)

if __name__ == "__main__":
    main(sys.argv[1:])

#finalDataPrep(['/Users/homeworkdude/Aedes_albopictus_genes.csv'])
