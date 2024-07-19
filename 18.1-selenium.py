# Beautiful Soup is an HTML and XML parsing library, while Selenium is a browser automation tool that can interact with web sites like a human user. 
# Because Selenium can automate browser actions like clicking buttons, completing forms, and traveling across pages, it thereby offers additional functionality. 
# More constrained, Beautiful Soup is primarily utilized for data extraction and parsing of 'static' web pages.
# When pages are dynamic, you would need Selenium.

# Sample Code from their documentation:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# The selenium.webdriver module provides all the WebDriver implementations. 
# Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote. 
# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc. 
# The By class is used to locate elements within a document.

driver = webdriver.Chrome()
# firefox web driver instance created
driver.get("http://www.python.org")
# The driver.get method  directs the browser to open the specified URL, which is the Python official website in this case.
# WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control to your test or script.

# print(driver.title)

assert "Python" in driver.title
# assert "Python" in driver.title

time.sleep(1) # 3 second delay to see the process slowly
elem = driver.find_element(By.NAME, "q")
# This line finds an element on the page using its name attribute. In this case, it's looking for an input element with the name "q", which is typically the search box on the Python website.

time.sleep(1)
elem.clear()
# This line clears any text currently present in the search box.

time.sleep(3)
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
# These lines type "pycon" into the search box and then simulate pressing the "Enter" key (Keys.RETURN), which submits the search.
time.sleep(3)

assert "No results found." not in driver.page_source
# This line verifies that the phrase "No results found." is not present in the page source. 
# If this phrase is found, an AssertionError will be raised, suggesting that the search did not return any results.

driver.close()
# This line closes the browser window.