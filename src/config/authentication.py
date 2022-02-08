#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from utils import prefer_envar

AUTH: dict = {}


def init_auth():
    global AUTH

    print(f"Boolean = {bool(AUTH)}")

    if len(AUTH) > 0:
        print(f'AUTH credentials already initialized: {AUTH}')
        return

    AUTH = prefer_envar({
        # App Credentials
        "reddit_client_id": "",
        "reddit_client_secret": "",
        # Reddit Account Credentials
        "reddit_username": "",
        "reddit_password": ""
    })

    print(f"AUTH is now...: {AUTH}")


def set_auth(auth: dict):
    global AUTH
    AUTH = auth

    print(f"AUTH updated to: {AUTH}")
