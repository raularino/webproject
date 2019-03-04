
from urllib.request import urlopen
from bs4 import BeautifulSoup

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient,self).__init__()

    def download_page(self, url):
        #connect to the web site
        f = urlopen(url)
        #get the download_page
        page = f.read()
        #close the connection
        f.close()
        return page

    def search_activities(self, page):
        tree=BeautifulSoup(page,'lxml')
        activities=tree.find_all("div", "featured-links-item")

        act_list=[]
        for activity in activities:
           title=activity.find("span", "flink-title")
           link=activity.find("a")
           act_list.append((title.text, link["href"]))
        return act_list

    def run(self):
    #download a web page
        page = self.download_page("http://www.eps.udl.cat/ca")
        data=self.search_activities(page)
    #search activities in web page
    #print the activities
        print(data)

if __name__ == "__main__" :
    c = WebClient()
    c.run()

