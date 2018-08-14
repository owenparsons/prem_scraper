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
from bs4 import BeautifulSoup

driver = webdriver.Chrome(path_to_chromedriver)

driver.get("https://www.premierleague.com/stats/top/players/touches")

html = driver.page_source

soup = BeautifulSoup(html)



url_pagination = "https://www.premierleague.com/stats/top/players/touches"
r = requests.get(url_pagination)
soup = BeautifulSoup(r.content, "html.parser")

for i in range(1,100):
    print "Scraping page %d" % i

    temp_df = pd.DataFrame()

    title =  soup.title.text
    print(title)
    name = soup.find('span', {'class': 'badge-50 LEI '}).text
    print(name)

    player_names = soup.find_all('a', {'class': 'playerName'})

    player_names_vec = np.chararray((20,1))

    for (a,b) in player_names:
        player_names_vec[[]] = a.text

    main_stat = soup.find_all('td', {'class': 'mainStat'})
    for a in main_stat:
        print(a.text)

    next_button = driver.find_element_by_css_selector("div.paginationBtn.paginationNextContainer")

    next_button.click()
