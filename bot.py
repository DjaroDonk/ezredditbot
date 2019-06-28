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

if not os.path.isfile("blacklist.txt"):
    blacklist = []
else:
    with open("blacklist.txt", "r") as f:
       blacklist = f.read()
       blacklist = blacklist.split("\n")
       blacklist = list(filter(None, blacklist))

def blacklist_person(name):
    global blacklist
    blacklist.append(name)
    with open("blacklist.txt","w") as f:
        f.write(name)
        f.close()

def scancomment(c):
    for instruction in instructions:
        if instruction[0] == 0:
            if c.body == instruction[1]:
                if instruction[2] == 0:
                    c.reply(instructions[3])
                elif instruction[2] == 2:
                    c.reply(instructions[3])
