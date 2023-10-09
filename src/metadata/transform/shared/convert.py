import pprint
from pathlib import Path

import settings

from urllib.parse import urlsplit
import re
from hashlib import md5
from datetime import datetime


def remove_query_string(url):
    parsed_url = urlsplit(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"


def generate_s3_key(domain, identifier, suffix):
    timestamp = datetime.now()
    year, month, day = timestamp.strftime('%Y'), timestamp.strftime('%m'), timestamp.strftime('%d')
    hour, minute, second = timestamp.strftime('%H'), timestamp.strftime('%M'), timestamp.strftime('%S')
    sanitized_domain = domain.replace('.', '__')
    s3_key = f'{year}/{month}/{day}/{sanitized_domain}/{hour}-{minute}-{second}_{identifier}.{suffix}'
    return s3_key


def url_to_filename(_url, use_hash=False, suffix=None, write_dir=None):
    # Remove the query string from the URL
    _url = remove_query_string(_url)

    # Split the URL into components
    parsed_url = urlsplit(_url)

    # Generate the filename for hashing or direct use
    filename = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}{parsed_url.query}{parsed_url.fragment}"

    # Remove or replace disallowed characters
    filename = re.sub(r'[^a-zA-Z0-9\-_.]', '_', filename)
    filename = filename.rstrip('_')

    # If the URL is still too long, hash it
    if use_hash and len(filename) > 250:  # Giving some buffer below the 255 limit
        filename = md5(_url.encode()).hexdigest()

    # Generate the S3 key using the domain from the URL and the filename as the identifier
    s3_key = generate_s3_key(parsed_url.netloc, filename, suffix)

    # If a write_dir is provided, append it
    if write_dir:
        return str(write_dir / s3_key)
    return s3_key


# def url_to_filename(_url, use_hash=False, suffix=None, write_dir=None):
#     # Split the URL into components
#     parsed_url = urlsplit(_url)
#
#     # Keep the scheme and netloc (domain), and combine the rest
#     filename = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}{parsed_url.query}{parsed_url.fragment}"
#
#     # Remove or replace disallowed characters
#     filename = re.sub(r'[^a-zA-Z0-9\-_.]', '_', filename)
#
#     # Handle trailing underscores (which might have been slashes or other characters)
#     filename = filename.rstrip('_')
#
#     # If the URL is still too long, hash it
#     if use_hash and len(filename) > 250:  # Giving some buffer below the 255 limit
#         hashed = md5(_url.encode()).hexdigest()
#         filename = f"{hashed}"
#
#     filename = f"{filename}.{suffix}"
#
#     return str(write_dir / filename)


def split_path(path, keywords=None):
    """
    Splits the given path after any keyword match.

    :param path: The path to be split.
    :param keywords: List of keywords to search for in the path.
    :return: The split path or None if no keyword is found.

    This can break if we encounter a path including screenshots or html on some website,
    this is a bit fragile.
    """
    if keywords is None:
        keywords = ["html", "screenshots", "har_files"]

    p = Path(path)
    for keyword in keywords:
        if keyword in p.parts:
            index = p.parts.index(keyword)
            return '/'.join(p.parts[index + 1:])
    return None


def get_filename(file_path):
    return split_path(file_path)


if __name__ == '__main__':
    # spike test
    TEST_URL = 'https://www.yahoo.com/'
    TEST_SUFFIXES = ['html',
                     'png',
                     'har']

    TEST_WRITE_DIRS = [settings.HTML_DIR,
                       settings.SCREENSHOT_DIR,
                       settings.HAR_DIR]

    RES = []
    RES_2 = []

    for _suffix, _write_dir in zip(TEST_SUFFIXES, TEST_WRITE_DIRS):
        f_name = url_to_filename(_url=TEST_URL, suffix=_suffix, write_dir=_write_dir)
        RES.append(f_name)

    # for _suffix, _write_dir in zip(TEST_SUFFIXES, TEST_WRITE_DIRS):
    #     f_name = url_to_filename_2(_url=TEST_URL, suffix=_suffix, write_dir=_write_dir)
    #     RES_2.append(f_name)

    pprint.pprint(RES)

    pprint.pprint(RES_2)
