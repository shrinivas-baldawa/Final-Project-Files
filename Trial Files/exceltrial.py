import pandas as pd
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
filetypes = (('Excel Files', '*.xlsx'),('All files', '*.*'))
root.withdraw()

fileName = askopenfilename(title='Open A File',initialdir='/',filetypes=filetypes)

df = pd.read_excel(fileName)

present_dataframe = df[df['Status'] == 'P']
presentIDS = present_dataframe.iloc[:,1]
print('Present Students Email Ids: {}'.format(presentIDS.values.tolist()))

absent_dataframe = df[df['Status'] == 'A']
absentIDS = absent_dataframe.iloc[:,1]
print('Absent Students Email Ids: {}'.format(absentIDS.values.tolist()))

# present_rollNumbers_df = df[df['Status'] == 'P']
# presentRollNumbers = present_rollNumbers_df.iloc[:,0]
# print('Present Students Roll Numbers: {}'.format(presentRollNumbers.values.tolist()))

# absent_rollNumbers_df = df[df['Status'] == 'A']
# absentRollNumbers = absent_rollNumbers_df.iloc[:,0]
# print('Absent Students Roll Numbers: {}'.format(absentRollNumbers.values.tolist()))

allRollNumbers = df['PRN']
print(allRollNumbers.values.tolist())
