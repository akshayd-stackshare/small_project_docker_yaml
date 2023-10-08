import pprint
from pathlib import Path

CUR_FILE = Path(__file__)
SETTINGS_DIR = CUR_FILE.parent
DATA_DIR = SETTINGS_DIR / 'data'
HAR_DIR = DATA_DIR / 'har_files'
SCREENSHOT_DIR = DATA_DIR / 'screenshots'
HTML_DIR = DATA_DIR / 'html'
SRC_DIR = SETTINGS_DIR / 'src'
CLI_DIR = SRC_DIR / 'cli'

HAR_BUCKET = 'har'
HTML_BUCKET = 'html'
SCREENSHOT_BUCKET = 'screenshot'

MINIO_ACCESS_KEY = 'minioaccesskey'
MINIO_SECRET_KEY = 'miniosecretkey'


if __name__ == '__main__':
    pprint.pprint([
        SETTINGS_DIR,
        DATA_DIR,
        HAR_DIR,
        SCREENSHOT_DIR,
        HTML_DIR
    ])