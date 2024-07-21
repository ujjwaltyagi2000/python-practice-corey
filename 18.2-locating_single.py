# locating single elements on a webpage using selenium
# Beautiful Soup is an HTML and XML parsing library, while Selenium is a browser automation tool that can interact with web sites like a human user. 
# Because Selenium can automate browser actions like clicking buttons, completing forms, and traveling across pages, it thereby offers additional functionality. 
# More constrained, Beautiful Soup is primarily utilized for data extraction and parsing of 'static' web pages.
# When pages are dynamic, you would need Selenium.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=90IDMGCNQ28V&sprefix=laptop%2Caps%2C248&ref=nb_sb_noss_1")
elem = driver.find_element(By.CLASS_NAME,'puis-card-container') # look at html to find the required class name
# this class contains card of an item
print("The name of the item is:")
print(elem.text)
print("\nThe outer HTML of the element looks like this:\n")
print(elem.get_attribute("outerHTML"))
time.sleep(4)
driver.close()
# a good practice while scraping 100s of webpages is to first get their HTML, save it locally, and then use it to find the required data.
# this is exactly what we'll try to do with a few more scripts