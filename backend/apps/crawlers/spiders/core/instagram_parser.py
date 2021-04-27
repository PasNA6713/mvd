from datetime import datetime
import json
import os
from time import sleep

import requests.utils

from apps.chat.services import a_send_all


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.116 Safari/537.36',
}


def login(session):
    login_get_url = 'https://www.instagram.com/accounts/login/'
    login_post_url = 'https://www.instagram.com/accounts/login/ajax/'

    time = int(datetime.now().timestamp())

    response = session.get(url=login_get_url, headers=HEADERS)
    csrf = response.cookies['csrftoken']

    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")

    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = session.post(login_post_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)

    if json_data["authenticated"]:
        print("login successful")
        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
        csrf_token = cookie_jar['csrftoken']
        session_id = cookie_jar['sessionid']
    else:
        print("login failed ", login_response.text)

    return session


def extract_post_data(posts_list):
    for i in range(len(posts_list)-1):
        try:
            shortcode = posts_list[i].get("node").get("shortcode")
            text = posts_list[i].get("node").get("edge_media_to_caption").get("edges")[0].get("node").get("text")
        except Exception as e:
            print(e)
            print(posts_list[i])

        sleep(0.5)
        yield {"shortcode": shortcode, "text": text}


def get_posts_list(tag, session):
    tag = "навальный"
    search_url = f"https://www.instagram.com/explore/tags/{tag}/?__a=1"

    response = session.get(url=search_url, headers=HEADERS)

    page_data = json.loads(response.text)
    has_next_page = page_data.get("graphql").get("hashtag").get("edge_hashtag_to_media").get("page_info").get("has_next_page")
    end_cursor = page_data.get("graphql").get("hashtag").get("edge_hashtag_to_media").get("page_info").get("end_cursor")

    posts = page_data.get("graphql").get("hashtag").get("edge_hashtag_to_media").get("edges")

    query_hash = "9b498c08113f1e09617a1703c22b2f32"
    posts_quontity = 50

    while has_next_page:
        try:
            yield from extract_post_data(posts)
            next_url = f"https://www.instagram.com/graphql/query/?query_hash={query_hash}\
                &variables='tag_name':'{tag}','first':{posts_quontity},'after':'{end_cursor}'"
            response = session.get(url=next_url, headers=HEADERS)
            page_data = json.loads(response.text)
            has_next_page = page_data.get("data").get("hashtag").get("edge_hashtag_to_media").get("page_info").get("has_next_page")
            end_cursor = page_data.get("data").get("hashtag").get("edge_hashtag_to_media").get("page_info").get("end_cursor")

            posts = page_data.get("data").get("hashtag").get("edge_hashtag_to_media").get("edges")

            yield from extract_post_data(posts)
        except AttributeError:
            return


def insta_parse(tag: str):
    session = requests.session()
    for post in get_posts_list(tag, session):
        yield post.get('text')


async def insta_broadcast(number, tag):
    for i, message in zip(range(number), insta_parse(tag)):
        await a_send_all(message)