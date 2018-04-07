import requests
from pyquery import PyQuery as pq
from requests import RequestException

first_page='http://www.lhh1.com/modules/article/reader.php?aid=33&amp;cid=466'
def getFirstPage():
    try:
        response=requests.get(first_page)
        if response.status_code==200:
            response.encoding = 'gbk'
            return response.text
    except RequestException:
        return None
def parseFirstPage(html):
    doc=pq(html)
    print(type(doc))
    links=doc('tr td a')
    items=links.items()
    for item in items:
        link=item.attr('href')
        name=item.text()
        print(link+'--'+name)
        content=getDetailpage(link)
        write2file(name,content)
    print(type(links))
def write2file(name,content):
    nc = name + '\n' + content+'\n'
    with open('novel\jpm.txt','a') as f:
        f.write(nc)
        f.close()
def getDetailpage(link):
    try:
        response=requests.get(link)
        if response.status_code==200:
            response.encoding='gbk'
            doc=pq(response.text)
            content=doc(' #content')
            return content.text()
    except RequestException:
        return None

def main():
    html=getFirstPage()
    if(html==None):
        print("get first page wrong")
        return
    parseFirstPage(html)


if __name__=='__main__':
    main()
