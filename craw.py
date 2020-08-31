from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from multiprocessing import Process, Queue
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Scrapper:

    def __init__(self, name, range):
        self.name = name
        self.range = range
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                'referer': 'https://...'
                }

    def scrape(self):

        counter = 0
        for i in range(self.range):
            url = "url.{}/".format(self.range+i)
            req = Request(url, headers=self.headers)

            try:
                page = urlopen(req)
                html = page.read().decode("utf-8")
                soup = BeautifulSoup(html, "html.parser")

                try:
                    headline = soup.find("article").contents
                    lead = soup.find("div", {"class": "article__lead"}).get_text().strip()
                    article_body = soup.find("div", {"class": "article__body"}).get_text()
                    article = headline[1].get_text() + "\n" + lead + "\n" + article_body + "\n"
                    with open('{}.txt'.format(self.name), 'a') as f:
                        f.write(article)

                except Exception as e:
                    print(e)

                counter = counter + 1
                print("Process {} scrapped {} articles".format(self.name, counter))

            except Exception as e:
                print(e)

            time.sleep(20)

if __name__ == "__main__":
    queue = Queue()

    scrapper = [Scrapper(input(), int(input())) for x in range(20)]
    processes = [Process(target=scrapper.scrape, args=()) for scrapper in scrapper]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
