from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np
options = Options()
options.add_argument('start-maximized')

def get_jobs(url, num_jobs, verbose,sleep):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    #options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
        
    #driver = webdriver.Chrome()
    #driver.set_window_size(1120, 1000) 
    #url = 'https://www.glassdoor.com/Job/'+keyword+'-jobs-SRCH_KO0,17_IP2.htm'
    #driver_path = "C:/Users/user/Documents/chromedriver.exe"
    #brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application"

    #option = webdriver.ChromeOptions()
    #option.binary_location = brave_path
    # option.add_argument("--incognito") OPTIONAL
    # option.add_argument("--headless") OPTIONAL
    # Create new Instance of Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.set_window_size(1120,1000)
    link = url
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=np.nan&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=np.nan&minRating=0.0&industryId=np.nan&sgocId=np.nan&seniorityType=all&companyId=np.nan&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(link)
    
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(sleep)

        #Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element(By.CLASS_NAME,"selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(sleep)

        try:
            driver.find_element(By.CSS_SELECTOR,'[alt="Close"]').click()  #clicking to the X.
        except NoSuchElementException:
            pass

        
        #Going through each job in this page
        job_buttons = driver.find_elements(By.CSS_SELECTOR,"li.react-job-listing")
       
        for job_button in job_buttons:

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break
            job_button.click()
            time.sleep(sleep)
            collected_successfully = False
            try:
                driver.find_element(By.CSS_SELECTOR,'[alt="Close"]').click()
            except NoSuchElementException:
                pass 
            
            while not collected_successfully:
                try:
                    company_name = driver.find_element(By.XPATH,'//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]').text
                    location = driver.find_element(By.XPATH,'//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    job_title = driver.find_element(By.XPATH,'//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    driver.find_element(By.XPATH,'//*[@id="JobDescriptionContainer"]/div[2]').click()
                    job_description = driver.find_element(By.XPATH,'//*[@id="JobDescriptionContainer"]').text
                    collected_successfully = True
                except:
                    pass

            try:
                salary_estimate = driver.find_element(By.XPATH,'//*[@id="JDCol"]/div/article/div/div[1]/div/div/div/div/div[1]/div[4]/span').text
            except NoSuchElementException:
                salary_estimate = np.nan #You need to set a "not found value. It's important."
            
            try:
                rating = driver.find_element(By.XPATH,'.//span[@class="rating"]').text
            except NoSuchElementException:
                rating = np.nan #You need to set a "not found value. It's important."

                #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

                #Going to the Company tab...
                #clicking on this:
                #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/h2').click()

                try:
                        #<div class="infoEntity">
                        #    <label>Headquarters</label>
                        #    <span class="value">San Francisco, CA</span>
                        #</div>
                    headquarters = driver.find_element(By.XPATH,'aaaaa').text
                except NoSuchElementException:
                    headquarters = np.nan

                try:
                    size = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
                except NoSuchElementException:
                    size = np.nan

                try:
                    founded = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
                except NoSuchElementException:
                    founded = np.nan

                try:
                    type_of_ownership = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
                except NoSuchElementException:
                    type_of_ownership = np.nan

                try:
                    industry = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
                except NoSuchElementException:
                    industry = np.nan

                try:
                    sector = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
                except NoSuchElementException:
                    sector = np.nan

                try:
                    revenue = driver.find_element(By.XPATH,'//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]').text
                except NoSuchElementException:
                    revenue = np.nan

                try:
                    competitors = driver.find_element(By.XPATH,'.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                except NoSuchElementException:
                    competitors = np.nan
               



            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                headquarters = np.nan
                size = np.nan
                founded = np.nan
                type_of_ownership = np.nan
                industry = np.nan
                sector = np.nan
                revenue = np.nan
                competitors = np.nan

                
            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Headquarters" : headquarters,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            "Competitors" : competitors})
                #add job to jobs

            #Clicking on the "next page" button
        try:
            driver.find_element(By.XPATH,'//*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()
            time.sleep(5)
            #//*[@id="MainCol"]/div[2]/div/div[1]/button[7]

        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
        

    return pd.DataFrame(jobs) 

df = get_jobs('https://www.glassdoor.com/Job/united-states-process-engineer-jobs-SRCH_IL.0,13_IN1_KO14,30.htm?fromAge=3',200,False,5)
df.to_csv(r'C:/Users/user/Desktop/Project/Data/page199.csv', index=False)
print(df.head(5))