import praw
import parserforbot
import os
instructions=parserforbot.instr_list
config=parserforbot.config
privateinfo=parserforbot.privateinfo
theBot = praw.Reddit(client_id=privateinfo["client_id"],
                     client_secret=privateinfo["client_secret"],
                     password=privateinfo["password"],
                     user_agent=privateinfo["user_agent"],
                     username=privateinfo["username"])

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))
