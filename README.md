
# Regression Based Model for predicting salaries of individuals in Chemical Engineering-Related professions.

The project is aimed at providing Chemical Engineering practitioners with information about the current job market in the USA and to also aid with providing a general idea on salaries they are expected to earn given certain criteria. The data was scraped from the employer rating site [Glassdoor.com](https://glassdoor.com). It features a salary predictor and a dashboard displaying some important information like geographical location of job postings, salary distribution based off different factors etc.

## Acknowledgements

 - [Omer Sakarya](https://github.com/arapfaik)
 - [Ken Jee](https://github.com/PlayingNumbers)
 
## Data Collection

The data was collected from the web and was done using selenium, a python library primarily used for automation. The data was collected regulary over the period of a month. Search terms like **"chemical process engineer"**,**"chemical engineer"** and **"process engineer"** were used to generate results for the web scraping.


## Data Cleaning and Feature Engineering

**Data Cleaning**

The data was cleaned using the pandas library. Over 8000 job postings were scraped over the month long period. In the course of the data cleaning the following tasks were carried out using pandas:
- **Dropping duplicate data**
- **Data standardization**
- **Dropping unwanted features**
- **Outlier detection and removal**
- **Removal of missing values**

1) **Dropping duplicate data**
Out of the 8630 job posting collected, 3999 of them turned out to be duplicates which were removed so as to prevent multi-collinearity during the model building phase.

2) **Data standardization**
In order to make the columns in the data consistent, columns that contained data which they weren't supposed to contain were corrected.

3) **Dropping unwanted features**
Features which provided no value during the analysis process were removed. Features such as the Number of Competitors, Headquarters and Employee Rating.

4) **Outlier detection and removal**
Outliers (abnormally high or low salaries) were removed using the inter-quartile range, this amounted to 199 data points.

5) **Removal of missing values**
The tolerance for missing values was set to "any" i.e any rows that contained any missing value were removed, this accounted for 2253 rows

**Feature Engineering**


The data set originally contained 14 feature as in the screenshot below:
![Initial Features](https://github.com/AngeloRules/Regression-Based-Model-For-Predicting-Chemical-Engineers-Salaries/blob/main/Screenshot%20(10).png?raw=true)


After the process of feature engineering additional features were created bringing the total to 32:
![After Feature Engineering](https://github.com/AngeloRules/Regression-Based-Model-For-Predicting-Chemical-Engineers-Salaries/blob/main/Screenshot%20(11).png?raw=true)


Some important feature include:

- Company Age: The company age was computed by subtracting the founding date from the year 2022.

- Bachelors/Master/PHD: These features were created by parsing through the Job descriptions looking for matches such as BSc,Msc,PH.D,B.Tech,M.Tech etc.

- Years of Experience: This was created by parsing through the job description using regular expression (regex) to find patterns such as "5 years","5+ years" and "(5) years" as these were the most commonly found patterns in the job description. 
 *N.B* *It must be however noted that some compromises had to be made concerning the years of experience*
 
   a) a threshold of **25 years** was set because often, time years above that threshold often referred to other things like the company's age. 
   
   b) Another compromise was excluding all instances of **"18 years"** because these often referred to the minimum age candidates applying for some jobs had to be.
   
   c) In cases where the pattern search returned more than one instance of a match, the highest matching year was selected.
   
- Microsoft Skill: The job description of each of the jobs was parsed to look for instances where microsoft packages like excel, word, powerpoint etc were mentioned.

- Chem Eng: This feature was created by parsing through each of the job descriptions to find out which of the jobs required a degree in chemical engineering.

- Senior: The job title was parsed to find out which of them were senior roles.

- Average Salary: This was created from the salary estimate column, it was converted into numeric form by matching patterns using regex.

- Longitude/Latitude: The longitude and latitude of each of the job postings were gotten using the python library Geopy.

- States: The two letter abbreviation was of each of the fifty states was gotten by parsing the location column.

- Simulation software: The job description was parsed to find mentions of popular software like CHEMCAD, HYSYS, AUTOCAD, ASPEN ONE,etc.

- Hourly wage: The salary estimate was parsed to find out which of the employers paid wage on an hourly basis.

- Coding Skill: The job description was parsed to find out which of the jobs required certain coding skills like use of python, java, c++ etc.

- Full-Time: The job description was parsed to find out which of the jobs was a full-time role.


## Exploratory Data Analysis


Exploratory data analysis was done using pandas, plotly, seaborn and matplotlib. During EDA some of the following questions were posed:
- what is the correlation between some of the features like years of experience and the average salary?
- which state(s) and region(s) pay the most wage to chemical engineers?
- what sector employs the most chemical engineers and pays them the most?
- which companies were hiring the most at the time?
- what is the salary distribution between those who were BSc/Msc/PhD holders and those in senior roles?
- what kinds of industries were popular in each of the states?

Some visuals from the EDA are displayed below:
![visual](https://github.com/AngeloRules/Regression-Based-Model-For-Predicting-Chemical-Engineers-Salaries/blob/main/Screenshot%20(12).png?raw=true)

![visual](https://github.com/AngeloRules/Regression-Based-Model-For-Predicting-Chemical-Engineers-Salaries/blob/main/Screenshot%20(13).png?raw=true)

![visual](https://github.com/AngeloRules/Regression-Based-Model-For-Predicting-Chemical-Engineers-Salaries/blob/main/Screenshot%20(14).png?raw=true)



## Model Building


The model building process was done using the python library Sci-kit learn.
- Preprocessing: All the categorical columns were encoded using the get dummies feature in pandas.
- Model Selection: Linear Regression, Ridge Regression, Lasso Regression, Decision Tree Regression and Random Forest Regression were all considered, after cross-validation was carried out the model of choice was Random Forest Regression. KFold cross validation was used
- Tran-Test Split: 80% of the data set was used for training the model and the rest was used for evaluating the model.
- Hyperparameter Tuning: A grid search was carried out to find the optimal set of parameters to improve the model's performance. 
- Model Traning & Evaluation: After subsequent traning and evaluation the metrics gotten were as follows:

    - **Mean Absolute Error** : 7890

    - **Mean Squared Error** : 1.237 * 10e8

    - **Root Mean Squared Error** : 1.112 * 10e4

    - **R2 Score** : 0.602


## Authors

- [AngeloRules](https://www.github.com/AngeloRules)


## Features

- Salary Predictor
- Interactive Dashboard


## Libraries/Technologies
**Web-Scraping:** Selenium <img alt="selenium" width="30px" src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/selenium/selenium-original.svg" />

**Data Cleaning and Feature Engineering:** Numpy <img alt="Numpy" width="30px" src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/numpy/numpy-original.svg" />, Pandas <img alt="Pandas" width="30px" src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/pandas/pandas-original.svg" />, Regex, Geopy <img alt="seaborn" width="30px" src="https://geopy.readthedocs.io/en/stable/_images/logo-wide.png" />


**Visualization:** Matplotlib <img alt="seaborn" width="30px" src="https://seeklogo.com/images/M/matplotlib-logo-7676870AC0-seeklogo.com.png" />
 , Seaborn <img alt="seaborn" width="30px" src="https://github.com/mwaskom/seaborn/raw/master/doc/_static/logo-wide-lightbg.svg" />
, Plotly <img alt="seaborn" width="30px" src="https://www.vectorlogo.zone/logos/plot_ly/plot_ly-ar21.svg" />


**Model Building:** Sci-kit Learn <img alt="seaborn" width="30px" src="https://seeklogo.com/images/S/scikit-learn-logo-8766D07E2E-seeklogo.com.png" />


**UI building:** Streamlit <img alt="seaborn" width="30px" src="https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png" /> 

**Deployment:** Heroku <img alt="seaborn" width="30px" src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/heroku/heroku-original.svg" />


## Web App
 - [Live Web App](https://predictchemsalaries.herokuapp.com/)


## Screenshots

![Salary Prediction Tab](https://github.com/AngeloRules/Regression-Based-Model-For-Predicting-Chemical-Engineers-Salaries/blob/main/Screenshot%20(6).png)
![Dashboard Tab](https://github.com/AngeloRules/Regression-Based-Model-For-Predicting-Chemical-Engineers-Salaries/blob/main/Screenshot%20(7).png)
![Dashboard Tab](https://github.com/AngeloRules/Regression-Based-Model-For-Predicting-Chemical-Engineers-Salaries/blob/main/Screenshot%20(8).png)





