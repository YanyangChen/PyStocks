import requests
from bs4 import BeautifulSoup

proxies = {
'http': 'http://adb.def.hk:8080/',
}

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print(list(soup.children))
print([type(item) for item in list(soup.children)])
html = list(soup.children)[2]
body = list(html.children)[3]
print(list(body.children))
p = list(body.children)[1]
print(p.get_text())
p.get_text()
# print(page.content)