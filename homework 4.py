import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('E:\DSS\homework 3\census_income_dataset.csv')

plt.rcParams.update({'font.size': 12})

# Plot 1: Age distribution of respondents (Histogram)
plt.figure(figsize=(12, 8))
sns.histplot(df['AGE'], bins=30, kde=True, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Respondents')
plt.xlabel('AGE')
plt.ylabel('Frequency')
# Save the plot as SVG
plt.savefig('E:\DSS\homework 3\homework 4/age_distribution.svg', format='svg')
plt.savefig('E:\DSS\homework 3\homework 4/age_distribution.png', format='png')
plt.show()

# Plot 2: Frequency of Relationship Status (Pie chart)
plt.figure(figsize=(12, 8))  
relationship_count = df['RELATIONSHIP'].value_counts()

# Define a color palette with at least 6 colors
colors = ['green', 'red', 'blue', 'yellow', 'orange', 'purple']

# Create a pie chart
relationship_count.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=colors,  # Add enough colors
    wedgeprops={'edgecolor': 'black'},
    figsize=(12, 8)
)

# Title and labels
plt.title('Frequency of Relationship Status')
plt.ylabel('')  

# Save the plot as SVG
plt.savefig('E:\DSS\homework 3\homework 4/relationship_status_frequency_pie.svg', format='svg')
plt.savefig('E:\DSS\homework 3\homework 4/relationship_status_frequency_pie.png', format='png')

# Display the plot
plt.show()

# Plot 3: Salary <=50k vs >50k within each educational level (Stacked Bar plot)
# Mapping salary to 0 (<=50K) and 1 (>50K)
df['salary_label'] = df['SALARY'].apply(lambda x: 0 if x == '<=50K' else 1)

# Group by education and salary label
salary_by_education = df.groupby(['EDUCATION', 'salary_label']).size().unstack(fill_value=0)

# Prepare data for plotting lollipop chart
# Plot 3: Salary <=50k vs >50k within each educational level (Stacked Bar plot)
# Mapping salary to 0 (<=50k) and 1 (>50k)
df['salary_label'] = df['SALARY'].apply(lambda x: 0 if x == '<=50K' else 1)

# Group by education and salary label
salary_by_education = df.groupby(['EDUCATION', 'salary_label']).size().unstack(fill_value=0)

# Plot stacked bar chart
plt.figure(figsize=(12, 8))
salary_by_education.plot(kind='barh', stacked=True, color=['blue', 'red'], edgecolor='black')
plt.title('Salary Distribution by Educational Level')
plt.xlabel('Number of Respondents')
plt.ylabel('Education Level')
plt.xticks(rotation=45, ha='right')
# Save the plot as SVG
plt.savefig('E:\DSS\homework 3\homework 4/salary_by_education_level.svg', format='svg')
plt.savefig('E:\DSS\homework 3\homework 4/salary_by_education_level.png', format='png')
plt.show()