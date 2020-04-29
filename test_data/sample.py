import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report
import csv
import sys
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import operator

#get gene file first and make dataframe

text = []
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
with open('genes.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in spamreader:
        text.append(row)


genes = pd.DataFrame(text[0][0].split(","),columns=['sequence'])

genes['is_gene'] = 1

#get random sequences file and make dataframe

text = []
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
with open('random.csv') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=',')
    text = list(spamreader)

random = pd.DataFrame(str(text[0]).split(','),columns=['sequence'])
random['sequence'] = random['sequence'].str.strip('\\n')
random['sequence'] = random['sequence'].replace(r'\\n','',regex=True)
random['sequence'] = random['sequence'].replace(r'\[','',regex=True)
random['sequence'] = random['sequence'].replace(r'\]','',regex=True)
random['sequence'] = random['sequence'].replace(r"'","",regex=True)
random['is_gene'] = 0


df = genes.append(random)



def string_to_array(seq_string):
    #seq_string = seq_string.lower()
    seq_string = re.sub('[^acgtACTGN]', 'z', seq_string)
    seq_string = np.array(list(seq_string))
    return seq_string# create a label encoder with 'acgtn' alphabet

label_encoder = LabelEncoder()
label_encoder.fit(np.array(['a','c','g','t','A','C','G','T','N','z']))

def ordinal_encoder(my_array):
    integer_encoded = label_encoder.transform(my_array)
    float_encoded = integer_encoded.astype(float)
    float_encoded[float_encoded == 0] = 0.25 # a
    float_encoded[float_encoded == 1] = 0.50 # c
    float_encoded[float_encoded == 2] = 0.75 # g
    float_encoded[float_encoded == 3] = 1.00 # t
    float_encoded[float_encoded == 4] = 1.25 # A
    float_encoded[float_encoded == 5] = 1.50 # C
    float_encoded[float_encoded == 6] = 1.75 # G
    float_encoded[float_encoded == 7] = 2.00 # T
    float_encoded[float_encoded == 8] = 2.25 # N
    float_encoded[float_encoded == 9] = 0 # everything else
    return float_encoded


ordinal = []
for sequence in df.sequence:
    ordinal.append(ordinal_encoder(string_to_array(sequence)))

df_or = pd.DataFrame(data=ordinal)

label = df['is_gene'].values
df_or['is_gene'] = label

df_or = df_or.fillna(0)

X = df_or.drop(columns=['is_gene'])
y = df_or['is_gene']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)


models = [LogisticRegression(),KNeighborsClassifier()]
lr_params = {
        'C':[0.005],
        'max_iter':[50000],
        'solver':['newton-cg','lbfgs'],
        'random_state':[42]
        }
knn_params = {
        'n_neighbors':[6]
        }


params = [lr_params,knn_params]

def crunch(model,params,x_tr,y_tr,x_te,y_te):
    grid = GridSearchCV(model,params,verbose=3,cv=5)
    grid.fit(x_tr,y_tr)
    print(grid.best_params_,grid.best_score_)
    pred = grid.predict(x_te)
    print(accuracy_score(y_te,pred))
    print(confusion_matrix(y_te,pred))
    print(classification_report(y_te,pred))

for model,param in zip(models,params):
    crunch(model,param,x_train,y_train,x_test,y_test)




