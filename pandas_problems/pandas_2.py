import pandas as pd

'''df operations'''

twodlist = [['He', 33 ,'Bu'],
            ['She', 29, 'Mu'],
            ['Baby',0,'Kuttan'],
            ['He', 33 ,'Bu'],
            ['She', 29, 'Mu'],
            ['Baby',0,'Kuttan'],
            ['He', 33 ,'Bu'],
            ['She', 29, 'Mu'],
            ['Baby',0,'Kuttan'],
            ['He', 33 ,'Bu'],
            ['She', 29, 'Mu'],
            ['Baby',0,'Kuttan'],
            ['He', 33 ,'Bu'],
            ['She', 29, 'Mu'],
            ['Baby',0,'Kuttan'],
            ['He', 33 ,'Bu'],
            ['She', 29, 'Mu'],
            ['Baby',0,'Kuttan']]

columns = ['Abbr','Age','Nick Names']
df = pd.DataFrame.from_records(twodlist,columns=columns)


''' Viewing Data'''
print(df)

print()
print("df.head() , printing first few records")
print(df.head())
print()
print("df.tail(), 'printing last few records")
print(df.tail())
print()
print("df.tail(), 'printing # Basic summary statistics")
print(df.describe())


# Select a single column
print(df['Abbr'])

# Select multiple columns
print(df[['Abbr','Age']])

#Select using indexing
print(df.iloc[0])


#Conditions
print(df[df['Age']>29])


'''Adding or Modifying Columns'''

# Adding a new column
df['Salary'] = [6000,2000,1000,6000,2000,1000,6000,2000,1000,6000,2000,1000,6000,2000,1000,6000,2000,1000]

print(df)

#modifying values

df['Salary'] = df['Salary'] + 500
print('\n')
print(df)

'''Grouping and Aggregation'''

grouped = df.groupby('Abbr')

print(grouped)