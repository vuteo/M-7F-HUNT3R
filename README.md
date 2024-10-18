# Medical cost
<ul>
<li>Subject:Data Science</li>
<li>Class:MAS2</li>
<li>Lecturer:Dr. Emmanuel Lance Christopher VI M. Plan</li>
</ul>
.

# Team Member 

![image](https://github.com/user-attachments/assets/b74ef97e-0826-4a53-94c5-641db8353f3e)



# I. Introduction


- The cost of healthcare is going up everywhere, and it's a big problem for many countries. To help fix this, we need to know what makes medical expenses high. This is important for insurance companies, healthcare providers, and the government. The report looks at the "Medical Cost Personal Dataset." This dataset shows health insurance costs based on things like age, sex, BMI, smoking, and where people live. It has 1,338 records with 7 different factors that affect insurance costs. These factors include age, region, smoking habits, and BMI. The main focus is on "charges," which means the medical costs billed. The data comes from Kaggle.
- The goal of this project is to analyze the dataset to find important patterns and relationships between different factors and medical costs. The analysis will include descriptive statistics, visualizations, and a prediction model to estimate medical expenses based on these factors. The findings could help insurance companies better understand individuals with high medical costs, which can support better risk management and adjust pricing strategies for premiums. 
<br>

- This data can be instrumental for analyzing sales performance, understanding customer preferences, and making informed business decisions.

# II. Data Discussion
- **Age**: Age of the person.
- **Sex**: Male or female.
- **BMI**: Body fat measurement.
- **Children**: Number of dependents.
- **Smoker**: Yes or no.
- **Region**: Area (northeast, northwest, southeast, southwest).
- **Charges**: Medical costs billed.
# III. Data Cleaning
![image](https://github.com/user-attachments/assets/8380c6ab-24e9-4a27-84cd-77063058214b)

- The data is already cleaned

# IV. Charts and Insights
**1. Smoking vs. Medical Charges**
Smokers pay way more. The box plot shows smokers have much higher charges than non-smokers. Recommendation: charge smokers more.
![image](https://github.com/user-attachments/assets/400166d9-384b-4f84-80c3-cfa311181709)
**Chart Analysis: Smoking vs Medical Charges**
**Which One is Highest?**
- **Smokers** pay significantly higher medical charges than non-smokers. The median cost for smokers is around **$35,000**, while for non-smokers it's just **$8,000**. The highest costs for smokers go over **$60,000**, compared to non-smokers who rarely exceed **$20,000**.
**Increasing/Decreasing Pattern?**
- There's no specific increasing or decreasing trend shown here because this is a comparison between two groups. What it clearly shows is a **huge difference** in medical costs between smokers and non-smokers. Smokers always have higher costs—no exceptions.
**Why is This Important?**
- **Decision for Manager**: Smokers are a high-risk group with much higher and more unpredictable medical expenses. This means **higher premiums** are needed for smokers to balance out the increased risk. The cost difference is too big to ignore; smokers need to pay more because they cost the company more. Straightforward decision—charge them more, minimize the company's financial risk.

**2. BMI Categories vs. Medical Charges**
People were grouped by BMI: underweight, normal, overweight, obese. The box plot shows obese people face higher charges. This means BMI is a good factor for predicting high costs.
![image](https://github.com/user-attachments/assets/ec0abee4-7214-4d00-b007-54f89cced786)
**Chart Analysis: BMI Category vs Medical Charges**
**Which One is Highest?**
- **Obese** individuals have the highest medical charges. The median cost is higher than the other BMI categories, and there are many outliers with extremely high charges (some even exceeding **$60,000**).
- **Underweight, Normal, and Overweight** categories have similar median charges, all much lower than the obese group.
**Increasing/Decreasing Pattern?**
- There is an **increasing pattern** in medical charges as BMI goes up. Medical charges steadily rise from **underweight to obese**. Obese individuals have a significant jump in costs compared to the others.
**Why is This Important?**
- **Decision for Manager**: Obese individuals are driving higher costs, which means they are a higher risk group. To manage this risk, insurance premiums should be higher for obese individuals. The cost difference is clear—people with higher BMIs (specifically those classified as obese) cost more in healthcare. Adjust the premiums accordingly to make sure the higher risk (higher medical expenses) is covered by higher pricing. Simple decision—higher risk, higher cost.

**3. Age vs. Medical Charges**
Charges increase with age, especially after 50. The scatter plot shows this clearly. Older people are more likely to need higher-cost insurance.
These charts directly show who has higher costs—smokers, older people, and those with higher BMI. This means insurance companies should adjust premiums accordingly.
![image](https://github.com/user-attachments/assets/85e7baca-e438-43b9-a7f9-5ddc387d20c5)
**Chart Analysis: Age vs Medical Charges**
**Which One is Highest?**
- **Smokers** always have the highest medical charges compared to non-smokers, regardless of age. The **blue dots** represent smokers, and they are consistently above the **orange dots** (non-smokers).
- As age increases, the medical charges also increase for both smokers and non-smokers, but smokers consistently pay much more. The highest charges go well above **$60,000**, mostly for older smokers.
**Increasing/Decreasing Pattern?**
- **Increasing Pattern**: Medical costs **increase with age**. The older the person, the more they pay, especially if they smoke. The charges rise for both groups, but the gap between smokers and non-smokers remains obvious and significant at every age group.
**Why is This Important?**
- **Decision for Manager**: Age and smoking are two major factors driving up medical costs. Older people cost more, and smokers cost way more. So, adjust the premiums—charge **older people higher premiums** based on the increased cost with age, and **charge smokers even more** to cover their significantly higher health risks. The costs aren't the same for everyone—insurance pricing needs to reflect this. Higher age and smoking mean higher costs, so premiums need to go up for these groups.

# V. Conclusion
Smoking, age, and BMI are the main factors driving medical costs. Smokers, older people, and those with high BMI should be charged higher premiums based on their risk. No fluff—just straight insights and recommendations.


