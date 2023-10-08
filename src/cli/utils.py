import pprint

from settings import CLI_DIR


def create_scrape_job(url):
    # Command sequence
    command = ["python", f"{CLI_DIR}/cli.py", "create-scrape-job-direct", f"--url={url}"]
    pprint.pprint(" ".join(command))
    return command


def create_scrape_request(url):
    # Command sequence
    command = ["python", f"{CLI_DIR}/cli.py", "send-scrape-request", f"--url={url}"]
    pprint.pprint(" ".join(command))
    return command
