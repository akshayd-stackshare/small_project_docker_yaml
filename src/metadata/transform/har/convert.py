from settings import HAR_DIR
from src.metadata.transform.shared.convert import url_to_filename


def har_url_to_filename(_url, use_hash=False, suffix='har', write_dir=HAR_DIR):
    return url_to_filename(_url, suffix=suffix, write_dir=write_dir, use_hash=use_hash)


if __name__ == '__main__':
    # Spike test, just ensure it visually looks correct
    url = "https://www.example.com/some/very/long/path/with/query?param=value&another_param=value2"
    print(har_url_to_filename(url))
