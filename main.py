import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# filtered values used to extract the max and min salary are setting a value on a copy of a slice from the dataframe.
# To ignore this warning as a means of only pulling the values, the chained mode assignment sets this to none for it to ignore the warning
pd.options.mode.chained_assignment = None

# function borrowed to print out banners/headers in order to separate different parts of the project for visibility


def banner(message, banner="-"):

    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(line)

# Create salary data dataframe from the SalaryData excel document.
# https://data.louisvilleky.gov/dataset/employee-salary-data


path = "/Users/miche/OneDrive/Desktop/Code Louisville/Final Project/Final_Project_Data_1/"

salary_data_df = pd.read_excel(os.path.join(
    path, 'Data_Source', 'SalaryData.xlsx'), usecols='A:I')

# Data Clean-up where we remove rows where names are missing/blank

salary_data_df['Employee_Name'].replace('', np.nan, inplace=True)
salary_data_df.dropna(subset=['Employee_Name'], inplace=True)

# Converting the Annual Rate in the data set to int64 to be used in later functions

salary_data_df['Annual_Rate'] = salary_data_df['Annual_Rate'].astype(
    np.int64)


# Data Analysis

# print the data types of each column in the data set
#####
banner("Information About the Data Set")
#####
print(salary_data_df.dtypes)


# display all available Departments in the data set and print them on new lines
dept = list(salary_data_df['Department'].unique())
print('These are the departments listed for the metro salary analysis: ', *dept, sep='\n')


#####
banner("Employee Information")
#####


# Function that filters the data by the selected 'year' and groups by Department to provide Employee Count and salary min, max, mean and sum.

def agg_salary(year):
    filterYear = salary_data_df["CalYear"].isin([year])
    dataByYear = salary_data_df[filterYear]
    salay_calc = dataByYear.groupby(
        dataByYear['Department']).Annual_Rate.agg(['count', 'min', 'max', 'mean', 'sum']).rename(columns={'count': 'Employee_Count', 'min': 'Lowest_Salary', 'max': 'Highest_Salary', 'mean': 'Average_Salary', 'sum': 'Department_Total'})

    return print(salay_calc)

# Insert the year that you would like to see count, min, max, mean and sum for:


agg_salary(2018)


# Function that allows you to select the year and return the employee that made the highest salary

def max_salary(year):
    filterYear = salary_data_df["CalYear"].isin([year])
    filterRateMax = salary_data_df["Annual_Rate"].max()
    dataByYearAsc = salary_data_df[filterYear]

    dataByYearAsc.sort_values(["Annual_Rate"],
                              axis=0,
                              ascending=[False],
                              inplace=True)

    dataByYearTop = dataByYearAsc[:1]
    return dataByYearTop

# Insert the year below to print out the highest paid employee:


print('The highest paid employee of the selected year is: \n',
      max_salary(2016))


# Function that allows you to select the year and return the employee that made the lowest salary

def min_salary(year):
    filterYear = salary_data_df["CalYear"].isin([year])
    filterRateMax = salary_data_df["Annual_Rate"].min()
    dataByYearDesc = salary_data_df[filterYear]

    dataByYearDesc.sort_values(["Annual_Rate"],
                               axis=0,
                               ascending=[True],
                               inplace=True)

    dataByYearBotton = dataByYearDesc[:1]
    return dataByYearBotton


# Insert the year below to print out the lowest paid employee:

print('The lowest paid employee of the selected year is: \n',
      min_salary(2019))


# Using NLargest to see employees that were provided the highest Incentive_Allowance with no filtered year

salary_top_allow = salary_data_df.nlargest(5, 'Incentive_Allowance')
print("Five positions and employees who were given the highest incentive allowance over the last 6 years: ",
      salary_top_allow, sep='\n')

# Using NSmallest to see employees that were provided the lowest Incentive_Allowance with no filtered year

salary_bottom_allow = salary_data_df.nsmallest(5, 'Incentive_Allowance')
print("Five positions and employees who were given the lowest incentive allowance over the last 6 years: ",
      salary_bottom_allow, sep='\n')


# Filtering the data set to view all Tech Employees for the Metro area in the selected year

def tech_emp(year):
    filterYear = salary_data_df["CalYear"].isin([year])
    tech_filter = salary_data_df[filterYear].loc[salary_data_df['Department']
                                                 == 'Technology Services']
    return tech_filter

# print of the tech employee function to print out the top 5 paid employees for the selected year


print(tech_emp(2022).nlargest(5, "Annual_Rate"))


#####
banner("MatplotLib Information")
#####

tech_salary_df = salary_data_df[salary_data_df['Department']
                                == 'Technology Services']
average_tech_salary = tech_salary_df.groupby('CalYear')['Annual_Rate'].mean()
year = sorted(tech_salary_df['CalYear'].unique())

plt.plot(year, average_tech_salary, color='green', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Average Salary')

plt.gca().set_yticklabels(['${:,.0f}'.format(x)
                           for x in plt.gca().get_yticks()])

plt.title('Average Salary for Technology Services Employees')
plt.show()
