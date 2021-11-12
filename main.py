from src.core import constants
from src.data import read_html
import logging
from src.data import character

if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    # html = read_html.read(constants.CHARACTER)
    # for link in read_html.get_links(html):
    #     resp = read_html.read(link)
    #     read_html.get_character(resp)
    #     break
    character.get_all()



