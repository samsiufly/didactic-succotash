# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import itertools

fname = input("Enter file:")
if len(fname) < 1:
    fname = "url_set.txt"
fhand = open(fname)

n = 0   # no of link counters

def selenium_spotify(url, date):
    options = webdriver.ChromeOptions()
    #Ignore all Chrome messages except fatal errors #default --long-level=0
    options.add_argument('--log-level=3')
    #launch Chrome without gui browser window 800x600 in default size
    options.add_argument('headless')
    #option"S".XXXXXXXXX not option
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(url)
    print("Retrieving data: ", driver.title)
    print("================================================")

    ls_position = list()
    ls_title = list()
    ls_artist = list()
    ls_stream = list()

    #positions in the chart
    positions = driver.find_elements(By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr/td[2]')
    for position in positions:
        ls_position.append(position.text)

    #song titles in the chart
    titles = driver.find_elements(By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr/td[4]/strong')
    for title in titles:
        ls_title.append(title.text)

    #artists in the chart
    artists = driver.find_elements(By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr/td[4]/span')
    for artist in artists:
        ls_artist.append(artist.text)

    #streams in the chart
    streams = driver.find_elements(By.XPATH, './/*[@id="content"]/div/div/div/span/table/tbody/tr/td[5]')
    for stream in streams:
        ls_stream.append(stream.text)

    group = zip (ls_position, ls_title, ls_artist, ls_stream)
    dataset = list (group)

    print ("=====Writing to CSV=====")
    #driver.close() #close the tab only .quit = quit browser
    driver.close() #close the browser

    # Use file to refer to the file object
    with open('%s.csv' % date,'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Position', 'Track Name', 'Artist', 'Streams'])
        writer.writerows(dataset)

for line in fhand:
    stripped_line = line.strip() #links
    url = str(stripped_line)
    date = url.split("/")[6]
    selenium_spotify(url, date)
    n = n + 1
    print ("Finished", n)
print (n, "of dataset done.")
