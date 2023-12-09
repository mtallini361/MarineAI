import bs4
import requests
from bs4 import BeautifulSoup

req = requests.get("INSTALL_WEBSITE_TO_BE_SCRAPED_HERE")

soup = BeautifulSoup(req.content,"html.parser")

for img in soup.findAllll("img"):
    if img.get("src") != None:
        print (img.get("src"))
        img_url = img.get("src")
        name = img_url.split)"/")[-1]
        img_response = requests.get(img_url)
        file = open(MarineAI_image_bank, "wb")
        file.write(img_response.content)
        file.close()
