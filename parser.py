def parse(line):
    line = line.split("#[#")
    conditions=line[0]
    actions=line[1]
    print("Conditions: " + conditions)
    print("Actions: " + actions)
    conditions=conditions.split("-[-")
    actions=actions.split("-[-")
    print("\n\n")
    print("Conditions: " + str(conditions))
    print("Actions: " + str(actions))
    
