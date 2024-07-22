from bs4 import BeautifulSoup
import pandas as pd
import os

query = 'laptop'
# generator to obtain all html files within data directory
files = [f for f in os.listdir("data") if f.endswith(".html")]
headers = ['title', 'price', 'link']
df = pd.DataFrame(columns=headers)

for index, file in enumerate(files):
    with open(f"data/{file}", "r", encoding="utf-8") as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
    
    t = soup.find("h2")
    title = t.get_text()
    l = t.find("a")
    link = "https://amazon.in/" + l['href']
   
    p = soup.find("span", class_="a-offscreen")
    price = p.get_text()
    
    # Add the new row to the DataFrame
    df.loc[index] = [title, price, link]
    
    print(title)
    print(link)
    print(price)
    
print(f"{len(files)} html files found in data directory")
print(df) 
df.to_csv(f"{query}_data.csv")