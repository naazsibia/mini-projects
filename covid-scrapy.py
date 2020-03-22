import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup, Tag
import sys

page = requests.get("https://www.worldometers.info/coronavirus/#countries")
soup = BeautifulSoup(page.content, 'html.parser')

countries = []
death_rates = []
total_cases_lst = []
for tr in soup.find_all('tr'):
    country = ""
    value_list = tr.find_all('td')
    if(value_list != []): 
        if(len(value_list[0].contents) > 0 and type(value_list[0].contents[0]) != Tag):
            country = value_list[0].contents[0]
        else: 
            country = value_list[0].contents[0].contents[0]
        total_deaths = value_list[3].contents[0].strip().replace(",", "")
        if total_deaths == "": total_deaths = "0"
        total_cases = value_list[1].contents[0].strip().replace(",", "")
        if total_cases == "": total_cases = "0"
        death_rate = (int(total_deaths) / int(total_cases)) * 100
        if(country not in countries):
            countries.append(country)
            death_rates.append(death_rate)
            total_cases_lst.append(total_cases)




death_df = pd.DataFrame({"Country": countries, "Death Rate": death_rates})
death_df["Death Rate"] = death_df["Death Rate"].astype('int') # convert temperatures to integers
death_df.sort_values("Death Rate",axis = 0, ascending = True, inplace = True, na_position ='last')
death_df.tail(20).plot(kind='barh',x='Country',y='Death Rate',color='red')


total_df = pd.DataFrame({"Country": countries, "Total Cases": total_cases_lst})
total_df["Total Cases"] = total_df["Total Cases"].astype('int')
total_df.sort_values("Total Cases",axis = 0, ascending = True, inplace = True, na_position ='last')
total_df.tail(20).plot(kind='barh',x='Country',y='Total Cases',color='red')
plt.show()