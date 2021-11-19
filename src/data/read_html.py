import re
from typing import Union
import logging

import requests
from bs4 import BeautifulSoup

from src.core.util import constants
from src.data.models import Character, Appearances, Creature, Game


def read(path: str) -> Union[BeautifulSoup, None]:
    resp = requests.get(path)
    if resp.status_code == 200:
        return BeautifulSoup(resp.content, 'html.parser')
    return None


def get_links(soup: BeautifulSoup) -> list:
    links = []
    if soup:
        for paragraph in soup.findAll('p'):
            for link in paragraph.findAll('a', href=True):
                link = str(link['href'])
                if link.__contains__(constants.URL_BASE):
                    links.append(link)
    return links


def get_link_ul(soup: BeautifulSoup) -> list:
    links = []
    if soup:
        div_content = soup.find('div', {'class', 'td-page-content'})
        for paragraph in div_content.findAll('ul'):
            for link in paragraph.findAll('li'):
                link = str(link.find('a')['href'])
                links.append(link)
    return links


def get_ul(soup: BeautifulSoup) -> list:
    lis = []
    if soup:
        for paragraph in soup.findAll('ul'):
            for link in paragraph.findAll('li'):
                em = link.find('em')
                if em:
                    lis.append(link.find('em').get_text().strip().replace(u'\xa0', ' '))
                else:
                    link.get_text()
    return lis


def get_character(soup: BeautifulSoup):
    if soup:
        name = soup.find("h1", {'class': 'entry-title td-page-title'}).find('span').get_text().split("|")[1].strip()
        img = soup.find("img", {'class': 'alignleft'})['src']
        year_burn = ''
        blood_type = ""
        height = ""
        weight = ""

        logging.info(f"importando o personagem {name}")

        paragraph_info_character = soup.find_all('p')[0]
        for index, description in enumerate(paragraph_info_character.findAll("em")):
            if index == 0:
                year_burn = _get_year(description)
            elif index == 1:
                blood_type = _get_description(description)
            elif index == 2:
                height = _get_description(description)
            elif index == 3:
                weight = _get_description(description)

        character = Character(name, year_burn, blood_type, height, weight, img).save()

        get_game(soup, character)


def _get_description(description) -> str:
    return description.get_text().split(':')[1].strip()


def get_game(soup: BeautifulSoup, character_id) -> None:
    if soup:
        paragraph_games = soup.find_all('p')[1]
        years = re.findall(r'[0-9]{4}', str(paragraph_games))
        for index, game in enumerate(paragraph_games.find_all('a')):
            name = game.get_text().strip().replace(u'\xa0', ' ')
            year = years[index]
            Appearances(name, year, character_id).save()


def _get_year(description):
    text_year = _get_description(description)
    math = re.findall(r'[0-9]{4}', text_year)
    if text_year.lower().__contains__("desconhecido"):
        return text_year.capitalize()
    elif math:
        return math[0]
    else:
        return "Desconhecido."


def get_creature(soup: BeautifulSoup):
    if soup:
        name = soup.find("h1", {'class': 'entry-title td-page-title'}).find('span').get_text().split("|")[1].strip()
        print(f"importando o {name}")
        div_content = soup.find("div", {'class': 'td-page-content'})
        img = div_content.find("img", {'class': 'alignleft'})['src']
        strategies = ""
        if div_content.hr:
            description = " ".join(list(map(lambda tag: tag.getText(), div_content.hr.find_previous_siblings("p"))))
            strategies = " ".join(list(map(lambda tag: tag.getText(), div_content.hr.find_next_siblings("p"))))
        else:
            description = " ".join(list(map(lambda tag: tag.getText(), div_content.findAll("p"))))
        Creature(name, img, description, strategies).save()


def get_info_game(soup: BeautifulSoup):
    if soup:
        div_content = soup.find('div', {'class', 'td-page-content'})
        name = soup.find("h1", {'class': 'entry-title td-page-title'}).find('span').get_text().split("|")[1].strip()
        img = div_content.find("img")['src']
        synopsis = ' '.join([t.get_text().replace('"', '') for t in div_content.find_all('p')])
        release = get_ul(div_content)

        Game(name, img, synopsis, release).save()
