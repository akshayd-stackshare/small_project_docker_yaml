import os


def write_html_to_file(content, file_path):
    """
    Writes the provided HTML content to a specified file.

    :param content: The HTML content to write.
    :param file_path: The path where the content should be saved. Defaults to 'output.html'.
    """
    # Ensure the directory exists; if not, create it
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    # Example usage:
    # html_content = "<html><head></head><body>Hello World!</body></html>"
    # write_html_to_file(html_content, 'test_output.html')
    pass
