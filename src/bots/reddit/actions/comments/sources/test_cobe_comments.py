#!/usr/bin/env python3

"""
Basic test of an existing Cobe brain database.
"""

from config.authentication import set_auth

set_auth({
    "reddit_client_id": "test",
    "reddit_client_secret": "test",
    "reddit_username": "test",
    "reddit_password": "test",
})


def test_replies_to_post_titles():
    from bots.reddit.actions.comments.comment_actions import Comments

    print("Running test...")
    comments = Comments()
    print(f"Initializing comments.comments property: {comments.comments}")
    comments.comments.init()

    if comments.comments.ready:
        print('Cobe comments are ready to be tested!')
    else:
        print('Cobe comments database has not been initialized'
              ' - run the appropriate shell script first.')
        raise SystemExit(0)

    post_titles: list = ['Apple', 'Banana', 'Cherry', 'Video Games', 'DIY Tricks',
                         'President', 'United States', 'Apple iPhone', 'Florida',
                         'Russia', 'Space Travel', 'New Pokemon Game', 'Broken Tablet',
                         'Fox News', 'CNN', 'Where did it go?', 'TIL: Chickens lay eggs']
    for post_title in post_titles:
        reply_message = comments.comments.get_reply(post_title)
        print(f"Response to post title '{post_title}' is: '{reply_message}'")

    pass


def main():
    test_replies_to_post_titles()
    print(r'All tests passed. Success! \o/')


main()
