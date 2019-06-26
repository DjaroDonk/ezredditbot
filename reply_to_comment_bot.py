import re
import praw
import os
from privateinfo import theBot
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
import time
import emoji

if not os.path.isfile("blacklist.txt"):
    blacklist = []
else:
    with open("blacklist.txt", "r") as f:
       blacklist = f.read()
       blacklist = blacklist.split("\n")
       blacklist = list(filter(None, blacklist))

#print(blacklist)

if not os.path.isfile("bcount.txt"):
    bcount = {}
else:
    bcount = {}
    with open("bcount.txt", "r") as bc:
        for line in bc:
            bcount[line.split(',')[0]] = line.split(',')[1].rstrip('\n')


if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))

def replyTo(c,regexPattern,reply,**kwargs):
    #print("Replying to the comment")
    global blacklist
    if re.search(regexPattern, c.body, re.IGNORECASE):
        #print("found pattern")
        #if c.parent().author.name == "says_lmao_bot":
            #c.reply("Very clever")
        #else:
        hasAuth = 1
        try:
            c.author.name
            hasAuth = 1
        except:
            hasAuth = 0
        #print("made it past hasauth")
        if hasAuth == 1:
            if (c.author.name.lower() in blacklist):
                return
            if (c.author.name.lower() == "pewdsvstseries_bot") or (c.author.name.lower() == "pewdstatus"):
                return
        #print("made it past hasAuth")
        if 'replyBack' in kwargs.keys():
            thisCom = c.reply(emoji.emojize(reply,use_aliases=True))
            thisCom.reply(kwargs['replyBack'])
        elif 'command' in kwargs.keys():
            kwargs['command']()
            c.reply(emoji.emojize(reply,use_aliases=True))
        else:
            c.reply(emoji.emojize(reply,use_aliases=True))
        try:
            print("Bot replying to :\n ", c.body.translate(non_bmp_map), "\nID: ", c.id, "\nBy: ", c.author.name)
        except:
            print("Bot replying to :\n ", c.body.translate(non_bmp_map), "\nID: ", c.id)
        comments_replied_to.append(c.id)
        with open("comments_replied_to.txt", "w") as f:
            for c_id in comments_replied_to:
                f.write(c_id + "\n")
        time.sleep(5)

def getBcount(comment):
    global bcount
    hasbc = 1
    try:
        comment.author.name
        hasbc = 1
    except:
        hasbc = 0
    if hasbc == 1:
        #print("Returned b count")
        bcount.setdefault(comment.author.name,0)
        if bcount[comment.author.name] == 0:
            return '1'
        else:
            return bcount[comment.author.name]
    else:
        return "undefined: can't get bcounter of [\"Deleted\"]"

def incBcount(comment):
    global bcount
    hasbc = 1
    try:
        comment.author.name
        hasbc = 1
    except:
        hasbc = 0
    if hasbc == 1:
        bcount.setdefault(comment.author.name, 0)
        bcount[comment.author.name] = str(int(bcount[comment.author.name]) + 1)
        #print("incremented b count")
        with open("bcount.txt", "w") as f:
            for key, val in bcount.items():
                f.write(str(key)+','+str(val)+'\n')
    else:
        return
    
def bcountMsg(c):
    return str("""Bro... That's kinda cringe normie. That little emoji you just used... That's right, the 'b' emoji. That's kinda cringe.
My reaction to that emoji is [bruh sound effect #2](https://www.youtube.com/watch?v=2ZIpFytCSVc). I mean... It really is that cringe. 
Each time you use that emoji in one of your little comments, your 'b-counter' goes up by one. Your current 'b-count' is: """) + str(getBcount(c) + ".  \nIf you're 'b counter' reaches 50 something very bad will happen, so be warned!")
  grandparent_author = 1


autoOrMan = input("Do you want automatic or manual mode?\n")

if autoOrMan.lower() == "manual":
    while True:
        whatsub = input("What subreddit?\n")
        subreddit = theBot.subreddit(whatsub)
        whatlimit = int(input("What limit\n"))
        whattype = input("What type (hot or new)\n")
        if whattype == 'new':
            theSubs = subreddit.new(limit=whatlimit)
        else:
            theSubs = subreddit.hot(limit=whatlimit)
        scanSub(whatsub,subreddit,theSubs)

else:
    while True:
        whatsub = 'youngpeopleyoutube'
        subreddit = theBot.subreddit(whatsub)
        theSubs = subreddit.hot(limit=100)
        scanSub(whatsub,subreddit,theSubs)
