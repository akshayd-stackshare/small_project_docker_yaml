import json
import pprint
import traceback
from datetime import datetime

from src.data_infrastructure.rabbitmq.service import RabbitMQService
from src.system.models.input import ScrapeRequest

if __name__ == '__main__':
    # create an input object to test against
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

    data = {
        "url": "https://www.yahoo.com",
        "time_requested": str(datetime.utcnow().isoformat())
    }
    test_request = json.dumps(ScrapeRequest(**data).model_dump(), default=str)
    print(test_request)
    print(type(test_request))
    rabbit_service = RabbitMQService()
    rabbit_service.publish('input_queue', test_request)

    # Print the lists to verify
    for key, urls in news_urls.items():
        print(f"{key}:\n{'-' * 20}")
        for _url in urls:
            try:
                data = {
                    "url": _url,
                    "time_requested": str(datetime.utcnow().isoformat())
                }
                test_request = json.dumps(ScrapeRequest(**data).model_dump(), default=str)
                print(test_request)
                print(type(test_request))
                rabbit_service = RabbitMQService()
                rabbit_service.publish('input_queue', test_request)
                pprint.pprint(_url)
            except:
                traceback.print_exc()
                pass