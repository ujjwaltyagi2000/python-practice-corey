from bs4 import BeautifulSoup   
import requests

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml') #lxml is the parser
    #  a parser is a program that parses an HTML document and builds the tree

print(soup.prettify())
# prettify() returns a string containing a formatted version of the XML or HTML document.

print(soup.title) # prints the entire title tag
# <title>Test - A Sample Website</title>

print(soup.title.string) # prints the text within the title tag
# Test - A Sample Website

print(soup.title.name) # prints the name of the tag

match = soup.div # finds the first div tag on the page
print(match)

# finding a specofic div
# all_divs = soup.find('div') # this will find the first div tag and the contents within it
footer = soup.find('div', class_='footer') # class is a keyword in python so class_ is used
print(f"\nHere is the content inside 'footer' div:")
print(footer)

# finding all article headings:
# use inspect element to find the name of the tag
headlines = soup.find_all('h2') # this will find all h2 tags
print(f"\nHere are all the headings:")
print(headlines)
    
# to get the text within the tag
article = soup.find('div', class_='article')
print("\nHere is the content within 'article' div: ")
print(article)

headline = article.h2.a.text # this will get the text within the h2 tag
print("\nHere is the headline: ")
print(headline)

summary  = article.p.text
print("\nHere is the summary: ")
print(summary)

# find() finds the first occurence of the given tag
# find_all() finds all occurences of the given tag

all_articles = soup.find_all('div', class_='article')
print("\nHere are all the articles: ")

index = 1

for article in all_articles:
    headline= article.h2.a.text
    print(f"\nHeadline of Article {index} - {headline} ")

    summary  = article.p.text
    print(f"\nSummary of Article {index} - {summary} ")
    index += 1