# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import itertools

fname = input("Enter generated URL file: ")
if len(fname) < 1:
    fname = "all_url_test.txt"

try:
    fhand = open(fname)
except:
    print('Generated URL is invalid. Please try again.')
    quit()

print ('Initializing Chromedriver......')
options = webdriver.ChromeOptions()

#Disabling Images in Chrome
chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
options.add_experimental_option('prefs', chrome_prefs)

#Ignore all Chrome messages except fatal errors #default --long-level=0
options.add_argument('--log-level=3')
#launch Chrome without gui browser window 800x600 in default size
options.add_argument('headless')
#option"S".XXXXXXXXX not option

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

n = 0 # no of link counters
print ("------Chromedriver Loaded------")

for line in fhand:
    #new lists in for loop
    ls_position = list()
    ls_title = list()
    ls_artist = list()
    ls_stream = list()

    stripped_line = line.strip() #link
    url = str(stripped_line)
    date = url.split("/")[6]
    country = url.split("/")[4]
    filename = country+'_'+date

    try:
        driver.get(url)
        # wait for the page to load
    except:
        print('Data Sprawling Error Found. Please initialize the app again.')

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr[1]/td[5]/')))
    except:
        print('Response expired...')

    #positions in the chart
    positions = driver.find_elements(By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr/td[2]')
    for position in positions:
        ls_position.append(position.text)

    #song titles in the chart
    titles = driver.find_elements(By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr/td[4]/strong')
    for title in titles:
        if len(title.text) < 1:
            title = 'nil'
            ls_title.append(title)
        else:
            ls_title.append(title.text)

    #artists in the chart
    artists = driver.find_elements(By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr/td[4]/span')
    for artist in artists:
        if len(artist.text) < 1:
            artist = 'nil'
            ls_artist.append(artist)
            print ('Empty cell found.')
        else:
            ls_artist.append(artist.text)

    #streams in the chart
    streams = driver.find_elements(By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr/td[5]')
    for stream in streams:
        ls_stream.append(stream.text)

    group = zip (ls_position, ls_title, ls_artist, ls_stream)
    dataset = list (group)

    print ("=======Writing to CSV=======")

    # Use file to refer to the file object
    with open('%s.csv' % filename,'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Position', 'Track Name', 'Artist', 'Streams'])
        writer.writerows(dataset)
        n = n + 1
        print ("Finished", n)

driver.close() #close the browser
print (n, "dataset done.")
