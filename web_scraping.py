#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs 

"""
This script extracts the user's Github profile picture by scraping the user's Github page using BeautifulSoup,
a Python library used for web scraping purposes. It prompts the user to input their Github username, and then
searches for the first occurrence of an HTML img tag that has an alt attribute equal to "Avatar" within the 
page's content. Once the image is found, the script prints its URL to the console.
"""


while True:

    username = input('Input the username: ')
    url = 'https://github.com/'+username

    try:
        r = requests.get(url) 
        r.raise_for_status()  #raise an HTTPError if the status code is not 200 OK

        #parse the content of the response and
        #searches for the first occurrence of an HTML img tag 
        #that has an alt attribute equal to "Avatar" within the contenu object 
        contenu = bs(r.content , 'html.parser') 
        image = contenu.find('img', {'alt' : 'Avatar'})['src'] 
        print(image)

        break # exit the loop if no exception occurs

    except :
        print("The username "+username+" doesn't exist. \nMake sure to imput he correct username ")
