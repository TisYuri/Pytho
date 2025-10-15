import requests # you need this module to make an API call
import pandas as pd
api_url = "http://api.open-notify.org/astros.json" # this url gives use the astronaut data
response = requests.get(api_url) # Call the API using the get method and store the
                                # output of the API call in a variable called response.
if response.ok:             # if all is well() no errors, no network timeouts)
    data = response.json()  # store the result in json format in a variable called data
                            # the variable data is of type dictionary.
print(data)   # print the data just to check the output or for debugging
print(data.get('number'))
astronauts = data.get('people')
print("There are {} astronauts on ISS".format(len(astronauts)))
print("And their names are :")
for astronaut in astronauts:
    print(astronaut.get('name'))
#Import required libraries
import pandas as pd
import json
api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
response = requests.get(api_url)
if response.ok:           
    data = response.json() 
    
technologies = [
    "C", "C#", "C++", "Java", "JavaScript", "Python", "Scala",
    "Oracle", "SQL Server", "MySQL Server", "PostgreSQL", "MongoDB"
]
api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
response = requests.get(api_url)
if response.ok:           
    data = response.json() 

def get_number_of_jobs_T(technology):
    number_of_jobs = 0
    for job in data:
        if technology.lower() in job.get("Key Skills", "").lower():
            number_of_jobs += 1
    return technology, number_of_jobs

get_number_of_jobs_T("Python")

def get_number_of_jobs_L(location):
    number_of_jobs = 0
    for job in data:
        if location.lower() in job.get("Location", "").lower():
            number_of_jobs += 1
    return location, number_of_jobs
get_number_of_jobs_L("Los Angeles")

results = [get_number_of_jobs_T(tech) for tech in technologies]

#pip install openpyxl

import pandas as pd

df = pd.DataFrame(results, columns=["Technology", "Number of Jobs"])
df.to_excel("job-postings.xlsx", index=False)
print("Excel file 'job-postings.xlsx' created successfully!")
