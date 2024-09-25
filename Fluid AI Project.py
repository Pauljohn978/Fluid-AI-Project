#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'D:\Black Coffer\enterprise_gpt_product_usage.csv'
data = pd.read_csv(file_path)

data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')

# Exploratory Data Analysis

# Setting up Seaborn style
sns.set(style="whitegrid")

# Plot 1: Distribution of Query Length
plt.figure(figsize=(12, 6))
sns.histplot(data['query_length'], bins=20, kde=True, color='blue')
plt.title('Distribution of Query Length')
plt.show()

# Plot 2: Distribution of Response Time
plt.figure(figsize=(12, 6))
sns.histplot(data['response_time'], bins=20, kde=True, color='green')
plt.title('Distribution of Response Time')
plt.show()

# Plot 3: Distribution of User Ratings
plt.figure(figsize=(12, 6))
sns.countplot(data['user_rating'], palette='coolwarm')
plt.title('Distribution of User Ratings')
plt.show()

# Plot 4: Count of Interaction Type
plt.figure(figsize=(12, 6))
sns.countplot(x='interaction_type', data=data, palette='viridis')
plt.title('Count of Interaction Type')
plt.show()

# Boxplots: Response Time vs User Rating by Industry and Subscription Level
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Plot 5: Response Time vs User Rating by Industry
sns.boxplot(x='user_rating', y='response_time', hue='industry', data=data, ax=axs[0], palette='Set2')
axs[0].set_title('Response Time vs User Rating by Industry')

# Plot 6: Response Time vs User Rating by Subscription Level
sns.boxplot(x='user_rating', y='response_time', hue='subscription_level', data=data, ax=axs[1], palette='Set3')
axs[1].set_title('Response Time vs User Rating by Subscription Level')

plt.tight_layout()
plt.show()


# In[4]:


import pandas as pd

file_path = 'D:\Black Coffer\enterprise_gpt_product_usage.csv'
data = pd.read_csv(file_path)

# Checking for null values in each column
null_values = data.isnull().sum()

# Displaying columns with null values
print("Null values in each column:\n", null_values)

#showing the percentage of missing values in each column
null_percentage = (data.isnull().sum() / len(data)) * 100
print("\nPercentage of missing values:\n", null_percentage)



#showing only the columns with missing values
missing_data = data[data.columns[data.isnull().any()]]
print("\nColumns with missing values:\n", missing_data.head())


# In[ ]:




