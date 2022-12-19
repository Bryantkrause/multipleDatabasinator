import pandas as pd
import numpy as np


# set columna that actually matter
columnsToUse = [
    'Acct','Type','Date','Num','Name','Memo','Class','Debit','Credit'
]

# open file
file = r'C:\Users\bkrause\Documents\RawDataInatorMachineLearningInator.csv'
# convert file to data frame
df = pd.read_csv(file, parse_dates=['Date'], usecols=columnsToUse)
# update null values to 0
df = df.fillna(0)

# create new column to see actual amount
df['Actual'] = df['Debit'] - df['Credit']
data = df.drop(columns=['Debit', 'Credit'])

# data check1 convert vague data names to actual locations based on NAME
conditionsName = [
    data['Name'].str.contains(r'CLI - CONTROL ACCOUNT', na=False),
    data['Name'].str.contains(r'WESTSET DISTRIBUTION INC.', na=False),
    data['Name'].str.contains(r'TOTAL', na=False),
    data['Name'].str.contains(r'INTERCOMPANY - SHARED', na=False),
    data['Name'].str.contains(r'WESTSET DISTRIBUTION INC. - 16107', na=False),
    data['Name'].str.contains(r'WESTSET DISTRIBUTION - 11937', na=False),
    data['Name'].str.contains(r'RANCHO CUCAMONGA CHAMBER OF COMMERCE', na=False),
    data['Name'].str.contains(r'HUGO GALINDO', na=False)

]
# choicesName = [
#     'Total', 'Fullerton', 'Total', 'Share', 'Cerritos', 'Downey', 'Total', 'Total'
# ]
choicesName =[
    'Total', 'Warehouse', 'Total', 'Share', 'Warehouse', 'Warehouse', 'Total', 'Total'
]
data['LocationName'] = np.select(conditionsName, choicesName, default='NA')

# data check 2 based on class

conditionsClass = [
    data['Class'].str.contains(r'000100 - Trans & Whse', na=False),
    data['Class'].str.contains(r'000100.1 - Transportation', na=False),
    data['Class'].str.contains(
        r'000100.1 - Transportation:000106 - Dispatch', na=False),
    data['Class'].str.contains(
        r'000100.1 - Transportation:000107 - Sales', na=False),
    data['Class'].str.contains(
        r'000100.1 - Transportation:000109 - Trans Cust Serv', na=False),
    data['Class'].str.contains(
        r'000100.1 - Transportation:000111 - Nightdock', na=False),
    data['Class'].str.contains(
        r'000100.1 - Transportation:000113 - Drivers', na=False),
    data['Class'].str.contains(r'000100.2 - Warehouse & Logistic', na=False),
    data['Class'].str.contains(
        r'000100.2 - Warehouse & Logistic:000105 - Warehouse - 1st Shift', na=False),
    data['Class'].str.contains(
        r'000100.2 - Warehouse & Logistic:000108 - Logistics Cust Serv', na=False),
    data['Class'].str.contains(
        r'000100.2 - Warehouse & Logistic:000110 - Whse Office Personel', na=False),
    data['Class'].str.contains(
        r'000100.2 - Warehouse & Logistic:000111 - Warehouse - 2nd Shift', na=False),
    data['Class'].str.contains(
        r'000100.2 - Warehouse & Logistic:000114 - Safety / Maintenance', na=False),
    data['Class'].str.contains(r'000101 - Officer', na=False),
    data['Class'].str.contains(r'000102 - VP', na=False),
    data['Class'].str.contains(r'000103 - Acct / Hr', na=False),
    data['Class'].str.contains(r'000104 - Manager', na=False),
    data['Class'].str.contains(r'000112 - IT / Special Projects', na=False),
    data['Class'].str.contains(r'000200 - Trans & Whse', na=False),
    data['Class'].str.contains(r'000200.1 - Transportation', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000205 - Trans Whse - 1st Shift', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000206 - Dispatch', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000207 - Sales', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000209 - Trans Cust Serv', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000210 - Trans Office Personnel', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000211 - Trans Whse - 2nd Shift', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000213 - Drivers', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000214 - Safety/Maintenance', na=False),
    data['Class'].str.contains(
        r'000200.1 - Transportation:000215 - Trans Whse - 3rd Shift', na=False),
    data['Class'].str.contains(r'000203 - Acct / Hr', na=False),
    data['Class'].str.contains(r'000204 - Manager', na=False),
    data['Class'].str.contains(r'000212 - IT / Special Projects', na=False)
]

choicesClass = ['Share',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Warehouse',
                'Share',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total',
                'Total'
                ]

data['LocationClass'] = np.select(conditionsClass, choicesClass, default='NA')


# validate data

data['checkLocation'] = data.apply(
    lambda x: 0 if x['LocationName'] == x['LocationClass'] else x['Num'], axis=1)

check = data.loc[data['checkLocation'] != 0]
print(check.head())
# 1 version of data
monthly = data.groupby([data.Date.dt.month, 'Acct', 'Class']).sum()




