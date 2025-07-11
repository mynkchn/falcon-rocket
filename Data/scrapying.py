import numpy as np
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json
import time
import re
import unicodedata

headers=[]

# scrapying using beautiful soup
def scrape_bs4(url):
    if url is not None:
        try:
         response=requests.get(url,headers=headers)
         response.raise_for_status()
         soup=BeautifulSoup(response.text,'html.parser')
         return soup
        except Exception as e:
           return f'Error occured due to {e}'
    else :
       return None

# scrapying using selenium
def scrape_sel(url):
   if url is not None:
      try :
         driver=webdriver.Chrome()
         driver.get(url)
         time.sleep(5)
         page_source=driver.page_source
         soup=BeautifulSoup(page_source,'html.parser')
         return soup
      except Exception as e:
         return f'Error occured due to {e}'
   else :
      return None

def date_time(table_cells):
   return [date_time.strip() for date_time in list(table_cells.strings)][0:2]

def booster_version(table_cells):
   out=''.join([booster_version for i,booster_version in enumerate(table_cells.strings) if i%2==0][0:-1])
   return out

def landing_status(table_cells):
   out=[i for i in table_cells.strings][0]
   return out

def get_mass(table_cells):
   mass=unicodedata.normalize('NFKD',table_cells.text).strip()
   if mass :
      mass.find('kg')
      new_mass=mass[0:mass.find('kg')+2]
   else :
      new_mass=0
   return new_mass

def extract_column_from_header(row):
   if (row.br):
      row.br.extract()
   if row.a:
      row.a.extract()
   if row.sup():
      row.sup.extract()
   column_name=' '.join(row.contents)

   if not(column_name.strip().isdigit()):
      column_name=column_name.strip()
      return column_name
   
static_url = "https://en.wikipedia.org/w/index.php?title=List_of_Falcon_9_and_Falcon_Heavy_launches&oldid=1027686922"
soup=scrape_bs4(static_url)

# lets find tables 
html_tables=soup.find_all('table')

# first launch table
first_launch_table=html_tables[2]

# column names
column_names=[]

# find_all with th
for name in first_launch_table.find_all('th'):
   if name is not None and len(name)>0 :
      column_names.append(name.text.strip())


# lets create dataframe
launch_dict=dict.fromkeys(column_names)

# remove an irrelvant column 
# del launch_dict['Date and time ( )']


# Let's initial the launch_dict with each value to be an empty list
launch_dict['Flight No.'] = []
launch_dict['Launch site'] = []
launch_dict['Payload'] = []
launch_dict['Payload mass'] = []
launch_dict['Orbit'] = []
launch_dict['Customer'] = []
launch_dict['Launch outcome'] = []
# Added some new columns
launch_dict['Version Booster']=[]
launch_dict['Booster landing']=[]
launch_dict['Date']=[]
launch_dict['Time']=[]


extracted_row = 0

#Extract each table 
for table_number,table in enumerate(soup.find_all('table',"wikitable plainrowheaders collapsible")):
   # get table row 
    for rows in table.find_all("tr"):
        #check to see if first table heading is as number corresponding to launch a number 
        if rows.th:
            if rows.th.string:
                flight_number=rows.th.string.strip()
                flag=flight_number.isdigit()
        else:
            flag=False
        #get table element 
        row=rows.find_all('td')
        #if it is number save cells in a dictonary 
        if flag:
            extracted_row += 1
            # Flight Number value
           
            # TODO: Append the flight_number into launch_dict with key `Flight N.`
            launch_dict['Flight No.'].append(flight_number)
            datatimelist=date_time(row[0])
            
            # Date value
            # TODO: Append the date into launch_dict with key `Date`
            date = datatimelist[0].strip(',')
            launch_dict['Date'].append(date)
            #print(date)
            
            # Time value
            # TODO: Append the time into launch_dict with key `Time`
            time = datatimelist[1]
            launch_dict['Time'].append(time)
            #print(time)
              
            # Booster version
            # TODO: Append the bv into launch_dict with key `Version Booster`
            bv=booster_version(row[1])
            if not(bv):
                bv=row[1].a.string
            launch_dict['Version Booster'].append(bv)
            # print(bv)
            
            # Launch Site
            # TODO: Append the bv into launch_dict with key `Launch Site`
            launch_site = row[2].a.string
            launch_dict['Launch site'].append(launch_site)
            #print(launch_site)
            
            # Payload
            # TODO: Append the payload into launch_dict with key `Payload`
            payload = row[3].a.string
            launch_dict['Payload'].append(payload)
            #print(payload)
            
            # Payload Mass
            # TODO: Append the payload_mass into launch_dict with key `Payload mass`
            payload_mass = get_mass(row[4])
            launch_dict['Payload mass'].append(payload_mass)
            #print(payload)
            
            # Orbit
            # TODO: Append the orbit into launch_dict with key `Orbit`
            orbit = row[5].a.string
            launch_dict['Orbit'].append(orbit)            
            #print(orbit)
            
            # Customer
            # TODO: Append the customer into launch_dict with key `Customer`
            customer = row[6].a.string if row[6].a is not None else None
            launch_dict['Customer'].append(customer)
            print(customer)
            
            # Launch outcome
            # TODO: Append the launch_outcome into launch_dict with key `Launch outcome`
            launch_outcome = list(row[7].strings)[0]
            launch_dict['Launch outcome'].append(launch_outcome)
            #print(launch_outcome)
            
            # Booster landing
            # TODO: Append the launch_outcome into launch_dict with key `Booster landing`
            booster_landing = landing_status(row[8])
            launch_dict['Booster landing'].append(booster_landing)
            #print(booster_landing)

df= pd.DataFrame({ key:pd.Series(value) for key, value in launch_dict.items() })
df.to_csv('spacex_web_scraped.csv',index=False)
print(df.head())