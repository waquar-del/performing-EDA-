# -*- coding: utf-8 -*-
"""AsiaCup.project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ezi4rUpeDm74sCn-swWtreiZ43WrQ5V5
"""

pip install matplotlib

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# %matplotlib inline

#Read csv file:
df=pd.read_csv('asiacup.csv')
df

#displaying numerical and categorical column:
num_col=df.select_dtypes(["int","float"]).columns
num_col

cat_col=df.select_dtypes(['O']).columns
cat_col





"""Q1.Display first 10 record of dataset:"""

df.head(10)



"""Q2.Display last 10 record of dataset:"""

df.tail()



"""Q3.Find the shape of Dataset(Number of rows and columns):"""

df.shape
print("Number of Rows:",df.shape[0])
print("Number of columns:",df.shape[1])



"""Q4) Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement."""

df.info()

# We can observe that our dataset contains 254 rows and 20 columns.
# We also observe that there are 12 columns of integer datatype,
# and 8 columns of object datatype.



"""Q5) Check for missing values in the dataset."""

df.isnull().sum()

df.dropna(inplace=True,axis=1)
df

df.isnull().sum()



"""Q7) Get overall statistics about the dataframe."""

df.describe()

#we observe that year column is left skewed,as medain is greator than mean:
sns.distplot(df['Year'],color='r')
plt.show()

cat_col=df.select_dtypes(['O']).columns
cat_col

df['Team'].unique()





"""Q8 show the percentage of the format played in asia cup:"""

df['Format'].value_counts().plot(kind='pie',autopct="%.2f%%")



"""Q10.Display percentage of  most winner no of matches:"""

df['Team'].value_counts().plot(kind='pie',autopct="%.2f%%")

"""Q11 Display All mathes of india:"""

df[df['Team'].str.contains("India")]

"""Q12 Display  result of winner by each team"""

df[df['Result'].str.contains("Win")]

#we can observe that there are 124 rows of data and 8 columns,winner by each team:

"""Q13.Display All Oppnent team  of India:"""

df[df['Opponent'].str.contains("India")]

#we can observe that,there are two many team played againt india:

cat_col

"""Q14 Create Count for Format column"""

sns.countplot(x=df['Format'])
plt.show()

# We can observe that there are more number of ODI mathes played



"""Q15 Create a pairplot for the given dataset."""

sns.pairplot(df)
plt.show()



"""Q16.Create Countplot for Team Column"""

sns.countplot(x=df['Team'])
plt.xticks(rotation=90)
plt.show()

#we can observe that srilanka  and india almost win most number of mathes:

cat_col

"""Q17 Create Sctterplot Between Team and Result"""

sns.scatterplot(x=df['Team'],y=df['Result'],c='orange')
plt.show()



