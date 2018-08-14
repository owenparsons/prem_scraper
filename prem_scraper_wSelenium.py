path_to_chromedriver = '/Users/julianashwin/Desktop/text_data_scraper/chromedriver'

import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import requests
import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(path_to_chromedriver)

driver.get("https://www.premierleague.com/stats/top/players/touches")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Create an empty dataframe to fill iteratively
columns = ['player_name','touches', 'year']
touches_df = pd.DataFrame(columns = columns)

for i in range(1,100):

    time.sleep(np.random.uniform(1.5,3))
    #wait = WebDriverWait(driver, 300)
    #ok_button_success = wait.until(EC.element_to_be_clickable((By.css_selector, "div.paginationBtn.paginationNextContainer")))
    print "Scraping page %d" % i

    temp_df = pd.DataFrame(index = range(0,20), columns = columns)

    title =  soup.title.text
    print(title)
    name = soup.find('span', {'class': 'badge-50 LEI '}).text
    print(name)

    player_names = soup.find_all('a', {'class': 'playerName'})
    main_stat = soup.find_all('td', {'class': 'mainStat'})

    player_names_vec = []
    touches_vec = []

    for a in range(0,20):
        temptext = player_names[a].text
        temptext = temptext.encode("utf-8")
        print temptext
        player_names_vec.append(temptext)

        temptext = main_stat[a].text
        temptext = temptext.encode("utf-8")
        touches_vec.append(temptext)

    temp_df.player_name = player_names_vec
    temp_df.touches = touches_vec

    touches_df = touches_df.append(temp_df)

    next_button = driver.find_element_by_css_selector("div.paginationBtn.paginationNextContainer")

    next_button.click()

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")


touches_df.touches = touches_df.touches.str.replace(",","")
touches_df.touches = touches_df.touches.astype(int)

# Plot histogram
plt.hist(touches_df.touches)
plt.show()
