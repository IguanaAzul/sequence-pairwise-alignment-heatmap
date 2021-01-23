def read_sequences(path):
    file = open(path, "r")
    sequences_lines = file.readlines()

    sequences_names = list()
    sequences = list()
    change = False
    i = -1
    for line in sequences_lines:
        if line == "\n":
            continue
        elif line[0] == ">":
            sequences_names.append(line)
            change = True
            i += 1
            continue
        elif change == True:
            sequences.append(line)
            change = False
            continue
        elif change == False:
            sequences[i] += line
            continue
    replaces = ["#", "%", "&", "*", ":", "<", ">", "?", "/",  "\\", "{", "|", "}", "\n", "\t", "\'", "\""]
    names = list()
    for name in sequences_names:
        for char in replaces:
            name = name.replace(char, "")
        names.append(name)
    return sequences, names
