import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from unidecode import unidecode



chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")

webdriver_service = Service('/path/to/chromedriver')

user_input = input("Enter the song name: ")

songName = ' '.join(user_input.split())

partsOfName = songName.split(' ')

urlLink = "https://genius.com/search?q="

for index,part in enumerate(partsOfName):
    if (index == 0):
        urlLink += f"{part}"
    else:
        urlLink += f"%20{part}"

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

os.system('cls')

driver.get(urlLink)



card_elements = driver.find_elements(By.CLASS_NAME, 'mini_card-title_and_subtitle')

titles = [card.find_element(By.CLASS_NAME, 'mini_card-title').text.strip() for card in card_elements]

subTitles = [card.find_element(By.CLASS_NAME, 'mini_card-subtitle').text.strip() for card in card_elements]

os.system('cls')
print("On process...")

driver.quit()


if len(titles) == 0:
    with open('query.txt','w') as ffile:
        ffile.write("none")
    exit()

for index,title in enumerate(titles):
    print(f"{index+1}. {title}")
    print(f"- {subTitles[index]} ")

    if (index == 4):
        break


input_number = input("Input the number , whose lyrics you want : " )


def writeInFile(user_input):
    userr_input = int(user_input)

    songName = titles[userr_input - 1]
    artistName = subTitles[userr_input-1]

    mix = artistName + '-' + songName

    decmix = unidecode(mix)

    combo = ' '.join(decmix.split())

    trimmedCombo = combo.capitalize().replace(' ','-').replace('&','and')

    searchQuery = trimmedCombo.replace('.','').replace("'",'').replace('(','').replace(')','').replace('\u2019','')

    searchQuery = 'https://genius.com/' + searchQuery + '-lyrics'

    with open('query.txt','w') as ffile:
        ffile.write(searchQuery)


if input_number.isdigit() and 1 <= int(input_number) <= 5:
    writeInFile(input_number)
    
else:
    loopin = True
    while loopin:


        input_numberr = input("Invalid input , select from 1 - 5 : ")

        if input_numberr.isdigit() and 1 <= int(input_numberr) <= 5:
            loopin = False
            writeInFile(input_numberr)


        




# import requests
# from bs4 import BeautifulSoup

# url = 'https://genius.com/search?q=beautiful%20mistakes'

# # Send a GET request to the URL
# response = requests.get(url)

# # Get the HTML content
# html_content = response.text

# # Create a Beautiful Soup object
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all div elements with class 'mini_class-title'
# div_elements = soup.find_all('div', class_='mini_card-info')


# print(div_elements)
# # # Store the titles in an array
# # titles = [div.text.strip() for div in div_elements]

# # # Print the array of titles
# # print(titles)
