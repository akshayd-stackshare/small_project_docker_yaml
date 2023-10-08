# create pipenv
# e.g.
# (url_fetcher_service) clu@clu-ThinkPad-P15-Gen-2i:~/Projects/url_fetcher_service/src$
# PYTHONPATH=../src/ python cli/cli.py create-scrape-job
import pprint
import os

from cli.utils import create_scrape_job, create_scrape_request
from settings import SRC_DIR

news_urls = {
    "North America": [
        "https://www.cnbc.com/",
        "https://www.bloomberg.com/",
        "https://www.wsj.com/",
        "https://www.businessinsider.com/",
        "https://fortune.com/",
        "https://www.forbes.com/",
        "https://www.marketwatch.com/",
        "https://www.nasdaq.com/",
        "https://www.bnnbloomberg.ca/",
        "https://www.barrons.com/"
    ],
    "South America": [
        "https://www.valor.com.br/",
        "https://www.infobae.com/",
        "https://www.larepublica.co/",
        "https://www.ambito.com/",
        "https://www.cronista.com/",
        "https://www.eleconomistaamerica.com/",
        "https://www.gestion.pe/",
        "https://www.pulso.cl/",
        "https://www.portafolio.co/",
        "https://www.elobservador.com.uy/"
    ],
    "Europe": [
        "https://www.ft.com/",
        "https://www.economist.com/",
        "https://www.bbc.com/news/business",
        "https://www.reuters.com/",
        "https://www.handelsblatt.com/english/",
        "https://www.lesechos.fr/",
        "https://elpais.com/economia/",
        "https://www.ilsole24ore.com/",
        "https://www.borsen.dk/",
        "https://www.rte.ie/news/business/"
    ],
    "Africa": [
        "https://www.businesslive.co.za/bd/",
        "https://www.moneyweb.co.za/",
        "https://www.businessdailyafrica.com/",
        "https://www.nairobibusinessmonthly.com/",
        "https://northafricapost.com/",
        "https://www.businessamlive.com/",
        "https://www.theafricareport.com/",
        "https://africanbusinessmagazine.com/",
        "https://www.businesstech.co.za/",
        "https://www.businessghana.com/"
    ],
    "Asia": [
        "https://asia.nikkei.com/",
        "https://www.caixinglobal.com/",
        "https://economictimes.indiatimes.com/",
        "https://www.straitstimes.com/business",
        "https://www.scmp.com/business",
        "https://www.thejakartapost.com/business",
        "https://www.arabnews.com/business-economy",
        "https://www.hindustantimes.com/business-news/",
        "https://www.businesstimes.com.sg/",
        "https://www.bangkokpost.com/business"
    ],
    "Australia/Oceania": [
        "https://www.afr.com/",
        "https://www.smh.com.au/business",
        "https://www.nzherald.co.nz/business/",
        "https://www.theaustralian.com.au/business/",
        "https://www.abc.net.au/news/business/",
        "https://www.businessnews.com.au/",
        "https://www.stuff.co.nz/business",
        "https://www.rnz.co.nz/news/business",
        "https://www.fijitimes.com/business/",
        "https://www.samoatimes.co.nz/"
    ],
    "social_media": [
        'https://www.yahoo.com',
        'https://www.facebook.com',
        'https://www.tiktok.com',
        'https://www.twitter.com',
        'https://www.instagram.com'
    ]
}

if __name__ == "__main__":
    import subprocess

    test_urls = ["https://old.reddit.com"]
    # Print the lists to verify
    for key, urls in news_urls.items():
        print(f"{key}:\n{'-' * 20}")
        for _url in urls:
            test_urls.append(_url)

    # Environment variables
    env = os.environ.copy()
    env['PYTHONPATH'] = SRC_DIR

    # Command sequence
    commands = [create_scrape_request(url=u) for u in test_urls]
    commands.extend([create_scrape_job(url=u) for u in test_urls])

    stuffs = [subprocess.run(c, env=env) for c in commands]
    pprint.pprint(stuffs)
