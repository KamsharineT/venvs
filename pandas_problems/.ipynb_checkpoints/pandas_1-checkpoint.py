'''These scripts contain the pandas problems from geeks for geeks'''

import pandas as pd

lst = [['One',1],['Two',2],['Three',3]]

df = pd.DataFrame(lst,columns=['Name','Numbers']) # For list you have to define columns when converting to df

print(df)


dicts = {
    'Name':['Sharine','Bu'],
    'Age':[29,33]
    }

df2 = pd.DataFrame(dicts) # For dict you don't need to define columns when converting to df

print(df2)



# Dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)

# Output:
#       Name  Age         City
# 0    Alice   24     New York
# 1      Bob   27  Los Angeles
# 2  Charlie   22      Chicago

lst2 = [['Alice','Wonderland'],['How','Why']]

df3 = pd.DataFrame(lst2,columns=['Name','Questions'])

dict2 = {'Name':['Alice','Wonderland'],
         'Questions':['How','Why']}
df4 = pd.DataFrame(dict2)

print(df3)
print(df4)


'''Converts 2D list to df 
using pandas library pd.DataFrame.from_records()'''
print()
print("Converts 2D list to df using from_records()")
twodlist = [['He', 33 ,'Bu'],
            ['She', 29, 'Mu'],
            ['Baby',0,'Kuttan']]

columns = ['Abbr','Age','Nick Names']
df5 = pd.DataFrame.from_records(twodlist,columns=columns)
print(df5)

print()
print("Converts 2D list to df using from_dict()")
df6 = pd.DataFrame.from_dict(dict(zip(columns,zip(*twodlist))))

print(df6)