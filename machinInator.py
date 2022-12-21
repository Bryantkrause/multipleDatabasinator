import pandas as pd
import numpy as np


# set columna that actually matter
columnNames = [
    'Accts', 'Type', 'Date', 'Num', 'Name', 'Memo', 'Class', 'Clr', 'Split', 'Debit', 'Credit', 'Balance'
]
columnsToDelete = [
    'Balance', 'Clr', 'Split',
]

# open file
file = r'C:\Users\bkrause\Documents\MachineLearning2022.csv'
refined = r'C:\Users\bkrause\Documents\refinedMachineLearning2022.xlsx'
# convert file to data frame
df = pd.read_csv(file, parse_dates=['Date'])
df.columns = columnNames
df = df.drop(columnsToDelete, axis=1)
print(df.columns)
print(df.head())
# change format from amazing qb to usable data
df['Accts'].ffill(inplace=True)
df = df.dropna(subset=['Date'])
# update null values to 0
df = df.fillna(0)

# create new column to see actual amount
df['Actual'] = df['Debit'] - df['Credit']
data = df.drop(columns=['Debit', 'Credit'])


# convert 0 to error
data['Name'] = data['Name'].replace([0], 'Error')

# data check1 convert vague data names to actual locations based on NAME

conditionsName = [
    data['Name'].str.contains(r'Error', na=False),
    data['Name'].str.contains(r'11937-1 - TT', na=False),
    data['Name'].str.contains(r'16700 Cerritos', na=False),
    data['Name'].str.contains(r'CASH', na=False),
    data['Name'].str.contains(r'CLI - CONTROL ACCOUNT', na=False),
    data['Name'].str.contains(r'INTERCOMPANY - SHARED', na=False),
    data['Name'].str.contains(r'JOSE V. GARCIA', na=False),
    data['Name'].str.contains(r'MARCO ANTONIO FLORES', na=False),
    data['Name'].str.contains(r'OSWALDO MESINA VENTURA', na=False),
    data['Name'].str.contains(r'QTOT', na=False),
    data['Name'].str.contains(r'SALVADOR CUEVAS JR.', na=False),
    data['Name'].str.contains(r'SAMUEL F MACHUCA TINAJERO', na=False),
    data['Name'].str.contains(
        r'THE SUPERIOR COURT OF CA, COUNTY VENTURA', na=False),
    data['Name'].str.contains(r'TOSHIBA FINANCIAL SERVICES', na=False),
    data['Name'].str.contains(r'TOTAL', na=False),
    data['Name'].str.contains(r'Vendor', na=False),
    data['Name'].str.contains(r'VOID CHECK', na=False),
    data['Name'].str.contains(r'WESTSET DISTRIBUTION  - 11937', na=False),
    data['Name'].str.contains(r'WESTSET DISTRIBUTION - 11937', na=False),
    data['Name'].str.contains(r'WESTSET DISTRIBUTION INC.', na=False),
    data['Name'].str.contains(r'WESTSET DISTRIBUTION INC. - 16107', na=False),
    data['Name'].str.contains(r'WESTSET LOGISTICS', na=False)


]

choicesName = [
    'Error',
    'Warehouse',
    'Warehouse',
    'Total',
    'Total',
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
    'Warehouse',
    'Warehouse',
    'Warehouse',
    'Warehouse',
    'Warehouse'
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
                'Total',
                'Total',
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
# extrapilate exceptions due to terrible data integrity
#  if no invoice provide date and dollar amount
data['checkLocation'] = data.apply(
    lambda x: 0 if x['LocationName'] == x['LocationClass'] else f"{x['Date']}-{x['Actual']}-{x['Num']}", axis=1)
# escape the character please
data['checkLocation'] = data.apply(
    lambda x: 0 if x['LocationName'] == 'Total' and x['LocationClass'] == '000112 - IT / Special Projects' else x['checkLocation'], axis=1)

data['checkLocation'] = data.apply(
    lambda x: 0 if x['LocationName'] == 'INTERCOMPANY - SHARED' and x['LocationClass'] == '000103 - Acct / Hr' else x['checkLocation'], axis=1)

check = data.loc[data['checkLocation'] != 0]

check = data.groupby(
    ['checkLocation', 'Accts', 'Name',  check.Date.dt.month, 'Class']).sum()
print(check.head())

# 1 version of data
monthly = data.groupby([data.Date.dt.month, 'Accts', 'Class']).sum()

writer = pd.ExcelWriter(refined, engine='xlsxwriter')
data.to_excel(writer, sheet_name='moreBetterer')
check.to_excel(writer, sheet_name='ITSWRONG')
monthly.to_excel(writer, sheet_name='monthly')
writer.close()
