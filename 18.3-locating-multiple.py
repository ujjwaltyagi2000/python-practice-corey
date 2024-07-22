# locating multiple elements on a webpage using selenium

# this code will locate item cards from Amazon and store its data in text files, and its HTML in HTML files

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop" # enter your query

'''
steps to find the required URL:
> enter your query on amazon 
> select a page other than the first page, 
> copy the url and place placeholders in the URL to replace query and page as per your requirement
'''

text_file = 1 # text file counter
html_file = 1 # html file counter0

# within this iterator we will move from page 1 to page 4 of the search results and store the data and it's HTML within files
for page in range(1,3): # we can do it for as many pages as we want but we don't want too much clutter in the data folder as of now 

    driver.get(f"https://www.amazon.in/s?k={query}&page={page}&crid=90IDMGCNQ28V&qid=1721550606&sprefix=laptop%2Caps%2C248&ref=sr_pg_2")
    elems = driver.find_elements(By.CLASS_NAME,'puis-card-container') # look at html to find the required class name
    
    print(f"\n{len(elems)} items found on page {page}:\n") 
    
    for elem in elems:
    
        # print(elem.text) # this will show you the data on terminal
        # to save the data in a text file
        with open(f"data/{query}_{text_file}.txt", "w", encoding = "utf-8") as f:
            f.write(elem.text)
            text_file += 1
    
        data = elem.get_attribute("outerHTML")
        # to save the html of the cards in a html file
        with open(f"data/{query}_{html_file}.html", "w", encoding = "utf-8") as f:
            f.write(data)
            html_file += 1

time.sleep(2)
driver.close()