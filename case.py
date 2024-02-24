import random
from player import *

import requests
from bs4 import BeautifulSoup

color_earnings = [0.1, 1.2, 8, 60, 500]
colors = {"Blue": '🟦', "Purple": '🟪', "Pink": '🟫', "Red": '🟥', "Yellow": '🟨'}
arrow = '⬅️'

cases = []

def create_case(num):
    case_ = []
    for i in range(num):
        count = 0
        temp_colors = ['Blue', 'Purple', 'Pink', 'Red']
        for k in range(3):
            if(random.randint(1, 5) == 3):
                count += 1
            else:
                break
        case_.append(temp_colors[count])
    return case_

def get_gun(self, case_name, item_name):
    pass

def scrapeAllItemInformation():
    stickers_url = "https://wiki.cs.money/capsules"
    cases_url = 'https://wiki.cs.money/cases'
    souv_url = 'https://wiki.cs.money/souvenir-packages'

    stickers_response = requests.get(stickers_url)
    if stickers_response.status_code == 200:
        soup = BeautifulSoup(stickers_response.text, 'html.parser')
        test = soup.find('div', class_='kxmatkcipwonxvwweiqqdoumxg')
        print(test)

class Case:

    #names include actual case name and shortened names that make it easier to open cases
    def __init__(self, names, type, img_url, item_url):
        self.names = names
        self.type = type
        self.img_url = img_url
        self.item_url = item_url
        self.createItemHolders(item_url)

    def createItemHolders(self, file_name):
        with open(file_name, 'r') as file:
            pass

    def createItem(self, rarity):
        pass
    

# url = 'https://wiki.cs.money/cases'
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # # Find and extract the information you need
#     #print(soup.contents)
#     name_and_prices = soup.find('div', class_='gasovxczmdwrpzliptyovkjrjp').text
#     cases = soup.find('div', class_='gasovxczmdwrpzliptyovkjrjp')
#     individual_cases = cases.find('div', class_='kxmatkcipwonxvwweiqqdoumxg')
#     #print(individual_cases)
#     print(name_and_prices)

