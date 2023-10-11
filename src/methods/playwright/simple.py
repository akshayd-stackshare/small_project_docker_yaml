import io
import pprint
import traceback
import uuid
from datetime import datetime
from uuid import UUID

from playwright.sync_api import sync_playwright

from src.data_infrastructure.arangodb.shared.pydantic.write import write_pydantic_to_arangodb
from src.metadata.database.object_storage.har.upload import har_upload_to_minio
from src.metadata.database.object_storage.html.upload import html_upload_to_minio
from src.metadata.database.object_storage.screenshot.upload import screenshot_upload_to_minio

from src.metadata.transform.har.convert import har_url_to_filename
from src.metadata.transform.html.write import write_html_to_file
from src.metadata.transform.shared.convert import get_filename
from src.metadata.transform.html.convert import html_url_to_filename
from src.metadata.transform.screenshot.convert import screenshot_url_to_filename

from src.system.models.errors import ScrapeError
from src.system.models.urls import URLMetadata


def download_url(url: str, correlation_id: UUID) -> URLMetadata:
    with sync_playwright() as p:
        browser = p.chromium.launch()

        screenshot_path = screenshot_url_to_filename(url)
        screenshot_object_name = get_filename(screenshot_path)

        html_path = html_url_to_filename(url)
        html_object_name = get_filename(html_path)

        har_path = har_url_to_filename(url)
        har_object_name = get_filename(har_path)

        pprint.pprint([
            'Object Names:',
            html_object_name,
            har_object_name,
            screenshot_object_name
        ])

        pprint.pprint([
            'File Names:',
            html_path,
            screenshot_path,
            har_path
        ])

        # capture HAR file
        context = browser.new_context(record_har_path=har_path,
                                      viewport={"width": 1920, "height": 1080})

        # create new page
        page = context.new_page()

        # Navigate to the URL
        page.goto(url)

        # Capture screenshot
        # take screenshot
        page.screenshot(path=screenshot_path)
        screenshot_bytes = io.BytesIO(page.screenshot())
        screenshot_object_path = screenshot_upload_to_minio(screenshot_bytes, object_name=screenshot_object_name)

        # capture current html state
        html_src = page.content()
        # todo: only write to filesystem in DEBUG mode
        write_html_to_file(content=html_src, file_path=html_path)
        html_object_path = html_upload_to_minio(io.StringIO(html_src), object_name=html_object_name)

        # ensure closing of context and browser so har file writes.
        context.close()
        browser.close()

        har_object_path = har_upload_to_minio(file_path=har_path, object_name=har_object_name)

        # write metadata object to arangoDB
        print(screenshot_object_path)
        print(har_object_path)
        print(html_object_path)
        _url_metadata = URLMetadata(
            correlation_id=correlation_id,
            url=url,
            utc_time=datetime.utcnow(),
            screenshot_path=screenshot_object_path,
            har_path=har_object_path,
            html_path=html_object_path
        )
        write_pydantic_to_arangodb(_url_metadata)
        return _url_metadata


if __name__ == '__main__':
    errs = []
    count = 0
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

    # Print the lists to verify
    for key, urls in news_urls.items():
        print(f"{key}:\n{'-' * 20}")
        for _url in urls:
            count += 1
            _correlation_id = uuid.uuid4()

            try:
                url_metadata = download_url(url=_url, correlation_id=_correlation_id)
                pprint.pprint(url_metadata)
            except Exception as e:
                traceback.print_exc()
                # capture unknown / unhandled exceptions for further review
                tb_str = traceback.format_exc()
                error_class_str = e.__class__.__name__

                # todo: small front end for these
                se = ScrapeError(correlation_id=_correlation_id,
                                 url=_url,
                                 err_type=error_class_str,
                                 err_msg=tb_str,
                                 utc_time=datetime.utcnow())
                errs.append(se)

    pprint.pprint("ERRORS!!!!")
    pprint.pprint(errs)

    pprint.pprint("Successes / Failures")
    pprint.pprint(f"{count} / {len(errs)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
