# -*- coding: utf-8 -*-
"""MiniPresentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H0ghSIbOUQ4T-BqxZVe7Sj9VxFwLPoZ3
"""

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

"""**This scatter plot, titled BMI vs. Charges, shows BMI on the x-axis and insurance charges on the y-axis. It uses color to distinguish between smokers and non-smokers: blue for smokers and orange for non-smokers.**

1. Higher Charges for Smokers: Smokers (blue points) generally incur higher charges. Their charges can exceed 60,000 dollar, whereas non-smokers (orange points) charges rarely go beyond $20,000. This highlights the significant financial impact of smoking on health costs.
2.
Correlation Between BMI and Charges: There's a clear upward trend, especially for smokers, suggesting higher BMIs often lead to higher insurance charges. This aligns with the understanding that higher BMI can be associated with health risks, increasing medical cost

3.

Clustering of Non-Smokers: Most non-smokers' charges are clustered below $20,000, showing more manageable health costs for this group compared to smokers.
"""

sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Charges Distribution by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Charges')
plt.show()

"""**This boxplot underscores the substantial financial burden of smoking. It visually communicates how smoking leads to significantly higher and more variable health insurance charges. For insurers, this could inform risk assessment and policy pricing. For individuals, it's a stark reminder of the economic benefits of avoiding smoking.**

Higher Median Charges for Smokers:

The median charge for smokers is significantly higher than that for non-smokers. The median line within the smokers' box is around $35,000, compared to aroun $10,000 for non-smokers. This stark difference highlights the financial impact of smoking on health insurance costs.

Greater Variability Among Smokers:

Smokers exhibit a wider interquartile range (IQR), meaning there’s more variability in their charges. The IQR for smokers is larger, indicating that while some smokers might have lower charges, many face significantly higher costs due to the health risks associated with smoking.

Presence of Outliers:

Both smokers and non-smokers have outliers, but smokers show more extreme values (higher charges). This indicates that some smokers face exceptionally high insurance costs due to severe health issues.

Overall Distribution:

The overall distribution for non-smokers is more compact with fewer extreme values, suggesting more stable and predictable health costs. Conversely, smokers’ charges vary widely, reflecting the broader range of health impacts linked to smoking.
"""

sns.lmplot(x='age', y='charges', hue='smoker', data=df)
plt.title('Charges vs. Age by Smoking Status')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

"""**The chart effectively highlights the long-term financial impact of smoking. It demonstrates how both age and smoking status contribute to rising health insurance costs, with smokers bearing a heavier burden as they age. This insight is crucial for insurers in risk assessment and policy pricing, as well as for individuals considering the long-term financial implications of smoking.**

Increasing Charges with Age:

Both smokers and non-smokers show an increase in insurance charges as they age. This is visually represented by the upward slope of the regression lines for both groups.

Higher Charges for Smokers:

Smokers consistently incur higher charges compared to non-smokers at any given age. This is indicated by the higher regression line for smokers. The financial burden of smoking is evident, showing increased healthcare costs due to smoking-related health issues.

Variation in Charges:

Non-smokers exhibit a more predictable increase in charges with age, indicated by a tighter clustering of data points. Smokers, on the other hand, show more variability in charges, highlighting the varied health impacts of smoking.

Compounding Effect of Age and Smoking:

The plot indicates that as individuals get older, their health costs increase. This increase is more pronounced for smokers, suggesting that the combined effects of aging and smoking significantly elevate insurance costs.
"""

smoker_counts = df.groupby(['region', 'smoker']).size().reset_index(name='count')
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x='region', y='count', hue='smoker', data=smoker_counts)
plt.title('Number of Smokers and Non-Smokers in Each Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.legend(title='Smoker Status')

"""**This visualization highlights the prevalence of non-smokers across all regions, pointing to a potential public health success. However, the consistent presence of smokers in all regions also indicates ongoing public health challenges. This data can be crucial for targeted health interventions, regional health policies, and smoking cessation programs.**


"""

# Install libraries if needed
# !pip install pandas matplotlib seaborn scikit-learn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

url = 'https://raw.githubusercontent.com/hoangkazari/minipresentation/main/insurance.csv'
df = pd.read_csv(url)
df.head()

# Convert categorical variables to numeric using one-hot encoding
df_encoded = pd.get_dummies(df, drop_first=True)

# Now you can create the correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df_encoded.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['charges'], kde=True, color='blue')
plt.title('Distribution of Medical Charges')
plt.xlabel('Charges')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='charges', data=df, hue='smoker', palette='coolwarm')
plt.title('Age vs Medical Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='smoker', y='charges', data=df)
plt.title('Average Charges by Smoking Status')
plt.show()

# Convert categorical variables to numerical (one-hot encoding)
df_encoded = pd.get_dummies(df, drop_first=True)

# Define features and target
X = df_encoded.drop('charges', axis=1)
y = df_encoded['charges']

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.title('Actual vs Predicted Medical Charges')
plt.xlabel('Actual Charges')
plt.ylabel('Predicted Charges')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')
plt.show()