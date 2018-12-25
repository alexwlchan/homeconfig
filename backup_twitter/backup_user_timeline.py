#!/usr/bin/env python
# -*- encoding: utf-8

import os

from twitter_oauth import BACKUP_DIR, TwitterSession, save_tweet


if __name__ == '__main__':
    sess = TwitterSession()

    for tweet in sess.user_timeline():
        save_tweet(tweet, backup_dir=os.path.join(BACKUP_DIR, "user_timeline"))
