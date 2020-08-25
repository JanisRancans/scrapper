from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

for i in range(): # Number of articles
    url = "link_here{}/".format(i)
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    page = urlopen(req)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    try:
        headline = soup.find("article").contents
        lead = soup.find("div", {"class": "article__lead"}).get_text().strip()
        article_body = soup.find("div", {"class": "article__body"}).get_text()
        article = headline[1].get_text() + "\n" + lead + "\n" + article_body + "\n"
        with open('name_of_file.txt', 'a') as f:
            f.write(article)

    except Exception as e:
        pass
