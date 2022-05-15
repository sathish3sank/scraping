from constant import flipkart, FlipkartLiterals, Scrap
from bs4 import BeautifulSoup


from scrap.scrap.utils.index import get_url

def getTitleWithDivAndClass(soup : BeautifulSoup) -> str:
    title : str = ''
    for titleClass in flipkart.get(FlipkartLiterals.TITLE):
        title += soup.find('div', attrs= { 'class' : titleClass })
        break
    return title != '' if title else 'None'

def getImageWithDivAndClass(soup : BeautifulSoup) -> str:
    image : str = ''
    for imgClass in flipkart.get(FlipkartLiterals.IMAGE):
        image += soup.find('div', attrs= { 'class' : imgClass })
        break
    return image != '' if image else 'None'

def getPriceWithDivAndClass(soup : BeautifulSoup) -> str:
    price : str = ''
    for priceClass in flipkart.get(FlipkartLiterals.PRICE):
        price += soup.find('div', attrs= { 'class' : priceClass })
        break
    return price != '' if price else 'None'

def getURLWithDivAndClass(soup : BeautifulSoup) -> str:
    url : str = ''
    for urlClass in flipkart.get(FlipkartLiterals.URL):
        url += soup.find('div', attrs= { 'class' : urlClass })
        break
    return url != '' if url else 'None'

def getDescriptionWithDivAndClass(soup : BeautifulSoup) -> str:
    desc : str = ''
    for descClass in flipkart.get(FlipkartLiterals.DESCRIPTION):
        desc += soup.find('div', attrs= { 'class' : descClass })
        break
    return desc != '' if desc else 'None'

def makeScrap(soup : BeautifulSoup) -> Scrap:
    return {
        'title' : getTitleWithDivAndClass(soup),
        'image' : getImageWithDivAndClass(soup),
        'description' : getDescriptionWithDivAndClass(soup),
        'price' : getPriceWithDivAndClass(soup),
        'url' : getURLWithDivAndClass(soup)
    }

def flipkartScraping(url : str, soup : BeautifulSoup) -> Scrap:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    res = get_url(url, headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    return makeScrap(soup)
