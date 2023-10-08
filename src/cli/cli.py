import json
from datetime import datetime

import click
import requests

# todo: change this to communicate with an API
from data_infrastructure.rabbitmq.service import RabbitMQService
from system.models.input import ScrapeRequest


@click.group()
def cli():
    """Main entry point for our CLI tool."""
    pass


@cli.command()
@click.option('--url', prompt='url to scrape?', help='Send a single url for a scrape')
def create_scrape_job_direct(url):
    # create ScrapeRequest object
    click.echo(f'Sending scrape job to queue, url:{url}!')

    # send object to rabbitmq
    data = {
        "url": url,
        "time_requested": str(datetime.utcnow().isoformat())
    }
    test_request = json.dumps(ScrapeRequest(**data).model_dump(), default=str)
    print(test_request)
    print(type(test_request))
    rabbit_service = RabbitMQService()
    rabbit_service.publish('input_queue', test_request)


@cli.command()
@click.option('--url', prompt='URL to scrape?', help='Provide the URL you want to scrape')
def send_scrape_request(url):
    """
    Sends a scraping request to the FastAPI endpoint.
    """
    api_endpoint = 'http://localhost:8000/scrape'

    data = {
        'url': url,
        'time_requested': str(datetime.utcnow().isoformat())
    }

    response = requests.post(api_endpoint, json=data)

    if response.status_code == 200:
        result = response.json()
        click.echo(result.get('message', 'Scrape job successfully sent!'))
    else:
        click.echo(f"Failed to send scrape job. Server responded with: {response.status_code} - {response.text}")

if __name__ == '__main__':
    cli()
