import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/hoangkazari/minipresentation/main/insurance.csv'
df = pd.read_csv(url)
df.head()

sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df)
plt.title('BMI vs. Charges')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.show()

sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Charges Distribution by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Charges')
plt.show()

sns.lmplot(x='age', y='charges', hue='smoker', data=df)
plt.title('Charges vs. Age by Smoking Status')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

smoker_counts = df.groupby(['region', 'smoker']).size().reset_index(name='count')
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x='region', y='count', hue='smoker', data=smoker_counts)
plt.title('Number of Smokers and Non-Smokers in Each Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.legend(title='Smoker Status')
