Crime Data Analysis
# Crime Data Analysis (2020-Present)

## Project Overview
This project provides a comprehensive analysis of crime data from 2020 to the present. The main objectives were to clean and preprocess the dataset, perform exploratory data analysis (EDA) to uncover trends and patterns, and investigate factors influencing crime rates. Insights were derived on seasonal patterns, common crime types, regional differences, economic correlations, and demographic distributions.  

## Table of Contents
- [Introduction](#introduction)  
- [Data Preprocessing & Cleaning](#data-preprocessing--cleaning)  
- [Analyzing Trends](#analyzing-trends)  
- [Future Predictions](#future-predictions)  
- [Conclusion](#conclusion)  
- [References](#references)  

## Introduction
The aim of this project is to analyze real-world crime data to identify trends, patterns, and influencing factors. The dataset, *Crime Data from 2020 to Present*, was processed and analyzed to answer key questions related to crime frequency, seasonality, regional variations, and economic impacts.  

## Data Preprocessing & Cleaning
The dataset was loaded into a Pandas DataFrame and cleaned using the following steps:  

- **Date Conversion:** Converted 'Date Rptd' and 'DATE OCC' columns to datetime format.  
- **Missing Values:** Removed null values, particularly in the 'Vict Sex' column (106,524 entries).  
- **Duplicate Check:** No duplicates were found.  
- **Data Integrity:**  
  - Removed negative values in 'Vict Age'.  
  - Eliminated outliers and anomalous entries (e.g., 'h', '-').  
- **Column Removal:** Dropped redundant or non-essential columns, including 'Crm Cd 2', 'Crm Cd 3', and 'Crm Cd 4'.  

**Output:** A cleaned CSV file was generated for further analysis.  

## Analyzing Trends

### 1. Overall Crime Trends
- **2020-2021:** Crime rates remained around 175,000 incidents.  
- **2022-2023:** Significant decrease in crime, with 2023 recording less than half of previous years.  
- **Possible Cause:** Influence of the global pandemic.  

### 2. Seasonal Patterns
- **Peak Months:** July and August  
- **Lowest Month:** February  

### 3. Most Common Crime Types
| Crime Type                        | Number of Incidents |
|----------------------------------|------------------|
| BATTERY - SIMPLE ASSAULT          | 63,648           |
| BURGLARY FROM VEHICLE             | 49,342           |
| VANDALISM - FELONY ($400 & OVER) | 49,000           |
| THEFT OF IDENTITY                 | 48,929           |
| BURGLARY                          | 48,046           |

### 4. Regional Differences
- **Highest Crime Area:** 77th Street  
- **Most Common Crime in Region:** ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT (38,469 incidents)  

### 5. Correlation with Economic Factors
- **Unemployment:** Positive correlation with crime rates  
- **Median Household Income:** Negative correlation; higher income areas experience less crime  

### 6. Day of the Week Analysis
- **Highest Crime Rate:** Friday  
- **Lowest Crime Rate:** Tuesday  

### 7. Impact of Major Events
- **COVID-19:** Rise in identity theft due to increased digital activity  
- **Gun Laws:** California legislation reduced crimes involving untraceable firearms  
- **Inflation:** Economic hardship correlated with increased criminal activity  

### 8. Outliers and Anomalies
- Distribution of top crime types across demographics was analyzed to identify disparities in victimization.  

### 9. Demographic Factors
- **Age Groups:** Certain crimes more prevalent among specific ages  
- **Genders:** Crime types are distributed disproportionately across genders  

## Future Predictions
- **Historical Trends:** Fluctuating crime rates with noticeable peaks  
- **Forecast:** Stabilization in crime rates expected, influenced by law enforcement efforts and seasonal factors  

## Conclusion
- Significant decrease in crime rates from 2022 to 2023  
- Seasonal peaks in summer and lows in winter  
- Economic factors like unemployment and median household income strongly correlate with crime trends  
- Top crime types highlight prevalent criminal activities  
- Regional analysis identifies high-risk areas  
- Future trends suggest stabilization influenced by law enforcement and environmental factors  

## References
- [Crime Data Source]  
- [Economic Data Source]  
