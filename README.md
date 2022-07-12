This is my final project for the Code Louisville Data 1 course.  
This project is using SalaryData.xlsx pulled from https://data.louisvilleky.gov/dataset/employee-salary-data

This data set contains the salary information for Metro Louisville employees from 2016 to present. 



This project reads in the data set in excel format and drops the YTD_Total column from analysis as it is not needed or provides any value to the review being completed. 

The data clean up that is performed drops any rows where the name field is null. 
The Annual_Rate field is converted to datatype int to allow it to be used with no converting issues later on in the project. 

Under the banner "Information About the Data Set" the data types are printed for review and a list of unique departments is printed for review. 

Recognizing that there is some repetitive coding, a user should be able to select different years for each function for review. 
The function for agg_salary computes for a selected year the following: 
-count of employees included in the department
-min value for annual salary
-max value for annual salary
-mean value for annual salary
-sum value for the department of annual salary paid to employees


Function for max_salary allows a user to select a year and see the highest paid employee that year which includes: name, department, job title, annual rate, incentive_allowances, and overtime pay

Function for min_salary allows a user to select a year and see the lowest paid employee that year which will include the same information from the data set provided in max_salary


Using the NLargest and NSmallest, it is set to pull 5 employees from the data set that were given the highest and lowest incentive allowances for their positions. 

The tech_emp function silos out the employees in the Technology Services Department in a selected year to show the top 5 paid employees. 

 
Using Matplotlib, tech employees for the Metro area were siloed out of the data and grouped by year to show the upward trend of annual salary in the IT industry. 
