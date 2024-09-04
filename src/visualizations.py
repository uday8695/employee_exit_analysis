# visualizations.py

import seaborn as sns
import matplotlib.pyplot as plt

def plot_satisfaction_vs_hours(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='satisfaction_level', y='average_montly_hours', data=df, alpha=0.6)
    plt.title('Satisfaction Level vs. Average Monthly Hours (Employees who Left)')
    plt.xlabel('Satisfaction Level')
    plt.ylabel('Average Monthly Hours')
    plt.show()

def plot_satisfaction_by_salary(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='salary', y='satisfaction_level', data=df, palette='muted')
    plt.title('Satisfaction Level by Salary (Employees who Left)')
    plt.xlabel('Salary Level')
    plt.ylabel('Satisfaction Level')
    plt.show()

def plot_departments_left(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Department', data=df, palette='viridis', order=df['Department'].value_counts().index)
    plt.title('Count of Employees who Left by Department')
    plt.xlabel('Department')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def plot_promotion_vs_salary(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='promotion_last_5years', hue='salary', data=df, palette='coolwarm')
    plt.title('Promotion in Last 5 Years vs Salary Level (Employees who Left)')
    plt.xlabel('Promotion in Last 5 Years')
    plt.ylabel('Count')
    plt.show()
