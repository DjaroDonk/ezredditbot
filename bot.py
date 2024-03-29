logs = True
def log(string):
    global logs
    if logs == True:
        print('#' + string)

log("start of the file")
import re
import praw
import parserforbot
import os
import emoji
import time
import random
instructions=parserforbot.instr_list
config=parserforbot.config
privateinfo=parserforbot.privateinfo
the_bot = praw.Reddit(client_id=privateinfo["client_id"],
                     client_secret=privateinfo["client_secret"],
                     password=privateinfo["password"],
                     user_agent=privateinfo["user_agent"],
                     username=privateinfo["username"])


def end():
    input()
    exit()

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

log("imported everything")

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))

log("opened the comments_replied_to.txt file and read it")

if not os.path.isfile("blacklist.txt"):
    blacklist = []
else:
    with open("blacklist.txt", "r") as f:
       blacklist = f.read()
       blacklist = blacklist.split("\n")
       blacklist = list(filter(None, blacklist))

log("opened the blacklist.txt file and read it")

def blacklistperson(name):
    print("blacklisted: " + name)
    log("just blacklisted" + name)
    global blacklist
    blacklist.append(name)
    with open("blacklist.txt","w") as f:
        f.write(name+"\n")
        f.close()

log("created the blacklist_person function")

def replied_to(c):
    print("replying to:\n" + c.body.translate(non_bmp_map))
    global comments_replied_to
    comments_replied_to.append(c.id)
    with open("comments_replied_to.txt","a") as f:
        f.write(c.id+"\n")
        f.close()

log("created the replied_to function")

def scancomment(c):
    try:
        comment_author = c.author.name
        if comment_author in blacklist:
            return()
    except:
        pass
    for instruction in instructions:
        if (instruction[0] == 0 and c.body.lower() == instruction[1]) or (instruction[0] == 1 and re.search(instruction[1],c.body.lower())):
            if instruction[2] == 0 or instruction[2] == 2:
                try:
                    current_com = c
                    for i in list(instruction[3]):
                        current_com = current_com.reply(emoji.emojize(random.choice(i)))
                        log("replied to " + current_com.body)
                        time.sleep(5)
                    time.sleep(5)
                except Exception as e:
                    print(e)
                    log("place 0")
                    if "ratelimit" in str(e).lower():
                        end()
                    pass
                replied_to(c)
            if instruction[2] == 1 or instruction[2] == 2:
                try:
                    blacklistperson(c.author.name)
                except Exception as e:
                    print(e)
                    log("place 1")
                    pass

log("created the scancomment function")

def scansub(whatsubreddit,sub_type,amount):
    user = the_bot.redditor(privateinfo["username"])
    log("whatsubreddit = " + whatsubreddit)
    log("sub_type = " + sub_type)
    log("amount = " + str(amount))
    log("created the user in scansub")
    threads_scanned = 0
    log("created the threads scanned variable")
    if sub_type == "hot":
        the_sub = the_bot.subreddit(whatsubreddit).hot(limit=amount)
    elif sub_type == "new":
        the_sub = the_bot.subreddit(whatsubreddit).new(limit=amount)
    log("created the_sub")
    for submission in the_sub:
        try:
            submission.comments.replace_more()
            for c in submission.comments.list():
                is_author = 1
                try:
                    c.author.name
                except:
                    is_author = 0
                if is_author == 1:
                    if c.author.name == privateinfo["username"]:
                        pass
                    elif (c.id not in comments_replied_to) and (c.author not in blacklist):
                        scancomment(c)
                elif is_author == 0:
                    if (c.id not in comments_replied_to):
                        scancomment(c)
            threads_scanned += 1
            print("scanned a thread --- " + str(threads_scanned))
        except Exception as e:
            print(e)
            log("place 3")
            threads_scanned += 1
            print("scanned a thread --- " + str(threads_scanned))

log("created the scansub function")
scansub(config["subreddit"],config["type"],config["amount"])
input()
