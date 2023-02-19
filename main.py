import requests
from bs4 import BeautifulSoup

#Made with @mustafamret / @mustafamret.dev
#Bu proje @mustafamret / @mustafamret.dev tarafından yapılmıştır.

url = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
pre = soup.find("pre")
text = pre.text
deprem_listesi = text.split("\n")[4:24]

for deprem in deprem_listesi:
print(deprem)
