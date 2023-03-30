import requests
from bs4 import BeautifulSoup as bs 

# BeautifulSoup is a Python library used for web scraping purposes. 
# It allows you to extract data from HTML and XML files by parsing the HTML/XML documents
# and providing you with a navigable tree-like structure of the document.

while True:

    username = input('Input the username: ')
    url = 'https://github.com/'+username

    try:
        r = requests.get(url) #send get request,  the status code should be  "200 OK"
        r.raise_for_status()  #raise an HTTPError if the status code is not 200 OK

        contenu = bs(r.content , 'html.parser')
        image = contenu.find('img', {'alt' : 'Avatar'})['src']
        print(image)

        break # exit the loop if no exception occurs

    except :
        print("The username "+username+" doesn't exist. \nMake sure to imput he correct username ")
