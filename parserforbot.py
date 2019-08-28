import re
#Imports Regex 

logs = True #If it uses logs or not
#Creates the log function
def log(string):
    global logs
    if logs == True:
        print('#' + string)
log("initialised logs")

#Creates the instruction class. It has a condition (cond) and an activity (act)
class temp_instruction:
    def __init__(self,cond,act):
        self.condition = cond
        self.action = act
log("created the temp_instruction class")

#Creates the parseline function. It splits the condition and the action with ':::'
def parseline(line):
    line = line.split(":::")
    line[0] = re.sub(r"(_triple_colons_)(?!])",":::",line[0])
    line[0] = re.sub(r"\[_triple_colons_\]","_triple_colons_",line[0])
    line[1] = re.sub(r"(_triple_colons_)(?!])",":::",line[1])
    line[1] = re.sub(r"\[_triple_colons_\]","_triple_colons_",line[1])
    line[1] = re.sub(r"newlinereddit","\n",line[1])
    return(temp_instruction(line[0],line[1]))

log("created the parse line function")

def parseinstruction(instr):
    condition = instr.condition.split("=")
    condition = [{"exact":0,"keyword":1}[condition[0]],condition[1].strip('"')]
    action = instr.action.split("=")
    if len(action) == 1:
        action = [1]
    else:
        temp_action = action[1]
        temp_action = temp_action.split("|'|")
        temp_action_2 = []
        for i in temp_action:
            temp_action_3 = []
            a = i.split("?|?")
            b = []
            for j in a:
                j = j.strip('"')
                b.append(j)
            temp_action_3.append(b)
            for k in temp_action_3:
                temp_action_2.append(k)
        action = [{"reply":0,"blacklistreply":2}[action[0]],temp_action_2]
    instruct = condition+action
    return instruct

log("created the parseinstruction function")

instructions = open("instructions.txt","r")
instr_list = []
for newline in instructions:
    if not newline.startswith("##"):
        instr_list.append(parseinstruction(parseline(newline.strip())))

log("parsed the instructions")

config_file = open("config.txt","r")
config = {"subreddit":"all","type":"hot","amount":200}
for newline in config_file:
    try:
        config[newline.split("=")[0]] = newline.split("=")[1].strip()
    except:
        pass
config["amount"]=int(config["amount"])

log("created the config file")

privateinfofile = open("privateinfo.txt","r")
privateinfofile.seek(0)
privateinfo = {"client_id":"","client_secret":"","password":"","user_agent":"","username":""}
for newline in privateinfofile:
    try:
        privateinfo[newline.split("=")[0]] = newline.split("=")[1].strip()
    except:
        pass

log("created the privateinfo file")
log("the parser has completed succesfully without bugs")
