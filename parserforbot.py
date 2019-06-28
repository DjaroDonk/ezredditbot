import re

class temp_instruction:
    def __init__(self,cond,act):
        self.condition = cond
        self.action = act

def parseline(line):
    line = line.split(":::")
    line[0] = re.sub(r"(_triple_colons_)(?!])",":::",line[0])
    line[0] = re.sub(r"\[_triple_colons_\]","_triple_colons_",line[0])
    line[1] = re.sub(r"(_triple_colons_)(?!])",":::",line[1])
    line[1] = re.sub(r"\[_triple_colons_\]","_triple_colons_",line[1])
    return(temp_instruction(line[0],line[1]))

def parseinstruction(instr):
    condition = instr.condition.split("=")
    condition = [{"exact":0,"keyword":1}[condition[0]],condition[1].strip('"')]
    action = instr.action.split("=")
    if len(action) == 1:
        action = [1]
    else:
        action = [{"reply":0,"blacklistreply":2}[action[0]],action[1].strip('"')]
    instruct = condition+action
    return instruct

instructions = open("instructions.txt","r")
instr_list = []
for newline in instructions:
    if not newline.startswith("##"):
        instr_list.append(parseinstruction(parseline(newline.strip())))

config_file = open("config.txt","r")
config = {"subreddit":"all","type":"hot","amount":200}
for newline in config_file:
    try:
        config[newline.split("=")[0]] = newline.split("=")[1].strip()
    except:
        pass
config["amount"]=int(config["amount"])

instructions = open("privateinfo.txt","r")
privateinfo = {"client_id":"","client_secret":"","password":"","user_agent":"","username":""}
for newline in config_file:
    try:
        config[newline.split("=")[0]] = newline.split("=")[1].strip()
    except:
        pass
