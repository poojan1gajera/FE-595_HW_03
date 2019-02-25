####Importing Libraries
import requests
from requests import get
from requests import post
from bs4 import BeautifulSoup

def web_scraper(url):
    Male= open("Male.txt","w+")
    Female=open("Female.txt","w+")
    for i in range(0,50):
        get_req=get(url)
        soup = BeautifulSoup(get_req.text, "html.parser")
        links = soup.select("center p")
        texts=links[0].get_text()
        list_split=texts.split("She")
        Male.write(list_split[0]+"\n")
        Female_split=('She'+list_split[1]).split(".")
        Female.write(Female_split[0]+"\n")

    Male.close()
    Female.close()

if __name__=="__main__":
    web_scraper("https://theyfightcrime.org/")
