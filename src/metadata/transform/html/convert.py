from settings import HTML_DIR
from src.metadata.transform.shared.convert import url_to_filename


def html_url_to_filename(_url, use_hash=False, suffix='html', write_dir=HTML_DIR):
    return url_to_filename(_url, use_hash=use_hash, suffix=suffix, write_dir=write_dir)


if __name__ == '__main__':
    # Spike test, just ensure it visually looks correct
    url = "https://www.example.com/some/very/long/path/with/query?param=value&another_param=value2"
    print(html_url_to_filename(url))
