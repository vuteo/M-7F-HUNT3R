# Medical cost
<ul>
<li>Subject:Data Science</li>
<li>Class:MAS2</li>
<li>Lecturer:Dr. Emmanuel Lance Christopher VI M. Plan</li>
</ul>

<br>
# Team Member 
<br>
![image](https://github.com/user-attachments/assets/2168e09d-03b2-4c1d-a6d0-ebc390930c97)
<br>
# 1. Introduction

<br>
## The cost of healthcare is going up everywhere, and it's a big problem for many countries. To help fix this, we need to know what makes medical expenses high. This is important for insurance companies, healthcare providers, and the government. The report looks at the "Medical Cost Personal Dataset." This dataset shows health insurance costs based on things like age, sex, BMI, smoking, and where people live. It has 1,338 records with 7 different factors that affect insurance costs. These factors include age, region, smoking habits, and BMI. The main focus is on "charges," which means the medical costs billed. The data comes from Kaggle.
The goal of this project is to analyze the dataset to find important patterns and relationships between different factors and medical costs. The analysis will include descriptive statistics, visualizations, and a prediction model to estimate medical expenses based on these factors. The findings could help insurance companies better understand individuals with high medical costs, which can support better risk management and adjust pricing strategies for premiums. 
<br>

- This data can be instrumental for analyzing sales performance, understanding customer preferences, and making informed business decisions.

# 2. Data Mining 
- This dataset is sourced from Medical Cost Personal.
- The dataset has 1,338 individuals, including:
- Age
- Sex (male or female)
- BMI (Body Mass Index)
- Children (number of dependents)
- Smoker (yes or no)
- Region (northeast, northwest, southeast, southwest)
- Charges (total medical charges, target variable for prediction)
- This data helps understand medical cost patterns and predict future charges.
# 3. Data Cleaning
![image](https://github.com/user-attachments/assets/8380c6ab-24e9-4a27-84cd-77063058214b)

- The data is already cleaned

# 4. Data Exploration
  Exploratory Data Analysis (EDA) helps us understand the data. The main points from EDA are:
- **Smoking and Medical Charges**: There is a strong link between smoking and medical costs. Smokers usually pay much higher medical bills.
- **Age and Charges**: Medical costs rise with age, especially for people over 50. This shows that older people often face higher medical expenses.
- **BMI and Charges**: People with a higher BMI (who are overweight or obese) have higher medical costs. Obesity is a big reason for these higher charges.
- **Region Differences**: Medical costs are different in each region. People living in the southeast region usually have to pay more.
# 5. Feature Engineering
In this step, we created new features and chose the most important variables to boost model accuracy:
- **BMI Category**: We added a new feature that categorizes individuals as underweight, normal, overweight, or obese to better understand how BMI affects charges.
- **Interaction Terms**: We looked into interactions between key variables, like smoker status and BMI, to capture their combined effect on medical costs.
These new features helped improve the model’s predictions and provided more accurate results.
# 6. Predictive Modeling
We used a linear regression model to predict medical charges based on factors like age, BMI, smoking status, and region. Linear regression was chosen because it’s easy to interpret, allowing us to see how each feature impacts medical costs.
Key factors affecting charges:
- **Smoking status**: Smokers have much higher charges than non-smokers.
- **Age**: Older individuals, especially those over 50, face higher costs.
- **BMI**: People with higher BMI, particularly those classified as obese, also have higher medical costs.
We evaluated the model using Mean Squared Error (MSE) and R² score. The R² score of 0.74 indicates that 74% of the variation in medical costs can be explained by the model’s features.


