""" Q1: 
Load and read the 'imdb.xlsx' file. Read the 'imdb' sheet into a DataFrame, df.
"""

import pandas as pd

# your code here
xls = pd.ExcelFile("imdb.xlsx")
df = xls.parse("imdb")

""" Q2: 
Store the dimensions of the DataFrame as a tuple in a variable called 'shape' and print it.

Hint: A tuple is made up of comma separated values inside parenthesis.  e.g. (1, 2)
"""

# your code here
shape = df.shape
print(shape)

""" Q3: 
Store the column titles and the types of data in variables named 'columns' and 'dtypes', then print them.
"""

# your code here
columns = df.columns
dtypes = df.dtypes
print(columns)
print(dtypes)

""" Q4: 
Examine the first 10 rows of data; store them in a variable called first10
"""

# your code here
first10 = df.head(10)

""" Q5: 
Examine the first 5 rows of data; store them in a variable called first5
"""

# your code here
first5 = df.head()

""" Q6: 
Import the "directors" and "countries" sheets into their own DataFrames, df_directors and df_countries.
"""

# your code here
df_directors = xls.parse("directors")
df_countries = xls.parse("countries")

""" Q7: 
Check the "directors" sheet
1. Count how many records there are based on the "id" column. (To get the number of records per "id", 
   use the value_counts method.) Store the result in a variable named count.
2. Remove the duplicates from the directors dataframe and store the result in a variable called df_directors_clean.
"""

# your code here
count = df_directors["id"].value_counts()
df_directors_clean = df_directors.drop_duplicates()
