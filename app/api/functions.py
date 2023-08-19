from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

from .models import BookmarkType


def get_page_info(url: str) -> dict:
    """
    Функция для получения информации со страницы,
    загруженной с переданной ссылки.
    :param url: str. Ссылка
    :return: dict. Возвращается словарь, где названия ключей
     соответствуют полям модели models.Bookmark,
     а значения - заполняемым данным.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    og_title = soup.find('meta', property='og:title')
    og_description = soup.find('meta', property='og:description')
    og_type = soup.find('meta', property='og:type')
    og_image = soup.find('meta', property='og:image')

    if og_title:
        title = og_title['content']
    else:
        title = soup.find('title').get_text() if soup.find('title') else ''

    description = og_description['content'] if og_description else ''
    type = og_type['content'] if og_type else ''
    type = BookmarkType.objects.get(name=type) if type else BookmarkType.objects.get(name='website')
    image_url = og_image['content'] if og_image else ''

    return {
        'title': title,
        'description': description,
        'type': type,
        'preview_image': image_url,
    }
