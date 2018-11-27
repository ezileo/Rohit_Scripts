# URL: http://www.practicepython.org/
# Author: Rohit Gupta
# Date Scheduled: September 01, 2017
# Date Written: November 27, 2018
# Version 1.0
# Problem Exercise: 17
import datetime
import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    print(r)
    r_html = r.text
    # print(r_html)
    # soup_1 = BeautifulSoup(r_html)
    soup_2 = BeautifulSoup(r_html, 'html.parser')
    # print(soup_1)
    # print(soup_2)
    # print(soup_2.prettify())
    print(soup_2.title)
    for link in soup_2.find_all('a'):
        print(link.get('href'))
        print(len(link.get('href')))
        # print(soup_2.get_text())
    for headings in soup_2.find_all('h2'):
        print(headings.text)
        print(len(headings.text))


if __name__ == '__main__':
    print("Welcome to the programme to Decode a WebPage")
    user_name = input("Please enter your name: ")
    print("The programme was run on: ", datetime.datetime.now())
    print("Your interaction with the script starts {} . . . . .".format(user_name))
    main()