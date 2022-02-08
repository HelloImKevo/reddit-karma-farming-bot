#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from .sources.cobe import Cobe
from logs.logger import log
from collections import namedtuple
from utils import chance
from apis import reddit_api
from config import reddit_config
from ..utils import get_subreddit, AVOID_WORDS
import random
from praw.exceptions import APIException

Source = namedtuple('Source', ['name', 'api'])


class Comments:
    def __init__(self, source='cobe'):
        self.ready = False
        self.config = reddit_config.CONFIG
        self.rapi = reddit_api
        self.source_name = source
        self.sources = {
            "cobe": Source('cobe', Cobe)
        }
        self.comments = self.sources.get(self.source_name).api()

    def init(self):
        log.info("initializing comments")
        self.ready = False
        self.comments.init()
        self.ready = True
        log.info("commenting ready")

    def comment(self, roll=1):
        if not self.ready:
            log.info("comments need to be initialized")
            self.init()

        if chance(roll):
            log.info("going to make a comment")

            # keep searching posts until we find one with comments
            post_with_comments = False
            while not post_with_comments:
                # pick a subreddit to comment on
                subreddit = get_subreddit(getsubclass=True)
                # get a random hot post from the subreddit
                post = random.choice(list(subreddit.hot()))
                # replace the "MoreReplies" with all of the submission replies
                post.comments.replace_more(limit=0)

                if len(post.comments.list()) > 0:
                    post_with_comments = True

            try:
                # choose if we're replying to the post or to a comment
                if chance(self.config.get('reddit_reply_to_comment')):
                    # reply to the post with a response based on the post title
                    reply_message = self.comments.get_reply(post.title)
                    log.info(f"replying directly to post with: '{reply_message}'")
                    post.reply(reply_message)
                else:
                    # get a random comment from the post
                    comment = random.choice(post.comments.list())
                    # reply to the comment
                    reply_message = self.comments.get_reply(comment.body)
                    log.info(f"replying to comment with: '{reply_message}'")
                    comment.reply(reply_message)
            except APIException as e:
                log.info(f"error commenting: {e}")
