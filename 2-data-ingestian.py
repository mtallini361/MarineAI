import bs4
import requests
from bs4 import BeautifulSoup
#need to input URL of chosen website for data collection.
req = requests.get("INSTALL_WEBSITE_TO_BE_SCRAPED_HERE")

soup = BeautifulSoup(req.content,"html.parser")
#find picture
for img in soup.findAll("img"):
    if img.get("src") != None:
        print (img.get("src"))
        img_url = img.get("src")
        name = img_url.split)"/")[-1]
        img_response = requests.get(img_url)
        #save image to MarineAI_image_bank
        file = open(MarineAI_image_bank, "wb")
        file.write(img_response.content)
        file.close()