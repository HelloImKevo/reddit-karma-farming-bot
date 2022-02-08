#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from config import authentication
from .reddit import RedditAPI
from .pushshift import PS

reddit_api = RedditAPI(**authentication.AUTH).api

pushshift_api = PS()