"""
Scrape les pages de BRA et les sauvegardes. Les métadonnées sont sauvegardé dans une base sqlite.
"""
from scrapy import Spider
from urllib.parse import urljoin
from datetime import datetime

BASE_URL = "https://www.meteofrance.com/previsions-meteo-montagne/bulletin-avalanches/"
REGION_LIST = [
"chablais",
"aravis",
"mont-blanc",
"bauges",
"beaufortin",
"haute-tarentaise",
"chartreuse",
"belledonne",
"maurienne",
"vanoise",
"haute-maurienne",
"grandes-rousses",
"thabor",
"vercors",
"oissans",
"pelvoux",
"queyras",
"devoluy",
"champsaur",
"embrunnais-parpaillon",
"ubaye",
"haut-var-haut-verdon",
"mercantour",
]

def to_two_digit(number: int) -> str:
    assert isinstance(number, int)
    if number >=10:
        return str(number)
    else:
        return str(f'0{number}')

def get_urls():
    rlist = []
    for i, x in enumerate(REGION_LIST, start=1):
        opp_number = to_two_digit(i)
        rlist.append(urljoin(BASE_URL, f'{x}/OPP{opp_number}'))
    return rlist


class BraScrapper(Spider):
    name = "bra-html"
    start_urls = get_urls()

    def parse(self, response):
        bra = response.selector.xpath('//div[@id="BRA"]').get()
        page  = response.url.split('/')[-2]
        date = datetime.now().strftime('%Y-%m-%d')
        with open(f"{date}-{page}.html", 'w') as f:
            f.write(bra)
        self.log(f'saved file {page}.html')






