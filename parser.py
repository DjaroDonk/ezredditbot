import re
def parse(line):
    line = line.split(":::")
    line[0] = re.sub(r"(_triple_colons_)(?!])",":::",line[0])
    line[0] = re.sub(r"\[_triple_colons_\]","_triple_colons_",line[0])
    line[1] = re.sub(r"(_triple_colons_)(?!])",":::",line[1])
    line[1] = re.sub(r"\[_triple_colons_\]","_triple_colons_",line[1])
    print(line)
