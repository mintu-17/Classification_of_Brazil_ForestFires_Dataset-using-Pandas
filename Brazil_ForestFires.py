import sys
sys.path.insert(1, './lib/python3.7/site-packages')
import googletrans

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

import os
# Print the current working directory
print("Current working directory:", os.getcwd())

# Use the relative path to the CSV file
file_path = 'amazon.csv'
df = pd.read_csv(file_path, thousands='.', encoding='ISO-8859-1')


df.head()
df.tail()
type(df)
df.keys()
df.shape
df.describe()
df.describe(include="all")
df.info()
df.isnull().sum()
df.isna()
df.isna().sum()


df=df.replace(0,np.nan)
df=df.dropna(subset=['number'])
df


df.describe(include="all")

fire_per_month=df.groupby("month")["number"].sum()
print(fire_per_month)

months_unique=list(df.month.unique())
months_unique


fire_per_month=fire_per_month.reindex(months_unique,axis=0)
fire_per_month


fire_per_month=fire_per_month.to_frame()
fire_per_month.head()

fire_per_month=fire_per_month.reset_index(level=0)
fire_per_month


translator=googletrans.Translator()

for month in months_unique:
    detected=translator.detect(month)
    translated=translator.translate(month)
    print(detected)
    print(translated)
    print("...")


# Initialize the translator
translator1 = googletrans.Translator()


# Translate month names from Portuguese to English
for i, m in enumerate(fire_per_month['month']):
    translated = translator1.translate(m)
    month1 = translated.text
    fire_per_month.at[i, 'month'] = month1


print(fire_per_month)


plt.figure(figsize=(25, 10)) 
plt.bar(fire_per_month['month'], fire_per_month['number'], color=(0.5, 0.1, 0.5, 0.6))

plt.suptitle('Total Number of Forest Fires per Month', fontsize=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Number of Fires', fontsize=15)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()
