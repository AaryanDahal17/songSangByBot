from bs4 import BeautifulSoup

with open('query.txt','r',encoding='utf-8') as ffs:
    daData = ffs.read()
    if daData == "none":
        exit()

with open('dahtml.txt', 'r',encoding='utf-8') as file:
    lyricsData = file.read()



soup = BeautifulSoup(lyricsData, 'html.parser')



div_element = soup.findAll('div', class_ = 'Lyrics__Container-sc-1ynbvzw-5 Dzxov')  



filee = open('lyrics.txt','w',encoding='utf-8')
    

indd = 0


for lyrsDiv in div_element:

    indd += 1
    daData = lyrsDiv.get_text()
    filee.write(daData)

    fullLyrics = lyrsDiv.findAll('span',class_ = 'ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw')


    for index,elem in enumerate(fullLyrics):
        daText = elem.get_text()
        # print(daText)
        daString = str(elem)

        
        # if '<br/>' in daString:
        #     trimmedString = daString.replace('<span class="ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw">','').replace('</span>','')
        #     daRealTrim = trimmedString
        #     if "<i>" in trimmedString:
        #         daRealTrim = trimmedString.replace('<i>','').replace('</i>','')
        #     daParts = daRealTrim.split('<br/>')
        #     for part in daParts:
        #         filee.write(f"{part} \n")
            
        # else:
        #     filee.write(f"{daText} \n")

    filee.write("\n")

filee.close()

print("Lyrics added to file successfully.")


