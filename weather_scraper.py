import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
page = requests.get("https://weather.gc.ca/canada_e.html")
soup = BeautifulSoup(page.content, 'html.parser')
weatherTable = soup.find(id="wxo-section") # using the div id to find the table with temperatures
items = weatherTable.select("div td")  # using CSS selectors to find each temperature
count = 0 
cities = [] 
temperatures = [] 
for element in items: 
    if count % 3 == 0:
        cities.append(element.get_text()) # found a city

    elif count % 3 == 2:
        temperatures.append(element.get_text()) # corresponding temperature
    count += 1
weather = pd.DataFrame({"City": cities, "Temperature(C)": temperatures}) # creating a dataframe with cities and temperatures
temperature_ints = weather["Temperature(C)"].str.extract(r"(?P<temp_num>\d+)", expand=False)  # extract temperatures using regex
# the P<temp_num part is useless here. But P stands for place holder, and this syntax can be used to refer to groups using their name
weather["Temperature(C)"] = temperature_ints.astype('int') # convert temperatures to integers
weather.sort_values("Temperature(C)",axis = 0, ascending = True, inplace = True, na_position ='last') # sort temperatures in ascending order
weather.plot(kind='barh',x='City',y='Temperature(C)',color='maroon') # plotting a bar graph with sorted temperatures 
plt.subplots_adjust(left=0.35, bottom=0.1, right=0.90, top=0.95, wspace=0.35 , hspace=0.45 ) # adjusting plot's dimensions to make it visible
plt.show()