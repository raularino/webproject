
from urllib.request import urlopen
from bs4 import BeautifulSoup

class BanggoodClient(object):
    """WebClient class"""
    def __init__(self):
        super(BanggoodClient,self).__init__()

    def download_page(self, url):
        #connect to the web site
        f = urlopen(url)
        #get the download_page
        page = f.read()
        #close the connection
        f.close()
        return page

    def search_products(self, page):
        tree=BeautifulSoup(page,'lxml')
        ul=tree.find("ul", "goodlist_1")
        li=ul.find_all("li")
        prices_list=[]
        titles_list=[]
        for item in li:
            #process item
            price=item.find("span","price")
            price_old=item.find("span","price")
            title=item.find("span","title")
            prices_list.append((price['oriprice']))
            titles_list.append((title.text))
            print(title.text + " NORMAL PRICE: " + price_old['oriprice'] + " OFFER: " + price['oriprice'] + "\n")

        return prices_list,titles_list

    def run(self):
    #download a web page
        page = self.download_page("https://www.banggood.com/es/Flashdeals.html")
        data=self.search_products(page)
    #search activities in web page
    #print the activities
        #print(data)

if __name__ == "__main__" :
    c = BanggoodClient()
    c.run()
