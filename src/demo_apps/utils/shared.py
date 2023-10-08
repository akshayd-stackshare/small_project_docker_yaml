import os
import subprocess
import pprint

from cli.utils import create_scrape_request
from settings import SRC_DIR


class UrlUploader:
    def __init__(self, urls=None):
        if urls is None:
            self.urls = []
        else:
            self.urls = urls

    def print_urls(self):
        for key, url_list in self.urls.items():
            print(f"{key}:\n{'-' * 20}")
            for _url in url_list:
                print(_url)

    def run_commands(self):
        # Assuming `create_scrape_request` is a function that you've defined elsewhere

        # Environment variables
        env = os.environ.copy()
        env['PYTHONPATH'] = SRC_DIR

        # Command sequence
        commands = [create_scrape_request(url=u) for u in self.flatten_urls()]
        # commands.extend([create_scrape_job(url=u) for u in self.flatten_urls()])
        # Uncomment the above line if you have a `create_scrape_job` function

        results = [subprocess.run(c, env=env) for c in commands]
        pprint.pprint(results)

    def flatten_urls(self):
        """Returns a flattened list of all URLs."""
        flattened = []
        for url_list in self.urls.values():
            for _url in url_list:
                flattened.append(_url)
        return flattened


if __name__ == '__main__':
    # example usage
    # tester = UrlUploader()
    # tester.print_urls()
    # tester.run_commands()
    pass
